"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.scanContentSafety = scanContentSafety;
const contentRules = [
    {
        ruleId: 'malware_intent',
        severity: 'high',
        message: 'May indicate intent to create or deploy malware/phishing.',
        test: (s) => /\b(malware|ransomware|trojan|phish(ing)?|payload)\b/i.test(s),
    },
    {
        ruleId: 'exploit_instructions',
        severity: 'high',
        message: 'May include exploit-style or weaponized instructions.',
        test: (s) => /\b(exploit|shell\s*code|reverse\s*shell|sql\s*injection|xss)\b/i.test(s),
    },
    {
        ruleId: 'sensitive_data_requests',
        severity: 'medium',
        message: 'May request sensitive secrets like API keys or credentials.',
        test: (s) => /\b(api[_-]?key|secret|password|token|credential|private\s*key)\b/i.test(s),
    },
    {
        ruleId: 'prompt_injection_like',
        severity: 'medium',
        message: 'May contain prompt injection-like instruction override patterns.',
        test: (s) => /\b(ignore|disregard|override)\b/i.test(s) && /\b(system|developer|previous)\b/i.test(s),
    },
];
/**
 * Defensive-only heuristic classifier for text.
 * No external calls, no scanning, no exploitation.
 */
function scanContentSafety(text) {
    const findings = [];
    for (const r of contentRules) {
        if (r.test(text)) {
            findings.push({ ruleId: r.ruleId, severity: r.severity, message: r.message });
        }
    }
    return {
        isPotentiallyUnsafe: findings.some((f) => f.severity === 'high'),
        findings,
    };
}
