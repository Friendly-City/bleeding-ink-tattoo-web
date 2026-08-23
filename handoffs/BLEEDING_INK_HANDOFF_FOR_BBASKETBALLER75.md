# Bleeding Ink Tattoo — Austin’s Partner and Repository Administration Handoff

**Audience:** Austin / `bbasketballer75`  
**Purpose:** Set up and operate the current two-person GitHub workflow with Ean without changing the current account structure.  
**Repository:** <https://github.com/bbasketballer75/bleeding-ink-tattoo-web>  
**GitHub account currently holding the repository:** `bbasketballer75`  
**Default branch:** `main`  
**Repository visibility:** Public  
**Prepared:** 2026-08-22

> Keep this handoff private. It is not stored in the public repository. Send Ean only the Ean handoff document, not this owner document.

## What this setup means

Austin and Ean are equal project partners. The code, product decisions, priorities, and creative direction belong to both partners; this is not a manager/contributor arrangement.

The repository currently lives under Austin’s personal GitHub account, so Austin’s account has the technical ability to manage repository settings and the provider credentials that already exist. That is an account-structure fact, not a higher project role. The current GitHub permissions and deployment boundary can be changed later by mutual agreement.

The collaboration contract is:

1. Either partner chooses or agrees on a task.
2. The partner doing the work creates a feature branch from `main`.
3. That partner makes and tests the change locally.
4. That partner pushes the feature branch and opens a pull request.
5. The other partner reviews the pull request as an equal peer.
6. Both partners discuss questions, requested changes, and readiness to merge.
7. The partner who did not author the pull request approves it when satisfied; the account with the required GitHub permission completes the merge.
8. Both partners agree before production deployment or major infrastructure changes.

Neither person shares a GitHub password, personal access token, Copilot account, Cloudflare credential, Vercel credential, Resend secret, or production `.env` file.

## Equal technical ownership option

A personal-account repository cannot have two equal repository owners. GitHub’s personal-repository model has one owner and collaborators. A collaborator can contribute code, push branches, create and review pull requests, and merge pull requests when the repository rules allow it, but the collaborator does not become a second owner of the personal account repository.

If Austin and Ean want equal GitHub administration as well as equal project partnership, the recommended structure is a dedicated GitHub Organization for Bleeding Ink:

1. Create a project organization rather than using either person’s personal or business account as the shared owner.
2. Keep Austin and Ean signed into their own personal GitHub accounts.
3. Add both personal accounts as organization owners.
4. Transfer the repository into that organization.
5. Recheck branch protection, deployment connections, webhooks, environment secrets, and provider integrations after the transfer.

This gives both partners the same organization-level administration. It does not require a shared password. Organization-owner access is powerful: both owners can manage organization settings, members, repositories, and billing-related administration, so both partners should use two-factor authentication and agree on recovery procedures.

GitHub says organizations are available on GitHub Free, with feature limits for private repositories. Because this repository is currently public, creating the shared organization should not require another paid GitHub subscription; compare plans again if the repository becomes private or the team needs paid organization features.

This organization option has not been performed yet. Do not transfer the repository until both partners agree on the organization name, verify the deployment integrations, and make a recovery plan. The current personal-repository setup can still support normal equal code collaboration while that decision is being made.

Official references: [personal repository permission levels](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/permission-levels-for-a-personal-account-repository), [about organizations](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/about-organizations), and [transferring a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository).

### Exact creation steps from `bbasketballer75`

Do this while signed into your personal account `bbasketballer75`, not `FriendlyCityJohnstown`:

1. Open GitHub and click your profile picture in the upper-right corner.
2. Click **Settings**.
3. In the left sidebar, under **Access**, click **Organizations**.
4. Next to the **Organizations** heading, click **New organization**.
5. Choose **GitHub Free**. Do not start a paid Team plan unless both partners have agreed to that cost.
6. Enter the organization name that both partners chose for Bleeding Ink.
7. Enter a project contact email that both partners can access or that has an agreed recovery plan.
8. Leave the business or institution option unchecked unless this organization is formally being created for a legal business or institution.
9. Complete the prompts and create the organization.

