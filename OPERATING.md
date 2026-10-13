# MCG operating doc

Last updated: 2026-10-12 (seeded by Claude from working notes; anything marked [verify] came from notes, not a live check)
Last morning run: never

Status words mean exactly this:
- designed: a spec exists, nothing is built
- built: files exist, not deployed
- deployed: it is on a URL
- verified: someone opened the URL on a stated date and the expected thing happened
- not verified: everything else, no matter how done it felt

## This week (as of Mon Oct 12, 2026)
- Tue Oct 13, 2pm ET: 20/20 Vision pod, Session 6 "The Return" (return conversion) [verify date with Nicole Heinz-Trefrey]. Open by reviewing the finish-line checklist with numbers. Weeks 4 and 5 were missed (low attendance, then a cancelled week, then nobody showed); the catch-up email and digital syllabus went out Oct 12 instead. Remaining after this: live pipeline review. Pod ends Oct 22.
- Vetted VA Credit Readiness: waiting on their logo, brand colors, and sign-off. Own Vercel project, separate from plain Credit Readiness. Must carry "Not affiliated with the Dept. of Veterans Affairs or any government agency."
- Consumer site (MCG-C3): Ashley to redeploy the merged build (front end plus the v44 /api folder: analyze, track, contract, lead) in place and copy env vars (AI key, TRACK_WEBHOOK_URL, Zoho set, contract templates) from the lender project. [verify: done or not]
- CreditDIY: what is live on creditdiy.com is at most the July 24 generation. Stamped Build 2026-09-10.1 (partner and demo) still needs to go up. Footer stamp is the check.

## Tools (the fleet)

| Tool | What it is | Where | Status | Open items |
|---|---|---|---|---|
| MCG Pre-Flight, Automated Credit Review (LO tool, v44) | Parses mortgage credit reports (8 dialects, test suite, validated with Mortgage Nerds); Zoho Sign contract send; 2026 contract suite (6 plans); usage tracking gated on LO email to a webhook | https://mcg-auto-credit-review.vercel.app/ | deployed, not verified | Score Plan tab (ranked score game plan from a parsed report, with disclosures); fold LO Answer Desk in as a second tab (needs the real Answer Desk file; decide whether standalone stays canonical); branded versions per partner company |
| Consumer site (MCG-C3) | Public credit review site, Ledger theme; SmartCredit $1 tri-bureau link wired; LO attribution via ?lo links plus on-page "working with a loan officer?" fallback; "submit to MCG as a lead" via /api/lead | https://mcg-c3-consumer-with-api.vercel.app/ (older c1 deployment still at https://mcg-credit-review-consumer-c1.vercel.app/, and the partner page's generated links point there) | deployed; API merge not verified | see This week; this is now the home of the LO-unique-URL client path (rebuilt here Oct 2026 instead of recovering the lost attribution front end) |
| LO link generator page | LOs make their own consumer-site attribution link; requires work email; logs each link to the tool-usage Google Sheet via Apps Script webhook | https://mcg-lo-partner-page-v2-flat-2.vercel.app/ | handed to Ashley for deployment, not verified | partner contact email still to be supplied; marketing campaign planned around it |
| Credit Readiness (servicemember and veteran site, CR-v6) | Military-framed version of the review tool; SCRA/MLA content; $50 off first payment for veterans and active duty | https://site-military-credit-readiness-crv6.vercel.app/ | deployed [verify] | CROA 1679c consumer-rights disclosure must be confirmed in the enrollment flow before launch; SCRA education deck to add; more veteran resources planned |
| Vetted VA Credit Readiness | ?p=vettedva partner skin on the Credit Readiness build, own Vercel project | URL: add | built, waiting on partner assets and sign-off | disclaimer required (see This week) |
| CreditDIY | Consumer DIY dispute app; partner build (creditdiy.com) and demo build (demo controls, Jane Doe data); prompt library MCG_AI_Prompt_Library.js (7 engines) drives /api | https://creditdiy.com | deployed, old generation | deploy Build 2026-09-10.1 and Rev 2026-09-10.1 library; twin-project comingling check via footer stamp; Ken may hold backend copies |
| LO Answer Desk | LO-facing credit Q&A lookup; per-LO links ?lo=name; Google Sheets webhook with leaderboard; offline buffer | https://mcg-lo-answer-desk.vercel.app/ (also reached through CreditWhat.com) | deployed, taking off with lenders | may merge into the LO tool as a tab |
| MCG Coach Lookup | Internal searchable playbook for coaches (Aug 2026) | URL: add | deployed [verify] | |
| Budget & Goal Builder (v7) | Budgeting for coaches and self-serve clients; credits Erin; tested on a real Credco tri-merge | URL: add | built; deploy status [verify] | requested: guided interview plus voice dictation, per-paycheck breakdown, bill calendar with MCG payment and monitoring dates plus phone reminders, direct-deposit savings split, debt-settlement war chest tracker, credit report import with card reporting dates ("pay before it reports") |
| Autonomous Dispute Engine (Assist and Demo variants) | | URL: add | [verify] | |
| Sales call checklist | Checklist page with Zoho CRM write-back via serverless function | URL: add | [verify] | |
| Coach performance scoreboard (for Tricia) | Weighted Google vs internal review scoring | URL: add | [verify] | |
| One-on-one employee check-in app | Same flat-zip workflow | URL: add | [verify] | |
| Pod web tools | Session 1 decline worksheet; Decline Conversation Playbook (with Coach Lookup script library); Old Ruler, New Ruler comparison | URL: add | [verify] | pod ends Oct 22 |
| CreditWhat.com | Brand hub Sam is building for credit tools and credit knowledge, "credit everything"; marketed to LOs now, who go there to run the simulator and use the knowledge base | https://www.creditwhat.com/ | live | decide how to monetize (sponsorships, affiliate links, or similar) |
| Internal MCG version of the LO tool | Fork of the LO build for MCG staff | none | designed, not started | define scope |

