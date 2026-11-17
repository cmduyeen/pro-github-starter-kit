# 🚀 Pro GitHub Starter Kit

[![Validate Themes, Plugins & Tests](https://github.com/cmduyeen/pro-github-starter-kit/actions/workflows/validate-extensions.yml/badge.svg)](https://github.com/cmduyeen/pro-github-starter-kit/actions/workflows/validate-extensions.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An extensible, **Obsidian-inspired** starter kit to build a clean, high-impact **GitHub Profile README**—featuring modular **Themes**, plug-and-play **Automation Plugins** (Blog RSS, YouTube RSS, Spotify, WakaTime), curated community tools, a policy-safe **GitHub Achievement Badges** guide, and a **GitHub SEO/GEO checklist**.

## Table of Contents

- [Step 1: Create Your Special Profile Repo](#step-1-create-your-special-profile-repo)
- [Step 2: Pick a Theme & Plugins (CLI Builder)](#step-2-pick-a-theme--plugins-cli-builder)
- [Step 3: Curated Profile Tools & Automation](#step-3-curated-profile-tools--automation)
- [Step 4: Achievement Badges & SEO Checklist](#step-4-achievement-badges--seo-checklist)
- [Extend with Your Own Themes & Plugins](#extend-with-your-own-themes--plugins)
- [FAQ](#faq)

---

## Step 1: Create Your Special Profile Repo

1. Click **Use this template → Create a new repository** (or create a public repository named **exact match** `<your-username>/<your-username>`).
2. Make sure the repository is **Public** and initialized with a `README.md`—GitHub automatically displays it at the top of your profile page.

---

## Step 2: Pick a Theme & Plugins (CLI Builder)

Instead of editing raw Markdown placeholders by hand, use the zero-dependency `setup.py` CLI to compose a theme with any combination of plugins:

```bash
# List all available themes and plugins
python setup.py --list

# Example: Indie Maker theme + Blog RSS + Spotify + GitHub Stats
python setup.py --username <your-username> \
  --theme indie-maker \
  --plugins blog-rss,spotify-now-playing,github-stats \
  --var BLOG_RSS_URL=https://yourblog.com/index.xml \
  --var SPOTIFY_UID=your_spotify_uid
```

### Built-in Themes (`themes/`)

| Theme ID | Style | Best For |
| --- | --- | --- |
| `minimalist` | Clean text & links, zero widget clutter | Writers, engineers who prefer *less is more* |
| `indie-maker` | Featured products table + writing/video feeds | Solo builders & indie hackers |
| `developer-portfolio` | Bio bullets + tech stack icons + stats cards | Job seekers & full-stack developers |
| `terminal-hacker` | Neofetch-inspired terminal block layout | CLI, Linux & systems developers |
| `research-student` | Learning roadmap + public study notes | Students & self-learners building in public |

### Built-in Plugins (`plugins/`)

| Plugin ID | What It Adds | Includes GitHub Action? |
| --- | --- | --- |
| `blog-rss` | Auto-syncs latest articles from any RSS feed | ✅ `blog-rss-sync.yml` |
| `youtube-rss` | Auto-syncs latest videos from a YouTube channel | ✅ `youtube-rss-sync.yml` |
| `wakatime-stats` | Auto-updates weekly coding hours & languages | ✅ `wakatime-sync.yml` |
| `spotify-now-playing` | Embeds currently playing / recent Spotify track | — |
| `github-stats` | Embeds GitHub summary & streak SVG cards | — |
| `skill-icons` | Crisp SVG tech stack grid via `skillicons.dev` | — |
| `typing-svg` | Animated typing banner powered by `readme-typing-svg` | — |
| `activity-graph` | 31-day contribution line graph | — |
| `social-badges` | Crisp `shields.io` GitHub, X & Blog badges | — |

---

## Step 3: Curated Profile Tools & Automation

Looking for the best external generators, SVG widgets, and inspiration galleries? Browse the full contextual directory in **[docs/RESOURCES.md](docs/RESOURCES.md)** and setup instructions in **[docs/AUTOMATION.md](docs/AUTOMATION.md)**:

| Tool / Repo | What It Does | Link |
| --- | --- | --- |
| **readme.so** | Visual drag-and-drop README builder | [readme.so](https://readme.so/) |
| **GitHub Readme Stats** | Dynamic SVG stats & top languages cards | [anuraghazra/github-readme-stats](https://github.com/anuraghazra/github-readme-stats) |
| **Skill Icons** | Clean SVG tech stack icon grids | [tandpfun/skill-icons](https://github.com/tandpfun/skill-icons) |
| **Blog Post Workflow** | Syncs Blog/YouTube RSS feeds via GitHub Actions | [gautamkrishnar/blog-post-workflow](https://github.com/gautamkrishnar/blog-post-workflow) |
| **Awesome GitHub Profile README** | Gallery of standout profile layouts for inspiration | [abhisheknaiidu/awesome-github-profile-readme](https://github.com/abhisheknaiidu/awesome-github-profile-readme) |

---

## Step 4: Achievement Badges & SEO Checklist

### Active GitHub Achievement Badges

| Badge | Requirement | Tiers (Default / Bronze / Silver / Gold) |
| --- | --- | --- |
| 🦈 **Pull Shark** | Open pull requests that get merged | 2 / 16 / 128 / 1,024 PRs |
| 👯 **Pair Extraordinaire** | Co-author a commit in a merged PR (`Co-authored-by:`) | 1 / 10 / 24 / 48 PRs |
| 🚀 **Quickdraw** | Close an issue or PR within **5 minutes** of opening | 1 fast close (single tier) |
| 🤠 **YOLO** | Merge a pull request **without a code review** | 1 unreviewed merge (single tier) |
| 🧠 **Galaxy Brain** | Accepted answer in GitHub Discussions (Q&A) | 2 / 8 / 16 / 32 answers |
| ⭐ **Starstruck** | Own a public repo reaching star milestones | 16 / 128 / 512 / 4,096 stars |
| 💖 **Public Sponsor** | Sponsor a developer/org via GitHub Sponsors | 1 sponsorship (single tier) |

Read **[docs/BADGES.md](docs/BADGES.md)** for legitimate, policy-safe ways to earn each badge, Profile Highlights, and Retired Badges. Follow **[docs/SEO-CHECKLIST.md](docs/SEO-CHECKLIST.md)** to optimize your Bio, 6 Pinned Repos, Topics, and Social Preview.

---

## Extend with Your Own Themes & Plugins

Just like Obsidian, this kit is built for community extensions. Add a folder under `themes/<id>/` or `plugins/<id>/` with its JSON manifest and open a Pull Request—no changes to `setup.py` required. See **[CONTRIBUTING.md](CONTRIBUTING.md)** for the 5-minute spec.

---

## FAQ

**1. How do I create a GitHub Profile README?**  
Create a public repository whose name matches your GitHub username (`<username>/<username>`), add a `README.md` at the root, and commit it.

**2. Can I use automated scripts to farm Pull Shark or Contribution Graph squares?**  
No. Bulk empty commits or fake PR loops violate GitHub's Acceptable Use Policies (*Spam and Inauthentic Activity*) and can lead to ignored stats or account flagging. Always earn badges through real workflows.

**3. How do I sync my blog or YouTube channel automatically?**  
Use the `blog-rss` or `youtube-rss` plugin in `setup.py`. Both generate a scheduled GitHub Actions workflow powered by `gautamkrishnar/blog-post-workflow` that only commits when new content is published.

---

[MIT License](LICENSE) · Maintained by [cmduyeen](https://github.com/cmduyeen)
