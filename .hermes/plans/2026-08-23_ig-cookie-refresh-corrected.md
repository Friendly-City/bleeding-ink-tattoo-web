# Plan: IG Cookie Refresh — Source Correction (Austin Out-Of-Band, 2026-08-23)

> **CORRECTION**: Two earlier versions of this plan were wrong. The truth:
>
> 1. **Austin does own** the cookies. The `ds_user_id` in `active.json` is
>    `34517615` — that's Austin's PERSONAL Instagram account (confirmed live
>    at audit time by reading `ds_user_id` + `sessionid` prefix from the file).
>
> 2. **The cookies are from Austin's personal IG, VIEWING `@ibleedink_600`'s
>    public profile.** Not the other way around. IG lets any logged-in user
>    read public profiles, so the scraper just needs ANY valid IG session.
>    Isiah's account is not required.
>
> 3. **Cookie lifecycle is NOT a coordination problem with Isiah** — it's just
>    "open IG in Chrome, log in to your personal account, export, drop here."
>    No third party involved.

## Current state (verified live 2026-08-23 00:30 ET)

**Active file:** `C:\Users\bbask\Coding_Projects\bleeding-ink-tattoo-web\scripts\cookies\active.json`

(11 cookies, last modified 2026-08-19 16:28 — same as prior audit)

| Cookie | Days remaining | Expires (UTC) | Status |
|--------|---------------:|---------------|--------|
| sessionid, ps_n, datr, ig_nrcb, ig_did, ps_l, mid, csrftoken | +272 to +396 | 2027-05 → 2027-09 | 🟢 healthy |
| **ds_user_id** | +86 | 2026-11-17 20:25 UTC | 🟡 refresh before Nov |
| **wd** | **+3** | **2026-08-26 20:24 UTC** | 🔴 urgent — 3 days left |
| rur | (session) | no expiry | 🟡 placeholder, not critical |

**ds_user_id = 34517615** → confirmed (Austin OOB 2026-08-23) to be his
**personal Instagram**, not Isiah Jackson's. The scraper uses Austin's
session to hit IG's `/api/v1/users/web_profile_info/?username=ibleedink_600`
endpoint (public profile, no auth needed beyond a logged-in browser).

## Refresh procedure (~30 seconds, all by Austin)

No third-party coordination needed. Same procedure as always:

1. Open Chrome → log into instagram.com as **your personal account** (Austin's)
2. Install [Cookie-Editor Chrome extension](https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm) — one-time
3. Click Cookie-Editor icon → **Export** dropdown → **Cookies (JSON)** → **Export to file**
4. Save to `Downloads/ig_cookies_<today>.json`
5. In PowerShell:
   ```powershell
   Move-Item "$env:USERPROFILE\Downloads\ig_cookies_2026-08-23.json" `
            "C:\Users\bbask\Coding_Projects\bleeding-ink-tattoo-web\scripts\cookies\ig_cookies_2026-08-23.json"
   cd "C:\Users\bbask\Coding_Projects\bleeding-ink-tattoo-web"
   python scripts/cookie_refresh.py --path scripts/cookies/ig_cookies_2026-08-23.json
   ```

**Success looks like:**
```
[INFO] Read 11 cookies from ig_cookies_2026-08-23.json
[INFO] Validated: sessionid, csrftoken, ds_user_id present
[INFO] Archived old active.json → archive/<timestamp>.json
[INFO] Wrote new active.json
[INFO] No cookie expires within 7 days. Schedule next refresh in 30 days.
```

## Time pressure

| Cookie | Date | Days from now (2026-08-23) | Action needed |
|--------|------|------|------|
| wd | 2026-08-26 | **3** | Refresh before this or scraper alerts go red |
| ds_user_id | 2026-11-17 | 86 | Refresh in Oct |
| sessionid | 2027-08-19 | 361 | Refresh in mid-2027 |

**The next 30 seconds that matter are:** the ones between now and 2026-08-26
when `wd` expires. Even if the scraper keeps running past `wd`'s expiry
(sessionid is the real auth — `wd` is mostly display-state), the
`e1bf3329` IG cookie watcher cron will keep firing Telegram red alerts
until `wd` is back. Cleaner to refresh now than to mute the cron.

## Rollback if new cookies break the scraper

```powershell
cd "C:\Users\bbask\Coding_Projects\bleeding-ink-tattoo-web"
ls scripts/cookies/archive/ | sort
# Copy the most recent one back
Copy-Item "scripts\cookies\archive\2026-08-19_111915.json" "scripts\cookies\active.json" -Force
```

## Why this is being re-planned in writing

The original plan (`2026-08-22_ig-cookie-refresh-reminder.md`) assumed Austin
owned `@ibleedink_600`'s session — wrong. The middle plan
(`2026-08-23_ig-cookie-refresh-actual-owner.md`) assumed the cookies needed
Isiah's cooperation — also wrong. This is the third and correct version:
the cookies are from Austin's personal IG, viewing `@ibleedink_600`'s public
profile. The procedure is the same as always, just attributed correctly.

This **supersedes both prior plans**. The misleading ones remain on disk
for audit history but should be flagged `[SUPERSEDED 2026-08-23]` if you
want to clean up later.

## Action

- [ ] Austin refreshes cookies within next 3 days (the 30-sec procedure above)
- [ ] Verify by running: `curl -X POST https://graph.instagram.com/v20.0/ig_refresh_token?grant_type=ig_refresh_token&access_token=$IG_TOKEN` (or just trigger a manual scrape test from the bleed-ink-tattoo-web repo)

## Owner

Austin Porada (single-person task, no dependencies)
