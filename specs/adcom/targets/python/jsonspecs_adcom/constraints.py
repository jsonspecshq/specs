"""The constraint tier: the rules that are validator code and never a type.

**Why this layer exists.** Type rules § 2a puts `anyOf` and `oneOf` of `required`,
`if` / `then` / `else`, `not`, a numeric bound, a `pattern` and a length in the constraint
tier, and target rules § 3 sends every constraint construct to the validation layer: no
target language says "`url` is required when `method` is 1 or 2" at the type level, so a
target that carried one in a type would have widened it.

**The published schema states them and `fast_validate` enforces them.** A constraint
reaches a caller as the published document's own keyword, graded by an independent 2020-12
implementation against the published bytes, so this module declares no rule of its own and
transcribes none. A rule written here as Python would be a second statement of a keyword
the document already carries, and the two would disagree the first time a reading moved
one of them.

**So this module is the census and the seam.** `CONSTRUCTS` is every constraint construct
the published tree states, by the node and the pointer that state it. A construct joins it
by appearing in the published bytes and never by being added here, so a reading that emits
a new keyword -- a `oneOf` of `required`, an `if` with a `const` and a `then`
`required` -- arrives in this census and in `fast_validate`'s verdict in the same run that
publishes it, with no edit to this package's code.

`of` reads the census per node, which is what lets a consumer ask what a type's verdict
turns on beyond its own shape, and what lets a check grade this layer's coverage against
the document rather than against a list somebody kept.
"""

from __future__ import annotations

from collections.abc import Sequence

__all__ = ["CONSTRAINT_KEYWORDS", "CONSTRUCTS", "Construct", "of"]


class Construct(tuple[str, str, str]):
    """One constraint construct the published tree states: its node, its pointer, its keyword."""

    __slots__ = ()

    @property
    def node(self) -> str:
        """The published node the construct is under, as a document's `$id` and a pointer."""
        return self[0]

    @property
    def pointer(self) -> str:
        """Where in that node the keyword sits, as a JSON pointer relative to it."""
        return self[1]

    @property
    def keyword(self) -> str:
        """The keyword, which is the document's own and not a name this package gave it."""
        return self[2]


#: The keywords this census counts: type rules § 2a's constraint tier.
CONSTRAINT_KEYWORDS: tuple[str, ...] = (
    'anyOf',
    'oneOf',
    'if',
    'then',
    'else',
    'not',
    'dependentRequired',
    'dependentSchemas',
    'minimum',
    'maximum',
    'exclusiveMinimum',
    'exclusiveMaximum',
    'multipleOf',
    'pattern',
    'minLength',
    'maxLength',
    'minItems',
    'maxItems',
    'uniqueItems',
    'minProperties',
    'maxProperties',
)

#: Every constraint construct the published tree states, by the node that states it.
CONSTRUCTS: tuple[Construct, ...] = (
    Construct(('https://jsonspecs.com/adcom/schemas/kernel/1/kernel.json#/$defs/Count', '/maximum', 'maximum')),
    Construct(('https://jsonspecs.com/adcom/schemas/kernel/1/kernel.json#/$defs/Count', '/minimum', 'minimum')),
    Construct(('https://jsonspecs.com/adcom/schemas/kernel/1/kernel.json#/$defs/Domain', '/maxLength', 'maxLength')),
    Construct(('https://jsonspecs.com/adcom/schemas/kernel/1/kernel.json#/$defs/Domain', '/pattern', 'pattern')),
    Construct(('https://jsonspecs.com/adcom/schemas/kernel/1/kernel.json#/$defs/DurationSeconds', '/maximum', 'maximum')),
    Construct(('https://jsonspecs.com/adcom/schemas/kernel/1/kernel.json#/$defs/DurationSeconds', '/minimum', 'minimum')),
    Construct(('https://jsonspecs.com/adcom/schemas/kernel/1/kernel.json#/$defs/EpochMilliseconds', '/maximum', 'maximum')),
    Construct(('https://jsonspecs.com/adcom/schemas/kernel/1/kernel.json#/$defs/EpochMilliseconds', '/minimum', 'minimum')),
    Construct(('https://jsonspecs.com/adcom/schemas/kernel/1/kernel.json#/$defs/ExtendedDuration', '/minimum', 'minimum')),
    Construct(('https://jsonspecs.com/adcom/schemas/kernel/1/kernel.json#/$defs/IntegerFlag', '/oneOf', 'oneOf')),
    Construct(('https://jsonspecs.com/adcom/schemas/kernel/1/kernel.json#/$defs/IntegerId', '/maximum', 'maximum')),
    Construct(('https://jsonspecs.com/adcom/schemas/kernel/1/kernel.json#/$defs/IntegerId', '/minimum', 'minimum')),
    Construct(('https://jsonspecs.com/adcom/schemas/kernel/1/kernel.json#/$defs/Measure', '/minimum', 'minimum')),
    Construct(('https://jsonspecs.com/adcom/schemas/kernel/1/kernel.json#/$defs/MediaOffset', '/maximum', 'maximum')),
    Construct(('https://jsonspecs.com/adcom/schemas/kernel/1/kernel.json#/$defs/MediaOffset', '/minimum', 'minimum')),
    Construct(('https://jsonspecs.com/adcom/schemas/kernel/1/kernel.json#/$defs/VendorCode', '/minimum', 'minimum')),
    Construct(('https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/Ad', '/anyOf', 'anyOf')),
    Construct(('https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/Asset', '/anyOf', 'anyOf')),
    Construct(('https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/AssetFormat', '/anyOf', 'anyOf')),
    Construct(('https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/Event', '/else', 'else')),
    Construct(('https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/Event', '/else/if', 'if')),
    Construct(('https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/Event', '/else/then', 'then')),
    Construct(('https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/Event', '/if', 'if')),
    Construct(('https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/Event', '/then', 'then')),
    Construct(('https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/Placement', '/anyOf', 'anyOf')),
    Construct(('https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/VideoAsset', '/oneOf', 'oneOf')),
)


def of(node: str) -> Sequence[Construct]:
    """Every constraint construct the published schema states under `node`."""
    return tuple(c for c in CONSTRUCTS if c.node == node)
