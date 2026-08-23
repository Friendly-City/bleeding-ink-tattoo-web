# 03 — Booking Platforms

> **Status:** Pending Austin's answer to "already using a booking system?" in `CLIENT-INTAKE.md` §4.

## Landscape (researched 2026-08-17, 3 independent sources)

| Platform | What it does | Cost | Embed style | Best for |
|----------|--------------|------|-------------|----------|
| **GlossGenius** | Booking + payments + forms + client mgmt + branded app | ~$24/mo per user | iframe widget | Studios wanting all-in-one, modern UI |
| **Booksy** | Booking + payments + marketplace discovery | ~$30/mo | iframe widget | Studios wanting new-client discovery from Booksy marketplace |
| **Square Appointments** | Booking + Square payments | Free w/ Square, $16+/mo for advanced | iframe + Square button | Studios already on Square POS |
| **Calendly** | Generic scheduling | Free tier, $8–$16/mo paid | inline embed or popup | Solo artists, simple flow |
| **Acuity** | Scheduling + intake forms | $16–$76/mo | inline embed | Studios wanting custom intake forms |
| **Custom Next.js form** | Bespoke, hits your email/Telegram/CRM | Free (just dev time) | native page | Studios wanting zero SaaS dependency, full brand control |

## What jadas-jazz-cafe-web does (reference)

Built a **custom server-action form** that emails the shop. No third-party booking widget. Works well because:
- Reservations are simple (party size + time)
- Brand control matters more than booking UX
- No per-transaction fees
- No SaaS dependency to break

For Bleeding Ink, this translates differently — tattoo consultations are heavier (need reference images, placement, size, artist preference) than restaurant reservations. **A native consultation form is well-suited; real-time booking is harder to replicate without a SaaS.**

## Recommendation Tiers

### Tier 1 — If Austin already uses one
**Embed their existing widget.** Don't fight working systems. Native iframe, styled to match site chrome. Zero dev time.

### Tier 2 — If Austin wants to add one
**GlossGenius** is the best fit for tattoo studios in 2026 — purpose-built for the industry, modern UI, payment processing built in, branded client app. ~$24/mo. Trade-off: monthly SaaS cost + per-card processing fees.

### Tier 3 — If Austin wants to stay SaaS-free
**Build a custom consultation request form** (Next.js server action → email/Telegram/CRM). Mirror jadas-jazz-cafe-web pattern. Defer real-time booking to a "stretch goal." Trade-off: consultation-only, not direct booking.

## Hybrid Approach (recommended if Austin wants both)

- **Native consultation form** for custom work (the 80% case) → emails shop
- **GlossGenius widget** embedded on Flash Sheets page only (where same-day / set-price booking actually works) → instant booking

This gives clients the right tool for the right job without forcing all bookings through one flow.

---

## Austin's Decision

> (filled during intake review)

**Booking flow for v1:** ____

**Implementation plan:** ____

**Stretch goal (post-launch):** ____