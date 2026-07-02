"""Markdown report builders."""

from __future__ import annotations

from .models import Finding


def finding_to_markdown(finding: Finding) -> str:
    lines = [f"### {finding.title}", f"- Severity: {finding.severity}"]
    if finding.detail:
        lines.append(f"- Detail: {finding.detail}")
    if finding.recommendation:
        lines.append(f"- Recommendation: {finding.recommendation}")
    return "\n".join(lines)


def markdown_report(title: str, findings: list[Finding]) -> str:
    body = "\n\n".join(finding_to_markdown(finding) for finding in findings) or "No findings recorded."
    return f"# {title}\n\n{body}\n"
