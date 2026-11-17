<div align="center">

# 🚀 Pro GitHub Starter Kit

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=3B82F6&center=true&vCenter=true&width=640&lines=Build+a+Standout+GitHub+Profile+in+Minutes.;Modular+Themes+%2B+Plug-and-Play+Automation.;Curated+Tools%2C+Legit+Badges+%26+SEO+Ready.)](https://github.com/cmduyeen/pro-github-starter-kit)

[![Validate Themes, Plugins & Tests](https://github.com/cmduyeen/pro-github-starter-kit/actions/workflows/validate-extensions.yml/badge.svg)](https://github.com/cmduyeen/pro-github-starter-kit/actions/workflows/validate-extensions.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg?style=flat-square)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)
[![Template Repo](https://img.shields.io/badge/Use%20This%20Template-Click%20Here-2ea44f?style=flat-square&logo=github)](https://github.com/cmduyeen/pro-github-starter-kit/generate)

**An Obsidian-inspired, extensible starter kit for crafting a clean, automated, and high-converting GitHub Profile.**

[Quick Start](#-quick-start-no-coding-required) · [Live Preview](#-see-what-you-can-build) · [Themes (9)](#-1-pick-a-theme-themes) · [Plugins (12)](#-2-snap-in-plugins-plugins) · [Badges](#-legit-github-achievements)

</div>

---

## 📑 Table of Contents

- [⚡ Quick Start (No Coding Required)](#-quick-start-no-coding-required)
  - [Option A: 100% in Browser (Recommended)](#option-a-100-in-browser-recommended-for-beginners--non-tech)
  - [Option B: Interactive Terminal Wizard](#option-b-interactive-terminal-wizard-1-simple-command)
- [🎨 See What You Can Build](#-see-what-you-can-build)
- [🧩 Modular Themes & Plugins](#-modular-themes--plugins)
  - [1. Pick a Theme (`themes/`)](#-1-pick-a-theme-themes)
  - [2. Snap in Plugins (`plugins/`)](#-2-snap-in-plugins-plugins)
- [🛠 Curated Resources & SEO](#-curated-resources--seo)
- [🏆 Legit GitHub Achievements](#-legit-github-achievements)
- [🤝 Build Together & FAQ](#-build-together-add-your-own-theme-or-plugin)

---

## ⚡ Quick Start (No Coding Required)

### Option A: 100% in Browser (Recommended for Beginners & Non-Tech)

No terminal, no Python, no Git commands needed:

1. Click **[Use this template](https://github.com/cmduyeen/pro-github-starter-kit/generate)** and name your new public repository **exactly** `<your-username>/<your-username>`.
2. Open the **Actions** tab in your new repository → select **Build My Profile** → click **Run workflow**.
3. Pick your **Theme** from the dropdown, tick the **Plugins** you want (optional: paste your Blog RSS or Spotify UID), and click **Run workflow**. GitHub automatically builds and commits your new `README.md`!

### Option B: Interactive Terminal Wizard (1 Simple Command)

If you prefer running locally, just clone your repo and run:

```bash
python setup.py
```

A guided Q&A menu will walk you through picking a theme and plugins by number—no flags to memorize.

<details>
<summary><b>Option C: One-Line CLI (For Power Users)</b></summary>

```bash
python setup.py --username <your-username> \
  --theme indie-maker \
  --plugins typing-svg,skill-icons,blog-rss,spotify-now-playing,github-stats \
  --var BLOG_RSS_URL=https://yourblog.com/index.xml \
  --var SPOTIFY_UID=your_spotify_uid
```

</details>

> [!TIP]
> Want to preview available options first? Run `python setup.py --list` or add `--dry-run`.

---

## 🎨 See What You Can Build

Why settle for plain text when you can snap together live, zero-maintenance widgets? Here is a live preview of what the built-in plugins render:

<div align="center">

**Tech Stack Grid (`skill-icons` plugin)**

[![My Skills](https://skillicons.dev/icons?i=py,ts,js,react,nodejs,docker,git,github,vscode,obsidian)](https://skillicons.dev)

**Crisp Social & Contact Bar (`social-badges` plugin)**

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/cmduyeen)
[![X](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/cmduyeen)
[![Blog](https://img.shields.io/badge/Blog-2563EB?style=for-the-badge&logo=rss&logoColor=white)](https://cmduyeen.github.io)

</div>

---

## 🧩 Modular Themes & Plugins

Just like **Obsidian**, this kit separates **Layout (`themes/`)** from **Features (`plugins/`)** so you can mix, match, or contribute your own.

### 1. Pick a Theme (`themes/`)

Click any preview card or **Live Preview** link to see the rendered profile immediately on GitHub:

<!-- THEMES-TABLE:START -->
| Preview | Theme | Description | Quick Links |
| :---: | --- | --- | --- |
| [<img src="assets/previews/catppuccin.svg" width="150" alt="Catppuccin Mocha Preview"/>](themes/catppuccin/PREVIEW.md) | **`catppuccin`**<br/>Catppuccin Mocha *(by @cmduyeen)* | Soothing pastel-dark palette inspired by Catppuccin (catppuccin/catppuccin). | [Live Preview](themes/catppuccin/PREVIEW.md) · [Template](themes/catppuccin/README.template.md) |
| [<img src="assets/previews/developer-portfolio.svg" width="150" alt="Developer Portfolio Preview"/>](themes/developer-portfolio/PREVIEW.md) | **`developer-portfolio`**<br/>Developer Portfolio *(by @cmduyeen)* | Full developer showcase ready for tech stack icons, stats cards, and activity widgets. | [Live Preview](themes/developer-portfolio/PREVIEW.md) · [Template](themes/developer-portfolio/README.template.md) |
| [<img src="assets/previews/dracula.svg" width="150" alt="Dracula Palette Preview"/>](themes/dracula/PREVIEW.md) | **`dracula`**<br/>Dracula Palette *(by @cmduyeen)* | Dark purple & neon palette inspired by Dracula Theme (dracula/dracula-theme). | [Live Preview](themes/dracula/PREVIEW.md) · [Template](themes/dracula/README.template.md) |
| [<img src="assets/previews/indie-maker.svg" width="150" alt="Indie Maker Preview"/>](themes/indie-maker/PREVIEW.md) | **`indie-maker`**<br/>Indie Maker *(by @cmduyeen)* | Product-focused layout highlighting shipped projects, writing, and updates. | [Live Preview](themes/indie-maker/PREVIEW.md) · [Template](themes/indie-maker/README.template.md) |
| [<img src="assets/previews/minimalist.svg" width="150" alt="Minimalist Preview"/>](themes/minimalist/PREVIEW.md) | **`minimalist`**<br/>Minimalist *(by @cmduyeen)* | Clean text-first profile with zero visual clutter. | [Live Preview](themes/minimalist/PREVIEW.md) · [Template](themes/minimalist/README.template.md) |
| [<img src="assets/previews/pinkie.svg" width="150" alt="Pinkie Pastel Preview"/>](themes/pinkie/PREVIEW.md) | **`pinkie`**<br/>Pinkie Pastel *(by @cmduyeen)* | Soft pastel-pink aesthetic from Pinkie Theme (cmduyeen/pinkie-theme). | [Live Preview](themes/pinkie/PREVIEW.md) · [Template](themes/pinkie/README.template.md) |
| [<img src="assets/previews/research-student.svg" width="150" alt="Student & Self-Learner Preview"/>](themes/research-student/PREVIEW.md) | **`research-student`**<br/>Student & Self-Learner *(by @cmduyeen)* | Structured layout highlighting learning roadmap, notes, and starter projects. | [Live Preview](themes/research-student/PREVIEW.md) · [Template](themes/research-student/README.template.md) |
| [<img src="assets/previews/serein.svg" width="150" alt="Serein Warm Minimal Preview"/>](themes/serein/PREVIEW.md) | **`serein`**<br/>Serein Warm Minimal *(by @cmduyeen)* | Warm, low-distraction palette from Serein Theme (cmduyeen/serein-theme). | [Live Preview](themes/serein/PREVIEW.md) · [Template](themes/serein/README.template.md) |
| [<img src="assets/previews/terminal-hacker.svg" width="150" alt="Terminal / CLI Preview"/>](themes/terminal-hacker/PREVIEW.md) | **`terminal-hacker`**<br/>Terminal / CLI *(by @cmduyeen)* | Neofetch-inspired terminal block layout for CLI and systems developers. | [Live Preview](themes/terminal-hacker/PREVIEW.md) · [Template](themes/terminal-hacker/README.template.md) |
<!-- THEMES-TABLE:END -->

### 2. Snap in Plugins (`plugins/`)

<!-- PLUGINS-TABLE:START -->
| Preview | Plugin | Description | Quick Links |
| :---: | --- | --- | --- |
| [<img src="assets/previews/plugins/activity-graph.svg" width="150" alt="Contribution Activity Graph Preview"/>](plugins/activity-graph/PREVIEW.md) | **`activity-graph`**<br/>*(by @cmduyeen)* | Renders a 31-day contribution line graph using github-readme-activity-graph. | [Live Preview](plugins/activity-graph/PREVIEW.md) · [Snippet](plugins/activity-graph/snippet.md) |
| [<img src="assets/previews/plugins/blog-rss.svg" width="150" alt="Blog RSS Sync Preview"/>](plugins/blog-rss/PREVIEW.md) | **`blog-rss`**<br/>*(by @cmduyeen · *Auto-sync*)* | Automatically syncs your latest blog posts via RSS using GitHub Actions. | [Live Preview](plugins/blog-rss/PREVIEW.md) · [Snippet](plugins/blog-rss/snippet.md) |
| [<img src="assets/previews/plugins/github-stats.svg" width="150" alt="GitHub Stats & Streak Cards Preview"/>](plugins/github-stats/PREVIEW.md) | **`github-stats`**<br/>*(by @cmduyeen)* | Embeds dynamic GitHub summary stats, top languages, and streak cards. | [Live Preview](plugins/github-stats/PREVIEW.md) · [Snippet](plugins/github-stats/snippet.md) |
| [<img src="assets/previews/plugins/profile-views.svg" width="150" alt="Profile Views Counter Preview"/>](plugins/profile-views/PREVIEW.md) | **`profile-views`**<br/>*(by @cmduyeen)* | Adds a live profile visitor counter badge via komarev.com. | [Live Preview](plugins/profile-views/PREVIEW.md) · [Snippet](plugins/profile-views/snippet.md) |
| [<img src="assets/previews/plugins/skill-icons.svg" width="150" alt="Skill Icons Grid Preview"/>](plugins/skill-icons/PREVIEW.md) | **`skill-icons`**<br/>*(by @cmduyeen)* | Displays your tech stack cleanly using skillicons.dev. | [Live Preview](plugins/skill-icons/PREVIEW.md) · [Snippet](plugins/skill-icons/snippet.md) |
| [<img src="assets/previews/plugins/snake-contribution.svg" width="150" alt="Contribution Snake Animation Preview"/>](plugins/snake-contribution/PREVIEW.md) | **`snake-contribution`**<br/>*(by @cmduyeen · *Auto-sync*)* | Generates an animated SVG snake eating your contribution graph daily via Platane/snk. | [Live Preview](plugins/snake-contribution/PREVIEW.md) · [Snippet](plugins/snake-contribution/snippet.md) |
| [<img src="assets/previews/plugins/social-badges.svg" width="150" alt="Social & Contact Badges Preview"/>](plugins/social-badges/PREVIEW.md) | **`social-badges`**<br/>*(by @cmduyeen)* | Adds crisp shields.io social and portfolio badges. | [Live Preview](plugins/social-badges/PREVIEW.md) · [Snippet](plugins/social-badges/snippet.md) |
| [<img src="assets/previews/plugins/sponsor-badge.svg" width="150" alt="Sponsor & Support Badges Preview"/>](plugins/sponsor-badge/PREVIEW.md) | **`sponsor-badge`**<br/>*(by @cmduyeen)* | Adds GitHub Sponsors and support buttons to help fund your open-source work. | [Live Preview](plugins/sponsor-badge/PREVIEW.md) · [Snippet](plugins/sponsor-badge/snippet.md) |
| [<img src="assets/previews/plugins/spotify-now-playing.svg" width="150" alt="Spotify Now Playing Preview"/>](plugins/spotify-now-playing/PREVIEW.md) | **`spotify-now-playing`**<br/>*(by @cmduyeen)* | Displays your currently playing or recently played Spotify track. | [Live Preview](plugins/spotify-now-playing/PREVIEW.md) · [Snippet](plugins/spotify-now-playing/snippet.md) |
| [<img src="assets/previews/plugins/typing-svg.svg" width="150" alt="Typing SVG Banner Preview"/>](plugins/typing-svg/PREVIEW.md) | **`typing-svg`**<br/>*(by @cmduyeen)* | Adds an animated typing header powered by readme-typing-svg. | [Live Preview](plugins/typing-svg/PREVIEW.md) · [Snippet](plugins/typing-svg/snippet.md) |
| [<img src="assets/previews/plugins/wakatime-stats.svg" width="150" alt="WakaTime Coding Stats Preview"/>](plugins/wakatime-stats/PREVIEW.md) | **`wakatime-stats`**<br/>*(by @cmduyeen · *Auto-sync*)* | Automatically updates your weekly coding time and language breakdown via WakaTime. | [Live Preview](plugins/wakatime-stats/PREVIEW.md) · [Snippet](plugins/wakatime-stats/snippet.md) |
| [<img src="assets/previews/plugins/youtube-rss.svg" width="150" alt="YouTube RSS Sync Preview"/>](plugins/youtube-rss/PREVIEW.md) | **`youtube-rss`**<br/>*(by @cmduyeen · *Auto-sync*)* | Automatically lists your latest YouTube videos via channel RSS feed. | [Live Preview](plugins/youtube-rss/PREVIEW.md) · [Snippet](plugins/youtube-rss/snippet.md) |
<!-- PLUGINS-TABLE:END -->

> [!NOTE]
> All GitHub Actions workflows run **once per day** and only commit when new content appears—keeping your contribution graph authentic and clean. See **[docs/AUTOMATION.md](docs/AUTOMATION.md)** for setup details.

---

## 🛠 Curated Resources & SEO

### Famous Tools & Open-Source Repositories

We vetted the most reliable profile builders, SVG widgets, color palettes, and automation workflows—with direct links and usage notes:

| Category | Popular Tools & Repos | Why Use Them | Full Guide |
| --- | --- | --- | --- |
| **Visual Builders** | [readme.so](https://readme.so/) · [github-profile-readme-generator](https://github.com/rahuldkjain/github-profile-readme-generator) | Drag-and-drop Markdown blocks without writing syntax from scratch | [RESOURCES.md](docs/RESOURCES.md) |
| **Stats & Graphs** | [streak-stats](https://github.com/DenverCoder1/github-readme-streak-stats) · [activity-graph](https://github.com/ashutosh00710/github-readme-activity-graph) · [github-readme-stats](https://github.com/anuraghazra/github-readme-stats) · [metrics](https://github.com/lowlighter/metrics) | Showcase coding streaks, 31-day activity, and language stats *(self-host `github-readme-stats` on Vercel to avoid 503 limits)* | [RESOURCES.md](docs/RESOURCES.md) |
| **Icons & Badges** | [skill-icons](https://github.com/tandpfun/skill-icons) · [shields.io](https://shields.io/) · [simpleicons.org](https://simpleicons.org/) · [readme-typing-svg](https://github.com/DenverCoder1/readme-typing-svg) | Crisp SVG tech grids, custom social buttons, and animated typing headers | [RESOURCES.md](docs/RESOURCES.md) |
| **Automation** | [blog-post-workflow](https://github.com/gautamkrishnar/blog-post-workflow) · [Platane/snk](https://github.com/Platane/snk) · [waka-readme-stats](https://github.com/anmol098/waka-readme-stats) · [spotify-github-profile](https://github.com/kittinan/spotify-github-profile) | Auto-sync Blog/YouTube RSS, contribution snake, WakaTime, and Spotify | [AUTOMATION.md](docs/AUTOMATION.md) |
| **Color Palettes** | [catppuccin](https://github.com/catppuccin/catppuccin) · [dracula](https://github.com/dracula/dracula-theme) · [serein-theme](https://github.com/cmduyeen/serein-theme) · [pinkie-theme](https://github.com/cmduyeen/pinkie-theme) | Cohesive color systems for profiles, editors, and terminals | [Themes](#-1-pick-a-theme-themes) |
| **Inspiration** | [awesome-github-profile-readme](https://github.com/abhisheknaiidu/awesome-github-profile-readme) · [creative-profile-readme](https://github.com/coderjojo/creative-profile-readme) | Hundreds of real-world creative and minimalist profile examples | [RESOURCES.md](docs/RESOURCES.md) |

### GitHub SEO & GEO Checklist (Rank on Google, GitHub & AI Search)

<details>
<summary><b>🔍 Click to open the 4-Part GitHub SEO & GEO Checklist</b></summary>

1. **Profile Sidebar (First 5 Seconds):**
   - Use a recognizable **Name** (`Name (handle)`), a crisp **1-line Bio** stating what you build, and link your **Website/Blog** + **Social handle**.
2. **The 6 Pinned Repositories Strategy:**
   - Pin **6 flagship "gateway" repositories** (e.g., 1 main product, 1 theme/design system, 1 starter kit, 1 knowledge base/blog) instead of scattered minor sub-repos.
3. **Per-Repository On-Page SEO:**
   - **URL Slug:** Clear kebab-case keywords (e.g., `pro-github-starter-kit`).
   - **Description (140–160 chars):** Lead with primary keywords and clear value.
   - **Topics (up to 20/20):** Mix broad tags (`python`, `open-source`) with high-intent tags (`github-profile-readme`, `starter-kit`).
   - **Social Preview (`1280×640px`):** Upload a custom banner in **Settings → General → Social preview** for rich link cards on X, LinkedIn, and Discord.
4. **GEO (Generative Engine Optimization for AI Search):**
   - Add an **`llms.txt`** at the repo root summarizing key files, use **structured Markdown tables** with exact numbers, and include a direct **FAQ** section.

</details>

See the full printable checklist in **[docs/SEO-CHECKLIST.md](docs/SEO-CHECKLIST.md)**.

---

## 🏆 Legit GitHub Achievements

All **7 active GitHub Achievement Badges**, their tier thresholds, and legitimate ways to unlock them through real workflows:

| Badge | Exact Requirement | Tiers (Default / Bronze / Silver / Gold) | Legit Tip for Beginners |
| --- | --- | --- | --- |
| 🦈 **Pull Shark** | Open pull requests that get merged | 2 / 16 / 128 / 1,024 PRs | Use feature branches + PRs for your own projects, or fix typos in open-source docs |
| 👯 **Pair Extraordinaire** | Co-author a commit in a merged PR | 1 / 10 / 24 / 48 PRs | Add `Co-authored-by: Name <email>` in your commit footer when pairing with a friend |
| 🚀 **Quickdraw** | Close an issue or PR within **5 minutes** | 1 fast close *(single tier)* | Open an issue for a quick fix you already have ready, then close it right after |
| 🤠 **YOLO** | Merge a PR **without a code review** | 1 unreviewed merge *(single tier)* | On your own project, merge a real update PR directly without requesting review |
| 🧠 **Galaxy Brain** | Accepted answer in GitHub Discussions | 2 / 8 / 16 / 32 answers | Answer `Q&A` questions in repos you use and wait for *Mark as answer* |
| ⭐ **Starstruck** | Own a public repo hitting star milestones | 16 / 128 / 512 / 4,096 stars | Ship a genuinely helpful tool/kit with live previews & clean SEO topics |
| 💖 **Public Sponsor** | Sponsor an open-source dev/org | 1 sponsorship *(single tier)* | Sponsor any maintainer via **GitHub Sponsors** (even $1/month) |

<details>
<summary><b>📌 Step-by-Step: Unlock Your First 4 Badges Legitimately (No Bots Needed)</b></summary>

1. **Pull Shark + YOLO:** Instead of pushing directly to `main` on your personal project, create a real branch (`git checkout -b docs/update-bio`), edit your file, open a Pull Request on GitHub, and click **Merge pull request** without review (**YOLO** unlocked; do this for 2 real updates for **Pull Shark**).
2. **Pair Extraordinaire:** When collaborating on a PR, end your commit message with a blank line followed by:
   ```text
   Co-authored-by: Teammate Name <teammate-github-email@example.com>
   ```
   *(The email must belong to a real GitHub account).*
3. **Quickdraw:** When you notice a small bug or missing link in your repo, open an Issue, push the fix, and close the Issue within 5 minutes.

</details>

<details>
<summary><b>🎖️ Profile Highlights, Retired Badges & Common Myths</b></summary>

- **Profile Highlights (Sidebar):** `GitHub Pro` (free for students via GitHub Education) and `GitHub Developer Program` member badge.
- **Retired Badges (No longer obtainable):** `Arctic Code Vault Contributor` (2020 snapshot) and `Mars 2020 Helicopter Contributor`.
- **Green Squares ≠ Badge:** The contribution calendar tracks daily activity, not an Achievement Badge.

</details>

> [!WARNING]
> Never use bots to push empty commits or loop fake PRs. That violates GitHub's Acceptable Use Policies (*Spam and Inauthentic Activity*) and risks account flagging. Read **[docs/BADGES.md](docs/BADGES.md)** for full details.

---

## 🤝 Build Together (Add Your Own Theme or Plugin)

Want to share your own layout or widget with the community? Drop a folder into `themes/<id>/` or `plugins/<id>/` with its JSON manifest and open a PR—our CI automatically validates everything! See **[CONTRIBUTING.md](CONTRIBUTING.md)**.

<details>
<summary><b>❓ FAQ — Quick Answers</b></summary>

1. **How do I activate my GitHub Profile README?**  
   Create a public repository named `<your-username>/<your-username>` with a `README.md` at the root.
2. **Do I need to install any Python packages to use `setup.py`?**  
   No. `setup.py` uses only the Python 3.10+ standard library.
3. **How do I sync my YouTube channel or blog automatically?**  
   Enable `--plugins blog-rss,youtube-rss` when running `setup.py`, then pass your RSS URL or YouTube Channel ID (`UC...`).

</details>

---

<div align="center">

[MIT License](LICENSE) · Crafted by [cmduyeen](https://github.com/cmduyeen) · **Star ⭐ this repo if it helped you level up your profile!**

</div>
