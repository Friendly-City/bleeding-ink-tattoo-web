# Plan: IG Cookie Refresh — Owner Dependency (Corrected 2026-08-23)

> **Correction from prior plan**: This was originally written as a 30-second
> task for the project owner (Austin). That was WRONG. Austin built the
> website for the shop but is NOT the [@ibleedink_600](https://instagram.com/ibleedink_600)
> account holder. The cookies must come from a real browser login as the
> shop's account, which means **Isiah Jackson (the shop owner)** must do
> the cookie export, not Austin. This plan correctly attributes the work.

## Why this is NOT on Austin's plate

- **Shop IG account holder**: Isiah Jackson / Bleeding Ink Tattooing (per
  `CLIENT-INTAKE.md` lines 21, 29, 57-58 — confirmed by Austin 2026-08-17
  that the @ibleedink_600 handle "is the SHOP's account, not [Austin]'s").
- **PITCH.md target audience**: "For: Isiah Jackson (owner) — sales pitch
  conversation". The whole project is built FOR Isiah, not BY him on
  Austin's behalf.
- **Austin does not have**: the IG password, 2FA device, or any way to
  authenticate as `@ibleedink_600` to obtain fresh sessionid/csrf cookies.
- **IG cookie export requires**: a real logged-in browser session at
  instagram.com. Headless/captive logins are blocked by IG fingerprinting.

## Current state (verified live 2026-08-23 00:25 ET)

**Active file**: `C:\Users\bbask\Coding_Projects\bleeding-ink-tattoo-web\scripts\cookies\active.json`
(last modified 2026-08-19 16:28, 3.5 days old)

| Cookie | Days remaining | Expires (UTC) | Status |
|--------|---------------:|---------------|--------|
| ps_n, datr, ig_nrcb, ps_l, mid | +270 to +311 | 2027-05 → 2027-06 | 🟢 healthy |
| ig_did | +272 | 2027-05-23 | 🟢 healthy |
| csrftoken | +396 | 2027-09-23 | 🟢 healthy |
| sessionid | +361 | 2027-08-19 | 🟢 healthy |
| **ds_user_id** | **+86** | **2026-11-17 20:25 UTC** | 🟡 refresh before Nov |
| **wd** | **+3** | **2026-08-26 20:24 UTC** | 🔴 **urgent — 3 days left** |
| rur | (session) | no expiry | 🟡 placeholder, not critical |

The **sessionid** is good for 361 days (long-lived), so technically the scraper
might keep working past the 3-day `wd` expiry (Instagram treats `wd` as a UX
pref cookie, not a security one). But:
- The 4-day rolling cron alert sends Telegram red warnings on `wd` ≤ 7 days
- Many IG endpoints reset on `wd` mismatch
- The next hard cliff (besides `wd`) is `ds_user_id` on **2026-11-17**

## Three workable paths

### Path A (correct one-time): Isiah exports the cookies

Need:
- Isiah to open instagram.com in his browser, logged in
- Isiah installs Cookie-Editor extension (or you walk him through it on a call)
- Isiah exports cookies → sends to Austin over Signal/Discord
- Austin drops the JSON into `scripts/cookies/` and runs the refresh script

**Action**: This needs to happen **before 2026-08-26 20:24 UTC**. The Isiah-
handoff conversation is the natural moment to do this (he already signed off
on IG photo usage 2026-08-19 per CLIENT-INTAKE line 64 — he knows you're
working with his data).

### Path B (de-risk without Isiah): Patch the scrape cron to ignore `wd`

If Isiah is slow / unreachable for a few days, the right stop-gap is to
patch the scraper to NOT treat `wd` as a hard failure. Edit
`scripts/scrapers/instagram.py` (or wherever the cookie check lives) to
warn-only on missing `wd` instead of erroring out. The sessionid is the
real auth cookie; `wd` is mostly display-state. After the patch, the cron
stops red-alerting and Isiah can refresh at his convenience.

### Path C (right answer long-term): Move cookie ownership to Isiah

The cookies currently live in **Austin's** repo, which means they only
work when Austin's box is online, and only when scraped FROM Austin's box.
That's fragile. Right answer: bake the cookie management into the
production pitch site (Cloudflare Worker at
bleeding-ink-tattoo-web.inquiry-970.workers.dev) so IG portfolio refresh
runs server-side with cookies Isiah rotated ONCE per 30 days via a small
admin form (or a Resend-driven magic link). This is the right design for
the eventual handoff but is beyond the cron-audit scope right now.

## Refresh procedure (when Isiah is ready)

The full procedure is in `scripts/cookies/README.md`. Short version:

1. Isiah opens Chrome → instagram.com → logs in as `@ibleedink_600`
2. He opens Cookie-Editor extension → Export → Cookies (JSON)
3. He sends the file to Austin (Signal, DM, whatever)
4. Austin:
   ```
   Move-Item "ig_cookies_<date>.json" "C:\Users\bbask\Coding_Projects\bleeding-ink-tattoo-web\scripts\cookies\ig_cookies_<date>.json"
   cd "C:\Users\bbask\Coding_Projects\bleeding-ink-tattoo-web"
   python scripts/cookie_refresh.py --path scripts/cookies/ig_cookies_<date>.json
   ```

**Success looks like:**
```
[INFO] Read 11 cookies from ig_cookies_<date>.json
[INFO] Validated: sessionid, csrftoken, ds_user_id present
[INFO] Archived old active.json → archive/<timestamp>.json
[INFO] Wrote new active.json
[INFO] No cookie expires within 7 days. Schedule next refresh in 30 days.
```

## Rollback if new cookies break scraper
```bash
ls scripts/cookies/archive/
cp scripts/cookies/archive/<most-recent>.json scripts/cookies/active.json
```

## Action items for Austin (decision required)

- [ ] **Pick Path A / B / C** for handling this 3-day-out cookie expiry
- [ ] If Path A: schedule a 5-min Isiah call or DM to walk him through Cookie-Editor export
- [ ] If Path B: I can patch the scraper to warn-only on missing `wd` (5-line change)
- [ ] If Path C: out of scope right now, file as future work after the build is shipped

## Why this matters beyond just the 3-day cliff

The cron `e1bf3329` that watches IG cookies has been firing red alerts
since `wd` hit the 7-day-remaining threshold. The next 3-day window is
`ds_user_id` on 2026-11-17 — but you'll see red alerts 7 days before that
(2026-11-10). Same dependency on Isiah unless Path B/C is taken.

## Related findings from the 2026-08-22 cron audit

- **`e1bf3329` IG cookie watcher**: GREEN (alerting correctly). Documented
  in cron audit logs at `~\AppData\Local\hermes\cron\manual-audit-20260822\`.
  The alert is real, not a bug.
- **The fix path**: stop-gap patches must come paired with a written plan
  (Austin-validated 2026-08-22). This file IS that plan for the IG-side
  half; the PR Mirror side has its own plan at
  `.hermes\plans\2026-08-22_pr-mirror-pause-restore.md`.

## Owner

Austin Porada (project coordinator)
Isiah Jackson (cookie holder / shop owner) — blocking dependency for Path A
