# Bleeding Ink Tattoo — Ean’s Setup and Collaboration Handoff

**Welcome, Ean.** This document is written for you and assumes you are setting up the project on a fresh Windows PC.

Repository:

<https://github.com/bbasketballer75/bleeding-ink-tattoo-web>

## Important: use your own accounts

Austin and Ean are equal project partners. This document is a learning guide for getting started with the tools, not a boss/employee instruction sheet.

The repository currently lives under Austin’s personal GitHub account. That means Austin’s account has the technical ability to manage repository settings and the provider credentials already attached to the project. It does not mean Austin is your manager or that he has a higher project role. Code decisions, priorities, creative direction, and review conversations belong to both partners.

You do **not** need Austin’s:

- GitHub password.
- GitHub personal access token.
- Copilot account.
- Cloudflare account or token.
- Vercel account or token.
- Resend API key.
- Production `.env` file.

You will use your own GitHub account and your own computer. If something says permission denied, troubleshoot the account or invitation together rather than sharing credentials as a shortcut.

The repository is currently public, so you can view and clone it once you know the URL. You must accept Austin’s GitHub collaborator invitation before you can push your work back to the repository.

## What you will be doing

The normal partner workflow is:

1. You and Austin agree on a task or choose a task together.
2. The partner doing the work starts from the latest `main` branch.
3. That partner creates a feature branch.
4. That partner makes one focused change and tests it locally.
5. That partner pushes the feature branch.
6. That partner opens a pull request into `main`.
7. The pull request explains what changed and what was tested.
8. The partner who did not author the pull request reviews it.
9. Both partners discuss questions or requested changes.
10. The change is merged only after the partners agree it is ready and the required GitHub review is present.
11. Production deployment remains a separate technical-access step until the partners agree on a shared deployment arrangement.

Do **not** work directly on `main`. Do **not** deploy production. Do **not** use `--force`.

## Equal technical ownership option

Right now, the repository is owned by Austin’s personal GitHub account. That gives Austin’s account administrative control over repository settings, but it does not make him your boss or make you a lower-level project participant. You and Austin are equal partners in the project.

If both partners want equal GitHub administration too, the project can later move into a dedicated GitHub Organization. Austin and Ean would continue using their own personal GitHub accounts, and both could be made organization owners. The repository would then belong to the shared organization instead of to one personal account.

GitHub organizations are available on GitHub Free, with feature limits for private repositories. Because this repository is currently public, the shared-organization path should not require another paid GitHub subscription. The partners can compare plans later if the repository becomes private or the team needs paid organization features.

That change has not happened yet. Until both partners agree on the organization name and verify the repository’s deployment connections and secrets, use the current personal-repository workflow: separate clones, feature branches, peer review, and pull requests. The current account boundary is technical, not a project hierarchy.

Official references: [personal repository permission levels](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/permission-levels-for-a-personal-account-repository), [about organizations](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/about-organizations), and [transferring a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository).

## Step 1: create or secure your GitHub account

Before cloning:

- [ ] Create a GitHub account or confirm that you already have one.
- [ ] Enable two-factor authentication.
- [ ] Send Austin your exact GitHub username.
- [ ] Wait for Austin to invite that username to the repository.
- [ ] Accept the invitation from GitHub.

Use the exact username that appears on your GitHub profile. Do not rely only on a display name because multiple people can have similar display names.

## Step 2: install the local tools

Install these on your Windows PC:

- Git for Windows or GitHub Desktop.
- Node.js LTS, satisfying Node.js `>=20.9.0`.
- Your preferred code editor, such as VS Code.

Open a new PowerShell window after installing Node and check:

~~~powershell
node --version
npm --version
~~~

The Node version must be `20.9.0` or newer.

## Step 3: clone the repository

Choose either GitHub Desktop or PowerShell.

### Option A — GitHub Desktop

1. Open GitHub Desktop.
2. Sign in with **your own** GitHub account.
3. Choose **File → Clone repository**.
4. Select the **URL** tab.
5. Paste:

   ~~~text
   https://github.com/bbasketballer75/bleeding-ink-tattoo-web.git
   ~~~

