#!/usr/bin/env python3
"""Run lightweight skill checks without external dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


def parse_frontmatter(skill_md: Path) -> dict[str, str]:
    text = skill_md.read_text(encoding="utf-8")
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.DOTALL)
    if not match:
        raise ValueError("SKILL.md is missing YAML frontmatter")

    data: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if ":" not in line:
            raise ValueError(f"Invalid frontmatter line: {raw_line}")
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()

    return data


def collect_markdown_links(text: str) -> list[str]:
    links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
    results: list[str] = []
    for link in links:
        if "://" in link:
            continue
        path_only = link.split("#", 1)[0].strip()
        if not path_only:
            continue
        results.append(path_only)
    return results


def main() -> int:
    skill_dir = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd().resolve()
    issues: list[str] = []
    notes: list[str] = []

    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        print(f"FAIL: missing {skill_md}")
        return 1

    try:
        frontmatter = parse_frontmatter(skill_md)
    except ValueError as exc:
        print(f"FAIL: {exc}")
        return 1

    allowed_keys = {"name", "description"}
    actual_keys = set(frontmatter)
    missing_keys = allowed_keys - actual_keys
    extra_keys = actual_keys - allowed_keys
    if missing_keys:
        issues.append(f"frontmatter missing keys: {sorted(missing_keys)}")
    if extra_keys:
        issues.append(f"frontmatter has unexpected keys: {sorted(extra_keys)}")

    skill_name = frontmatter.get("name", "")
    if skill_name:
        if skill_dir.name != skill_name:
            issues.append(
                f"folder name '{skill_dir.name}' does not match skill name '{skill_name}'"
            )
        else:
            notes.append(f"frontmatter name matches folder: {skill_name}")
    else:
        issues.append("frontmatter name is empty")

    description = frontmatter.get("description", "").strip()
    if not description:
        issues.append("frontmatter description is empty")
    else:
        notes.append("frontmatter description is present")

    skill_text = skill_md.read_text(encoding="utf-8")
    for link in collect_markdown_links(skill_text):
        target = (skill_dir / link).resolve()
        if not target.exists():
            issues.append(f"missing referenced file from SKILL.md: {link}")
        else:
            notes.append(f"linked file exists: {link}")

    openai_yaml = skill_dir / "agents" / "openai.yaml"
    if openai_yaml.exists():
        yaml_text = openai_yaml.read_text(encoding="utf-8")
        if "default_prompt:" not in yaml_text:
            issues.append("agents/openai.yaml is missing interface.default_prompt")
        elif skill_name and f"${skill_name}" not in yaml_text:
            issues.append("agents/openai.yaml default_prompt does not mention the skill name")
        else:
            notes.append("agents/openai.yaml default_prompt mentions the skill name")
    else:
        notes.append("agents/openai.yaml not present; skipping UI metadata checks")

    if issues:
        for issue in issues:
            print(f"FAIL: {issue}")
        for note in notes:
            print(f"OK: {note}")
        return 1

    for note in notes:
        print(f"OK: {note}")
    print("OK: lightweight validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
