# Bleeding Ink Tattoo Website — Project Setup Plan

> **For Hermes:** Stage 1 of the `local-business-website-pipeline` skill. This is the **setup + research** plan, NOT the build plan. Build plan comes after Austin fills in the intake form.

**Goal:** Stand up a proper, automation-friendly Next.js project folder for the Bleeding Ink tattoo shop, ready to receive business info and build a complete marketing/booking website.

**Architecture:** Fresh Next.js 16 + React 19 + TypeScript + Tailwind v4 site, mirroring the proven `jadas-jazz-cafe-web` structure but custom-tailored for a tattoo studio. This folder becomes the canonical home for the project; all dev work, automation, and future deploy tooling lives here.

**Tech Stack (verified working on this machine 2026-08-17):**

| Layer | Tool / Version | Verified |
|-------|----------------|----------|
| Node | v22.22.0 (`/c/nvm4w/nodejs/node`) | ✅ live |
| npm | 10.9.4 | ✅ live |
| Framework | Next.js 16.2.6 App Router | ✅ proven (jadas-jazz-cafe-web) |
| UI | React 19.2.4 | ✅ proven |
| Language | TypeScript 5 | ✅ proven |
| Styling | Tailwind CSS v4 + inline styles | ✅ proven pattern |
| Fonts | `next/font/google` | ✅ proven |
| Lint | ESLint 9 + `eslint-config-next` | ✅ proven |
| Build | Turbopack disabled via env (avoid 16.x bugs) | ✅ proven |
| Python | 3.11.15 (venv) + 3.14.3 (system) | ✅ live |
| Git | `/mingw64/bin/git` | ✅ live |
| GitHub CLI | `/c/Program Files/GitHub CLI/gh` | ✅ live |
| Firecrawl (local) | `http://localhost:3002/v2/scrape` — bearer `local_dev_key_12345` | ✅ live (smoke tested 2026-08-17) |
| Honcho | `http://localhost:8000` (up but root 404 — use honcho_profile/honcho_search tools, not HTTP) | ✅ live |
| Vercel CLI | not installed yet — `npm i -g vercel` later in deploy phase | ⚠️ Stage 4 |

---

## Verified Facts — What Drives Each Decision

### Fact 1: This folder is the right home

```
$ ls "C:/Users/bbask/Hermes-Workspace/bleeding-ink-website"
(empty)
```

Empty folder, cwd is set. Per `.hermes.md` (workspace-level), production websites live under `C:/Users/bbask/Coding_Projects/`. **Decision:** Use the workspace folder as a **planning/research scratchpad** during setup, then move the actual Next.js project to `C:/Users/bbask/Coding_Projects/bleeding-ink-tattoo-web/` at Stage 3 build time (matches `jadas-jazz-cafe-web` convention). The workspace folder keeps the `.hermes/plans/`, intake doc, research notes, and competitor snapshots for the duration of the project.

### Fact 2: A proven structure already exists locally

`C:/Users/bbask/Coding_Projects/jadas-jazz-cafe-web/` (Next.js 16 + React 19 + TS + Tailwind v4) shipped to production at `jadasjazzcafe.com`. Its AGENTS.md documents exact pitfalls that bit them:
- `jsx: "preserve"` required in tsconfig (Next 16 resets to `react-jsx` and breaks prerendering)
- `global-error.tsx` incompatible with Next 16 App Router — delete it
- `not-found.tsx` must not include `<html>` wrappers
- Remove invalid `experimental.turbo: undefined` from `next.config.ts`
- `npx next lint` returns "Invalid project directory" on some WSL combos — use `npx eslint src/ --max-warnings 999` instead
- WSL2 NTFS SIGBUS crashes when serving from `/mnt/c/...` — copy to `/tmp/` if running `next start` from WSL

**Decision:** Replicate the directory structure and `next.config.ts` pattern. Apply the known fixes proactively so we don't relearn the lessons.

### Fact 3: Tattoo shop websites have specific, documented feature requirements

Three independent sources agree on the same core feature set:

| Source | URL | Date |
|--------|-----|------|
| Qrolic | https://qrolic.com/blog/top-website-features-tattoo-studios-2025/ | 2025-04-28 |
| Seahawk | https://seahawkmedia.com/design/tattoo-website-design-tips/ | 2025-05-01 |
| Nodedr | https://www.nodedr.com/blog/tattoo-studio-website-guide | 2026-06-09 |

