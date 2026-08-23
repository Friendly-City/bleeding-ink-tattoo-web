# Hosting Pivot — Demo Without Buying a Domain

> **Date:** 2026-08-18
> **Context:** Austin clarified this site is a **sales pitch / live demo** to present to Bleeding Ink, not for the shop to use directly yet. Don't buy bleedinginktattoo.com. Need a free / no-domain option.

---

## Option A — Cloudflare "Quick Tunnel" (free, no account, ~5s setup)

**How it works:** run `cloudflared tunnel --url http://localhost:3013` and Cloudflare gives you a public `*.trycloudflare.com` URL in 5 seconds.

- ✅ Truly free (no account needed)
- ✅ HTTPS automatic
- ✅ No DNS work
- ❌ **URL changes every time you restart the tunnel** (looks unprofessional for demos)
- ❌ **Cloudflare TOS warns "no uptime guarantee, may be revoked"** (bad for a live pitch)
- ❌ **TESTED — DOESN'T WORK ON THIS BOX.** I ran it twice tonight, both times the tunnel registered but Cloudflare returned 404 on every request, and the metrics showed 0 requests served. The existing `hermes-dashboard` tunnel uses Cloudflare Access for security, which appears to be blocking / interfering with anonymous trycloudflare tunnels from the same machine. Diagnosed but not fixable without changing global Hermes tunnel config.

**Verdict: ruled out for live demo** — works on a fresh box but not yours.

---

## Option B — Cloudflare Pages (free, no custom domain needed)

**How it works:** push the repo to Cloudflare Pages via the dashboard or CLI. You get a public URL like `bleeding-ink-tattoo-web.pages.dev` immediately. Free tier includes:

- ✅ Unlimited bandwidth (Cloudflare's free tier is genuinely unlimited)
- ✅ HTTPS automatic
- ✅ 300+ edge POPs (faster than Vercel for visitors in PA)
- ✅ Integrates with your existing Cloudflare account (no new signup)
- ✅ Same Next.js framework support as Vercel
- ⚠️ URL format `yourproject.pages.dev` (always uses subdomain — no custom domain unless you bring one)
- ❌ Slightly more friction than Vercel for Next.js App Router (some features need adapters)

**Cost: $0 forever** (Cloudflare Workers Free tier: 100,000 requests/day — far more than a demo needs).

---

## Option C — Vercel Free Tier

**How it works:** `vercel --prod` from the project directory. URL: `bleeding-ink-tattoo-web.vercel.app`.

- ✅ Free tier (100 GB bandwidth/month, plenty for demo)
- ✅ Zero-config Next.js — literally built by the same team
- ✅ Custom domain optional (you can add `bleedinginktattoo.com` later for $12/yr if they bite)
- ✅ Automatic preview deploys on every git push
- ⚠️ URL format `<project-name>.vercel.app`
- ⚠️ Requires Vercel account (free, GitHub login works) — about 2 minutes to set up
- ❌ Vercel brand visible in URL

**Cost: $0 for demo tier.**

---

## Option D — `bleeding.theporadas.com` via your existing tunnel

**How it works:** add a 3rd ingress rule to `~/.cloudflared/config.yml` pointing to `localhost:3013`, and add a CNAME in Cloudflare DNS pointing `bleeding.theporadas.com` to your tunnel UUID.

- ✅ Free
- ✅ Clean URL that looks like a real production site
- ✅ Uses your existing infrastructure
- ❌ Requires you to make 2 changes:
  1. Add CNAME in Cloudflare DNS for theporadas.com zone
  2. Edit `~/.cloudflared/config.yml` and restart the tunnel
- ⚠️ Would also need me to set HTTP host header rewrite (the same trick `hermes.theporadas.com` uses)
- ❌ Still leaves theporadas.com branding visible (it's your personal brand, not theirs)

**Cost: $0.**

---

## Option E — Local only (no deploy)

Just generate a bunch of screenshots of every page + a local recording as you click through.

- ✅ Zero risk
- ✅ Zero cost
- ❌ Not as compelling as a live URL they can click
- ❌ More work for you to assemble the demo packet

---

## My Recommendation

**Option C (Vercel free tier)**, because:

1. It's the most reliable free hosting for Next.js specifically
2. The URL is stable — give Isiah one URL and it works forever (as long as the project exists)
3. If they say yes and buy the domain, I add the custom domain to the same Vercel project in 2 minutes — no re-deploy
4. If they say no, the Vercel free project just sits there unused, $0 cost
5. Uses your existing GitHub auth (`bbasketballer75`) — no new account

Backup choice: **Option D (`bleeding.theporadas.com`)** if you want it under your own domain for the pitch. Tell me to go ahead and I'll set it up.