### Add Ean as an equal organization owner

After the organization exists:

1. Open the new organization.
2. Click **People**.
3. Click **Invite member**.
4. Enter Ean’s exact GitHub username.
5. Under **Role in the organization**, choose **Owner**.
6. Click **Send invitation**.
7. Wait for Ean to accept the invitation using his own GitHub account.
8. Return to **Organization → People** and confirm that both `bbasketballer75` and Ean’s account show the **Owner** role.

Both organization owners will have broad administrative access. Before accepting this arrangement, both partners should have two-factor authentication enabled and agree on how account recovery, billing, repository deletion, and access changes will be handled.

### Transfer the repository into the organization

Do this only after Ean has accepted the organization-owner invitation and both partners have checked the current deployment integrations:

1. Open the current repository at <https://github.com/bbasketballer75/bleeding-ink-tattoo-web>.
2. Click **Settings**.
3. Scroll to the **Danger Zone** section.
4. Click **Transfer**.
5. Under **New owner**, choose the new Bleeding Ink organization.
6. Read the warnings carefully.
7. Type `bleeding-ink-tattoo-web` to confirm.
8. Click the final transfer confirmation.

After the transfer, both partners should verify branch protection, collaborator/team access, Actions settings, webhooks, environment secrets, and the Vercel/Cloudflare deployment connections. Update each local clone to use the organization URL:

~~~powershell
git remote -v
git remote set-url origin https://github.com/ORGNAME/bleeding-ink-tattoo-web.git
git remote -v
~~~

Replace `ORGNAME` with the exact organization name. GitHub may redirect the old URL, but the new organization URL should become the canonical remote for both computers.

## Current project facts

| Item | Current value |
|---|---|
| GitHub repository | `bbasketballer75/bleeding-ink-tattoo-web` |
| Clone URL | `https://github.com/bbasketballer75/bleeding-ink-tattoo-web.git` |
| Default branch | `main` |
| Framework | Next.js 16.3.1 |
| UI/runtime | React 19.2.4 + TypeScript |
| Styling | Tailwind CSS v4 plus the project’s inline-style pattern |
| Package manager | npm with the committed `package-lock.json` |
| Node requirement | Node.js `>=20.9.0` |
| Local development URL | `http://localhost:3009` |
| Local install | `npm ci` |
| Local development | `npm run dev` |
| Production build check | `npm run build` |
| TypeScript check | `npx tsc --noEmit` |
| Test runner | None currently installed |
| Known lint state | `npm run lint` currently has known project failures |

The repository is public. Anyone can view and clone it. Only invited collaborators can push changes.

## Before inviting Ean

Complete this checklist while signed into `bbasketballer75`.

### Account and repository checks

- [ ] Confirm you are signed into `bbasketballer75`, not `FriendlyCityJohnstown`.
- [ ] Open <https://github.com/bbasketballer75/bleeding-ink-tattoo-web>.
- [ ] Confirm the repository is the intended Bleeding Ink project.
- [ ] Confirm `main` is the default branch.
- [ ] Confirm the repository is intentionally public.
- [ ] Confirm you have not accidentally staged or committed unrelated work.
- [ ] Keep unrelated local material such as `scripts/cookies/archive/` out of project commits.

### Secret and privacy checks

Because this repository is public, check for secrets before giving anyone write access.

- [ ] Confirm no API key, password, token, private key, production `.env`, or database credential is in the working tree.
- [ ] Confirm `.env.local`, `.env`, and other local environment files are not tracked.
- [ ] Confirm production credentials live only in the deployment provider or a secure secret store.
- [ ] If a secret was ever committed, rotate/revoke it. Deleting the file is not enough.
- [ ] Do not put Ean’s personalized handoff document in this public repository.

The current `.gitignore` excludes `.env`, `.env.local`, `.env.*.local`, `.next`, `.open-next`, `.wrangler`, and other local/generated material. Still inspect `git status` before committing; an ignore rule is not a substitute for reviewing the staged file list.

