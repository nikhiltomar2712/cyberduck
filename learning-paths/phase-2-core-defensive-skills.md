# Phase 2: Core Defensive Skills (6–8 weeks)

> **Ethics & Authorization**: Use this material only on systems you own or have explicit written permission to test. This repository is for defensive education, awareness, and authorized security work.

## Learning objectives
- Translate risk assessments into actionable controls.
- Review vulnerabilities and decide patching/mitigation priorities.
- Understand IAM fundamentals and how to reduce account-related risk.
- Perform initial incident response triage and basic forensic collection (defensive, non-invasive).
- Think like a SOC: how alerts become decisions.

## Key topics (expanded)
- **Threat modeling & risk assessment**
  - assets, trust boundaries
  - likelihood vs impact
  - ownership, mitigations, verification steps
- **Incident Response & Forensics basics**
  - triage workflow
  - timeline concepts (what happened when)
  - evidence handling (what to collect, how to document)
- **Vulnerability management & patching**
  - intake: what scanners/alerts mean
  - patch strategy (risk-based prioritization)
  - compensating controls
- **Identity & Access Management (IAM)**
  - MFA, least privilege, access reviews
  - session hardening concepts
- **Cryptography essentials**
  - hashing vs encryption
  - TLS basics for defenders
  - key management high-level
- **Security Operations (SOC) intro**
  - detections as hypotheses
  - log sources and signal quality

## Weekly goals & mini-projects

### Week 1: Threat modeling to mitigations
- Mini-project: create a simple threat model for a small app/service (data flow + trust boundaries).
- Deliverable: threat model + mitigation table.

### Week 2: Risk scoring + control selection
- Mini-project: write a risk assessment for 3–5 realistic risks and propose verification steps.
- Deliverable: risk assessment report.

### Week 3: Patch/mitigation decision-making
- Mini-project: “vuln intake” exercise using sample findings (provided in repo templates).
- Deliverable: prioritized mitigation plan.

### Week 4: IAM hardening review
- Mini-project: produce an account/access checklist (least privilege, MFA, access reviews).

### Week 5: IR triage runbook
- Mini-project: write an IR triage runbook using the incident timeline template.

### Week 6–8: Forensics basics (defensive collection)
- Mini-project: timeline-building lab using defensive log sources.
- Deliverable: a completed timeline + evidence list.

## Success checkpoints
- You can produce a threat model and a risk assessment with mitigations.
- You can triage an incident and outline next actions.
- You can explain core SOC workflow concepts.