6. Choose the local folder where you want to keep the project.
7. Click **Clone**.
8. Open the cloned folder in your editor.

### Option B — GitHub CLI and PowerShell

If GitHub CLI is installed:

~~~powershell
gh auth login
~~~

When prompted:

1. Choose **GitHub.com**.
2. Choose **HTTPS**.
3. Choose **Login with a web browser**.
4. Complete the browser sign-in using your own GitHub account.

Then clone the project:

~~~powershell
gh repo clone bbasketballer75/bleeding-ink-tattoo-web
cd bleeding-ink-tattoo-web
~~~

### Option C — plain Git

~~~powershell
git clone https://github.com/bbasketballer75/bleeding-ink-tattoo-web.git
cd bleeding-ink-tattoo-web
~~~

Confirm that the remote is correct:

~~~powershell
git remote -v
~~~

You should see:

~~~text
https://github.com/bbasketballer75/bleeding-ink-tattoo-web.git
~~~

## Step 4: install the project dependencies

From inside the repository folder, run:

~~~powershell
npm ci
~~~

This installs the dependency versions recorded in the project’s `package-lock.json`.

Do not replace `npm ci` with a random package manager, and do not upgrade dependencies just to make the first install work. If the command fails, save the complete error and share it with Austin so you can troubleshoot it together.

## Step 5: start the website locally

Run:

~~~powershell
npm run dev
~~~

Open:

<http://localhost:3009>

The project is a Next.js application for Bleeding Ink Tattooing. The important areas include:

- `/` — home page.
- `/artists` — artist listing.
- `/portfolio` — portfolio and filters.
- `/services` — services and deposit information.
- `/contact` — contact page and form.
- `/faq` — frequently asked questions.
- `/book` — booking page.

If port `3009` is already being used, start on another local port:

~~~powershell
npm run dev -- -p 3010
~~~

Then open:

<http://localhost:3010>

## Windows fallback if development mode crashes

This project has a known Windows/Turbopack issue that can sometimes appear on a fresh machine as a `lightningcss` worker failure or an error such as `0xc0000142`.

If `npm run dev` fails with that type of error, use the production-build fallback:

~~~powershell
npm run build
npm run start -- -p 3009
~~~

Then open:

<http://localhost:3009>

This verifies the application using the built output without relying on the development worker that failed.

Do not immediately upgrade Next.js, React, or dependencies to solve this. Share the complete error with Austin first so you can troubleshoot it together.

## Step 6: local environment variables

The repository contains `.env.example`. If you need local environment configuration, copy it to `.env.local` in the repository root:

~~~powershell
Copy-Item .env.example .env.local
~~~

`.env.local` is for your computer only. Never commit it.

The current example references variables including:

- `RESEND_API_KEY`
- `RESEND_FROM_EMAIL`
- `CONTACT_TO_EMAIL`
- `NEXT_PUBLIC_GLOSSGENIUS_URL`
- `NEXT_PUBLIC_PLAUSIBLE_DOMAIN`

Do not request production values as part of normal setup. If a feature requires a secret, tell your project partner which feature needs it and discuss a separate development-safe value through a secure channel.

Never commit or share:

- `RESEND_API_KEY`.
- Cloudflare tokens.
- Vercel tokens.
- GitHub personal access tokens.
- Production database credentials.
- Production `.env` files.
- Passwords or private keys.

If you accidentally stage a local environment file, stop and remove it from the staged set before committing:

~~~powershell
git status
git restore --staged .env.local
~~~

Do not commit a secret and then assume deleting it later makes it safe.

## Step 7: run the current checks

Before opening a pull request, run:

~~~powershell
npm run build
npx tsc --noEmit
git status
~~~

The project’s current baseline expects the build and TypeScript checks to work.

The project does not currently have a test runner installed.

`npm run lint` currently has known project failures. You may run it to see the current state:

~~~powershell
npm run lint
~~~

If lint fails with the existing known errors, include that fact in the pull request. Do not treat it as proof that your PC setup is broken, and do not make a large unrelated lint cleanup unless both partners agree on that work.

