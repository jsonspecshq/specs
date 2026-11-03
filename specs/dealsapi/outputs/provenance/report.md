# Provenance of main's generated values

Every value a consumer sees records one of two origins: by rule, naming the
rule and the elements of the specification it read, or by override, naming the
record that set it and what the rule would have given. `npm run provenance`
writes this file from the model and the emitted schemas; don't edit it.

## By attribute

| Attribute | By rule | By override | Total |
|---|---|---|---|
| `code-name` | 42 | 0 | 42 |
| `defs-key` | 26 | 0 | 26 |
| `description` | 81 | 0 | 81 |
| `title` | 59 | 0 | 59 |
| **all** | **208** | **0** | **208** |

### Within those

| | By rule | By override | Total |
|---|---|---|---|
| vocabulary names | 11 | 0 | 11 |
| object names | 4 | 0 | 4 |
| kernel type names | 11 | 0 | 11 |
| branch titles | 45 | 0 | 45 |
| type and file titles | 14 | 0 | 14 |
| code names | 42 | 0 | 42 |

## Overridden values

None: every value this lock emits comes from a rule.

