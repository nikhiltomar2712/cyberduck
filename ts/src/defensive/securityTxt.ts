export type SecurityTxtValues = Record<string, string[]>;

/**
 * Parse a security.txt-like file.
 * Defensive purpose: extraction only (no network calls, no scanning).
 */
export function parseSecurityTxt(text: string): SecurityTxtValues {
  const values: SecurityTxtValues = {};

  for (const rawLine of text.split(/\r?\n/)) {
    const line = rawLine.trim();
    if (!line || line.startsWith('#') || !line.includes(':')) continue;
    const [k, ...rest] = line.split(':');
    const key = k.trim().toLowerCase();
    const value = rest.join(':').trim();
    if (!key) continue;
    if (!values[key]) values[key] = [];
    values[key].push(value);
  }

  return values;
}

export function hasContact(text: string): boolean {
  const parsed = parseSecurityTxt(text);
  return Array.isArray(parsed['contact']) && parsed['contact'].length > 0;
}

