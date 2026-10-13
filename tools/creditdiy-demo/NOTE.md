# What this file is
index.html was uploaded by Sam on Oct 13, 2026 as "CreditDIY_PARTNER.html".
It reads as the DEMO build, not the partner build:
- page title "CreditDIY Interactive Demo by My Credit Guy"
- on-page banner "Interactive demo: sample data. No real credit data used"
- the "I've set up my account, pull my report" button shows "Loading your sample report..." and loads the Jane Doe sample after 3 seconds instead of pulling a real report
- no Build 2026-09-10.1 stamp anywhere; the only date markers inside are 2026-06-16, so it predates the September baseline
Front end only: it calls /api/parse and /api/payments, which live in the api folder of the flat zip with the prompt library. Not deployable to creditdiy.com on its own.
Still needed: creditdiy-partner-flat.zip and creditdiy-demo-flat.zip stamped Build 2026-09-10.1, plus MCG_AI_Prompt_Library.js Rev 2026-09-10.1.