## Step 8: understand the project conventions

Before editing, read:

~~~text
README.md
AGENTS.md
~~~

Important project rules:

- Keep the existing inline-style approach. Do not convert the entire site to Tailwind utility classes.
- Keep brand constants in `src/lib/constants.ts`.
- Keep business information in `src/data/`.
- Keep the `$65` deposit amount sourced from `DEPOSIT_MIN`.
- Update metadata when changing business information.
- Test mobile layouts after visual changes.
- Do not add `jsx: "preserve"`.
- Do not add an incompatible `global-error.tsx`.
- Do not add `<html>` wrappers to `not-found.tsx`.
- Keep page-level server components and interactive `*Content.tsx` components organized as the project expects.
- Do not commit `node_modules`, `.next`, `.open-next`, `.wrangler`, `.env.local`, cookies, or generated exports.
- Do not casually upgrade framework or deployment dependencies in a feature change.

## Step 9: create your first branch

Always start from the latest `main`:

~~~powershell
git switch main
git pull origin main
git switch -c ean/short-description
~~~

Examples:

~~~powershell
git switch -c ean/contact-form
git switch -c ean/mobile-nav-fix
git switch -c ean/portfolio-update
~~~

Use a branch name that explains the work. Do not use `main` for personal edits.

## Step 10: commit and push your work

After editing:

~~~powershell
npm run build
npx tsc --noEmit
git status
git add .
git commit -m "Describe the change"
git push -u origin ean/short-description
~~~

Replace `ean/short-description` with the actual branch name. Before committing, inspect the `git status` output and make sure you are not including:

- `.env.local`.
- API keys or tokens.
- `node_modules`.
- `.next`, `.open-next`, or `.wrangler` output.
- Cookies or scraped exports.
- Unrelated files.

Never use:

~~~powershell
git push --force
~~~

Never force-push `main`.

## Step 11: open the pull request

After the branch push:

1. Open the repository on GitHub.
2. Choose **Compare & pull request** for your branch, or open **Pull requests → New pull request**.
3. Set the base branch to `main`.
4. Set the compare branch to your `ean/...` branch.
5. Explain what changed.
6. Explain why it changed.
7. List the pages or behavior affected.
8. List the commands you ran.
9. Mention any known failure, especially the current lint baseline if it applies.
10. Submit the pull request.

Do not merge your own pull request without a review from the other partner. The normal arrangement is that the partner who did not author the pull request reviews it, both partners agree it is ready, and the account with the required GitHub permission completes the merge. That may be Austin under the current personal-repository setup, but it is an administrative detail, not a senior project role.

If Austin requests changes, stay on the same branch, make the updates, commit them, and push again:

~~~powershell
git add .
git commit -m "Address review feedback"
git push
~~~

The existing pull request will update automatically.

## Deployment boundary

You and Austin are equal project partners. The current deployment and provider credentials are attached to accounts under Austin’s name because of how the project is currently set up. That is a technical access boundary, not a higher project role.

Until the partners reconcile the Vercel-versus-Cloudflare documentation and agree on a deployment process:

- Do not run production deployment commands as part of normal contribution.
- Do not request, copy, or use Austin’s provider credentials.
- Do not put production secrets in the repository.
- Discuss any production or infrastructure change with Austin as your project partner before taking action.
- Keep your normal contribution boundary to local development, testing, branches, and pull requests.

If both partners later decide that Ean should deploy, create separate least-privilege access and document the process first.

Do **not** run:

~~~powershell
npm run deploy
npm run deploy:cf
wrangler deploy
~~~

The project currently has conflicting deployment documentation. README.md refers to Vercel, while DEPLOY-NOTES.md identifies a Cloudflare Workers demo. The partners need to agree on the authoritative production path before either person expands deployment access.

## Troubleshooting

### GitHub says permission denied

Run:

~~~powershell
gh auth status
git remote -v
git ls-remote origin
~~~

Check:

- You are signed into your own GitHub account.
- You accepted Austin’s repository invitation.
- The remote is exactly:

  ~~~text
  https://github.com/bbasketballer75/bleeding-ink-tattoo-web.git
  ~~~

