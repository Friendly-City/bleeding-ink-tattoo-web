# 04 — SEO Keyword Research

> **Status:** Pending city + artist specialties from intake. Researched baseline patterns from Nodedr's guide (2026-06-09) + Seahawk (2025-05-01).

## Keyword Categories

### 1. Local Discovery (highest intent)

| Keyword pattern | Example | Page that should rank |
|-----------------|---------|-----------------------|
| `tattoo shop [city]` | "tattoo shop Johnstown" | Home |
| `tattoo [city]` | "tattoo Johnstown" | Home |
| `tattoo shop near me` | (Google auto local pack — GBP matters more than site) | Home + GBP |
| `[city] tattoo studio` | "Johnstown tattoo studio" | Home |

### 2. Style-Specific (mid intent, winnable)

| Keyword pattern | Example | Page that should rank |
|-----------------|---------|-----------------------|
| `[style] tattoo artist [city]` | "fine line tattoo artist Johnstown" | Per-artist page |
| `[style] tattoo [city]` | "traditional tattoo Johnstown" | Portfolio filtered by style |
| `[style] tattoos near me` | "Japanese tattoos near me" | Per-artist page |
| `custom [style] tattoos` | "custom blackwork tattoos" | Portfolio + home |

### 3. Service-Specific (high intent)

| Keyword pattern | Example | Page that should rank |
|-----------------|---------|-----------------------|
| `tattoo consultation [city]` | "tattoo consultation Johnstown" | Consultation form page |
| `[artist name] tattoos` | (own artist names) | Per-artist page |
| `flash tattoo [city]` | "flash tattoo Johnstown" | Flash Sheets page |
| `tattoo aftercare [city]` | "tattoo aftercare Johnstown" | Aftercare page |
| `tattoo shop hours [city]` | (near-me queries) | Contact + schema |

### 4. Trust / Educational (long tail)

| Keyword pattern | Example | Page that should rank |
|-----------------|---------|-----------------------|
| `how to care for a new tattoo` | | Aftercare page |
| `tattoo deposit policy` | | FAQ |
| `walk-in tattoo shop [city]` | "walk-in tattoo shop Johnstown" | FAQ + Home |
| `tattoo shop [city] reviews` | | Reviews embed page |
| `best tattoo shop [city]` | | Home + GBP reviews |

---

## Austin's Input Needed

| Question | Answer drives |
|----------|---------------|
| City / location? | All "near me" + "[city]" keywords |
| Artist specialties? | Per-style keyword targeting |
| Hours? | Schema.org `openingHours` |
| Walk-in policy? | "walk-in tattoo shop" keyword + FAQ |

---

## SEO Checklist (Stage 3 build phase)

When build plan runs, every page must include:

- [ ] Unique `<title>` with primary keyword + city
- [ ] Meta description with CTA + city
- [ ] H1 with primary keyword
- [ ] Schema.org `TattooParlor` JSON-LD (home + contact)
- [ ] Schema.org `Person` JSON-LD per artist page
- [ ] OG image + Twitter card
- [ ] Descriptive `alt` text on every image (alt = "fine line floral tattoo on forearm by [artist], [city]" not "tattoo")
- [ ] Semantic HTML (sections, headers, nav)
- [ ] Internal linking: every artist page links to 2-3 other artists + portfolio
- [ ] `sitemap.xml` + `robots.txt`
- [ ] Page-load < 3s on mobile (target: < 2s)
- [ ] Mobile-friendly test passes (Google Search Console)
- [ ] LocalBusiness schema includes hours, address, phone, geo coordinates