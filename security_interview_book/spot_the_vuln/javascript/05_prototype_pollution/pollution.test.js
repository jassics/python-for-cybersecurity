'use strict';

const test = require('node:test');
const assert = require('node:assert');

const vulnerable = require('./pollution_vulnerable.js');
const fixed = require('./pollution_fixed.js');

// JSON.parse creates "__proto__" as an ordinary own property, which is
// exactly what a request body parser hands to the merge helper.
const HOSTILE_BODY = '{"__proto__": {"isAdmin": true}}';

function cleanUp() {
  delete Object.prototype.isAdmin;
}

test('vulnerable merge handles normal settings', () => {
  const result = vulnerable.merge({ theme: 'dark' }, { language: 'en' });
  assert.deepStrictEqual(result, { theme: 'dark', language: 'en' });
});

test('vulnerable merge pollutes Object.prototype', () => {
  try {
    vulnerable.merge({}, JSON.parse(HOSTILE_BODY));
    assert.strictEqual({}.isAdmin, true); // every object now claims to be admin
  } finally {
    cleanUp();
  }
});

test('fixed merge handles nested settings', () => {
  const result = fixed.merge({ ui: { theme: 'dark' } }, { ui: { language: 'en' } });
  assert.deepStrictEqual(result, { ui: { theme: 'dark', language: 'en' } });
});

test('fixed merge ignores __proto__', () => {
  try {
    fixed.merge({}, JSON.parse(HOSTILE_BODY));
    assert.strictEqual({}.isAdmin, undefined);
  } finally {
    cleanUp();
  }
});

test('fixed merge ignores constructor.prototype', () => {
  try {
    fixed.merge({}, JSON.parse('{"constructor": {"prototype": {"isAdmin": true}}}'));
    assert.strictEqual({}.isAdmin, undefined);
  } finally {
    cleanUp();
  }
});
