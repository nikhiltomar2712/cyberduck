"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const testHarness_1 = require("../testHarness");
try {
    (0, testHarness_1.runAllTests)();
    // eslint-disable-next-line no-console
    console.log('All TS defensive tests passed.');
    process.exit(0);
}
catch (err) {
    // eslint-disable-next-line no-console
    console.error('TS tests failed:', err);
    process.exit(1);
}
