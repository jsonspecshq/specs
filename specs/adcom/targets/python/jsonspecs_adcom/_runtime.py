"""The hand-written half of this package: the base model, the documents, the verdict.

Every other module here is a function of a published schema tree. This one is a function
of none, which is why it is the only file that is not generated.

**Every type carries the node it came from.** `SCHEMA` is a published document's `$id`
with a JSON pointer into it, and that one fact is what makes the verdict generic:
`strict_validate` reads it off the class, and so does any check that grades this package.
A class that carries its own schema cannot be aimed at another tree's output.

**The verdict is the published schema's, the value is this library's, and the ORDER is
what makes the verdict right.** `fast_validate` grades a payload against the published
bytes, which this package carries verbatim under `schemas/`, through an independent
2020-12 implementation; `strict_validate` is that verdict and then the construction. The
clearest case is a `pattern`: a 2020-12 pattern is an ECMA-262 regular expression, where
`$` does not match before a trailing newline, and the data model's own engine is never
asked, because the schema has already refused the value. A single entry point that merged
the two would hand the value to a constructor whose accepted set is not the document's.

**`model_validate` is left as the language gives it**: it constructs and consults no
schema, so an explicit `null` where the schema states a type, and a string where it
states an integer, are invisible to it. A caller that wants the schema's accepted set
calls `strict_validate`; a caller holding a payload it has already graded calls
`model_validate` and pays for a constructor alone. Merging them would take that choice
away, and the data model's own widenings are declared in `representation.py` rather than
hidden behind one entry point.

**Absence is kept by the serialiser.** A schema here admits no `null` and states an
optional member by leaving it out of `required`, so of the three states a caller can mean
-- absent, null, a value -- the schema has two, and `model_fields_set` already tells them
apart. `to_payload` and `to_json` write the members a caller set and no others, which is
why a value this package builds round-trips through the schema it came from.
"""

from __future__ import annotations

import json
from collections.abc import Mapping
from importlib import resources
from typing import Any, ClassVar, Self, TypeVar

import jsonschema_rs
from pydantic import BaseModel, ConfigDict, RootModel

__all__ = [
    "Exact",
    "Refused",
    "Representation",
    "SchemaViolation",
    "SpecModel",
    "SpecRootModel",
    "Vocabulary",
    "Widened",
    "accepts",
    "document",
    "documents",
    "fast_validate",
    "validator_for",
]

#: The package folder the published documents are carried in, each at its path in the tree.
SCHEMAS = "schemas"


class SchemaViolation(ValueError):
    """A payload the published schema refuses, carrying the schema's own reasons.

    The reasons are the validator's, in the order it found them. No sentence here restates
    a constraint: a message this package wrote would be a second statement of a rule the
    document already makes, and the two would disagree the first time a reading moved one.
    """

    def __init__(self, schema: str, reasons: tuple[str, ...]) -> None:
        self.schema = schema
        self.reasons = reasons
        super().__init__(f"{schema}: {'; '.join(reasons) if reasons else 'refused'}")


class Representation:
    """What this target did with one fact of one node, as one of three (target rules § 7).

    A widening cannot be constructed without its declaration, nor a refusal without its
    reason, because the argument is required: an undeclared widening is unrepresentable
    here as it is in the emitter.
    """

    __slots__ = ()


class Exact(Representation):
    """The type states the fact the schema states, with nothing added and nothing lost."""

    __slots__ = ()

    def __repr__(self) -> str:
        return "Exact()"


class Widened(Representation):
    """The type admits values the schema refuses, or loses a distinction the schema makes."""

    __slots__ = ("declaration",)

    def __init__(self, declaration: str) -> None:
        self.declaration = declaration

    def __repr__(self) -> str:
        return f"Widened({self.declaration!r})"


class Refused(Representation):
    """The type states nothing for the node, and says why."""

    __slots__ = ("reason",)

    def __init__(self, reason: str) -> None:
        self.reason = reason

    def __repr__(self) -> str:
        return f"Refused({self.reason!r})"


_DOCUMENTS: dict[str, Any] = {}


def documents() -> Mapping[str, Any]:
    """Every published document this package carries, by its `$id`, parsed once.

    Read from the package's own data and not from a transcription of it: the bytes under
    `schemas/` are the published files, so what this package grades against is what a
    consumer fetching the `$id` receives.
    """
    if not _DOCUMENTS:
        from . import _documents

        root = resources.files(__package__).joinpath(SCHEMAS)
        for path in _documents.FILES:
            parsed = json.loads(root.joinpath(path).read_text(encoding="utf-8"))
            _DOCUMENTS[str(parsed["$id"])] = parsed
    return _DOCUMENTS


def document(schema_id: str) -> Any:
    """One published document, by its `$id`."""
    return documents()[schema_id]


def _retrieve(uri: object) -> Any:
    """A document the tree references, by the `$id` a relative reference resolved to.

    A reference that leaves the tree is refused rather than fetched: this package reads its
    own files and never the network, so a tree whose references do not close inside it
    fails here instead of grading against whatever a host served.
    """
    held = documents()
    key = str(uri)
    if key not in held:
        raise SchemaViolation(key, (f"references {key}, which this package does not carry",))
    return held[key]


_VALIDATORS: dict[str, Any] = {}


