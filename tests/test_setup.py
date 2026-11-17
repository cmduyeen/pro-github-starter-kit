import tempfile
import unittest
from pathlib import Path

import setup


class TestStarterKitSetup(unittest.TestCase):
    def test_validate_extensions_passes(self) -> None:
        errors = setup.validate_extensions()
        self.assertEqual(errors, [])

    def test_discover_themes_and_plugins(self) -> None:
        themes = setup.discover_themes()
        plugins = setup.discover_plugins()
        for tid in ("minimalist", "indie-maker", "developer-portfolio", "terminal-hacker", "research-student"):
            self.assertIn(tid, themes)
        for pid in (
            "blog-rss",
            "youtube-rss",
            "spotify-now-playing",
            "wakatime-stats",
            "github-stats",
            "skill-icons",
            "typing-svg",
            "activity-graph",
            "social-badges",
        ):
            self.assertIn(pid, plugins)

    def test_compose_profile_replaces_placeholders_and_collects_workflows(self) -> None:
        readme, workflows = setup.compose_profile(
            username="octocat",
            theme_id="indie-maker",
            plugin_ids=["blog-rss", "youtube-rss", "github-stats"],
            variables={
                "BLOG_RSS_URL": "https://octocat.dev/rss.xml",
                "YOUTUBE_CHANNEL_ID": "UC123456",
            },
        )
        self.assertIn("# Hey, I'm octocat", readme)
        self.assertIn("octocat's GitHub stats", readme)
        self.assertNotIn("{{PLUGINS}}", readme)
        self.assertNotIn("{{USERNAME}}", readme)

        wf_dict = dict(workflows)
        self.assertIn("blog-rss-sync.yml", wf_dict)
        self.assertIn("https://octocat.dev/rss.xml", wf_dict["blog-rss-sync.yml"])
        self.assertIn("youtube-rss-sync.yml", wf_dict)
        self.assertIn("UC123456", wf_dict["youtube-rss-sync.yml"])

    def test_cli_writes_output_directory(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            rc = setup.main(
                [
                    "--username",
                    "octocat",
                    "--theme",
                    "minimalist",
                    "--plugins",
                    "blog-rss,skill-icons",
                    "--output-dir",
                    tmp,
                ]
            )
            self.assertEqual(rc, 0)
            out = Path(tmp)
            self.assertTrue((out / "README.md").exists())
            self.assertTrue((out / ".github" / "workflows" / "blog-rss-sync.yml").exists())

    def test_invalid_username_fails(self) -> None:
        with self.assertRaises(ValueError):
            setup.compose_profile(
                username="bad username!",
                theme_id="minimalist",
                plugin_ids=[],
                variables={},
            )


if __name__ == "__main__":
    unittest.main()
