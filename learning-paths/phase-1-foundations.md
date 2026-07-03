# Phase 1: Foundations (4–6 weeks)

> **Ethics & Authorization**: Use this material only on systems you own or have explicit written permission to test.

## Learning objectives
- Explain CIA triad and how security controls map to risk.
- Identify common threat actors and motivations.
- Perform core Linux/CLI hygiene for defender work.
- Understand networking layers and how defenders think about traffic.

## Key topics (expanded)
- CIA triad (Confidentiality, Integrity, Availability)
- Threat actors, motivations, and capabilities (defender-level)
- Threats, vulnerabilities, controls, and risk
- Security posture fundamentals and least privilege

### Linux & Command Line mastery for security
- Users/groups, ownership, permissions
- Sudo hygiene and least privilege
- Readable logging & journald basics
- File permission review and safe command patterns

### Networking & traffic analysis (intro)
- OSI/TCP/IP layers
- Ports, protocols, and service exposure concepts
- DNS fundamentals and resolver behavior
- Defensive traffic monitoring mindset

## Recommended resources (add free + paid options)
Free:
- Linux Journey / CLI references (defensive reading)
- OWASP Top 10 (for later deep dive)
- Packet analysis overviews (intro level)

Paid:
- Security fundamentals courses (beginner track)

## Weekly goals & mini-projects

### Week 1: Security vocabulary + documentation
- Deliverable: 1-page “security vocabulary” glossary in your notes.

### Week 2: Linux defender CLI hygiene
- Mini-project: build a command cheat sheet you can safely run read-only.
- Deliverable: permission review notes for a sample directory.

### Week 3: Logs and observability basics
- Mini-project: identify which logs matter (auth, system, network-facing services) and write how you’d investigate.

### Week 4: Networking layers + port/service mapping
- Mini-project: create a “what should be exposed” table for a hypothetical service.

### Week 5 (optional if 5–6 week plan): DNS and traffic signals
- Mini-project: document how DNS queries/HTTP requests differ at a high level and what anomalies to watch.

## Success checkpoints
- You can explain CIA triad → risks → controls.
- You can complete a basic system hardening checklist.
- You can describe common network layers and map a service to expected ports.

