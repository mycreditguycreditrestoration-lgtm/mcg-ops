# Zoho daily partner export, setup (about 15 minutes)

What it does: every morning, Zoho writes one file, `data/partners.json`, into the mcg-ops repo. That file is how Claude knows who is going cold. Zoho pushes; Claude never logs into Zoho.

## 1. GitHub token (3 min)
1. GitHub > your profile picture > Settings > Developer settings > Personal access tokens > Fine-grained tokens > Generate new token.
2. Name: `zoho-partner-export`. Expiration: 1 year (set a calendar reminder). Repository access: Only select repositories > `mcg-ops`.
3. Permissions > Repository permissions > Contents: Read and write. Nothing else.
4. Generate, copy the token. You only see it once.

## 2. Match the field names (5 min)
1. Zoho CRM > Setup (gear) > Developer Space > APIs > API Names.
2. Open the module your referral partners live in (Contacts, or a custom module). Write down the API names for: full name, company, email, phone, partner type, RP health grade, last referral date, last value date, and the 30-day file count if you have one.
3. In `daily_partner_export.deluge`, change the `f_` lines in the SETTINGS block to match. If a field does not exist yet (for example a "last value date"), create it in the module first, or set the line to a field you do have. The 45-day clock needs both dates to work properly; until the second one exists, Claude will say so in the brief instead of guessing.
4. `partner_filter`: the criteria that picks out referral partners. The sample is `(Contact_Type:equals:Referral Partner)`. Use your field and your picklist value. If partners live in their own module, set the filter to `""`.

## 3. Paste the function (3 min)
1. Setup > Developer Space > Functions > + New Function.
2. Function name: `daily_partner_export`. Category: Standalone (sometimes shown as "Scheduled"). Create.
3. Delete the sample code, paste the whole file, fill in the SETTINGS block (token, GitHub username). Save.
4. Click Execute (or Save & Execute). Check the log at the bottom: you want `Exported N partners` and a GitHub response that includes `"content"`. On GitHub, `data/partners.json` now shows real data.

If the log says `Bad credentials`, the token is wrong or not scoped to this repo. If it says `Not Found`, check `gh_owner` and `gh_repo`. If a field name is wrong, the value comes through blank rather than crashing, so compare one partner in the file against their record.

## 4. Schedule it (2 min)
1. Setup > Automation > Schedules > + Create New Schedule.
2. Name: `Daily partner export to GitHub`. Function to be executed: `daily_partner_export`. Frequency: Daily, at 5:00 AM (your time, before the morning run). Save.

## Notes
- Menu names move around a little between Zoho editions; the pieces are Functions, Schedules, and API Names.
- The token lives inside Zoho only. Never paste it into a chat.
- Want more in the file (stalled clients, upcoming appointments)? Add them the same way: a search on the Deals or Events module, a map per record, `payload.put("stalled_clients", list)`. Tell Claude and it will write that block for you.