## Invite Ean to the repository

Ask Ean for his exact GitHub username. Use his username rather than guessing from a display name or email address.

1. Sign into GitHub as `bbasketballer75`.
2. Open <https://github.com/bbasketballer75/bleeding-ink-tattoo-web>.
3. Click **Settings**.
4. In the left sidebar, under **Access**, click **Collaborators**.
5. Click **Add people**.
6. Search for Ean’s exact GitHub username.
7. Select the correct account.
8. Send the repository invitation.
9. Tell Ean to accept the invitation from his own GitHub account.

GitHub’s personal-repository collaboration flow gives a collaborator read/write access to the repository. There is no separate read-only or write-only selector for a personal-account repository. See [Inviting collaborators to a personal repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/inviting-collaborators-to-a-personal-repository) and [personal repository permission levels](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/permission-levels-for-a-personal-repository).

Do not send Ean a ZIP of your working directory as the normal setup. A fresh clone gives him the correct Git history, remote, branches, and pull-request relationship.

## Protect `main`

Protect `main` before Ean’s first real change is merged. This keeps the live branch reviewable without requiring an organization or a new subscription.

1. Open the repository on GitHub.
2. Go to **Settings**.
3. Open **Branches**.
4. Choose **Add branch protection rule**.
5. Set the branch pattern to `main`.

Enable these settings:

- [ ] Require a pull request before merging.
- [ ] Require at least **1** approving review.
- [ ] Dismiss stale pull-request approvals when new commits are pushed, if shown.
- [ ] Require conversation resolution before merging.
- [ ] Keep force pushes disabled.
- [ ] Keep branch deletion disabled.
- [ ] Enable **Do not allow bypassing the above settings** if GitHub shows that option.

Do **not** require status checks that do not exist. The current repository does not have a reliable active GitHub Actions CI workflow, so requiring a nonexistent check can block every pull request. Add required checks only after a real workflow has been created and its exact check names have been verified.

GitHub supports protected branches for public repositories and GitHub Pro repositories, including pull-request review and status-check requirements. See [About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches).

## Branch and pull-request rules

Use branch names that identify the person and the work:

~~~text
ean/contact-form
ean/mobile-nav-fix
ean/portfolio-update
austin/content-update
austin/deployment-docs
~~~

Avoid vague names such as `test`, `new`, or `changes`.

Every pull request should state:

- What changed.
- Why it changed.
- Which pages or behavior are affected.
- Which commands were run.
- Any known failure or follow-up work.
- Whether mobile behavior was checked.

Do not merge a pull request merely because the code compiles. Review the actual diff, open the affected page locally, and check the relevant mobile layout.

## First-day partner checklist

Use this as a shared setup session, not as a manager assigning work to a subordinate.

- [ ] Send Ean the private Ean handoff document.
- [ ] Invite Ean to the repository, or agree on the organization path first.
- [ ] Confirm Ean accepted the invitation.
- [ ] Clone the repository on both computers.
- [ ] Run the local setup commands together or compare results.
- [ ] Compare the results of `npm run build` and `npx tsc --noEmit`.
- [ ] Agree together on one small, real first task.
- [ ] Have the partner doing the task create a feature branch.
- [ ] Have that partner push the feature branch.
- [ ] Have that partner open a pull request into `main`.
- [ ] Review the pull request together as peers.
- [ ] Confirm that both partners understand the branch, review, and credential rules.
- [ ] Merge only after the non-author partner has reviewed it and both partners agree.

For the first task, prefer a contained UI or content correction over a deployment, dependency upgrade, authentication change, or broad refactor.

## Repository-account administration checks

These checks confirm the current GitHub permission structure. They do not define who leads the project; Austin and Ean remain equal partners.

After Ean accepts the invitation, confirm:

- [ ] Ean appears under the repository’s collaborators.
- [ ] Ean can clone the repository.
- [ ] Ean can create and push a feature branch.
- [ ] Both partners can open and review pull requests.
- [ ] A pull request receives review from the partner who did not author it before merge.
- [ ] Direct pushes to protected `main` are blocked.
- [ ] Repository settings and collaborator management remain limited to the GitHub account that currently holds the repository.
- [ ] Neither partner receives credentials belonging to the other person.
- [ ] Production provider credentials remain in their current secure location.
- [ ] Both partners understand that the administrative account boundary is not a project hierarchy.

