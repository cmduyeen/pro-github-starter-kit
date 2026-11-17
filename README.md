<div align="center">

# 🚀 Pro GitHub Starter Kit

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=3B82F6&center=true&vCenter=true&width=640&lines=Build+a+Standout+GitHub+Profile+in+Minutes.;Modular+Themes+%2B+Plug-and-Play+Automation.;Curated+Tools%2C+Legit+Badges+%26+SEO+Ready.)](https://github.com/cmduyeen/pro-github-starter-kit)

[![Validate Themes, Plugins & Tests](https://github.com/cmduyeen/pro-github-starter-kit/actions/workflows/validate-extensions.yml/badge.svg)](https://github.com/cmduyeen/pro-github-starter-kit/actions/workflows/validate-extensions.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg?style=flat-square)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)
[![Template Repo](https://img.shields.io/badge/Use%20This%20Template-Click%20Here-2ea44f?style=flat-square&logo=github)](https://github.com/cmduyeen/pro-github-starter-kit/generate)

**An Obsidian-inspired, extensible starter kit for crafting a clean, automated, and high-converting GitHub Profile.**

[Quick Start](#-quick-start-60-seconds) · [Live Previews](#-see-what-you-can-build) · [Themes & Plugins](#-modular-themes--plugins) · [Badges](#-legit-github-achievements) · [Resources](docs/RESOURCES.md)

</div>

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
| [<img src="assets/previews/catppuccin.svg" width="220" alt="Catppuccin Mocha Preview"/>](themes/catppuccin/PREVIEW.md) | **`catppuccin`**<br/>Catppuccin Mocha *(by @cmduyeen)* | Soothing pastel-dark palette inspired by Catppuccin (catppuccin/catppuccin). | [Live Preview](themes/catppuccin/PREVIEW.md) · [Template](themes/catppuccin/README.template.md) |
| [<img src="assets/previews/developer-portfolio.svg" width="220" alt="Developer Portfolio Preview"/>](themes/developer-portfolio/PREVIEW.md) | **`developer-portfolio`**<br/>Developer Portfolio *(by @cmduyeen)* | Full developer showcase ready for tech stack icons, stats cards, and activity widgets. | [Live Preview](themes/developer-portfolio/PREVIEW.md) · [Template](themes/developer-portfolio/README.template.md) |
| [<img src="assets/previews/dracula.svg" width="220" alt="Dracula Palette Preview"/>](themes/dracula/PREVIEW.md) | **`dracula`**<br/>Dracula Palette *(by @cmduyeen)* | Dark purple & neon palette inspired by Dracula Theme (dracula/dracula-theme). | [Live Preview](themes/dracula/PREVIEW.md) · [Template](themes/dracula/README.template.md) |
| [<img src="assets/previews/indie-maker.svg" width="220" alt="Indie Maker Preview"/>](themes/indie-maker/PREVIEW.md) | **`indie-maker`**<br/>Indie Maker *(by @cmduyeen)* | Product-focused layout highlighting shipped projects, writing, and updates. | [Live Preview](themes/indie-maker/PREVIEW.md) · [Template](themes/indie-maker/README.template.md) |
| [<img src="assets/previews/minimalist.svg" width="220" alt="Minimalist Preview"/>](themes/minimalist/PREVIEW.md) | **`minimalist`**<br/>Minimalist *(by @cmduyeen)* | Clean text-first profile with zero visual clutter. | [Live Preview](themes/minimalist/PREVIEW.md) · [Template](themes/minimalist/README.template.md) |
| [<img src="assets/previews/pinkie.svg" width="220" alt="Pinkie Pastel Preview"/>](themes/pinkie/PREVIEW.md) | **`pinkie`**<br/>Pinkie Pastel *(by @cmduyeen)* | Soft pastel-pink aesthetic from Pinkie Theme (cmduyeen/pinkie-theme). | [Live Preview](themes/pinkie/PREVIEW.md) · [Template](themes/pinkie/README.template.md) |
| [<img src="assets/previews/research-student.svg" width="220" alt="Student & Self-Learner Preview"/>](themes/research-student/PREVIEW.md) | **`research-student`**<br/>Student & Self-Learner *(by @cmduyeen)* | Structured layout highlighting learning roadmap, notes, and starter projects. | [Live Preview](themes/research-student/PREVIEW.md) · [Template](themes/research-student/README.template.md) |
| [<img src="assets/previews/serein.svg" width="220" alt="Serein Warm Minimal Preview"/>](themes/serein/PREVIEW.md) | **`serein`**<br/>Serein Warm Minimal *(by @cmduyeen)* | Warm, low-distraction palette from Serein Theme (cmduyeen/serein-theme). | [Live Preview](themes/serein/PREVIEW.md) · [Template](themes/serein/README.template.md) |
| [<img src="assets/previews/terminal-hacker.svg" width="220" alt="Terminal / CLI Preview"/>](themes/terminal-hacker/PREVIEW.md) | **`terminal-hacker`**<br/>Terminal / CLI *(by @cmduyeen)* | Neofetch-inspired terminal block layout for CLI and systems developers. | [Live Preview](themes/terminal-hacker/PREVIEW.md) · [Template](themes/terminal-hacker/README.template.md) |
<!-- THEMES-TABLE:END -->

### 2. Snap in Plugins (`plugins/`)

<!-- PLUGINS-TABLE:START -->
| Plugin ID | What It Adds | Automation Included? | Preview |
| --- | --- | --- | --- |
| `activity-graph` | Renders a 31-day contribution line graph using github-readme-activity-graph. | — | [Live Preview](plugins/activity-graph/PREVIEW.md) |
| `blog-rss` | Automatically syncs your latest blog posts via RSS using GitHub Actions. | ✅ `blog-rss-sync.yml` | [Live Preview](plugins/blog-rss/PREVIEW.md) |
| `github-stats` | Embeds dynamic GitHub summary stats, top languages, and streak cards. | — | [Live Preview](plugins/github-stats/PREVIEW.md) |
| `skill-icons` | Displays your tech stack cleanly using skillicons.dev. | — | [Live Preview](plugins/skill-icons/PREVIEW.md) |
| `social-badges` | Adds crisp shields.io social and portfolio badges. | — | [Live Preview](plugins/social-badges/PREVIEW.md) |
| `spotify-now-playing` | Displays your currently playing or recently played Spotify track. | — | [Live Preview](plugins/spotify-now-playing/PREVIEW.md) |
| `typing-svg` | Adds an animated typing header powered by readme-typing-svg. | — | [Live Preview](plugins/typing-svg/PREVIEW.md) |
| `wakatime-stats` | Automatically updates your weekly coding time and language breakdown via WakaTime. | ✅ `wakatime-sync.yml` | [Live Preview](plugins/wakatime-stats/PREVIEW.md) |
| `youtube-rss` | Automatically lists your latest YouTube videos via channel RSS feed. | ✅ `youtube-rss-sync.yml` | [Live Preview](plugins/youtube-rss/PREVIEW.md) |
<!-- PLUGINS-TABLE:END -->

> [!NOTE]
> All GitHub Actions workflows run **once per day** and only commit when new content appears—keeping your contribution graph authentic and clean. See **[docs/AUTOMATION.md](docs/AUTOMATION.md)** for setup details.

---

## 🛠 Curated Resources & SEO

We vetted the top open-source profile tools so you don't have to hunt across 20 tabs:

| Category | Top Picks | Guide |
| --- | --- | --- |
| **Visual Builders** | `readme.so`, `github-profile-readme-generator` | [docs/RESOURCES.md](docs/RESOURCES.md) |
| **Stats & Graphs** | `github-readme-stats`, `streak-stats`, `activity-graph`, `lowlighter/metrics` | [docs/RESOURCES.md](docs/RESOURCES.md) |
| **Automation** | `blog-post-workflow`, `waka-readme-stats`, `spotify-github-profile` | [docs/AUTOMATION.md](docs/AUTOMATION.md) |
| **Profile SEO & GEO** | 1-line Bio, 6 Gateway Pins, 20 Topics, `1280×640` Cover, `llms.txt` | [docs/SEO-CHECKLIST.md](docs/SEO-CHECKLIST.md) |
| **Inspiration** | `awesome-github-profile-readme`, `creative-profile-readme` | [docs/RESOURCES.md](docs/RESOURCES.md) |

---

## 🏆 Legit GitHub Achievements

| Badge | Requirement | Tiers (Default / Bronze / Silver / Gold) |
| --- | --- | --- |
| 🦈 **Pull Shark** | Open pull requests that get merged | 2 / 16 / 128 / 1,024 PRs |
| 👯 **Pair Extraordinaire** | Co-author a commit in a merged PR (`Co-authored-by:`) | 1 / 10 / 24 / 48 PRs |
| 🚀 **Quickdraw** | Close an issue or PR within **5 minutes** of opening | 1 fast close (single tier) |
| 🤠 **YOLO** | Merge a pull request **without a code review** | 1 unreviewed merge (single tier) |
| 🧠 **Galaxy Brain** | Accepted answer in GitHub Discussions (Q&A) | 2 / 8 / 16 / 32 answers |
| ⭐ **Starstruck** | Own a public repo reaching star milestones | 16 / 128 / 512 / 4,096 stars |
| 💖 **Public Sponsor** | Sponsor a developer/org via GitHub Sponsors | 1 sponsorship (single tier) |

> [!WARNING]
> Never use bots to push empty commits or loop fake PRs. That violates GitHub's Acceptable Use Policies (*Spam and Inauthentic Activity*) and risks account flagging. Read **[docs/BADGES.md](docs/BADGES.md)** for fast, 100% legitimate ways to earn every badge.

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