def validator_for(schema: str) -> Any:
    """A validator for one published node, compiled once per node.

    `schema` is a document's `$id` with a JSON pointer, which is what every type of this
    package carries as `SCHEMA`.

    **`format` is asserted and not annotated.** 2020-12 leaves `format` an annotation by
    default, so a validator left at its default accepts `"2026-02-30T00:00:00Z"` for a
    `date-time`: a string that names no instant. The schemas this package carries state
    `format` as a constraint and the conformance corpus labels its payloads with a
    format-asserting oracle, so a verdict taken without it is weaker than the verdict the
    published schema states, and a package reaching it would accept a payload the
    specification refuses.
    """
    got = _VALIDATORS.get(schema)
    if got is None:
        got = jsonschema_rs.validator_for({"$ref": schema}, retriever=_retrieve, validate_formats=True)
        _VALIDATORS[schema] = got
    return got


def fast_validate(schema: str, payload: Any) -> None:
    """Raise `SchemaViolation` unless the published schema at `schema` accepts `payload`.

    No value is built, so a caller that wants the verdict and not the value pays for the
    verdict alone.
    """
    validator = validator_for(schema)
    if validator.is_valid(payload):
        return
    raise SchemaViolation(schema, tuple(error.message for error in validator.iter_errors(payload)))


def accepts(schema: str, payload: Any) -> bool:
    """Whether the published schema at `schema` accepts `payload`: a verdict and no value."""
    return bool(validator_for(schema).is_valid(payload))


class _SchemaBound:
    """What every type of this package carries: the node it came from, and the verdict on it."""

    #: The published node this type was generated from: a document's `$id` and a pointer.
    SCHEMA: ClassVar[str] = ""

    @classmethod
    def fast_validate(cls, payload: Any) -> None:
        """Raise `SchemaViolation` unless the published schema accepts `payload`. No value is built."""
        fast_validate(cls.SCHEMA, payload)

    @classmethod
    def accepts(cls, payload: Any) -> bool:
        """Whether the published schema accepts `payload`: a verdict and no value."""
        return accepts(cls.SCHEMA, payload)

    @classmethod
    def strict_validate(cls, payload: Any) -> Self:
        """The published schema's verdict on `payload`, and then the value.

        The schema decides what is accepted and this library decides what the value is, in
        that order, so a payload the schema refuses builds nothing.
        """
        fast_validate(cls.SCHEMA, payload)
        return cls.model_validate(payload)  # type: ignore[attr-defined,no-any-return]


class SpecModel(_SchemaBound, BaseModel):
    """The base of every object type.

    `extra` is the document's own: a node stating `additionalProperties: false` forbids a
    member it does not name, and this default is what a node stating nothing gets.
    `validate_default` is set for every field, because a stated default that does not
    validate arrives as the type the JSON wrote rather than as the type the schema states,
    and one schema keyword would then reach a caller two ways.

    Nothing here reads an environment, and no type carries a policy its document does not
    state.
    """

    model_config = ConfigDict(extra="forbid", validate_default=True)

    def to_payload(self) -> Any:
        """This value as JSON types: the members set on it, and no others.

        The one serialiser this target exposes (target rules § 8). An absent member is
        absent rather than `null`, so the result validates against the schema the type came
        from.
        """
        return self.model_dump(mode="json", exclude_unset=True, by_alias=True)

    def to_json(self) -> str:
        """This value as JSON text: the members set on it, and no others."""
        return json.dumps(self.to_payload(), separators=(",", ":"), sort_keys=True, ensure_ascii=False)


RootT = TypeVar("RootT")


class SpecRootModel(_SchemaBound, RootModel[RootT]):
    """The base of every type whose value is not an object: a scalar, or a vocabulary."""

    def to_payload(self) -> Any:
        """This value as JSON types."""
        return self.model_dump(mode="json")

    def to_json(self) -> str:
        """This value as JSON text."""
        return json.dumps(self.to_payload(), separators=(",", ":"), ensure_ascii=False)


class Vocabulary(SpecRootModel[RootT]):
    """The base of every integer-coded vocabulary: its codes, each under its published name.

    **A code's name is the schema's and never this package's.** The schema publishes each
    code's decided name on the code's own branch and this package writes it verbatim, so
    one name reaches every artifact and no two of them derive two names for one code.

    **A vocabulary's branches are classes, and an open one is extended by subclassing its
    extension point.** A list that reserves codes it does not state has such a branch, and
    an application carries its own code by subclassing that class and naming the code in
    its own `CODES`: the published schema already admits the value, so the verdict does not
    change, and `codes()` is what a consumer writes its own coverage over. A branch
    subclasses the base and so does not exist while the base is built, which is why the
    declaring module assigns `_branch_models` and rebuilds afterwards.
    """

    #: Every code this class names, by code. A subclass adds its own and inherits these.
    CODES: ClassVar[Mapping[int, str]] = {}

    #: The classes this vocabulary's branches are, assigned once they are declared.
    _branch_models: ClassVar[tuple[type[Vocabulary[Any]], ...]] = ()

    @classmethod
    def name_of(cls, code: int) -> str | None:
        """The published name of `code`, or None where this class names no such code."""
        return cls.CODES.get(code)

    @classmethod
    def codes(cls) -> Mapping[int, str]:
        """Every code this class names, which is what a consumer writes its own coverage over."""
        return cls.CODES

    @classmethod
    def branches(cls) -> tuple[type[Vocabulary[Any]], ...]:
        """This vocabulary's branch classes: its listed codes, and its extension point where it has one."""
        return cls._branch_models

    @property
    def code(self) -> int:
        """This value as the integer it is."""
        return int(self.root)  # type: ignore[call-overload]

    @property
    def name(self) -> str | None:
        """The published name of this value, or None for a code this class does not name."""
        return type(self).CODES.get(self.code)
