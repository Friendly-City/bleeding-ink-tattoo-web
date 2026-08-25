#!/usr/bin/env python3
"""
Daily IG cookie health check for bleeding-ink-tattoo-web.

Thin wrapper around the project-agnostic scrape library. Reads
scripts/cookies/active.json, reports cookie age + last-scrape freshness.

The exit code reflects AUTH-cookie health only (sessionid/csrftoken/
ds_user_id) -- a full Cookie-Editor export routinely includes short-lived
telemetry cookies (e.g. Instagram's `wd`, a fixed ~7-day TTL) that have no
bearing on whether the login session itself still works. The all-cookie
minimum is still printed for context.

Exit codes:
    0 - healthy, or advisory (auth cookies still valid, even if inside the
        REFRESH_THIS_WEEK/WATCH window)
    2 - unusable: auth cookies expired, no active cookies file, cookie file
        corrupt, or no auth cookie found in the jar at all
"""

from __future__ import annotations
import json
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, "C:/Users/bbask/Hermes-Workspace/scripts")

from scrape.providers.cookies import (  # noqa: E402
    load_cookies, CookieError,
    cookie_days_remaining, auth_cookie_days_remaining, status_label,
)


COOKIES_PATH = Path(__file__).resolve().parent / "cookies" / "active.json"
LAST_SCRAPE_LOG = Path(__file__).resolve().parent / "cookies" / ".last_scrape"


def main():
    print(f"=== IG cookie health ({datetime.now().isoformat(timespec='seconds')}) ===")

    if not COOKIES_PATH.exists():
        print(f"CRITICAL: no active cookies at {COOKIES_PATH}")
        print(f"  action: export cookies from Chrome Cookie-Editor, save there, "
              f"then run scripts/cookie_refresh.py")
        return 2

    try:
        storage = load_cookies(COOKIES_PATH)
    except CookieError as e:
        print(f"CRITICAL: active cookies are corrupt: {e}")
        return 2

    cookies = storage["cookies"]
    all_days = cookie_days_remaining(cookies)
    all_status, all_emoji = status_label(all_days)
    auth_days = auth_cookie_days_remaining(cookies)
    auth_status, auth_emoji = status_label(auth_days)
    print(f"cookies: {len(cookies)} loaded, all-cookie min: {all_days} ({all_emoji} {all_status})")
    print(f"auth cookies (sessionid/csrftoken/ds_user_id): {auth_days} days remaining "
          f"({auth_emoji} {auth_status})")

    if LAST_SCRAPE_LOG.exists():
        try:
            mtime = datetime.fromtimestamp(LAST_SCRAPE_LOG.stat().st_mtime)
            age_days = (datetime.now() - mtime).total_seconds() / 86400
            print(f"last scrape: {age_days:.1f} days ago ({mtime.isoformat()})")
            if age_days > 14:
                print(f"  stale (>14d). Consider re-running update_portfolio.py")
        except Exception:
            pass
    else:
        print("last scrape: never (no .last_scrape file)")

    # Decide exit code from AUTH cookies only -- see module docstring. A
    # short-lived non-auth cookie decaying must never fail this check.
    if auth_days is None:
        print("\n!! no sessionid/csrftoken/ds_user_id cookie found - auth "
              "status is UNKNOWN. Treating the jar as unusable.")
        return 2
    if auth_days <= 0:
        print("\n!! auth cookies are EXPIRED. Refresh from Chrome.")
        return 2
    if auth_status in ("REFRESH_THIS_WEEK", "WATCH"):
        print(f"\n{auth_status}: auth cookies expire in {auth_days} days. "
              f"Plan a refresh soon (advisory only, not a failure).")
    print("\nOK: auth cookies are valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
