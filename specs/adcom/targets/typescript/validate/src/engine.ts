/**
 * The validator this layer runs, and the one module of this package that names a library.
 *
 * The interface demands the three terms a JSON Schema validator emits and a consumer reads: an RFC
 * 6901 pointer at the value, the schema keyword that rejected it, and the JSON Schema path of that
 * keyword.
 *
 * A 2020-12 engine implements the whole validation vocabulary, so a constraint the published schema
 * states — a conditional requirement, an exclusive one, a range, a pattern — needs no code here: it
 * arrives in the bytes and the engine decides it.
 */
import { Ajv2020, type ErrorObject } from "ajv/dist/2020.js";
import ajvFormats from "ajv-formats";

/**
 * The RFC 9562 string form of a UUID: 32 hexadecimal digits in five groups, either case. JSON
 * Schema 2020-12 asserts `uuid` by that form (validation § 7.3.5), and `ajv-formats` also accepts a
 * `urn:uuid:` prefix, which is a URN and not a UUID's string form. So the check is replaced,
 * because a layer that accepted the prefix would accept a payload the published schema refuses —
 * and verdict parity is the floor.
 */
const UUID = /^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}$/;

/**
 * One reason a payload was rejected, in the terms a JSON Schema validator emits.
 */
export interface Issue {
  /**
   * An RFC 6901 JSON Pointer at the value that was rejected; the empty string for the root.
   */
  readonly pointer: string;
  /**
   * The schema keyword that rejected it, as `required`, `type` or `additionalProperties`.
   */
  readonly keyword: string;
  /**
   * The JSON Schema path of the rejecting keyword, as `#/properties/api/items/oneOf/1`.
   */
  readonly schemaPath: string;
  /**
   * What the engine said, for a reader.
   */
  readonly message: string;
}

/**
 * A verdict on one payload: accepted, or rejected with every reason.
 */
export type Verdict = { readonly ok: true } | { readonly ok: false; readonly issues: readonly Issue[] };

/**
 * What this layer needs of a validator, and no more.
 */
export interface Engine {
  /**
   * The library and its version, for a report that has to say which engine reached a verdict.
   */
  readonly name: string;
  /**
   * Compiles a `$ref` into the tree the engine was built over. Throws where the engine cannot carry
   * the node, which is a refusal and not a verdict.
   */
  compile(ref: string): (value: unknown) => Verdict;
}

/**
 * The engine over a set of published documents, each added under the `$id` it declares, so a
 * cross-file `$ref` resolves exactly as a consumer's validator resolves it and the tree needs no
 * bundling.
 *
 * `strict` on with `strictRequired` off are the options this repository's own conformance corpus
 * was graded with, so this layer and that corpus compile one document the same way.
 */
export function engine(documents: readonly Readonly<Record<string, unknown>>[]): Engine {
  const ajv = new Ajv2020({ strict: true, strictRequired: false, allErrors: true });
  ajvFormats.default(ajv);
  ajv.addFormat("uuid", UUID);
  for (const d of documents) ajv.addSchema(d as object);
  return {
    name: "ajv 8.20.0 (2020-12)",
    compile: (ref) => {
      const validate = ajv.compile({ $ref: ref });
      return (value) => (validate(value) ? { ok: true } : { ok: false, issues: (validate.errors ?? []).map(issueOf) });
    },
  };
}

/**
 * One engine error in this layer's own terms.
 */
const issueOf = (e: ErrorObject): Issue => ({ pointer: e.instancePath, keyword: e.keyword, schemaPath: e.schemaPath, message: e.message ?? e.keyword });
