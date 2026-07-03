# Phase 0: Mindset & Setup (1–2 weeks)

> **Ethics & Authorization**: Use this material only on systems you own or have explicit written permission to test. This repository is for defensive education, awareness, and authorized security work. Do not attack, scan, exploit, or attempt unauthorized access against third-party systems.

## Learning objectives
- Understand ethical boundaries, consent, and safe lab practices.
- Create a “defensive practice” workflow for notes, evidence, and reporting.
- Set up your local environment using virtualization (VirtualBox) and snapshotting.

## Key topics
- Permission, scope, and safe boundaries
- Lab hygiene: isolation, backups, snapshots
- Documentation: evidence, assumptions, mitigations
- Security basics: CIA triad, assets, threat/vulnerability/risk (high-level refresher)

## Recommended resources (add free + paid options)
Free:
- OWASP Web Security Testing Guide (read defensively)
- MITRE ATT&CK (read as a defender)
- NIST risk concepts (overview)

Paid (optional):
- LinkedIn Learning / Pluralsight security beginner tracks
- Community-based blue-team courses

## Week-by-week plan

### Week 1: Safe lab foundation
**Weekly goals**
- Install VirtualBox (or equivalent)
- Create a dedicated “security lab” VM for analysis/observation
- Configure host-only or internal networking to avoid exposing services

**Mini-project**
- Write a `LAB_README.md` that includes:
  - VM names and purpose
  - networking mode
  - snapshot schedule
  - data handling rules (what you collect and where)

**Success checkpoint**
- You can start/stop the VM and restore from a snapshot without breaking your lab workflow.

### Week 2: First defensive write-up
**Weekly goals**
- Use a report template
- Practice “findings → impact → recommendation” writing

**Mini-project**
- Choose one defensive checklist item (e.g., disabling unused accounts, reviewing file permissions).
- Complete one checklist and write a 1-page report.

**Success checkpoint**
- Your report includes: evidence, observed risk, mitigation, and what you would verify next.

## Deliverables
- `LAB_README.md`
- 1 short defensive report using `templates/reports/security-review-report.md`

