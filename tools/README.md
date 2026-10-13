# tools/

One folder per live tool. The folder holds exactly what you would have zipped: `index.html` at the top, plus `/api` if the tool has serverless functions, plus any assets.

Folder names (match data/tools.json): lo-tool, consumer-site, lo-link-generator, credit-readiness, creditdiy, creditdiy-demo, lo-answer-desk, coach-lookup, budget-goal-builder, dispute-engine, sales-call-checklist, coach-scoreboard, one-on-one, pod-tools, creditwhat.

## Getting the current builds in (one time)
Unzip each flat zip on your computer and drag its contents into the matching folder on GitHub (open the folder, "Add file" > "Upload files"). Commit. If a folder does not exist yet, create it by uploading into a path: on the upload page type `tools/lo-tool/` ahead of the filename.

## Connecting Vercel (per tool, about 5 minutes)
Existing project (keeps its domain and env vars):
1. Vercel > the project > Settings > Git > Connect Git Repository > pick `mcg-ops`.
2. Settings > General > Root Directory > set to the tool's folder, for example `tools/consumer-site`. Save.
3. Framework Preset: Other. Build command: none. Output directory: leave blank (the folder itself is the site).
4. Push a small change (or Deployments > Redeploy). From then on, a commit to that folder is a deploy. The zip-drag still works any time; it just deploys the same files.

New tool:
Vercel > Add New > Project > Import `mcg-ops` > Root Directory = the folder > Deploy.

## Env vars
Env vars (AI key, TRACK_WEBHOOK_URL, Zoho settings, contract templates) stay in Vercel, never in this repo. The operating doc lists which project needs which.

Vercel team: my-credit-guy. Each project has one stable production address, <project-name>.vercel.app, and that is what goes in data/tools.json. Addresses with a hash in the middle (project-abc123xyz-my-credit-guy.vercel.app) are single deployments; they change every deploy and are not monitored.