**Consensus core features (all 3 sources agree):**
1. **Artist portfolios organized per-artist AND filterable by style** (fine line, traditional, blackwork, realism, Japanese, geometric) — this is THE most important page, not a generic gallery
2. **Consultation request form** (not direct slot booking for custom work) — collects idea, placement, size, reference images, preferred artist/style
3. **Clear deposit policy** upfront (amount, applies to final cost, cancellation terms)
4. **Realistic response-time SLA** ("we respond within 2 business days")
5. **Pricing transparency** — hourly rates, shop minimums, deposit amounts, ballpark for common sizes
6. **About page** — studio story + each artist's bio, specialties, years experience, IG link
7. **Aftercare page** — studio-specific guidance (products they recommend, healing timeline), with medical disclaimer
8. **Flash sheets section** — separate from custom work, for pre-designed pieces at set prices (walk-in / same-day)
9. **Contact / location** — full address, phone, email, hours, embedded Google Map
10. **Local SEO foundation** — schema.org markup, "tattoo shop [city]" + "[style] tattoo artist [city]" page targeting
11. **Reviews / testimonials** — embed Google + Yelp, with healed-tattoo photos
12. **Mobile-first** — Instagram bio link is the dominant traffic source, must load fast on phones

**Sources differ on:**
- Qrolic lists "SSL certificate" and "blog/news section" as core; Seahawk deprioritizes blog in favor of FAQ/aftercare. **Pick FAQ + aftercare + occasional news/updates** (no blog CMS, just markdown content updated by Austin).
- Seahawk emphasizes social media integration; Nodedr deemphasizes it (claims website should be the owned asset). **Include Instagram feed embed on artist pages, but don't depend on it.**

### Fact 4: A tattoo site has 2 specific pages most local-business templates miss

| Page | Why it matters | Sources |
|------|----------------|---------|
| **Flash Sheets** (`/flash`) | Different buyer journey from custom — walk-ins, set price, no consultation. Mixing into the main portfolio hurts both. | Nodedr |
| **Per-Artist Pages** (`/artists/[slug]`) | Most clients pick an artist, not a shop. Each artist needs their own portfolio, bio, specialties, booking link, IG. Rankable for "[style] tattoo artist [city]". | Nodedr, Seahawk |

These are the differentiators from a generic "small business website" template.

### Fact 5: Real example sites for design reference

| Site | Platform | Notable |
|------|----------|---------|
| https://www.sitebuilderreport.com/inspiration/tattoo-websites | Various (Squarespace, Wix, WP, Webflow) | 25+ live examples, platform-tagged |
| https://glossgenius.com/blog/tattoo-website-design | GlossGenius-built | Modern booking-first designs |
| https://colorlib.com/wp/tattoo-studio-website-examples/ | Various | Real studio screenshots |

**Decision:** Browse the Colorlib + Sitebuilderreport galleries during Stage 2 brand direction to pull concrete design references (hero composition, gallery layout, artist page structure) Austin can react to. Do NOT screenshot/copy any specific studio's design — only use as inspiration for our own original layout.

### Fact 6: Booking system options (verified landscape)

Most tattoo studios today use one of:
- **GlossGenius** — booking + payments + forms, SaaS, embed via iframe/widget
- **Booksy** — booking SaaS, embed widget
- **Square Appointments** — booking + payments, embed widget
- **Calendly** — generic scheduling, embed
- **Custom Next.js form → email/Telegram/CRM** — what jadas-jazz-cafe-web does

