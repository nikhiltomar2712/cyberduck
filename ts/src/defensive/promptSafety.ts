export type SafetyFinding = {
  ruleId: string;
  severity: 'low' | 'medium' | 'high';
  message: string;
};

export type SafetyScanResult = {
  isPotentiallyUnsafe: boolean;
  findings: SafetyFinding[];
};

const rules: Array<{
  ruleId: string;
  severity: SafetyFinding['severity'];
  message: string;
  test: (input: string) => boolean;
}> = [
  {
    ruleId: 'prompt_injection_like',
    severity: 'high',
    message: 'Contains patterns that resemble prompt-injection or instruction override attempts.',
    test: (s) =>
      /\b(ignore|disregard|override)\s+(all\s+)?(previous|system|developer)\b/i.test(s) ||
      /\b(as an?|act as)\s+(system|developer)\b/i.test(s),
  },
  {
    ruleId: 'secret_exfil_like',
    severity: 'high',
    message: 'Looks like it may request secrets, credentials, or sensitive data.',
    test: (s) =>
      /\b(api[_-]?key|secret|password|token|credential|private key)\b/i.test(s) ||
      /\b(exfiltrate|exfiltration|leak)\b/i.test(s),
  },
  {
    ruleId: 'unsafe_instructions',
    severity: 'medium',
    message: 'May contain unsafe instructions (e.g., malware, hacking, exploitation).',
    test: (s) =>
      /\b(malware|ransomware|phish(ing)?|exploit|hacking|ddos|sql\s+injection|xss)\b/i.test(s),
  },
  {
    ruleId: 'data_motive',
    severity: 'low',
    message: 'Requests or encourages unnecessary sensitive data handling.',
    test: (s) => /\b(mass\s+collect|bulk\s+collect|harvest|scrape)\b/i.test(s),
  },
];

/**
 * Rule-based safety scanner.
 * Defensive: identifies risk heuristically; does not execute or call external systems.
 */
export function scanPromptSafety(input: string): SafetyScanResult {
  const findings: SafetyFinding[] = [];
  for (const r of rules) {
    if (r.test(input)) {
      findings.push({ ruleId: r.ruleId, severity: r.severity, message: r.message });
    }
  }

  const isPotentiallyUnsafe = findings.some((f) => f.severity === 'high');
  return { isPotentiallyUnsafe, findings };
}

