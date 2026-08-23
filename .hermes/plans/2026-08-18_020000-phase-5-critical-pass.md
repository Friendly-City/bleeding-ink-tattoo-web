# Phase 5 — Critical-Pass Expansion Plan

> **Date:** 2026-08-18
> **Live URL:** https://bleeding-ink-tattoo-web.inquiry-970.workers.dev
> **Goal:** After confirming Phase 4 (3 P0 + 5 P1 + 4 P2) is fully complete, push the demo closer to production-quality through
the remaining critical gaps.

---

## Status: Phase 4 — 12/12 DONE ✅

Verified via `git log` + `python scripts/selftest-demo.py` (13/13) + site-wide audit:

- [x] **P0.1** Portfolio grid with 8 SVG cards + style filter — commit `534a674`
- [x] **P0.2** Consultation form on /book (10 fields + sidebar) — commit `534a674`
- [x] **P0.3** Contact form success polish — commit `534a674`
- [x] **P1.4** /aftercare 7-section healing guide — commit `c649c29`
- [x] **P1.5** IG feed on home (6 mock posts) — commit `f9c2fdb`
- [x] **P1.6** Reviews section (3 testimonials) — commit `f9c2fdb`
- [x] **P1.7** Hero backdrop SVG art — commit `7be60b7`
- [x] **P1.8** Improved 404 page — commit `344b04a`
- [x] **P2.9** FAQPage JSON-LD — commit `344b04a`
- [x] **P2.10** Mobile sticky CTA — commit `344b04a`
- [x] **P2.11** Breadcrumbs + JSON-LD — commit `7be60b7`
- [x] **P2.12** Per-page OG SVG images — commit `eaf9d14`

**SEO/a11y foundation added on top of Phase 4:**
- [x] sitemap.xml + robots.txt — commit `6dfa4d1`
- [x] Body bg a11y fix (transparency issue) — commit `d5cab54`
- [x] Self-test script (`selftest-demo.py`) — commit `6dfa4d1`
- [x] Real Lighthouse audit + reports — commit `aaf9633`
- [x] Visibility fix (Reviews Johnstown PA opacity) — commit `217a808`

---

## What's NOT in scope of Phase 4 (the gaps this plan fills)

### Gaps identified from live audit (2026-08-18):

1. **`/book` page has 0 `<h2>` tags** — no section structure. Hero + 2 h3s then jumps to deeper levels. Lighthouse `heading-order` failure.
2. **`/portfolio` page has only 1 `<h2>`** — same heading-order issue. 9 `<h3>` filters with no section structure.
3. **Every page** has `label-content-name-mismatch` (8/8 routes) — visible text labels without matching accessible names. Lighthouse 8/8 failures.
4. **`/` home page** has `aria-prohibited-attr` (3 nodes) — likely the CTA icon spans.
5. **`/`, `/aftercare`, `/portfolio`** still have `color-contrast` failures — LONGLIVEMYBRUDDAS marker + aftercare section numbers.
6. **`/book`, `/portfolio`** have `heading-order` issue — need section h2s.

### Pages competitors have that we DON'T:
- **No `/pricing` or `/rates`** — competitors show starting prices
- **No `/gift-cards`** — competitors offer gift cards
- **No `/testimonials` standalone** — we have it on home only
- **No individual `/services/[slug]` detail pages** — competitors have deep service pages
- **No `/legal` (privacy policy + terms)** — needed for form submissions + ad compliance
- **No `/hours` standalone** — hours are buried in contact
- **No `mailto:` or `tel:` formatting** — phone numbers might not be click-to-call
- **No `package.json` typo fixes / type improvements** — Next 16 strict TS could be tightened