If the collaboration ever changes, the current GitHub account holder can manage collaborator access under **Settings → Collaborators**. Removing GitHub access does not remove a local clone already on another person’s PC; if confidential information ever entered the repository, handle that separately.

## Local project baseline

The project’s expected commands are:

~~~powershell
node --version       # must satisfy >=20.9.0
npm --version
npm ci
npm run dev          # http://localhost:3009
npm run build
npx tsc --noEmit
~~~

Current validation expectations:

| Check | Expected state |
|---|---|
| `npm ci` | Should install from the committed lockfile |
| `npm run dev` | May hit a known Windows `lightningcss`/Turbopack problem on a fresh machine |
| `npm run build` | Expected to pass based on the current project baseline |
| `npx tsc --noEmit` | Expected to pass based on the current project baseline |
| `npm run lint` | Known current source/generation failures; not an Ean-specific setup failure |
| Test runner | None currently installed |

If `npm run dev` fails with a Windows `lightningcss` worker error such as `0xc0000142`, use the documented fallback:

~~~powershell
npm run build
npm run start -- -p 3009
~~~

Then open <http://localhost:3009>.

## Project conventions to enforce in review

Keep the current architecture and style unless a change is intentionally agreed:

- Use the existing inline-style pattern. Do not convert the project wholesale to Tailwind utility classes.
- Keep JavaScript/TypeScript brand constants in `src/lib/constants.ts`.
- Keep business information in `src/data/`.
- Keep the `$65` deposit amount sourced from `DEPOSIT_MIN`.
- Update metadata when changing business information.
- Test mobile layouts after layout changes.
- Do not add `jsx: "preserve"`.
- Do not add an incompatible `global-error.tsx`.
- Do not add `<html>` wrappers to `not-found.tsx`.
- Keep page-level server components and interactive `*Content.tsx` components organized as the project expects.
- Do not casually upgrade Next, React, OpenNext, Wrangler, or other deployment dependencies in a feature PR.
- Do not commit `node_modules`, `.next`, `.open-next`, `.wrangler`, `.env.local`, cookies, or generated exports.

## Deployment boundary

Austin and Ean are equal project partners. The current technical setup places the existing Cloudflare, Vercel, Resend, and related provider credentials under Austin’s accounts. That is a security and account-ownership boundary, not a statement that Austin outranks Ean.

Until the Vercel-versus-Cloudflare documentation is reconciled and both partners agree on a documented deployment process:

- Neither partner runs production deployment casually or as part of a normal feature branch.
- Both partners discuss and agree on the authoritative hosting path first.
- The person who currently holds the deployment credential performs the actual deployment when both partners agree it is ready.
- Credentials are never copied into the repository or shared as a shortcut.
- If the team later wants both partners to deploy, create separate least-privilege access and document it before using it.

The current routine contribution boundary is local development, testing, branches, and pull requests. The repository-account and deployment boundary may be redesigned later as a joint team decision.

Do not run:

~~~powershell
npm run deploy
npm run deploy:cf
wrangler deploy
~~~

There is currently a documentation conflict:

- `README.md` describes automatic Vercel deployment.
- `DEPLOY-NOTES.md` identifies the Cloudflare Workers demo at <https://bleeding-ink-tattoo-web.inquiry-970.workers.dev>.
- `LAUNCH-CHECKLIST.md` also contains older Vercel-oriented instructions.

Treat this as a shared project decision to resolve, not as permission for either person to deploy. Establish one authoritative production path and update the project documentation before expanding deployment access.

## Troubleshooting guide for helping Ean

### Invitation or permission denied

Ask Ean to run:

~~~powershell
gh auth status
git remote -v
git ls-remote origin
~~~

Verify:

- He accepted the invitation.
- He is signed into his own account.
- The remote is exactly:

  ~~~text
  https://github.com/bbasketballer75/bleeding-ink-tattoo-web.git
  ~~~

- He is not using a stale Windows GitHub credential.

Never solve this by sending Ean your token. Correct the account or Windows credential instead.

### Wrong account on Windows

If a wrong-account condition appears, pause before pushing. Confirm the GitHub Desktop account or `gh auth status`, then inspect Windows Credential Manager for stale GitHub credentials. Ean should remove or replace only the GitHub credential belonging to his own PC/account. Do not delete unrelated credentials or use your credential as a workaround.

### `npm ci` failure

Confirm:

~~~powershell
node --version
npm --version
Get-Location
~~~

The terminal must be in the repository root, and Node must satisfy `>=20.9.0`. Ask Ean for the complete error before changing `package-lock.json` or upgrading dependencies.

### Port already in use

Use another local port without changing the project:

~~~powershell
npm run dev -- -p 3010
~~~

Then open <http://localhost:3010>.

### Missing environment variable

Ean should copy `.env.example` to `.env.local`, leave secret fields blank unless you provide a development-safe value, and report the affected feature. He should not put a guessed key into GitHub.

### Branch divergence or merge conflict

Ean should stop before using `--force`. Inspect:

~~~powershell
git status
git branch -vv
git log --oneline --decorate -8
~~~

Discuss the intended result, then resolve deliberately. Never force-push `main` or rewrite shared history.

## Shared team setup definition of done

The partnership setup is complete when:

- [ ] Ean has accepted the invitation.
- [ ] Both partners use their own GitHub accounts and two-factor authentication.
- [ ] Both partners can clone and run the project locally.
- [ ] Both partners understand branches, commits, pushes, pull requests, reviews, and merges.
- [ ] Each partner can push a feature branch.
- [ ] `main` is protected from direct pushes.
- [ ] The partners have reviewed one real pull request together.
- [ ] The non-author partner has reviewed the first contribution before it is merged.
- [ ] No production credential has been shared.
- [ ] Both partners understand the current repository-account and deployment boundary as a technical setup issue, not a leadership hierarchy.
- [ ] Both partners agree on how the Vercel/Cloudflare documentation conflict will be resolved.

## GitHub from zero: what it is, why it works, and what you do

This section assumes you have never used Git, GitHub, or any code-collaboration service before. You do not need to know the terminology in advance. Start with the basic problem GitHub solves.

We have one website and two people. If both people edit the same folder or send files back and forth, someone can accidentally overwrite work, lose a change, or publish an unreviewed change. GitHub gives each person a separate working copy, records the history of changes, lets us compare proposed changes, and gives us a review step before the shared project changes.

### The three places involved

There are three different places. Keeping them separate is the most important idea in this whole process.

| Place | What it is | What happens there |
|---|---|---|
| Your PC | Your local project folder | You edit files and run the website |
| GitHub | The shared online repository | We exchange branches, review changes, and keep the project history |
| The live website | The version visitors can see | Deployment uses the current provider credentials |

The GitHub repository is not the live website. Changing a file on your PC does not change GitHub. Uploading a branch to GitHub does not change main. Merging a pull request changes main, but it still does not automatically deploy production. Deployment is a separate technical-access action; the current provider credentials remain with Austin until both partners agree on a shared process.

GitHub also does not continuously synchronize both computers like Dropbox. Each person has a separate local copy. We deliberately move changes between computers with clear commands and review points.

### Git and GitHub are different

**Git** is a program installed on your computer. Git watches the project folder, records snapshots of changes, creates separate branches, and helps you compare or recover work.

**GitHub** is the online service. It stores the shared repository and gives us pages for branches, pull requests, reviews, issues, access, and history.

Git is the local record keeper. GitHub is the shared online meeting place and backup for the project.

Your GitHub account is your identity on that service. You must use your own account. We do not share an account or a password.

### What actually happens to a change

A change moves through these steps:

~~~text
1. Edit a file
   The change exists only on your PC.

2. Stage the file with git add
   You choose which local changes are ready to save.