- You are not using a stale Windows GitHub credential.

Do not ask for another person’s token. Share the exact error with your project partner instead.

### GitHub invitation not found

Check the email address associated with your GitHub account and the GitHub notifications page. Coordinate with Austin to confirm that the correct username was invited.

### Git uses the wrong account

Stop before pushing. Run:

~~~powershell
gh auth status
~~~

If you use GitHub Desktop, verify the signed-in account there too. Correct your own Windows Git credential rather than borrowing someone else’s credential.

### `npm ci` fails

Run:

~~~powershell
node --version
npm --version
Get-Location
~~~

Confirm Node is `20.9.0` or newer and that PowerShell is in the repository root. Save the complete error and share it with Austin before changing `package-lock.json`.

### `npm run dev` fails with `lightningcss` or `0xc0000142`

Use:

~~~powershell
npm run build
npm run start -- -p 3009
~~~

If this works, report that development mode hit the known Windows fallback issue.

### Port `3009` is busy

Use:

~~~powershell
npm run dev -- -p 3010
~~~

Then open <http://localhost:3010>.

### Branches have diverged

Stop before using `--force`. Run:

~~~powershell
git status
git branch -vv
git log --oneline --decorate -8
~~~

Send the output and explain what you were trying to do. Do not rewrite shared history without agreement.

### A feature needs a secret

Do not invent a production value and do not put a secret in GitHub. Tell your project partner which feature needs it and what kind of development-safe value would be required.

## Your first contribution is complete when

- [ ] You can open the project locally.
- [ ] You can run `npm run build`.
- [ ] You can run `npx tsc --noEmit`.
- [ ] You created an `ean/...` branch.
- [ ] You made one focused change.
- [ ] You checked `git status` before committing.
- [ ] You pushed the branch without force-pushing.
- [ ] You opened a pull request into `main`.
- [ ] You listed the commands you ran.
- [ ] You responded to review comments on the same branch.
- [ ] You did not receive or use production credentials.

When reporting a problem to your project partner, include:

1. What you were trying to do.
2. The exact command you ran.
3. The complete error message.
4. The output of `node --version` and `npm --version` if it is a setup issue.
5. The output of `git remote -v` if it is a GitHub access issue.

## GitHub from zero: what it is, why it works, and exactly what you do

This section assumes you have never used Git, GitHub, or a code-collaboration service before. That is completely fine. You do not need to learn everything at once. You need to understand where your files are, how your work gets saved, and how your work reaches Austin for review.

### First: what problem does GitHub solve?

There is one website and two developers. You need to work on the project without accidentally changing Austin’s local files. Austin also needs to review your work before it becomes part of the shared project.

GitHub solves this by giving us:

- separate copies of the project on each computer;
- a shared online copy of the project;
- a history of saved changes;
- separate work lanes called branches;
- a review page called a pull request; and
- a controlled way to combine approved work.

Without this process, people often email folders, overwrite each other’s files, forget which version is newest, or make a live change without another person seeing it first.

### The three places you need to understand

| Place | What it means to you |
|---|---|
| Your PC | Your local project folder. You edit files and run the website here. |
| GitHub | The online shared repository. You upload your branch here and open a pull request here. |
| The live website | The version visitors can see. You do not deploy it; Austin controls that process. |

Your local folder is not automatically connected in a way that uploads every save. GitHub is not a shared network folder. You will have your own copy on your own PC, and your project partner will have a separate copy on their PC.

The GitHub repository is also not the live website. A local edit does not change the live website. A push to your branch does not change main. Even after a pull request is merged, production deployment is a separate technical-access step under the current provider credentials.

### Git and GitHub are different

**Git** is the program on your PC. Git records changes, creates branches, saves checkpoints, and compares versions.

**GitHub** is the website that stores the shared repository. GitHub displays the branches, pull requests, reviews, Issues, and history.

A simple way to remember this:

- Git works with files on your PC.
- GitHub stores the shared online copy.
- You use Git commands to move selected work between your PC and GitHub.

Your GitHub account is your personal identity. Use your own account and password. Never use Austin’s account or ask him for a token.

