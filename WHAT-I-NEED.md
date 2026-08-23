# What I Need to Continue — Bleeding Ink Tattoo Website

> **For Austin:** Here's the precise list, separated by priority. Everything is a question that ONLY you or the shop owner can answer — I can't research any of it.

---

## 🔴 BLOCKING (build literally cannot start without these)

These answer "who is this site for" and "what does it say."

| # | What | Why it's blocking | How I'd get it without it |
|---|------|-------------------|---------------------------|
| **B1** | **Shop owner's full name + best contact (email/phone for the contact form)** | The site needs a "Contact" page. Without it the form has nowhere to send. | Use a generic `hello@bleedinginktattoo.com` placeholder + a "We'll reply within 2 business days" note. Owner can swap later. |
| **B2** | **Confirmed current address** (still at Johnstown Galleria? moved?) | Footer + contact page + Google Maps embed need it. Embed doesn't work without a valid address. | Leave maps as "Johnstown, PA" without pin. Use 500 Galleria Dr as provisional with a comment that owner must confirm. |
| **B3** | **Real phone number for the shop** | Tap-to-call links + footer. | Use a placeholder "tap-to-call" link that goes to a placeholder, OR ship without phone and add post-launch. |
| **B4** | **Hours of operation** | Footer + Google Business sync + contact page. | Default to "Tue–Sat 11am–7pm" (matches Johnstown Galleria pattern) with a "call to confirm" disclaimer. |
| **B5** | **Shop owner's preference on the IG account** — is `@ibleedink_600` the shop's account, or a separate person's? | If it's the shop's: I can scrape & repurpose the portfolio (with permission note). If not: zero IG imagery on the site. | Default to "don't use IG photos" — safer. |

---

## 🟡 HIGH-VALUE (these shape design and content meaningfully)

These turn a generic tattoo-site template into **this shop's** site.

| # | What | Why it matters | Default if blank |
|---|------|----------------|------------------|
| **H1** | **Brand direction choice** (see CLIENT-INTAKE §5) — bold/gritty vs clean/minimal vs ornate/vintage vs custom | Drives the entire visual language: colors, typography, photography style, layout density | I'll propose a direction in Stage 2 brand-direction doc and you approve/edit before any code |
| **H2** | **Is the deposit $50 (IG) or $65 (FB)?** Or both (artist-specific)? | Goes on the booking/FAQ page as the literal number | Show both: "$50+ deposit, $65 minimum" — flag for owner to reconcile |
| **H3** | **Is the custom merch (clothes/hats/shoes) part of the shop or separate?** | Determines whether the site has a "Shop/Merch" page | Default to **separate** — out of scope for v1, add later if needed |
| **H4** | **Number of artists + names + specialties** | Drives the Artists page (huge for SEO — "[style] tattoo artist Johnstown") | Default to: Courtney Fetzer + 1 placeholder "Lead Artist TBD". One page each. |
| **H5** | **Permission to feature the FB gallery posts** (the color-work 💐🐢 turtles etc.) on the new site | Those are the only confirmed public portfolio pieces | Default to **no** — wait for owner to upload their own photos post-launch |
| **H6** | **Pricing posture** — publish hourly rates, or keep "DM for quote"? | Drives whether pricing/FAQ gets a dedicated page or just an FAQ | Default to **"DM for quote"** with deposit info on the FAQ page |
| **H7** | **Domain preference** — `bleedinginktattoo.com`? Do you own any? | Site URL, SEO, business cards, etc. | Default to `bleedinginktattoo.com` (buy as part of deploy) unless you say otherwise |
| **H8** | **Consultation response SLA** — how fast do you actually reply? | Sets expectation on the contact form confirmation message + drives auto-responder email tone | Default: "We respond within 2 business days" |

---

## 🟢 NICE-TO-HAVE (can ship v1 without; add incrementally)

