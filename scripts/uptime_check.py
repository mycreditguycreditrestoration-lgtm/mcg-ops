#!/usr/bin/env python3
"""Pings every tool in data/tools.json and writes data/uptime.json.
Only rewrites the file when a status changes (or once a day as a heartbeat),
so the repo does not fill up with commits. Standard library only."""
import json, os, sys, datetime, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor

TOOLS = "data/tools.json"
OUT = "data/uptime.json"
NOW = datetime.datetime.now(datetime.timezone.utc)
NOW_S = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")

tools = json.load(open(TOOLS))["tools"]
try:
    prev = json.load(open(OUT))
except Exception:
    prev = {}
prev_tools = {t["name"]: t for t in prev.get("tools", [])}

def check(t):
    name = t["name"]
    url = (t.get("url") or "").strip()
    if not url:
        return name, url, "no url", None, ""
    status, code, note = "up", None, ""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "mcg-ops-uptime/1.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            code = r.status
            body = r.read(500000).decode("utf-8", "ignore")
        expect = (t.get("expect") or "").strip()
        if expect and expect.lower() not in body.lower():
            status, note = "wrong content", "expected text not found: " + expect
    except urllib.error.HTTPError as e:
        status, code, note = "down", e.code, "HTTP %s" % e.code
    except Exception as e:
        status, note = "down", str(e)[:140]
    return name, url, status, code, note

results, changed = [], False
with ThreadPoolExecutor(max_workers=8) as ex:
    checked = list(ex.map(check, tools))
for name, url, status, code, note in checked:
    old = prev_tools.get(name, {})
    since = old.get("since", NOW_S) if old.get("status") == status else NOW_S
    if old.get("status") != status:
        changed = True
    results.append({"name": name, "url": url, "status": status, "http": code, "note": note, "since": since})

heartbeat = True
if prev.get("checked_at"):
    try:
        last = datetime.datetime.strptime(prev["checked_at"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=datetime.timezone.utc)
        heartbeat = (NOW - last) > datetime.timedelta(hours=23)
    except Exception:
        heartbeat = True

write = changed or heartbeat
if write:
    json.dump({"checked_at": NOW_S, "tools": results}, open(OUT, "w"), indent=2)

with open(os.environ.get("GITHUB_OUTPUT", "/dev/null"), "a") as f:
    f.write("changed=%s\n" % ("true" if write else "false"))

bad = [r for r in results if r["status"] in ("down", "wrong content")]
print("checked %d tools, %d problems, file %s" % (len(results), len(bad), "updated" if write else "unchanged"))
for r in bad:
    print(" - %s: %s %s (since %s)" % (r["name"], r["status"], r["note"], r["since"]))
