# jsonspecs

A deterministic pipeline that turns specification texts into machine-readable
artifacts, with every generated value accounted for. Unofficial; each
specification's text stays its owner's, and where this repository and a text
differ, the text wins.

Four things, in order:

1. the specification's text at a pinned commit, extracted deterministically;
2. reviewed overrides — decisions, names, numbers — each with its provenance;
3. JSON Schema 2020-12, published at its `$id`;
4. from the schemas: protocol buffers, SDKs, validators, and a site.

A generated value is either what a rule computed from quoted, digested lines
of the text, or what one override record set. Nothing else. Each target keeps
a committed lock of the names and numbers it has published, so a reworded row
keeps its value and reports the change rather than renaming silently.

The repository is built in **vertical slices**: one specification end to end
per slice, starting with AdCOM's code lists. The plans are in `docs/plans/`,
the architecture in `docs/architecture/`.

## The map

| I want | Open |
|---|---|
| what a specification's text says at the pinned commit | `specs/<spec>/input/snapshots/` |
| every table row and sentence the extractor read | `specs/<spec>/ir/` |
| why a value is what it is | `specs/<spec>/outputs/provenance/report.md`, or the type map's badge |
| the record that overrode a value | `specs/<spec>/model/overrides/` |
| the published schemas | `specs/<spec>/schemas/`, served at their `$id` |
| the rules JSON Schema can't express, with their vectors | `specs/<spec>/schemas/rules/`, `specs/<spec>/model/vectors/` |
| protocol buffers or an SDK, and the names it promised | `specs/<spec>/targets/<target>/`, and its `values.lock.yaml` |
| what changed between two inputs or two releases | `specs/<spec>/outputs/comparison/`, `specs/<spec>/outputs/releases/` |
| how our output compares with other artifacts' | `specs/<spec>/outputs/enum-drift/`, `specs/<spec>/outputs/matrix/` |
| whether a library I use can carry a specification | `specs/<spec>/outputs/matrix/`, `matrix/libraries.yaml` to add one |
| the shared types every specification rests on | `kernel/` |
| the format of any YAML or JSON file here | `formats/` |
| why a gate is as it is | `gates/decisions/` |
| which of the predecessor's gates are ported, planned, or not applicable | `gates/inventory.yaml` |
| whether our output still matches the predecessor's, byte for byte | `test/parity/oracle-adcom/`, `npm run parity` |
| the pipeline's stages, and what each writes | `src/stages.ts` |

## The method, in twenty lines

The pipeline is one ordered list of stages (`src/stages.ts`). A stage is a
pure function from committed inputs to committed outputs. A specification
supplies data — a profile, locks, a mapping, overrides, a kernel binding,
prose — and code only where its text has a form no reader covers yet.

Every output is committed, so a change to the text or to a rule shows up as a
diff a human reads. `npm run ci` holds that: it runs each gate over what the
pipeline really produced, then runs each gate's **known-bad fixtures** against
the same input, so a gate that cannot fail is a gate that does not count. A
gate's fingerprint digests its code, every declaration that code reaches in
any file, its fixtures, its data, and the exemption files it reads; the guard
fails when a fingerprint is not the one the latest record in
`gates/decisions/` accepts. Those records are append-only. A gate is never
weakened in the change that needs it weakened.

Correctness is not self-consistency. The gates prove the model agrees with
itself and with what the text states; they cannot prove that a reading the
text leaves open is right for the payloads people send. So artifacts other
people publish are pinned and compared against ours, and the predecessor
repository is kept as a **parity oracle**: a ported specification's outputs
equal its byte for byte, or each difference is recorded with the override or
gate decision that backs it.

## Running it

```bash
npm ci --ignore-scripts
npm run ci          # every gate, every fixture, every test
npm run gates       # the fingerprints a gate decision would have to accept
npm run parity      # this repository's outputs against the parity oracle
npm test
npm run typecheck
```

## Licences

Code is under the Apache License 2.0 (`LICENSE-CODE`); everything else under
the Creative Commons Attribution 3.0 License (`LICENSE`). See `NOTICE`.
