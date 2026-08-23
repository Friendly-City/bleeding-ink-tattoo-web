# Stage 2 — Brand Direction & Site Structure

> **Status:** Draft for Austin's review. Approved → unlocks Stage 3 build plan.
> **Date:** 2026-08-17
> **Method:** All recommendations grounded in (a) the shop's actual public voice/identity (from FB page + IG `@ibleedink_600`) and (b) research from `research/01-competitor-sites.md`, `research/02-design-inspiration.md`, `research/03-booking-platforms.md`, `research/04-seo-keywords.md`.

---

## 1. The Brand (what we know, sourced)

Sourced from confirmed-only public sources (FB page, IG `@ibleedink_600`):

- **Name**: Bleeding Ink (FB page: Bleeding Ink Tattooing)
- **Owner**: Isiah Jackson (confirmed by Austin 2026-08-17)
- **Artist #1**: Courtney Fetzer (confirmed apprentice, started Jun 19 2026)
- **Voice from public channels** (literal quotes):
  - FB page: *"Appointments preferred but walk-ins always welcome, free consultation, min Deposit $65 none refundable! talented artist, wide variety of style coverups as well with competitive pricing!"*
  - IG reels: *"bleeding ink back in full effect even tho I never left"* / *"imma be the youngest in charge watch"* / *"trust money💯"*
  - IG bio hashtags: `#ifyoudontgettattedyourscatted`, `#LONGLIVEMYBRUDDAS`, `#explorepage`, `#mostslepton`, `#freestyle`, `#keepsleeping`
- **Memorial / values tagline**: `LONGLIVEMYBRUDDAS 🪦🕊️` + `#ifyoudontgettattedyourscatted` — part of Isiah's personal identity
- **Positioning signals**: coverups, walk-ins welcome, free consultation, color work (visible portfolio pieces: 💐 + 🐢), competitive pricing, young/hustle culture
- **What this brand voice is NOT**: corporate, polished-corporate, luxury, "fine art gallery" sterile

**Implication for design**: lean into authentic, street-cred, hustle culture. Not luxury. Not minimalist-scandinavian. Real.

---

## 2. Three Brand-Direction Options

Three viable directions, all faithful to the voice. Pick one, or mix.

### Option A — **Street / Hustle** (RECOMMENDED)

The brand voice is already this. Lean all the way in.

