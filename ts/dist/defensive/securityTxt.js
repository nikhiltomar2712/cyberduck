"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.parseSecurityTxt = parseSecurityTxt;
exports.hasContact = hasContact;
/**
 * Parse a security.txt-like file.
 * Defensive purpose: extraction only (no network calls, no scanning).
 */
function parseSecurityTxt(text) {
    const values = {};
    for (const rawLine of text.split(/\r?\n/)) {
        const line = rawLine.trim();
        if (!line || line.startsWith('#') || !line.includes(':'))
            continue;
        const [k, ...rest] = line.split(':');
        const key = k.trim().toLowerCase();
        const value = rest.join(':').trim();
        if (!key)
            continue;
        if (!values[key])
            values[key] = [];
        values[key].push(value);
    }
    return values;
}
function hasContact(text) {
    const parsed = parseSecurityTxt(text);
    return Array.isArray(parsed['contact']) && parsed['contact'].length > 0;
}
