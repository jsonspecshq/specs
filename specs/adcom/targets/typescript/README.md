# @jsonspecshq/adcom

Two installable packages generated from one published JSON Schema tree, at the lock `main`.

- `@jsonspecshq/adcom-types` — the static types. Depends on nothing.
- `@jsonspecshq/adcom` — the validation layer. Depends on the types and a 2020-12 engine, and carries the documents it grades against.

They are two representations of one schema and they carry different fact sets, so each is graded on its own. The better of the two is not this language's result.

## What the tree publishes

| Node | Count |
|---|--:|
| closed integer-coded vocabulary | 29 |
| integer primitive of titled codes | 1 |
| integer primitive | 8 |
| number primitive | 2 |
| object | 47 |
| open integer-coded vocabulary | 16 |
| string primitive | 3 |

## What the static types carry

33 of 106 nodes are carried exactly. Every other node is a declared widening, and the validation layer re-checks what the type does not carry:

| What the type does instead | Nodes |
|---|--:|
| `additionalProperties: false` reaches a TypeScript type as an excess-property check on an object literal, which no value parsed from bytes goes through, so the type admits an undefined member on a parsed value | 45 |
| the extension branch's values are a brand only a checked constructor builds, so the type refuses an unlisted value where a caller writes one and admits any value of the base type where one is parsed from bytes | 16 |
| a TypeScript type carries no range, no length and no pattern, so the type admits every value of its JSON type | 9 |
| TypeScript has one `number`, so the type does not state that a value is a whole number | 8 |
| the node states `anyOf` of `required`, which type rules § 2a puts in the constraint tier: no TypeScript type states a requirement that reads a sibling member, so every conditional member stays optional and the type admits a payload the condition refuses | 4 |
| the object states no `additionalProperties: false`, so it admits a member it does not name and the type says nothing about what such a member holds | 2 |
| the node states `if` / `then`, which type rules § 2a puts in the constraint tier: no TypeScript type states a requirement that reads a sibling member, so every conditional member stays optional and the type admits a payload the condition refuses | 1 |
| the node states `oneOf` of `required`, which type rules § 2a puts in the constraint tier: no TypeScript type states a requirement that reads a sibling member, so every conditional member stays optional and the type admits a payload the condition refuses | 1 |

## What the validation layer carries

Every node, exactly. The engine implements the whole 2020-12 validation vocabulary over the published bytes, so a constraint the schema states is decided by the bytes and not by code in this package.

## Two lines

```ts
import { validator } from "@jsonspecshq/adcom";

const v = validator();
v.check("Ad", JSON.parse(body));          // the verdict the published schema gives
const d = v.decode("Ad", JSON.parse(body));  // the same verdict, and the typed value
```

## Unofficial

No specification's owner publishes these files.