| Element | Choice |
|---------|--------|
| **Mood** | Raw, energetic, unapologetic. Think streetwear-meets-tattoo-shop, not "tattoo parlor." |
| **Color palette** | Primary: **deep red (#8B0000)** = blood/bleeding. Accent: **off-black (#0A0A0A)** + **bone white (#F5F1E8)**. Optional pop: **gold (#C9A84C)** for CTAs/prices. |
| **Typography** | Display: **Anton** (condensed sans, free on Google Fonts, screams tattoo-shop signage). Body: **Inter** (clean, legible, mobile-first). Optional: **Permanent Marker** for handwritten accents (tagline, "trust money", etc.). |
| **Photography** | High-contrast B&W with selective color on the ink itself. Real tattoo photos, no stock. iPhone-shot IG aesthetic > studio lighting. |
| **Hero treatment** | Full-bleed tattoo photo with `BLEEDING INK` set in Anton across it, slight rotation, with the tagline underneath in Permanent Marker |
| **Signature element** | 🩸 emoji / red blood-drip divider between sections |
| **Footer** | "LONGLIVEMYBRUDDAS 🪦🕊️" in Permanent Marker, left-aligned, small |
| **Risk** | Can read "edgy 2010s tumblr" if overdone. Avoid all-caps everywhere, avoid skull overload, avoid glitch effects. |
| **Real-world refs** | Sailor Jerry brand identity, Suicide Silence, Lil Wayne mixtape covers, classic Lowrider magazine |

### Option B — **Modern Boutique**

Same voice, slightly more grown-up. Like a tattoo studio that happens to have a hustler's edge.

| Element | Choice |
|---------|--------|
| **Mood** | Boutique-clean, confident, monochrome with one bold accent |
| **Color palette** | Primary: **ink black (#0F0F0F)** + **paper (#FAFAF7)**. Accent: **single bold red (#C8102E)** for CTAs + hover states. Optional: muted gray (#8A8A8A) for body text accents. |
| **Typography** | Display: **Playfair Display** (serif, free on Google Fonts, contrast to the grit). Body: **Inter**. Optional: **JetBrains Mono** for prices/deposit amounts. |
| **Photography** | Editorial — clean backgrounds, less IG-feed. Real tattoo photos but cropped tight, framed, considered |
| **Hero treatment** | Big editorial tattoo photo with the shop name in Playfair, tagline in italic beneath |
| **Signature element** | Thin red horizontal rule under each section heading |
| **Risk** | Can drift into "luxury spa" territory. The memorial tagline + hustle voice need to stay to keep authenticity. |
| **Real-world refs** | Bang Bang NYC, JonBoy Tattoo, references in Gloss Genius blog top-tattoo-sites |

### Option C — **High-Contrast Illustrated** (most distinctive)

The most different. Uses graphic novel / comic-book aesthetic.

| Element | Choice |
|---------|--------|
| **Mood** | Graphic, illustrated, like a tattoo flash book meets a comic book |
| **Color palette** | Primary: **oxblood (#6B0F1A)** + **ivory (#FBF6E9)** + **ink (#1A1A1A)**. Optional: **electric blue (#1E5FFF)** or **chrome yellow (#FFD60A)** for pops |
| **Typography** | Display: **Bungee** (free, blocky, poster-style) or **Rubik Mono One**. Body: **Inter**. Hand-drawn accents via SVGs in the margins. |
| **Photography** | Mixed: real tattoo photos in a grid, mixed with custom SVG illustrations of tattoo motifs (drip, flame, skull, rose) |
| **Hero treatment** | Illustrated tattoo flash motifs forming a border + big Bungee headline |
| **Risk** | Highest build effort (need custom SVGs). Most polarizing — owners either love it or hate it. |
| **Real-world refs** | Sailor Jerry's flash art, Ed Hardy's modern revival, traditional Americana tattoo style |

---

## My recommendation: **Option A (Street / Hustle)**

It matches the existing voice exactly, costs the least to build (no custom SVGs), and reads as authentic rather than performed. If Isiah wants to elevate into Option B later (boutique polish), the color/typography choices can swap without rewriting layouts.

---

## 3. Site Structure (proposed)

7-page Next.js App Router site. Mobile-first. IG bio is primary traffic source so every page is shareable.

```
/
├── /                        ← Home (hero + featured artists + featured work + CTA)
├── /artists                 ← All artists grid
│   ├── /artists/isiah-jackson
│   └── /artists/courtney-fetzer
├── /portfolio               ← Style-filtered portfolio grid (coverups / color / etc.)
├── /services                ← What's offered + pricing posture
├── /contact                 ← Form + map + hours + phone
├── /faq                     ← Deposit, walk-ins, age policy, aftercare, etc.
└── /book                    ← Optional separate booking page if we add a booking system
```

### Page-by-page content outlines

#### `/` Home
- Hero: big tattoo photo + shop name in Anton + tagline + "Book a consultation" CTA (red button)
- 3-card row: Meet the artists | See the work | What we do
- Featured work: 6 latest tattoos in a masonry grid
- Coverup callout: 2-up section highlighting coverup specialty
- Final CTA: "Walk-ins welcome · 500 Galleria Dr · (215) 980-1386"

#### `/artists`
- Grid of all artists (1–5+ depending on roster)
- Hover reveals specialty tags
- Tap → artist detail page

#### `/artists/[slug]`
- Hero photo + name + specialties tag pills + bio
- Instagram embed (or styled IG-style grid via OG images)
- "Book with [name]" CTA

#### `/portfolio`
- Grid, filterable by: **coverup** / **color** / **black & grey** / **fine line** / **traditional** / **script** / etc.
- Lightbox on tap (mobile-friendly)

#### `/services`
- "What we do" + "What it costs" sections
- Pricing posture: "DM for quote" or hourly rate (TBD)
- Deposit info: $50–$65 minimum, non-refundable (will reconcile with Isiah)
- Walk-ins yes, appointments preferred
- Age policy: 18+ (PA state law — verify)
- Aftercare download link (PDF)

#### `/contact`
- Form: name, email, phone, tattoo idea / reference, preferred artist, body location, size estimate
- Map embed (Google Maps or free alternative — embedded iframe)
- Address: 500 Galleria Dr, Johnstown PA 15904
- Phone: (215) 980-1386 (tap-to-call link)
- Hours: Closed Sun & Mon · Tue–Sat 11–7
- IG embed (link in bio or contact footer)

#### `/faq`
- Accordion with: How do I book? · Do you do walk-ins? · What's the deposit? · Do you do coverups? · How old do I need to be? · How do I prepare for my appointment? · Do you do piercings? · Aftercare instructions · Can I bring a friend?
- Each FAQ item a separate permalink (#faq-booking) for shareability

#### `/book` (only if we add a booking system)
- TBD based on H11 — likely GlossGenius or Booksy embed, not custom-built

---

## 4. Domain Choice (RECOMMENDED)

Domain availability verified 2026-08-17 (RDAP lookup):

| Domain | Status | Notes |
|--------|--------|-------|
| `bleedinginktattoo.com` | ✅ Available | **RECOMMENDED** — exact match to "Bleeding Ink Tattoo" branding |
| `bleedingink.tattoo` | ✅ Available | Best TLD for tattoo shops but less universal |
| `bleedingink.gallery` | ✅ Available | Modern, premium feel |
| `bleedingink.studio` | ✅ Available | Less specific |
| `bleedinginkjohnstown.com` | ✅ Available | SEO boost for local searches but verbose |
| `bleeding-ink.com` | ❌ Taken | — |
| `ibleedink.com` | ❌ Taken | — |

**Pick**: `bleedinginktattoo.com`. Best for SEO (exact match for "Bleeding Ink Tattoo"), readable, professional, available. ~$12/yr at Namecheap.

---

## 5. Tech Stack Lock-In

| Layer | Choice | Why |
|-------|--------|-----|
| **Framework** | Next.js 16 + React 19 + TypeScript | Matches your existing `jadas-jazz-cafe-web` patterns |
| **Styling** | Inline styles + Tailwind v4 `@theme` component classes | Same as jadas-jazz-cafe-web |
| **Content** | Static MDX or JSON in `src/data/` | No DB needed for v1 |
| **Forms** | Server action → Resend (or Cloudflare Email Routing) | Simple, no third-party lock-in |
| **Maps** | Embedded iframe (Google Maps) | No API key required for basic embed |
| **Images** | `next/image` with AVIF/WebP | Best performance |
| **Hosting** | Vercel | Already in your local dev toolkit |
| **Analytics** | Plausible | Privacy-friendly, no cookie banner |

---

## 6. SEO Targets (per `research/04-seo-keywords.md`)

Top-priority landing pages (each = one search-intent match):

| Page target | Keywords | Priority |
|-------------|----------|----------|
| `/` | "tattoo shop johnstown pa" | High |
| `/artists/isiah-jackson` | "tattoo artist johnstown pa", "[style] tattoo johnstown pa" | **Highest** |
| `/artists/courtney-fetzer` | "apprentice tattoo artist johnstown pa" | Medium |
| `/portfolio` | "tattoo portfolio johnstown", "coverup tattoos johnstown" | High |
| `/services` | "tattoo consultation johnstown", "coverup tattoo johnstown" | High |
| `/contact` | "bleeding ink johnstown phone", "tattoo shop galleria johnstown" | High (local pack) |

Google Business Profile, Yelp, InkFinder, BBB, TattooShopsNearMe will all be **claimed and linked from the footer** at launch.

---

## 7. Build Phases (high-level — Stage 3 will bite-size these)

1. **Scaffold**: copy jadas-jazz-cafe-web skeleton, swap content, configure Vercel + domain
2. **Brand**: pick direction from §2, apply color tokens + typography
3. **Pages**: build each of the 7 pages per §3 outlines
4. **Forms + Maps**: contact form backend, Google Maps embed
5. **SEO**: meta tags, JSON-LD LocalBusiness, OG images
6. **Test**: cross-browser, mobile, Lighthouse 95+ performance
7. **Deploy**: Vercel + custom domain
8. **Claim directories**: Yelp / GBP / InkFinder / BBB / TattooShopsNearMe
9. **Cross-link**: update FB page "Website" field + IG bio link

---

## 8. Open Decisions for Austin

Before Stage 3 starts, I need:

1. **Brand direction** — A, B, or C (or mix)? My pick is **A**.
2. **Domain** — `bleedinginktattoo.com` ✅ or alternative?
3. **Pricing posture** — publish hourly rates, or "DM for quote"?
4. **Booking system** — embed (GlossGenius/Booksy) now, or form-only for v1?
5. **Artist roster** — just Isiah + Courtney, or more?
6. **Deposit number** — $50 (IG) or $65 (FB)? Single number on site.

---

## 9. What happens after you approve

- I write **Stage 3 build plan** as a new file in `.hermes/plans/` with bite-sized tasks (no single task > 30 min of work)
- I scaffold the Next.js project at `C:\Users\bbask\Coding_Projects\bleeding-ink-tattoo-web\`
- I commit each task with descriptive messages
- I show you what landed after each task
- I pause before each cross-cutting decision (color tokens, page-by-page content)

---

**Status: Awaiting Austin's approval on §8.**