### UX gaps:
- **No page-level `<noscript>` fallback** for JS-disabled
- **No focus-trap on mobile menu drawer** (a11y issue)
- **No skip-to-content link** (a11y issue)
- **No breadcrumb on home** (correctly omitted) but missing from `/artists` index page
- **No `aria-current="page"` on active nav link**
- **No `rel="nofollow"` on external social links**
- **No `loading="lazy"` on portfolio SVG cards** (page-load perf)
- **No service-schema for each service** (would help Google show service cards in search)
- **No "We're open today" dynamic indicator** based on hours
- **Footer phone is just text** — should be `<a href="tel:">`

---

## Phase 5 — What to build (priority order)

### P0 — Real-world polish (4 changes, ~45 min)

**1. Add proper heading structure to `/book`**
   - Add `<h2>What happens next</h2>` section heading above the sidebar + 4-step list
   - Add `<h2>Tell us about your idea</h2>` section heading above the form (if missing)
   - Fixes heading-order Lighthouse failure on /book
   - File: `src/app/book/page.tsx`

**2. Add proper heading structure to `/portfolio`**
   - Add `<h2>The Studio Collection</h2>` above the portfolio grid
   - Add `<h2>How this work was done</h2>` (or similar) below the grid
   - File: `src/app/portfolio/page.tsx` (or component `PortfolioGrid.tsx`)

**3. Fix `label-content-name-mismatch` on every page**
   - The hamburger nav toggle (`<button>` with `aria-label="Open menu"`) doesn't have visible text — and LH doesn't like that.
     - Fix: change `aria-label` to `aria-controls="nav-menu"` + add `aria-expanded`. No visible-text issue if aria-label removes content.
   - Skipped for now: this is hard to diagnose without per-page reasoning. Will pass with home page fix + add an action plan.

**4. Fix CTA strip `aria-prohibited-attr` on home**
   - The CTA strip has icon-style spans inside Links that use improper aria roles.
   - File: `src/app/page.tsx` (CTA section)

### P1 — Content depth + critical missing pages (6 changes, ~2 hr)

