# SV-05: Settings merge (JavaScript)

**Book chapters:** 2 (OWASP web), 4 (secure code review) · **CWE-1321:** Improperly controlled modification of object prototype attributes · **Level:** mid to senior

## Scenario

An Express app lets users `PATCH` their settings with a JSON body. The body is merged into the user's settings object by the helper in `pollution_vulnerable.js`. Which request body breaks the whole process?

## Hints

<details>
<summary>Hint 1</summary>

What does `target["__proto__"]` return in JavaScript? Is it a normal property?
</details>

<details>
<summary>Hint 2</summary>

`JSON.parse('{"__proto__": {...}}')` makes `__proto__` an *own* property. Which loop sees it?
</details>

<details>
<summary>Hint 3</summary>

After the pollution, some unrelated code checks `if (user.isAdmin)` on an object that never set `isAdmin`. What happens?
</details>

## What the interviewer listens for

- You explain the mechanism: the merge walks into `Object.prototype`, so every object inherits the attacker's property.
- You give impact beyond "weird bugs": authorization bypass, denial of service, and in some frameworks remote code execution through "gadgets" in template engines or child-process options.
- You list fixes: skip `__proto__`, `constructor` and `prototype`; use `Object.hasOwn`; or build target objects with `Object.create(null)` or `Map`; or freeze the prototype (`Object.freeze(Object.prototype)`) as defence in depth.
- You say the best fix is **validating the body against a schema** and accepting only known keys.
- Senior bonus: you can describe where else it appears: `lodash.merge` and `defaultsDeep` in old versions, query-string parsers, `Object.assign` deep-copy helpers.

## The fix, explained

`pollution_fixed.js` skips the three dangerous keys, only recurses into plain objects, and uses `Object.hasOwn` so inherited properties are never treated as existing settings. A schema check in front of it would be stronger.

## The same bug elsewhere

| Language | Look for |
| --- | --- |
| JavaScript / TypeScript | Recursive merge, clone, `set(path, value)` helpers, dotted-path setters |
| Python | The close cousin is mass assignment, for example `setattr` on a model from request data, or class pollution through `__class__` paths in dynamic setters |
| Ruby | Mass assignment without strong parameters |
| Java | Jackson or Spring binding straight into entities, so an attacker sets `role` or `admin` |
| Go | Decoding JSON into a struct that includes privileged fields without `json:"-"` |

## Desi analogy

Writing on the printed template of the society notice board instead of on one flat's notice. Every flat's notice now carries your line.

## Run it

```bash
cd security_interview_book
node --test spot_the_vuln/javascript/05_prototype_pollution/*.test.js
```

The test removes the polluted property after each run.