## Referral partner program
- Rule: a partner is cold when 45 days have passed since the most recent of (last referral they sent) and (last time MCG provided value: a client update, a free credit review, including reviews for clients who did not enroll). One clock, one drip, not two tracks.
- Message framing: "it has been about 45 days since we last provided value to you." MCG stays in the giving seat. Templates in ops/VOICE.md.
- Also wanted: outreach to the LO when a client stalls and needs a nudge.
- In Zoho today: RP health grading with monthly file-count shifting (Deluge) [verify it is still running]; a formula tracking deal recency off last-record-created date.
- Data feed: zoho/daily_partner_export writes data/partners.json every morning. Status: not set up.
- Reengagement drip: designed, not built. The morning run drafts the messages. Sending stays with Sam or Zoho until Sam says otherwise.

## Open threads
- 20/20 Vision pod (Christine Beckwith's company; Nicole Heinz-Trefrey coordinates): see This week. Certification for full attendance: Certified Credit Pipeline Strategist.
- Branded partner versions of the review tool: CrossCountry Mortgage (Brandon Adler) first [verify live]; Project Valor (Matthew Clanton, military-style branding) second [verify status]; Vetted VA third (in progress).
- Compliance: MCG-Credit-Review-Data-Flow.docx exists for proactive distribution to partner LOs and their compliance teams.
- Podcast: episode 2 recorded Oct 2026. Episode 1 (collections) did fine but was weak on socials. Want topics with online traction.
- Watch: ESCRA (H.R. 306) and the business-model changes under consideration.
- Possibly stale, confirm or drop: reAlpha due diligence package and partnership framing (Aug 2026); SMS opt-in message for A2P 10DLC/TCPA; Realtor social content strategy.

## People (business roles only)
- Tricia Parker: co-founder, CFO/COO
- Ashley: setup and deployment tasks (Vercel, Sheets webhooks, the link-creator page)
- Ken Brown (RFDM Solutions): external backend developer; may hold backend copies of CreditDIY. Not the default path for anything.
- Erin Stowell: Disputing Team; the Budget & Goal Builder grew from her ideas

## Standing decisions
- Deployment stays non-developer-dependent: single-file HTML (plus /api where needed) on Vercel. From now on the source lives in tools/<name>/ here and each Vercel project's Root Directory points at its folder.
- Five products, each with its own dedicated chat: consumer site (MCG-C3), LO tool (v44), Credit Readiness (CR-v6), internal MCG version (planned), CreditDIY.
- Student-loan doctrine for tools: isolated late, goodwill ask; many lates or loan past saving, call the servicer counselor; often refi into income-based repayment, servicer closes the old loan and opens a fresh one with no lates.
- Ashley's partner link-creator page stays, repointed at the consumer domain.

## Run log
(The morning run appends one line per run: date, partners flagged, tools down, inbox items filed.)
