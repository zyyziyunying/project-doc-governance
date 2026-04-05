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


def execution_heavy_activation_signals(text: str) -> dict[str, bool]:
    lowered = text.lower()
    return {
        "local_docs_trigger": bool(
            re.search(r"already documents (?:it|the pattern) locally", lowered)
        ),
        "repeated_split_trigger": bool(
            re.search(r"repeated split|formalize locally in the same task", lowered)
        ),
    }


def authority_model_signals(text: str) -> dict[str, bool]:
    lowered = text.lower()

    docs_readme_explicit = bool(
        re.search(
            r"docs/readme\.md.{0,120}only when it explicitly defines",
            lowered,
            re.DOTALL,
        )
    )
    docs_readme_human_facing = bool(
        re.search(
            r"docs/readme\.md.{0,180}human-facing.{0,120}(placement|structure|category meaning)",
            lowered,
            re.DOTALL,
        )
    )
    agents_operational_pointers = bool(
        re.search(
            r"agents\.md.{0,180}agent-operational.{0,180}pointer",
            lowered,
            re.DOTALL,
        )
    )
    agents_not_sole = bool(
        re.search(
            r"agents\.md.{0,240}only source of truth.{0,120}human-facing taxonomy",
            lowered,
            re.DOTALL,
        )
    )

    docs_readme_rank = re.search(r"\n3\.\s+`?docs/readme\.md`?", lowered)
    agents_rank = re.search(r"\n4\.\s+`?agents\.md`?", lowered)
    agents_precedence_guard = bool(
        docs_readme_rank and agents_rank and docs_readme_rank.start() < agents_rank.start()
    )

    return {
        "docs_readme_restricted": docs_readme_explicit and docs_readme_human_facing,
        "agents_guarded_role": agents_operational_pointers
        and (agents_not_sole or agents_precedence_guard),
    }


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

    fallback_reference = skill_dir / "references" / "default-doc-taxonomy.md"
    if not fallback_reference.exists():
        issues.append(f"missing fallback reference: {fallback_reference}")
    else:
        reference_text = fallback_reference.read_text(encoding="utf-8")
        skill_signals = execution_heavy_activation_signals(skill_text)
        reference_signals = execution_heavy_activation_signals(reference_text)

        if not skill_signals["local_docs_trigger"]:
            issues.append(
                "SKILL.md is missing the local-docs execution-heavy activation trigger"
            )
        if not reference_signals["local_docs_trigger"]:
            issues.append(
                "references/default-doc-taxonomy.md is missing the local-docs execution-heavy activation trigger"
            )
        if (
            skill_signals["local_docs_trigger"]
            and reference_signals["local_docs_trigger"]
            and skill_signals["repeated_split_trigger"]
            != reference_signals["repeated_split_trigger"]
        ):
            issues.append(
                "execution-heavy activation drift: SKILL.md and references/default-doc-taxonomy.md disagree on repeated-split/formalize fallback"
            )
        elif (
            skill_signals["local_docs_trigger"]
            and reference_signals["local_docs_trigger"]
            and skill_signals["repeated_split_trigger"]
            == reference_signals["repeated_split_trigger"]
        ):
            notes.append(
                "execution-heavy activation rule is consistent between SKILL.md and references/default-doc-taxonomy.md"
            )

        skill_authority = authority_model_signals(skill_text)
        reference_authority = authority_model_signals(reference_text)

        if not skill_authority["docs_readme_restricted"]:
            issues.append(
                "SKILL.md is missing the restricted docs/README.md authority rule (explicit human-facing placement/structure semantics)"
            )
        if not reference_authority["docs_readme_restricted"]:
            issues.append(
                "references/default-doc-taxonomy.md is missing the restricted docs/README.md authority rule (explicit human-facing placement/structure semantics)"
            )
        if (
            skill_authority["docs_readme_restricted"]
            and reference_authority["docs_readme_restricted"]
        ):
            notes.append(
                "docs/README.md authority restriction is consistent between SKILL.md and references/default-doc-taxonomy.md"
            )

        if not skill_authority["agents_guarded_role"]:
            issues.append(
                "SKILL.md is missing the guarded AGENTS.md authority rule (agent-operational role with explicit limits)"
            )
        if not reference_authority["agents_guarded_role"]:
            issues.append(
                "references/default-doc-taxonomy.md is missing the guarded AGENTS.md authority rule (agent-operational role with explicit limits)"
            )
        if skill_authority["agents_guarded_role"] and reference_authority[
            "agents_guarded_role"
        ]:
            notes.append(
                "AGENTS.md authority role is consistent between SKILL.md and references/default-doc-taxonomy.md"
            )

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
