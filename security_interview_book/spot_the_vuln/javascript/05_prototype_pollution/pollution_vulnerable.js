'use strict';

// SV-05: settings merge helper (vulnerable).
//
// An Express app lets users PATCH their profile settings with a JSON body.
// The body is merged into the user's settings object with this helper.
// Review merge().

function merge(target, source) {
  for (const key in source) {
    if (typeof source[key] === 'object' && source[key] !== null) {
      if (!target[key]) {
        target[key] = {};
      }
      merge(target[key], source[key]);
    } else {
      target[key] = source[key];
    }
  }
  return target;
}

module.exports = { merge };