**Decision (defer to Stage 2):** Ask Austin whether the shop already uses a booking platform. If yes → embed their widget, no custom flow needed. If no → build a consultation request form that emails the shop (mirror jadas-jazz-cafe-web's server-action pattern) and defer real-time booking to "stretch goal."

### Fact 7: Image strategy for a tattoo shop (no stock photos)

Tattoo portfolios are the soul of the site. Stock photos of generic tattoos will destroy credibility instantly. Three sources of real imagery:

1. **Artist-provided photos** (most authentic, best quality) — needs intake form upload field
2. **Scraped from existing social/website** (if shop has Instagram/Facebook) — extract via Firecrawl + direct HTTP
3. **AI-generated placeholder tattoos** for layout demos (MiniMax `mmx image_generate`) — clearly watermarked "DEMO" so no confusion during build phase

**Decision:** Stage 1 intake includes an "upload existing tattoo photos" prompt. Stage 2 review will swap AI demo images with real ones before launch.

---

## What "Proper Setup" Means Here

A proper project folder for this kind of site has:

1. **Clear separation** of plan/research (this folder) from build artifacts (later `Coding_Projects/`)
2. **Version control** initialized from day 1 (even before any code)
3. **Automation hooks** — CI config, deploy scripts, lint/test scripts defined up front
4. **Documentation** — intake form, brand direction, project README, agent guide, all in the repo
5. **Proven pattern baseline** — copy working configs from jadas-jazz-cafe-web, don't reinvent

---

## Phase 1 — Setup (this plan, before Austin fills intake)

### Task 1.1: Verify this folder is empty and writable

```bash
ls "C:/Users/bbask/Hermes-Workspace/bleeding-ink-website/"
# Expected: empty (only . and ..)
mkdir -p "C:/Users/bbask/Hermes-Workspace/bleeding-ink-website/.hermes/plans"
```

### Task 1.2: Initialize `.hermes.md` project-context file

Create the project-context file following the pattern at `C:/Users/bbask/Coding_Projects/Wedding_Website_Clean/.hermes.md` (minimal) and `Coding_Projects/jadas-jazz-cafe-web/AGENTS.md` (detailed agent guide).

**File:** `C:/Users/bbask/Hermes-Workspace/bleeding-ink-website/.hermes.md`

Contents (template):

```markdown
# Bleeding Ink Tattoo Website — Project Context

Purpose: Marketing + booking website for Bleeding Ink Tattoo shop.
Owner: Austin Porada
Primary language: TypeScript / React / Next.js
Package manager: npm
Status: pre-build (Stage 1 — research/intake)

## Important Paths (when build begins)

- Source: `C:/Users/bbask/Coding_Projects/bleeding-ink-tattoo-web/src/`
- Configuration: `C:/Users/bbask/Coding_Projects/bleeding-ink-tattoo-web/package.json`
- Intake doc: `C:/Users/bbask/Hermes-Workspace/bleeding-ink-website/CLIENT-INTAKE.md`
- Research notes: `C:/Users/bbask/Hermes-Workspace/bleeding-ink-website/research/`
- Plans: `C:/Users/bbask/Hermes-Workspace/bleeding-ink-website/.hermes/plans/`

## Required Commands (Stage 3+)

Install: `npm install`
Build: `npm run build`
Test: `npm run lint` (no tests in baseline)
Development: `npm run dev`

## Coding Rules

- Match jadas-jazz-cafe-web patterns: inline styles + Tailwind v4 component classes
- `jsx: "preserve"` in tsconfig.json (Next 16 reset bug)
- No `global-error.tsx` (Next 16 App Router incompatible)
- No `<html>` wrappers in `not-found.tsx`
- Mobile-first — Instagram bio link is primary traffic source
- All portfolio images must be real tattoo photos — never stock
```

### Task 1.3: Create the intake template Austin fills in

**File:** `C:/Users/bbask/Hermes-Workspace/bleeding-ink-website/CLIENT-INTAKE.md`

Based on the `local-business-website-pipeline` skill's intake template, but customized for a tattoo shop. Sections:

1. **Business basics** — name (confirm "Bleeding Ink" exact spelling/style), tagline, address, phone, email, hours, social URLs
2. **Artists roster** — name, IG handle, specialties (free-text or pick-list: traditional, fine line, realism, blackwork, Japanese, geometric, neo-traditional, color, script, coverup, flash), years experience, bio draft
3. **Services + pricing** — hourly rate(s), shop minimum, deposit amount/policy, cancellation policy, walk-in policy, age policy (18+, guardian consent?), piercing?
4. **Booking flow preference** — already using GlossGenius/Booksy/Square/Calendly? OR build custom consultation form?
5. **Existing assets** — logo file, brand colors (if any), existing photos, social media links, current website (if any — we'll scrape)
6. **Brand direction** — bold/gritty vs clean/minimal vs ornate, color palette preference, what should visitors FEEL when they land
7. **Approved site structure** — checkbox list of pages Austin wants:
   - Home, Artists (list), Artist detail page, Portfolio (filterable by style), Flash Sheets, Aftercare, FAQ, Contact, Consultation Request form, About, Reviews, Blog/News (skip?), Shop/merch (skip unless they sell)
8. **Open questions** — anything Austin wants me to research or ask about

### Task 1.4: Create research/ scratch folder

```
research/
├── README.md                  ← what goes here + how to organize
├── 01-competitor-sites.md     ← filled in Stage 1.5
├── 02-design-inspiration.md   ← filled in Stage 2
├── 03-booking-platforms.md    ← filled in Stage 2
└── 04-seo-keywords.md         ← filled in Stage 2
```

### Task 1.5: Initialize git in the workspace folder

```bash
cd "C:/Users/bbask/Hermes-Workspace/bleeding-ink-website"
git init
git add .hermes.md CLIENT-INTAKE.md research/ .hermes/plans/
git commit -m "chore: scaffold project context + intake template"
```

Why git in workspace folder even before code: keeps intake + research versioned, Austin can review changes, and we have a clean baseline before the build-phase repo splits off.

### Task 1.6: Create plan orchestration README

**File:** `C:/Users/bbask/Hermes-Workspace/bleeding-ink-website/.hermes/plans/README.md`

Quick index of all plans in this folder, what stage each covers, what's done vs pending.

---

## Phase 2 — Intake (Austin drives, I wait)

Austin fills `CLIENT-INTAKE.md`. Then Austin messages me to proceed to Stage 1.5 (research on the actual shop) or skips straight to Stage 2 (structure approval).

I will not write code until intake is complete. I will not run any scraping on the shop until Austin confirms the shop name + any existing URLs.

---

## Phase 3 — Research (after intake, conditional on URLs provided)

### Task 3.1: Scrape the shop's existing web presence (if any)

If Austin provides a current website URL, Instagram handle, Facebook page, or Google Business Profile:

```bash
# Local Firecrawl (verified running 2026-08-17)
curl -X POST http://localhost:3002/v2/scrape \
  -H "Authorization: Bearer local_dev_key_12345" \
  -H "Content-Type: application/json" \
  -d '{"url": "<shop-url>"}' | jq .
```

For Instagram/Facebook, expect name + bio + profile image only (login wall). Try `/menu`, `/artists`, `/flash` subpages manually if homepage is GoDaddy/WSite.

### Task 3.2: Search for the shop by name + city

```bash
curl -X POST http://localhost:3002/v2/search \
  -H "Authorization: Bearer local_dev_key_12345" \
  -H "Content-Type: application/json" \
  -d '{"query": "Bleeding Ink Tattoo <city>", "limit": 10}' | jq .
```

Confirms: official URLs, Google listing, Yelp, Chamber of Commerce, social profiles. Cross-reference with what Austin provided.

### Task 3.3: Pull competitor example galleries for design reference

Visit (do NOT copy):
- https://www.sitebuilderreport.com/inspiration/tattoo-websites
- https://glossgenius.com/blog/tattoo-website-design
- https://colorlib.com/wp/tattoo-studio-website-examples/

Screenshot 3-5 designs that match the brand direction Austin chose. Save to `research/02-design-inspiration.md` with what we like about each.

### Task 3.4: Document findings in `research/01-competitor-sites.md`

Standard sections:
- Business name + variations found
- Tagline + bio
- Hours, address, phone, email (verify against intake)
- Social links
- Existing photos found (URLs, no downloads yet)
- Pricing found (if public)
- What they have that's good
- What they have that's bad / gaps we can fill

---

## Phase 4 — Brand Direction (Austin approves)

`research/02-design-inspiration.md` is presented. Austin picks a direction (or a blend). Austin edits `CLIENT-INTAKE.md` brand direction section. Gate: Austin says "approved to build" before any code is written.

---

## Phase 5 — Build (separate plan, written after Phase 4 approval)

Out of scope for this setup plan. Will be a separate bite-sized `writing-plans` document once we know:
- Number of artists (drives artist page count)
- Whether booking is embed or custom form (drives form/server-action complexity)
- Whether shop has logo (drives brand asset setup)
- Color palette choice (drives theme tokens)

Rough scope (for sizing, not detailed):
- 1 home, 1 about, 1 contact, 1 portfolio (filterable), 1 flash, 1 aftercare, 1 FAQ, N artist pages, 1 consultation form, 1 reviews embed
- Server actions: consultation form → email (or Telegram via existing bot)
- Image optimization via `next/image`
- Local SEO: schema.org TattooParlor markup, sitemap, robots.txt, OG tags
- Single-page-locale initially (no i18n unless Austin asks — simpler scope)

---

## Open Questions for Austin (ask before or during intake)

1. **Shop name confirmation** — "Bleeding Ink" exact styling? (Bleeding Ink / BleedingInk / BLEEDING INK / Bleeding Ink Tattoo) — drives logo design and SEO title
2. **City / location** — drives local SEO and Google Map embed
3. **How many artists?** — drives the artist page build
4. **Booking system** — already using one, or build custom form?
5. **Existing website/social?** — drives Stage 3 research scope
6. **Logo** — have one, or generate one?
7. **DEMO_MODE?** — per the pipeline skill, do you want this built as a sales asset too (hire-us page + lead capture), or just the shop's site? Default = STANDARD unless you say otherwise.
8. **Brand direction preference** — bold/gritty (heavy black, gothic, edgy), clean/minimal (white space, modern, premium), or something else?

---

## Files This Plan Creates

| Path | Purpose |
|------|---------|
| `.hermes.md` | Project context (canonical) |
| `.hermes/plans/2026-08-17_000000-tattoo-shop-website-setup.md` | This plan |
| `.hermes/plans/README.md` | Plan index |
| `CLIENT-INTAKE.md` | Austin fills this |
| `research/README.md` | Research folder map |
| `research/01-competitor-sites.md` | Stage 3 output (placeholder) |
| `research/02-design-inspiration.md` | Stage 2 input (placeholder) |
| `research/03-booking-platforms.md` | Stage 2 input (placeholder) |
| `research/04-seo-keywords.md` | Stage 2 input (placeholder) |

Plus one initial git commit with all of the above.

---

## Verification (when "Setup" is done)

```bash
cd "C:/Users/bbask/Hermes-Workspace/bleeding-ink-website"
ls -la
# Expected: .git/ .hermes.md .hermes/ CLIENT-INTAKE.md research/
git log --oneline
# Expected: 1 commit "chore: scaffold project context + intake template"
```

This folder is then "ready to receive" — Austin fills intake, I proceed to Phase 3.

---

## Risks / Tradeoffs

| Risk | Mitigation |
|------|------------|
| Folder split (workspace = plans, Coding_Projects = build) is unusual | Document the path split in `.hermes.md` clearly; any agent can read it and know where to look |
| We don't know shop name spelling yet | Ask in Open Questions section; Austin answers in intake |
| Austin may not have any existing web presence to scrape | Stage 3 is conditional — if no URL, skip straight to brand direction |
| MiniMax `image_generate` watermarks demo tattoo images as "DEMO" → not great for portfolio | Owner must supply real photos; placeholder usage clearly labeled in code comments |
| Stage 5 build plan is not yet bite-sized | Intentional — build plan needs real intake answers to be concrete; writing it now would be guessing |

---

## What Comes Next

1. **Right now:** I execute Phase 1 (Tasks 1.1–1.6) — write all the scaffolding files, init repo, commit
2. **Then:** I hand off to Austin with the 8 open questions listed above and the path to `CLIENT-INTAKE.md`
3. **Then Austin:** fills intake, drops real photos in `research/`, optionally links existing site/social
4. **Then I:** execute Phase 3 research + Phase 4 brand direction, wait for "approved to build"
5. **Then I:** write the bite-sized build plan in `.hermes/plans/`, execute via subagent-driven-development

---

**Plan complete and saved at:** `C:/Users/bbask/Hermes-Workspace/bleeding-ink-website/.hermes/plans/2026-08-17_000000-tattoo-shop-website-setup.md`

Ready to execute Phase 1 immediately — Austin, give me the go-ahead (or just say "go" / "do it") and I'll scaffold the folder.