3. Commit the change
   Git saves a named local snapshot. GitHub still has not received it.

4. Push the branch
   The snapshot is uploaded to your branch on GitHub. main is still unchanged.

5. Open a pull request
   GitHub displays the difference and asks for review. main is still unchanged.

6. Review and merge
   The approved branch is combined into main on GitHub.

7. Deploy
   The person with the current deployment credentials sends the approved main version to the hosting provider after both partners agree.
~~~

This separation is intentional. It allows you to experiment locally, save work safely, ask for review, and correct mistakes before the shared branch or live site is affected.

### The words you will see

| Word | Plain meaning | Where it matters |
|---|---|---|
| Project folder | The folder containing this website on your PC | This is where you edit files |
| Repository / repo | The project files plus their complete change history | The online project on GitHub |
| Clone | The first download of the repository to your PC | Creates your local project folder |
| Local copy | Your separate copy on your computer | You can edit and test without changing Austin’s or Ean’s files |
| Remote | The saved connection to the online repository | This project’s remote is called origin |
| Working tree | The files currently changed or unchanged in your folder | What git status reports |
| main | The shared branch that contains the agreed project version | Treat it as stable and production-sensitive |
| Branch | A separate line of work based on main | Lets one person work without changing main |
| Staging area | A local holding area for files you intend to commit | Controlled by git add |
| Commit | A named snapshot of local changes | A checkpoint you can inspect or recover |
| Push | Upload your local commits to GitHub | Sends your feature branch online |
| Pull | Download commits from GitHub into your current local branch | Updates your local copy |
| Fetch | Check GitHub for new information without changing your files | Useful when you want to inspect first |
| Pull request / PR | A GitHub page asking to combine one branch into another | Ean asks Austin to review before main changes |
| Review | Reading the proposed difference and discussing it | The safety and quality checkpoint |
| Merge | Combining the approved branch into main | Changes the shared main branch |
| Conflict | Two changes that Git cannot combine automatically | Requires a person to decide which result is correct |
| Issue | A GitHub task, question, bug, or decision record | Describes work before or alongside coding |
| Deployment | Sending approved code to the hosting provider | A separate technical-access step |

### Why we use branches

main is the shared stable line of work. If people edit main directly, an unfinished change can immediately mix with the other person’s work. There is no clean review point, and a mistake is harder to identify.

A branch is a safe work lane created from main. For example:

~~~text
main
├── austin/contact-page-update
└── ean/mobile-nav-fix
~~~

Austin can work on the first branch while Ean works on the second. Their local edits stay separate. Each branch can be pushed to GitHub and reviewed independently.

Branches do not mean that the two people are building two unrelated websites. They are temporary work lanes that start from the same shared main branch and can be combined later through a pull request.

A branch does not automatically update. If main changes while you are working, you must deliberately pull or otherwise update your branch. If both people change the same lines, Git may report a conflict. That is normal; stop and resolve it together rather than choosing files blindly.

### What each action changes, and what it does not change

| Action | Where it changes something | Does it change shared main? | Why we do it |
|---|---|---:|---|
| Edit a file | Your PC | No | Create or modify the feature |
| git status | Nowhere; it only reports | No | See your branch and changed files |
| git diff | Nowhere; it only reports | No | Read the exact edits |
| git add | Your PC’s staging area | No | Choose files for the next commit |
| git commit | Your PC’s Git history | No | Save a named checkpoint |
| git push | Your branch on GitHub | No | Make your branch available for review |
| Open a PR | GitHub’s review system | No | Ask for an intentional review |
| Comment on a PR | GitHub’s review conversation | No | Ask questions or record decisions |
| Merge a PR | GitHub’s main branch | Yes | Combine approved work |
| Deploy | Hosting provider and live site | Not by itself | Publish the approved version |

The most common beginner confusion is this:

- Save in the editor is not a commit.
- A commit is not a push.
- A push is not a pull request.
- A pull request is not a merge.
- A merge is not a deployment.

Each step is separate so the team can see what is happening.

### The normal Austin work routine

When you start a new task:

1. Open PowerShell in the project folder. PowerShell is the Windows command window where you can run project commands.
2. Check where you are and which branch is active:

~~~powershell
git status
~~~

3. Update your local main branch:

~~~powershell
git switch main
git pull --ff-only origin main
~~~

4. Create a new branch for the task:

~~~powershell
git switch -c austin/short-description
~~~

5. Edit and test the files. The changes are still only on your PC.
6. Review your work:

~~~powershell
git status
git diff
~~~

7. Run the project checks:

~~~powershell
npm run build
npx tsc --noEmit
~~~

8. Stage only the files that belong to this task:

~~~powershell
git add path/to/changed-file
~~~

9. Check what is staged:

~~~powershell
git diff --cached
~~~

10. Create a local checkpoint:

~~~powershell
git commit -m "Describe the change"
~~~

11. Upload the branch to GitHub:

~~~powershell
git push -u origin austin/short-description
~~~

12. Open a pull request from austin/short-description into main.
13. Review the proposed difference as if you were reviewing Ean’s work. Do not merge until the checks and behavior are understood.
14. After the pull request is merged, update your local main before starting another task:

~~~powershell
git switch main
git pull --ff-only origin main
~~~

Use a new branch for each meaningful task. Do not keep unrelated work together merely because it is already in the same folder.

### How Ean’s pull request works

When Ean pushes a branch, GitHub does not place those changes into main automatically. GitHub creates a comparison between:

- the base branch: main, the shared version;
- the compare branch: Ean’s feature branch, the proposed version.

The pull request page shows the files and exact lines that would change. You can:

1. Read Ean’s explanation.
2. Inspect the changed files.
3. Read the line-by-line difference.
4. Check that no secrets or unrelated files are included.
5. Ask questions in the pull request.
6. Ask Ean to make changes if needed.
7. Confirm the local checks and browser behavior.
8. Approve and merge when the change is understood.

If you request changes, Ean stays on the same branch, makes another commit, and pushes that branch again. GitHub updates the existing pull request. He does not need to create a replacement pull request for every review comment.

Merging is the point at which Ean’s approved work becomes part of main. It is not a punishment, a grade, or a judgment of Ean. It is the team’s deliberate decision that the proposed code is ready to join the shared project.

### GitHub’s screens, explained plainly

- **Code:** The files and folders stored in the repository.
- **Issues:** A task list and discussion area for bugs, ideas, questions, and decisions.
- **Pull requests:** Proposed code changes waiting to be reviewed or already merged.
- **Actions:** Automated checks, if the project later adds GitHub Actions.
- **Branches:** The separate work lanes currently visible on GitHub.
- **History / commits:** The saved record of what changed, when, and in which branch.
- **Settings:** Access, branch protection, webhooks, and deployment controls. Keep these as repository-administration settings and discuss changes together.
- **Profile:** Your personal GitHub identity. It is separate from the repository itself.

Use an Issue when the work is still being described or discussed. Use a pull request when there is a branch containing actual code that someone can review.

### How to write an issue

An Issue is a written task or question. It is useful because the reason for a change stays with the project instead of being lost in text messages.

A good Issue says:

1. What is wrong or what should be added?
2. Which page or behavior is affected?
3. What should the user see or be able to do?
4. What must be true for the task to be complete?
5. Is there a screenshot, URL, example, or error message?

### How to write and review a pull request

A good pull request answers:

- What changed?
- Why was it needed?
- Which pages or behavior are affected?
- Which commands were run?
- Was mobile behavior checked?
- Is there a known failure or follow-up task?
- Does the change include only files related to the task?

Before merging, inspect the difference rather than trusting the description alone. The description explains the intention; the diff shows what will actually enter main.

### If you make a mistake

**You edited the wrong branch:** Stop. Run git status. Do not copy files around or reset blindly. Tell the other person what happened.

**You committed locally but did not push:** The commit is still on your PC. It can usually be inspected or corrected before anyone else sees it.

**You pushed the wrong branch:** Do not delete it immediately. Tell the other person and decide whether to keep, close, or replace the pull request.