| # | What | When I'd ask if not provided |
|---|------|-------------------------------|
| **N1** | Logo file (vector preferred, high-res PNG fallback) | At build time before launch |
| **N2** | Real tattoo photos for portfolio (10+ images minimum) | At build time before launch |
| **N3** | Studio interior photos (for About page) | At build time before launch |
| **N4** | Artist headshots | At build time before launch |
| **N5** | Brand colors (hex codes) if there's an existing identity | At brand-direction approval time |
| **N6** | Existing copy (about-us, aftercare, FAQs) | At build time |
| **N7** | Yelp + Google Business Profile creation access | At launch |
| **N8** | Cloudflare/Vercel token for deploy | At deploy time |

---

## 🛠️ Things I can decide on my own (no need to ask)

These are technical / design defaults I'll make and document in the Stage 2 brand-direction proposal. You can override any of them.

| Decision | Default | Why |
|----------|---------|-----|
| **Framework** | Next.js 16 + React 19 + TypeScript (same as `jadas-jazz-cafe-web`) | Matches the working reference, same pitfalls already known |
| **Styling** | Inline styles + Tailwind v4 component classes (matching jadas-jazz-cafe-web) | Already battle-tested, no need to reinvent |
| **Backend** | Static site + email-forwarding contact form (Resend or Cloudflare Email Routing) | No DB needed for v1, faster to ship, easier to maintain |
| **Hosting** | Vercel (free tier, instant deploys) | Already in the local dev toolkit |
| **Image optimization** | next/image with AVIF/WebP | Match reference project |
| **SEO** | next-seo + JSON-LD LocalBusiness schema | Match reference pattern |
| **Analytics** | Plausible (privacy-friendly, no cookie banner) | Can be added at launch |
| **Font pairing** | Display serif + sans-serif (to be confirmed in Stage 2 based on H1) | Industry standard for credibility |
| **Page structure** | Home / Artists / Portfolio / Services / Contact / FAQ / Booking (7 pages) | Standard tattoo shop template |

---

## ⚡ Fastest path to "start building"

If you want to unblock me in the next 5 minutes, the **minimum viable answers** are:

1. **B1** — Shop owner's name + a contact email (even a personal Gmail works for v1)
2. **B2** — "Still at Galleria" or "moved to [address]"
3. **B5** — "Yes the IG is the shop's" or "no, separate person"
4. **H1** — Pick a brand direction from §5 of the intake (or say "you decide")
5. **H7** — Domain preference or "buy bleedinginktattoo.com"

That gets me to Stage 2 (brand-direction doc for approval) → Stage 3 (build plan) → coding.

---

## 📋 Quick reference: what's already locked in (no decisions needed)

These came from research and are not changing:

- ✅ Tech stack (Next.js 16 + Tailwind v4 + inline styles)
- ✅ Reference project patterns (`jadas-jazz-cafe-web` AGENTS.md pitfalls to apply)
- ✅ Confirmed artist 1: **Courtney Fetzer** (junior, started Jun 19 2026)
- ✅ Confirmed shop tagline (FB): "Appointments preferred but walk-ins always welcome, free consultation, wide variety of styles + coverups at competitive pricing"
- ✅ Confirmed specialty differentiators: **color work, coverups, walk-in friendly**
- ✅ Competitive positioning vs Total Commitment / Screaming Needle / Lemon Bomb
- ✅ Local SEO target terms (per `research/04-seo-keywords.md`)
- ✅ Claim Yelp / Google Business Profile / InkFinder / BBB / TattooShopsNearMe at launch

---

## 🎯 What I do once you answer the blocking set

1. Write **Stage 2 plan**: brand-direction doc + page list for your approval
2. Once approved: write **Stage 3 build plan**: bite-sized tasks, file paths, verification gates
3. Once approved: scaffold the project at `C:\Users\bbask\Coding_Projects\bleeding-ink-tattoo-web\`, port jadas-jazz-cafe-web patterns
4. Build → test → deploy (Vercel) → claim directories → ship
5. At each stage: commit + show you what landed + ask before continuing

**You don't have to answer everything.** The 5 fastest items above get me to the next gate. The rest can fill in as we go.