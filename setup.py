#!/usr/bin/env python3
"""Zero-dependency CLI to compose a GitHub Profile README from extensible themes and plugins."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT_DIR = Path(__file__).resolve().parent
THEMES_DIR = ROOT_DIR / "themes"
PLUGINS_DIR = ROOT_DIR / "plugins"
USERNAME_PATTERN = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?$")


def load_json(path: Path) -> dict[str, Any]:
    """Load and parse a JSON manifest file."""
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"Manifest must be a JSON object: {path}")
    return data


def discover_themes(themes_dir: Path = THEMES_DIR) -> dict[str, dict[str, Any]]:
    """Discover all themes in themes/<id>/theme.json."""
    themes: dict[str, dict[str, Any]] = {}
    if not themes_dir.exists():
        return themes
    for item in sorted(themes_dir.iterdir()):
        if not item.is_dir():
            continue
        manifest_path = item / "theme.json"
        if manifest_path.exists():
            data = load_json(manifest_path)
            themes[item.name] = {**data, "_dir": item}
    return themes


def discover_plugins(plugins_dir: Path = PLUGINS_DIR) -> dict[str, dict[str, Any]]:
    """Discover all plugins in plugins/<id>/plugin.json."""
    plugins: dict[str, dict[str, Any]] = {}
    if not plugins_dir.exists():
        return plugins
    for item in sorted(plugins_dir.iterdir()):
        if not item.is_dir():
            continue
        manifest_path = item / "plugin.json"
        if manifest_path.exists():
            data = load_json(manifest_path)
            plugins[item.name] = {**data, "_dir": item}
    return plugins


def validate_extensions(
    themes_dir: Path = THEMES_DIR,
    plugins_dir: Path = PLUGINS_DIR,
) -> list[str]:
    """Validate all theme and plugin manifests and required files. Returns list of errors."""
    errors: list[str] = []

    if not themes_dir.exists():
        errors.append(f"Missing themes directory: {themes_dir}")
    else:
        for item in sorted(themes_dir.iterdir()):
            if not item.is_dir():
                continue
            manifest = item / "theme.json"
            template = item / "README.template.md"
            if not manifest.exists():
                errors.append(f"Theme '{item.name}' is missing theme.json")
                continue
            try:
                data = load_json(manifest)
            except Exception as exc:
                errors.append(f"Theme '{item.name}' invalid JSON: {exc}")
                continue
            for key in ("id", "name", "description", "author"):
                if not data.get(key):
                    errors.append(f"Theme '{item.name}' theme.json missing '{key}'")
            if not template.exists():
                errors.append(f"Theme '{item.name}' is missing README.template.md")
            else:
                text = template.read_text(encoding="utf-8")
                if "{{PLUGINS}}" not in text:
                    errors.append(f"Theme '{item.name}' README.template.md must include '{{{{PLUGINS}}}}' slot")

    if not plugins_dir.exists():
        errors.append(f"Missing plugins directory: {plugins_dir}")
    else:
        for item in sorted(plugins_dir.iterdir()):
            if not item.is_dir():
                continue
            manifest = item / "plugin.json"
            snippet = item / "snippet.md"
            if not manifest.exists():
                errors.append(f"Plugin '{item.name}' is missing plugin.json")
                continue
            try:
                data = load_json(manifest)
            except Exception as exc:
                errors.append(f"Plugin '{item.name}' invalid JSON: {exc}")
                continue
            for key in ("id", "name", "description", "author"):
                if not data.get(key):
                    errors.append(f"Plugin '{item.name}' plugin.json missing '{key}'")
            if not snippet.exists():
                errors.append(f"Plugin '{item.name}' is missing snippet.md")

    return errors


def parse_vars(raw_vars: list[str]) -> dict[str, str]:
    """Parse KEY=VALUE pairs from --var arguments."""
    parsed: dict[str, str] = {}
    for entry in raw_vars:
        if "=" not in entry:
            raise ValueError(f"Invalid --var '{entry}'. Expected KEY=VALUE format.")
        key, value = entry.split("=", 1)
        key = key.strip()
        if not key:
            raise ValueError(f"Empty key in --var '{entry}'.")
        parsed[key] = value.strip()
    return parsed


def render_placeholders(text: str, variables: dict[str, str]) -> str:
    """Replace {{KEY}} placeholders using provided variables."""
    rendered = text
    for key, value in variables.items():
        rendered = rendered.replace(f"{{{{{key}}}}}", value)
    return rendered


def compose_profile(
    *,
    username: str,
    theme_id: str,
    plugin_ids: list[str],
    variables: dict[str, str],
    themes_dir: Path = THEMES_DIR,
    plugins_dir: Path = PLUGINS_DIR,
) -> tuple[str, list[tuple[str, str]]]:
    """Render README.md content and collect (workflow_filename, workflow_content) pairs."""
    if not USERNAME_PATTERN.match(username):
        raise ValueError(f"Invalid GitHub username '{username}'.")

    themes = discover_themes(themes_dir)
    if theme_id not in themes:
        available = ", ".join(themes.keys()) or "(none)"
        raise ValueError(f"Unknown theme '{theme_id}'. Available: {available}")

    plugins = discover_plugins(plugins_dir)
    for pid in plugin_ids:
        if pid not in plugins:
            available = ", ".join(plugins.keys()) or "(none)"
            raise ValueError(f"Unknown plugin '{pid}'. Available: {available}")

    merged_vars: dict[str, str] = {"USERNAME": username}
    for pid in plugin_ids:
        defaults = plugins[pid].get("defaults", {})
        if isinstance(defaults, dict):
            for k, v in defaults.items():
                merged_vars.setdefault(str(k), str(v))
    merged_vars.update(variables)

    plugin_blocks: list[str] = []
    workflows: list[tuple[str, str]] = []

    for pid in plugin_ids:
        pdir: Path = plugins[pid]["_dir"]
        snippet = (pdir / "snippet.md").read_text(encoding="utf-8").strip()
        plugin_blocks.append(render_placeholders(snippet, merged_vars))

        wf_path = pdir / "workflow.yml"
        if wf_path.exists():
            wf_name = plugins[pid].get("workflow_file", f"{pid}.yml")
            wf_content = render_placeholders(wf_path.read_text(encoding="utf-8"), merged_vars)
            workflows.append((str(wf_name), wf_content))

    plugins_section = "\n\n".join(plugin_blocks)
    theme_dir: Path = themes[theme_id]["_dir"]
    template_text = (theme_dir / "README.template.md").read_text(encoding="utf-8")

    output = template_text.replace("{{PLUGINS}}", plugins_section)
    output = render_placeholders(output, merged_vars)
    output = re.sub(r"\n{3,}", "\n\n", output).strip() + "\n"
    return output, workflows


def list_catalog(themes_dir: Path = THEMES_DIR, plugins_dir: Path = PLUGINS_DIR) -> None:
    """Print available themes and plugins."""
    themes = discover_themes(themes_dir)
    plugins = discover_plugins(plugins_dir)

    print("Available Themes:")
    for tid, data in themes.items():
        print(f"  - {tid}: {data.get('name')} — {data.get('description')} (by {data.get('author')})")

    print("\nAvailable Plugins:")
    for pid, data in plugins.items():
        wf = " [includes workflow]" if (data["_dir"] / "workflow.yml").exists() else ""
        print(f"  - {pid}: {data.get('name')}{wf} — {data.get('description')}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Compose a GitHub Profile README and workflows from modular themes and plugins."
    )
    parser.add_argument("--list", action="store_true", help="List available themes and plugins.")
    parser.add_argument("--validate", action="store_true", help="Validate all theme and plugin manifests.")
    parser.add_argument("--username", help="Your GitHub username.")
    parser.add_argument("--theme", default="minimalist", help="Theme ID to use (default: minimalist).")
    parser.add_argument(
        "--plugins",
        default="",
        help="Comma-separated plugin IDs (e.g. blog-rss,github-stats).",
    )
    parser.add_argument(
        "--var",
        action="append",
        default=[],
        help="Custom placeholder variable in KEY=VALUE format (repeatable).",
    )
    parser.add_argument(
        "--output-dir",
        default=".",
        help="Target directory to write README.md and .github/workflows/ (default: current directory).",
    )
    parser.add_argument("--dry-run", action="store_true", help="Preview generated files without writing.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.validate:
        errors = validate_extensions()
        if errors:
            for err in errors:
                print(f"Error: {err}", file=sys.stderr)
            return 1
        print("All theme and plugin manifests are valid.")
        return 0

    if args.list:
        list_catalog()
        return 0

    if not args.username:
        parser.error("--username is required unless --list or --validate is specified.")

    try:
        plugin_ids = [p.strip() for p in args.plugins.split(",") if p.strip()]
        variables = parse_vars(args.var)
        readme_text, workflows = compose_profile(
            username=args.username,
            theme_id=args.theme,
            plugin_ids=plugin_ids,
            variables=variables,
        )

        out_root = Path(args.output_dir).resolve()
        readme_path = out_root / "README.md"
        wf_dir = out_root / ".github" / "workflows"

        if args.dry_run:
            print(f"[dry-run] Would write {readme_path} ({len(readme_text)} bytes)")
            for wf_name, _ in workflows:
                print(f"[dry-run] Would write {wf_dir / wf_name}")
            return 0

        out_root.mkdir(parents=True, exist_ok=True)
        readme_path.write_text(readme_text, encoding="utf-8")
        print(f"Generated {readme_path}")

        if workflows:
            wf_dir.mkdir(parents=True, exist_ok=True)
            for wf_name, wf_content in workflows:
                target = wf_dir / wf_name
                target.write_text(wf_content, encoding="utf-8")
                print(f"Generated {target}")

        return 0
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