### What happens to one change

Your change moves through this path:

~~~text
Edit file
  ↓
The change exists only on your PC

git add
  ↓
You choose the local files you want to save

git commit
  ↓
Git saves a named checkpoint on your PC

git push
  ↓
Your branch is uploaded to GitHub

Pull request
  ↓
The other partner sees the difference and reviews it

Merge
  ↓
The approved change is added to main

Deployment
  ↓
The partners agree when approved main code is ready; the current credential holder performs the deployment
~~~

These steps are separate on purpose.

- Saving a file in your editor does not create a Git checkpoint.
- A commit does not upload anything to GitHub.
- A push uploads your branch, not main.
- Opening a pull request does not merge anything.
- A pull request can receive comments and more commits.
- Only a merge changes main.
- A merge does not give you permission to deploy production.

### The words you will see

| Word | Plain-language meaning |
|---|---|
| Project folder | The website folder on your PC |
| Repository / repo | The website files plus their complete history |
| Clone | The first download that creates your local copy |
| Local copy | Your separate copy on your PC |
| Remote | The saved connection from your local copy to GitHub |
| origin | The usual name for this project’s GitHub connection |
| main | The shared stable branch |
| Branch | A separate work lane based on main |
| Staging area | A local list of files selected for the next checkpoint |
| Commit | A named saved checkpoint on your PC |
| Push | Upload your branch commits to GitHub |
| Pull | Download changes from GitHub into your current local branch |
| Fetch | Check for GitHub updates without changing your files |
| Pull request / PR | A request for the other partner to review and merge your branch |
| Review | Questions, suggestions, and approval on a pull request |
| Merge | Combine your approved branch into main |
| Conflict | Two edits Git cannot combine automatically |
| Issue | A task, bug, question, or decision written on GitHub |
| Deployment | Publishing approved code to the hosting provider and live website |

### Why you must use a branch

main is the shared stable version. You should not edit it directly.

Your branch is a separate work lane based on main. For example:

~~~text
main
└── ean/mobile-nav-fix
~~~

You can make incomplete edits, test them, and save them without changing the shared main branch. The other partner can see your branch on GitHub only after you push it.

Use a new branch for each meaningful task:

~~~text
ean/contact-form
ean/mobile-nav-fix
ean/portfolio-update
ean/faq-copy
~~~

A branch is not a folder you email to Austin. GitHub stores the branch and calculates the exact difference between your branch and main.

### Your exact work cycle

When you and your partner agree on a task, do these steps in order.

#### 1. Start from the current shared version

Open PowerShell in the project folder. PowerShell is the Windows command window where you run these commands.

Check your current location and branch:

~~~powershell
git status
~~~

Move to main and download the newest shared version:

~~~powershell
git switch main
git pull --ff-only origin main
~~~

The pull command updates your local main. It does not erase your feature branch.

#### 2. Create your work branch

Create a new branch with a short name describing the task:

~~~powershell
git switch -c ean/short-description
~~~

From this point until the task is complete, work on the ean/... branch. Do not switch back to main while you have uncommitted changes unless you understand exactly what Git will do.

#### 3. Edit and test locally

Change the files in your editor. The website is still only changing on your PC.

Check what you changed:

~~~powershell
git status
git diff
~~~

Run the project checks:

~~~powershell
npm run build
npx tsc --noEmit
~~~

Open the affected pages in the browser. Test mobile behavior when the change affects layout.

#### 4. Save a focused checkpoint

Choose the files for this task:

~~~powershell
git add path/to/changed-file
~~~

Read the staged difference:

~~~powershell
git diff --cached
~~~

If it looks correct, create a commit:

~~~powershell
git commit -m "Describe the change"
~~~

A commit is a saved checkpoint on your PC. Your partner cannot see it yet.

#### 5. Upload your branch

The first time you upload this branch, run:

~~~powershell
git push -u origin ean/short-description
~~~

This sends your branch to GitHub. It does not change main.

For later commits on the same branch, use:

~~~powershell
git push
~~~

#### 6. Open the pull request

On the repository page on GitHub:

1. Choose **Compare & pull request**, or choose **Pull requests → New pull request**.
2. Set the base branch to main.
3. Set the compare branch to your ean/... branch.
4. Explain what you changed.
5. Explain why you changed it.
6. List the checks you ran.
7. Mention anything that did not pass.
8. Submit the pull request.

The pull request is the place where your partner sees the proposed change. It is not an automatic merge.

#### 7. Respond to review

Your partner may approve the pull request or ask questions. Review comments are about the project, not a personal judgment.

If Austin asks for a change:

1. Stay on the same ean/... branch.
2. Edit the files.
3. Run the relevant checks again.
4. Make another commit.
5. Push the same branch.

~~~powershell
git add path/to/changed-file
git commit -m "Address review feedback"
git push
~~~

GitHub adds the new commit to the existing pull request. Do not open a second pull request just because Austin asked for a revision.

#### 8. Understand the merge

The non-author partner reviews the pull request; both partners agree it is ready, and the account with the required merge permission completes the merge.

After the merge:

- the approved code is part of main on GitHub;
- your branch may be deleted after the work is complete;
- your local files do not automatically update;
- you should update your local main before starting another task; and
- production deployment remains a separate technical-access step under the current credentials.

### What the important commands do

| Command or action | What it does | What it does not do |
|---|---|---|
| Edit and save | Changes files on your PC | Does not contact GitHub |
| git status | Reports your branch and changed files | Does not save or upload anything |
| git diff | Shows your uncommitted edits | Does not change the project |
| git add | Selects files for the next commit | Does not upload them |
| git commit | Saves a named local checkpoint | Does not upload it |
| git push | Uploads your branch to GitHub | Does not change main |
| Open pull request | Starts review on GitHub | Does not merge |
| git pull | Downloads updates into your current branch | Does not upload your work |
| Merge button | Combines the approved branch into main | Does not deploy production |

### What you will see on the GitHub website

- **Code:** The files stored in the repository.
- **Issues:** Written tasks, bugs, questions, and decisions.
- **Pull requests:** Proposed code changes waiting for review or already merged.
- **Branches:** Separate work lanes, including your ean/... branches.
- **Commits / history:** The record of saved checkpoints and who made them.
- **Actions:** Automated checks if the project adds them later.
- **Settings:** Access and repository controls. Do not change these unless both partners agree.

Use an Issue when you need to describe work or a problem. Use a pull request when you have code on a branch and are asking for review.

### How to write a useful pull request

A useful pull request answers:

- What did I change?
- Why did I change it?
- Which pages or behavior are affected?
- What commands did I run?
- Did I test on a phone-sized screen when needed?
- Is anything still failing?
- Did I change anything unrelated?

Your partner should be able to understand the purpose of the change without guessing. Before requesting review, read your own difference on the Files changed tab.

### If you make a mistake

**I edited main by accident:** Stop. Do not push. Run git status and tell your project partner what happened.

**I saved a file but did not commit:** The edit is still on your PC. Review git diff and decide whether it belongs in the task.

**I committed but did not push:** The checkpoint is still on your PC. It is not lost. Ask if you are unsure what to do next.

**I pushed the wrong branch:** Do not delete it immediately. Tell your project partner and discuss what to do with the branch or pull request.

**I see a conflict:** Git cannot automatically decide between two edits. Do not choose every incoming file automatically. Read the conflict and ask your project partner if the intended result is unclear.

**I committed a secret:** Stop immediately. Tell your project partner so the credential can be revoked or rotated. Removing the secret in a later commit does not make the old history safe.

**A command might delete work:** Stop and ask before running it. Never use hard reset, force-push, broad deletion, or history-rewriting commands as a guess.

### Your simple GitHub rules

1. Use your own GitHub account.
2. Work in your own local project folder.
3. Pull the latest main before starting.
4. Create an ean/... branch.
5. Never push directly to main.
6. Check git status and git diff before committing.
7. Commit one understandable change at a time.
8. Push your branch, then open a pull request.
9. Keep responding on the same pull request if Austin requests changes.
10. Never commit secrets or environment files.
11. Do not deploy production.
12. Ask when you do not understand a command.

