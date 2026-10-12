# mcg-ops

This is the shared desk between Sam, Claude, Zoho, and Vercel. If it is not in here, nobody owns it.

## What lives here

- `OPERATING.md`  the running doc: every tool, its status, what is owed to whom, what is due. Claude reads and updates it every run.
- `inbox/`        where Sam drops ideas, specs, voice dumps, build instructions. Claude files them.
- `outbox/`       drafted partner and client messages waiting for Sam's yes. Nothing here is sent by Claude.
- `briefs/`       one morning brief per weekday, so you can look back.
- `data/`         `partners.json` (written daily by Zoho), `uptime.json` (written by GitHub), `tools.json` (the tool registry), `outreach_log.json`
- `tools/`        one folder per live tool. Vercel deploys from these folders.
- `specs/`        the written-out version of inbox ideas, one file per build.
- `zoho/`         the Deluge function that exports partners daily, plus setup steps.
- `ops/`          `MORNING_RUN.md` (the scheduled run prompt), `SESSION_RULES.md`, `VOICE.md`
- `.github/`      the uptime checker that pings every tool every hour

## Setup, in order (about 45 minutes total, all in a browser)

### 1. GitHub (done Oct 12, 2026)
The repo is `github.com/mycreditguycreditrestoration-lgtm/mcg-ops` (private) and every folder is in place, including the uptime workflow.
One thing left: Actions tab > tool-uptime > Run workflow. A minute later `data/uptime.json` is real.
If that run fails on its commit step: Settings > Actions > General > Workflow permissions > "Read and write permissions" > Save, then run it again.

### 2. Tool URLs (5 min)
Open `data/tools.json` on GitHub, click the pencil, paste each tool's live URL. Leave `""` for anything not live. Commit. Run the uptime workflow again.

### 3. Zoho export (15 min)
`zoho/SETUP.md`, start to finish. When it works, `data/partners.json` updates every morning on its own.

### 4. Vercel (5 min per tool, important ones first)
`tools/README.md`. Each Vercel project points at its folder here. After that, a commit is a deploy and nothing gets lost.

### 5. The morning run (5 min)
`ops/MORNING_RUN.md` is the prompt. In Claude, create a recurring scheduled task (weekdays, early morning, your time) and paste the whole file in. support.claude.com has the current steps for scheduling. The first run tells us whether the scheduled environment can reach this repo; the fallback is at the bottom of the prompt.

## Day to day

- Idea at 11pm: drop a file in `inbox/`. The morning run files it and turns build instructions into `specs/`.
- Build something with Claude: the session ends with the source in `tools/<name>/`, `OPERATING.md` updated, `tools.json` updated. Not optional.
- A draft in `outbox/` you like: send it from Zoho or your phone, then tell Claude "sent <name>" so it gets logged.
- Something is down: the brief says so, with the time it went down.