**You see a merge conflict:** Git is telling you that it cannot safely choose between two edits. Read the marked files and discuss the intended result. Do not choose “ours” or “theirs” for every file without understanding the change.

**You committed a secret:** Stop immediately. Treat the secret as exposed, revoke or rotate it, and notify the other person. Removing it in a later commit is not enough.

**You are unsure what a command will delete:** Do not run it. Ask first. Avoid hard reset, force-push, broad deletion, and history-rewriting commands.

### The short version

For every task, remember:

1. Pull the latest main.
2. Create a branch.
3. Edit and test locally.
4. Check status and diff.
5. Commit a focused change.
6. Push the branch.
7. Use a pull request.
8. Review before merging.
9. Deploy only through the agreed and documented process.
10. Keep secrets out of GitHub.

The purpose of GitHub is not to make coding feel complicated. It is to make teamwork visible, reversible, and reviewable. Everyone can see which version is shared, which work is proposed, who reviewed it, and what changed.

## Fresh-PC readiness and the true co-work completion gate

This handoff is designed for Ean to begin with a fresh Windows PC. He should not need a copy of your computer, your GitHub login, your editor settings, your local environment files, or any deployment account. The portable project setup is:

- his own GitHub account;
- Git for Windows or GitHub Desktop;
- Node.js 20.9.0 or newer;
- npm using the committed package-lock.json;
- his preferred code editor; and
- the public repository clone.

He does not need Python, a local database, Wrangler, Cloudflare access, Vercel access, Resend access, or any production credential to run the normal website locally.

### What has been verified from a clean checkout

On August 22, 2026, a disposable clean clone of the public repository was used to verify the second-computer path without using the working copy or the untracked scripts/cookies/archive/ content:

1. The repository cloned from the documented GitHub URL.
2. The clean checkout installed successfully with npm ci.
3. npm run build passed.
4. npx tsc --noEmit passed.
5. npm run dev started the site on port 3009, and http://127.0.0.1:3009 returned HTTP 200.

This verifies that the committed source and lockfile are portable. It does not yet verify Ean's GitHub permission or his particular PC. Those require the repository invitation and Ean's own first branch push.

### What “true co-work” means for this project

We are ready for normal two-person co-development when all of these are true:

- Ean has accepted the invitation while signed into his own GitHub account.
- Ean has cloned the exact repository URL.
- Ean has completed npm ci successfully.
- Ean can open the site locally at http://localhost:3009, or has used the documented production-build fallback if Windows has the known lightningcss issue.
- Ean has run the build and TypeScript checks.
- Ean can create and push a feature branch, but a direct push to protected main is blocked.
- Ean has opened a first pull request to main.
- You have reviewed that pull request and merged it only after the checks and behavior are understood.
- Neither person is sharing credentials or committing environment files.

That is real co-development: GitHub is the shared source of truth, each person works in a separate local clone and branch, and the pull request is the review and handoff point. It is not a shared folder and it does not require either person to use the other person's account.

### Remaining shared setup items

The project is source-and-build ready for a second PC, but collaboration is not complete until you perform the access gates:

1. Invite Ean's exact GitHub username.
2. Ean accepts the invitation.
3. Ean completes the fresh-PC setup and shares the results of node --version, npm --version, npm run build, and npx tsc --noEmit.
4. Ean pushes a small branch such as ean/setup-verification.
5. Ean opens the first pull request.
6. Review the changed files, checks, and branch target together.

One reproducibility improvement remains optional: package.json does not currently declare an engines.node range and the repository does not include an .nvmrc or equivalent version file. Until that is added in a separate, coordinated change, the handoff's Node.js 20.9.0-or-newer requirement is the authoritative minimum. Do not add that tooling change as part of Ean's first contribution unless you agree on it first.

The known lint failure and the unresolved Vercel-versus-Cloudflare deployment documentation conflict remain project-level issues. Neither should prevent Ean from cloning, running, building, branching, or opening a pull request. They do mean that production deployment remains a separate technical-access responsibility until both partners agree on a shared process.
