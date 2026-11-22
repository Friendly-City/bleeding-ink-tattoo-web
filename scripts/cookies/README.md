# IG Cookie Workspace

This directory holds Instagram session cookies for scraping
[@ibleedink_600](https://instagram.com/ibleedink_600) (and future artists).

## Files

| File | Purpose | Committed? |
|------|---------|-----------|
| `active.json` | Current working cookies (the only file you edit) | ❌ gitignored |
| `archive/<timestamp>.json` | Old cookie sets, auto-archived when you rotate | � gitignored |
| `README.md` | This file | ✅ |

## How to refresh cookies (when IG logs you out)

**Total time: ~30 seconds.** No script edits needed.

1. Open Chrome → log into instagram.com (the account whose work you want to scrape)
2. Install the [Cookie-Editor Chrome extension](https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm)
3. Click the Cookie-Editor icon (cookie/jar icon in extensions bar)
4. Click **Export** → **Cookies (JSON)** → save anywhere (e.g., Desktop)
5. Move the saved file to this directory (`scripts/cookies/`) — name it whatever you want, e.g., `new_cookies.json`
6. Run the refresh script:

```bash
python scripts/cookie_refresh.py --path scripts/cookies/new_cookies.json
```

What it does:
- Validates the new cookie JSON (right keys, requires a `sessionid` cookie to be present)
- Computes days remaining for `sessionid`/`csrftoken`/`ds_user_id` specifically — not the
  soonest-expiring cookie in the file, which is usually a short-lived non-auth one (e.g.
  Instagram's `wd`, a fixed ~7-day cookie) and would otherwise dominate the reported number
- **Archives the old** `active.json` to `archive/<timestamp>.json` (so you have a rollback if needed)
- **Replaces** `active.json` with the new set
- Prints a one-line status (🟢 / 🟡 / 🔴 + days remaining)

After refresh, your next scrape (manual or cron) uses the new cookies.

## Auto-validation

The script checks for:
- ✅ `sessionid` cookie is present (rejects the file otherwise)
- ✅ Cookie file is valid JSON
- ✅ Reports days remaining for the auth cookies specifically (`sessionid`/`csrftoken`/`ds_user_id`)

If validation fails, the script prints what went wrong and exits with a non-zero code. **The old `active.json` is preserved** so you can debug.

## Cookie lifespan (what to expect)

The `sessionid` cookie typically lasts **~30 days**. Status is based on days
*remaining* for the auth cookies specifically (`sessionid`/`csrftoken`/
`ds_user_id`), not the full jar — a full Cookie-Editor export also contains
short-lived non-auth cookies (e.g. `wd`, a fixed ~7-day cookie) that say
nothing about whether the session is still valid:

| days remaining | status              |
|----------------:|--------------------|
| > 21             | 🟢 HEALTHY          |
| 8–21             | 🟡 WATCH            |
| 1–7              | 🟡 REFRESH_THIS_WEEK |
| ≤ 0              | 🔴 EXPIRED           |

The daily cron check (`ig-cookie-health-daily`) only fails (and pages
Telegram) on EXPIRED or an unreadable cookie file — WATCH/REFRESH_THIS_WEEK
print as an advisory, not a failure.

If you notice the scraper failing or no images showing up:
1. Check the Telegram alert from `ig-cookie-health-daily`
2. Re-export cookies (steps above)
3. Re-run the scrape

## Rollback (if new cookies are broken)

```bash
# Pick the most recent archived cookie set
ls scripts/cookies/archive/
cp scripts/cookies/archive/2026-XX-XX_HHMMSS.json scripts/cookies/active.json
```

## Why not just keep cookies in env vars / git?

- **Env vars:** Would require restarting the scraping environment on every cookie refresh — friction.
- **Git:** Even with `.gitignore`, accidentally committing credentials is one of the top 5 causes of token leaks. The `archive/` directory gives you a local-only history without that risk.