GitHub is not designed to make you guess which copy is correct. It gives us a visible path from your local edit, to your saved checkpoint, to your branch, to review, and finally to the shared main branch. That is how both partners can work without overwriting each other.

## Fresh-PC readiness and your first successful run

This guide assumes you are starting with a fresh Windows PC. You do not need anything from Austin's computer except the public repository link and the GitHub invitation. You will use your own GitHub account, your own Windows login, your own editor, and your own local clone.

### What you need to install

Before the project can run, install only these basics:

- Git for Windows, or GitHub Desktop. GitHub Desktop is the easiest option if you are new to Git.
- Node.js LTS with version 20.9.0 or newer.
- A code editor, such as Visual Studio Code.
- A normal internet connection so the repository and npm packages can be downloaded.

You do not need Python, a database, Wrangler, Cloudflare, Vercel, Resend, or any production account for normal local website development. Do not install or request those accounts just to get started.

### The exact fresh-PC sequence

Complete these steps in order:

1. Create or use your own GitHub account and turn on two-factor authentication.
2. Send Austin your exact GitHub username.
3. Wait for Austin's repository invitation and accept it while signed into that same account.
4. Install Git for Windows or GitHub Desktop, Node.js LTS, and your editor.
5. Clone the repository into a new folder. Do not copy Austin's local project folder.
6. Open PowerShell in the cloned repository root.
7. Confirm the tools:

~~~powershell
node --version
npm --version
git --version
git remote -v
~~~

Node must report 20.9.0 or newer. The remote must be:

~~~text
https://github.com/bbasketballer75/bleeding-ink-tattoo-web.git
~~~

8. Install exactly the dependency versions recorded by the project:

~~~powershell
npm ci
~~~

9. Start the website:

~~~powershell
npm run dev
~~~

10. Leave that terminal open and visit:

~~~text
http://localhost:3009
~~~

Because npm run dev is a running server, the terminal is expected to remain busy until you stop it with Ctrl+C. That is normal.

### What has already been proven

A disposable clean clone of the public repository was tested on August 22, 2026. The clone completed npm ci, npm run build passed, npx tsc --noEmit passed, and the development server returned HTTP 200 on port 3009. That means the committed project source and lockfile are set up for a second computer.

This does not replace your own first run: your computer may have a different Windows configuration, antivirus rule, Node installation, or port conflict. If your result differs, share the complete command and error output with Austin so you can troubleshoot it together instead of changing unrelated project files.

### If the development server has the known Windows problem

The project has a documented Windows/Turbopack fallback. If npm run dev fails with a lightningcss worker error or 0xc0000142, run:

~~~powershell
npm run build
npm run start -- -p 3009
~~~

Then visit http://localhost:3009. This starts the already-built production server and is a valid local verification path. Stop it with Ctrl+C when finished.

If port 3009 is already being used by another program, use:

~~~powershell
npm run dev -- -p 3010
~~~

Then visit http://localhost:3010.

### Your fresh-PC completion checklist

Share your setup results with Austin and agree on the first task together only after you can check every applicable box:

- [ ] I accepted the invitation using my own GitHub account.
- [ ] Git and Node.js are installed.
- [ ] Node reports 20.9.0 or newer.
- [ ] The remote points to the bleeding-ink-tattoo-web repository.
- [ ] npm ci completed.
- [ ] The website opens at port 3009, or I used the documented build fallback.
- [ ] npm run build passed.
- [ ] npx tsc --noEmit passed.
- [ ] I created an ean/ branch rather than working on main.
- [ ] I pushed that branch and opened a pull request.

When these boxes are complete, you and Austin have a real two-person workflow: you each have an independent local copy, GitHub records the shared history, branches keep work separate, and the pull request gives each partner a chance to review before anything reaches main. You do not need a shared network folder or either partner’s credentials.

The repository currently has a minimum Node requirement rather than one pinned exact Node version. Use Node 20.9.0 or newer, and use npm with package-lock.json as instructed. If a future team decision adds an .nvmrc or engines.node field, follow that newer project instruction.
