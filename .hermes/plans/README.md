# Plans Index

All implementation plans for the Bleeding Ink tattoo website project.

| Plan | Date | Stage | Status |
|------|------|-------|--------|
| [Setup plan](./2026-08-17_000000-tattoo-shop-website-setup.md) | 2026-08-17 | 1 — Setup | ✅ Complete |
| Build plan | TBD after intake | 3 — Build | ⏳ Blocked on `CLIENT-INTAKE.md` |

## Active Stage

**Stage 1 — Research / Intake.** Austin fills `CLIENT-INTAKE.md`. After that:

- **Stage 1.5** — Research: scrape existing web presence, pull design references, draft brand direction
- **Stage 2** — Structure Approval: Austin signs off on page list + design direction
- **Stage 3** — Build: I write a bite-sized build plan here, then execute via subagent-driven-development
- **Stage 4** — Deploy: Vercel + custom domain

## How to Add New Plans

1. Use ISO date + 6-digit time + kebab-case slug: `YYYY-MM-DD_HHMMSS-description.md`
2. Start with the same header block as the setup plan (Goal, Architecture, Tech Stack)
3. Cross-link from this index
4. Commit to git with the rest of the changes

## Plan Storage Convention

- This folder is the single source of truth for plans related to THIS project
- Plans for OTHER projects (e.g., friendly-city-print-shop, jadas-jazz-cafe-web) live in their own `.hermes/plans/`
- Obsidian-vault notes for this client go to `C:\Users\bbask\Documents\Obsidian Vault\Local Business Websites\bleeding-ink\` (Stage 1.5 setup, not yet done)