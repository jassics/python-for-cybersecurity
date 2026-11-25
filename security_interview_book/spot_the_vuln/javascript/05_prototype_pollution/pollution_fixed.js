'use strict';

// SV-05: settings merge helper (one reasonable fix).
//
// Dangerous keys are skipped, only own properties are touched, and nested
// objects are created only when the target does not already hold one.

const FORBIDDEN_KEYS = new Set(['__proto__', 'constructor', 'prototype']);

function isPlainObject(value) {
  return value !== null && typeof value === 'object' && !Array.isArray(value);
}

function merge(target, source) {
  for (const key of Object.keys(source)) {
    if (FORBIDDEN_KEYS.has(key)) {
      continue;
    }
    const value = source[key];
    if (isPlainObject(value)) {
      if (!Object.hasOwn(target, key) || !isPlainObject(target[key])) {
        target[key] = {};
      }
      merge(target[key], value);
    } else {
      target[key] = value;
    }
  }
  return target;
}

module.exports = { merge };