**5. Add `/pricing` or rate disclosure block**
   - Add a "Starting prices" section to `/services` (don't make a whole new page yet — keep demo).
   - "Custom tattoos: starting at $120/session. Coverups: starting at $200/session."
   - Mention hourly rates: "Most sessions: $150-200/hr."
   - File: `src/app/services/page.tsx` + add to `services.ts` data

**6. Add a legal/minimal `/legal` page**
   - Privacy policy + terms stub (template text)
   - Required before any real form submission can be GDPR/CCPA-compliant
   - File: `src/app/legal/page.tsx` + add to footer

**7. Convert phone numbers to `tel:` links sitewide**
   - Home, /contact, Footer, /book, MobileStickyCTA — currently text, should be `<a href="tel:+12159801386">`
   - Files: Footer.tsx, MobileStickyCTA.tsx, page.tsx, contact/page.tsx, book/page.tsx

**8. Add `rel="noopener"` + `target="_blank"` to external social links**
   - Footer Instagram, Facebook, Threads links
   - Already partially done — verify + complete
   - File: `src/components/Footer.tsx`

**9. Add `aria-current="page"` to active nav link**
   - Navbar: highlight current page in nav (left border, underline, color change)
   - File: `src/components/Navbar.tsx`

**10. Add per-service JSON-LD `Service` schema**
    - Each of the 4 services gets a `Service` JSON-LD block (priceRange, provider)
    - Boosts Google search appearance (service cards)
    - File: add to `src/lib/metadata.ts` or new `src/lib/jsonld.ts`

### P2 — Performance + UX polish (6 changes, ~1 hr)

**11. Add `<noscript>` fallback for SEO**
    - Meta noindex + banner if JS is disabled, since Next.js SSG delivers static HTML

**12. Mobile menu focus-trap + `Escape` to close**
    - When drawer is open, trap Tab focus inside + Esc closes
    - Need to upgrade MobileMenu / drawer state
    - File: `src/components/Navbar.tsx` (drawer handling)

**13. Add `loading="lazy"` + `decoding="async"` to portfolio SVGs**
    - Currently images load eagerly
    - File: `src/components/PortfolioCard.tsx` + `TattooSVG.tsx`

**14. Add "Open today" indicator to Footer or Navbar**
    - Dynamic check against SHOP.hours + day-of-week
    - Small green dot or "We're open today until 7 PM" near phone number

**15. Add skip-to-content link (visible on focus only)**
    - Currently layout has it but visual styling hides it always
    - Should become visible when focused (`:focus`)
    - File: `src/app/globals.css`

**16. Tighten TypeScript config**
    - Enable `strict: true` + `noUncheckedIndexedAccess: true` if not already
    - Fix any resulting type errors

---

## Files likely to change

| Path | Items |
|------|-------|
| `src/app/book/page.tsx` | P0.1, P2.7 |
| `src/app/portfolio/page.tsx` | P0.2 |
| `src/app/page.tsx` | P0.4, P2.7 |
| `src/app/services/page.tsx` + `services.ts` | P1.5 |
| `src/app/legal/page.tsx` (new) | P1.6 |
| `src/components/Footer.tsx` | P1.7, P1.8, P2.14 |
| `src/components/MobileStickyCTA.tsx` | P1.7 |
| `src/components/Navbar.tsx` | P1.9, P2.12 |
| `src/lib/metadata.ts` or new `src/lib/jsonld.ts` | P1.10 |
| `src/app/layout.tsx` | P2.11 |
| `src/components/PortfolioCard.tsx` + `TattooSVG.tsx` | P2.13 |
| `src/app/globals.css` | P2.15 |
| `tsconfig.json` | P2.16 |

---

## Tests / validation

1. Run `selftest-demo.py` after each batch — should stay at 13/13.
2. Run real Lighthouse via 1mcp chrome-devtools-mcp_1mcp_lighthouse_audit on each route.
3. New Lighthouse target: **Avg A11y 98+** (currently 97.4, lowest page / at 91).
4. After fixes, every route should show `/` ≤ 2 lighthouse failures (currently 3).
5. Manual smoke test: open site in browser, click phone number — should try to dial.

---

## Risks / tradeoffs / open questions

- **Skip privacy policy content?** — I'm using template language. Acceptable for demo since this is a demo, NOT a privacy disclaimer.
- **Tel: format:** the shop's number is `(215) 980-1386` — use `tel:+12159801386` (no dashes, +1 prefix for E.164).
- **Heading order fix:** Some sections are intentionally using h3 for "side info" (e.g. the artists page mini-cards). I might use h2 for top-level then h3 nested sub-sections. Will inspect each case.
- **aria-prohibited-attr fix:** Could be an `<i>` icon inside an `<a>` link with `aria-hidden="true"`. Often the fix is removing the `role` or moving `aria-hidden` correctly.
- **Service schema per service:** Will need to be careful not to bloat the HTML on pages with multiple services.
- **I don't need 1mcp for these** — purely file changes + build/deploy.

---

## Estimated time

- P0 (4 changes): 45 min + 1 deploy
- P1 (6 changes): 2 hr + 1 deploy
- P2 (6 changes): 1 hr + 1 deploy
- **Total: ~4 hr of work + 3 deploy cycles**

---

## Decision needed before starting

Austin, **do you want all 16 in this plan, or should I ask you for priorities first?** My default is: do all 16, deploy in 3 batches (P0, P1, P2), and re-run the lighthouse audit at the end to show before/after.

After Phase 5 lands, **what would you want for Phase 6?** (Possible: real-time hours indicator, blog/news section, multi-image portfolio gallery, real Instagram embed via oEmbed, multilingual support, dark mode toggle, CMS integration via Sanity/Contentful, real newsletter signup, etc.)

Save location: `.hermes/plans/2026-08-18_020000-phase-5-critical-pass.md` in the active project workspace.
