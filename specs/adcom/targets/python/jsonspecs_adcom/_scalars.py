"""The delegated scalars: every type of the published tree whose value is not an object.

A scalar is a leaf of the tree's type graph, so this module references nothing of the package but its base model. The vocabularies are written after it and the objects after them, which is the one order in which no module imports a module that imports it.

Generated from a published JSON Schema tree by an external generator and then restated by
this target; don't edit it by hand. What is delegated and what the target writes itself is
stated in the target's own module header.

Every type here carries the published node it came from as `SCHEMA` and takes its verdict
from `_runtime`, so a payload is graded against the published bytes and never against
this file.
"""

from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, RootModel, confloat, conint, constr
from enum import IntEnum

from ._runtime import SpecRootModel


class Count(SpecRootModel[conint(ge=0, le=9007199254740991)]):
    root: conint(ge=0, le=9007199254740991) = Field(
        ...,
        description="A whole number of things, never negative and at most 2^53 − 1, such as impressions, options, or a proposal's revisions, which its `version` counts.",
    )


class Degrees(SpecRootModel[float]):
    root: float = Field(
        ...,
        description="A geographic coordinate in signed decimal degrees, a latitude or a longitude, where the sign gives the hemisphere, as AdCOM 1.0 writes a `Geo`'s `lat` from −90.0 to +90.0 and its `lon` from −180.0 to +180.0. A receiver reads it as a number and never rounds it to a whole degree. The type states no bound, because the two bounds are the coordinate's and not the kind's, and one type carrying both would accept a latitude of 150.",
    )


class Domain(SpecRootModel[
        constr(
            pattern=r'^([a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]([a-z0-9-]{0,61}[a-z0-9])?$',
            max_length=253,
        )
    ]
):
    root: constr(
        pattern=r'^([a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]([a-z0-9-]{0,61}[a-z0-9])?$',
        max_length=253,
    ) = Field(
        ...,
        description='A domain name, written as lowercase A-labels with at least two labels, a top-level label that starts with a letter, and no trailing dot, such as `examplepub.example`.',
    )


class DurationSeconds(SpecRootModel[conint(ge=0, le=9007199254740991)]):
    root: conint(ge=0, le=9007199254740991) = Field(
        ...,
        description='A length of time in whole seconds, never negative, as AdCOM 1.0 writes a `Video`\'s `dur`, "Duration of the video creative in seconds", and a `Content`\'s `len`, "Length of content in seconds". The unit is seconds and never milliseconds, so `30` is half a minute. It is a length and not a point, so a receiver adds two of them and never compares one with an instant, and it is not a number of things, so nothing counts it. It carries no sentinel, because a field that states "no limit" in the same value is `ExtendedDuration`.',
    )


class EpochMilliseconds(SpecRootModel[conint(ge=-9007199254740991, le=9007199254740991)]):
    root: conint(ge=-9007199254740991, le=9007199254740991) = Field(
        ...,
        description='A point in time written as a whole number of milliseconds since the Unix epoch, `1970-01-01T00:00:00Z`, as AdCOM 1.0 writes an `Ad`\'s `init`, "Timestamp of the original instantiation of this ad … in Unix format (i.e., milliseconds since the epoch)". The unit is milliseconds and never seconds, so `1793664000000` is 2026-11-03 and the same instant written in seconds, `1793664000`, is a thousand times smaller and reads as 1970-01-21. The value is signed, because an instant before the epoch is a negative number of milliseconds, and it runs from −(2^53 − 1) to 2^53 − 1, the integers an I-JSON receiver reads exactly. A receiver compares two of them as instants, as it compares two Timestamps, and never adds them or reads one as a number of things.',
    )


class ExtendedDuration(SpecRootModel[conint(ge=-1)]):
    root: conint(ge=-1) = Field(
        ...,
        description='A length of extended play in whole seconds, where `0` states that no extension is allowed and `-1` that an extension is allowed with no limit, as AdCOM 1.0 writes a `VideoPlacement`\'s `maxext`. So the value is never below −1, and a receiver reads `-1` as "no limit" rather than as a length.',
    )


class ExternalId(SpecRootModel[str]):
    root: str = Field(
        ...,
        description="The identity of a record, a code, or a version that another system or list defines, such as a registry entry, a DSP seat, a geo code, a content category, a published document's version, or a field of the specification, named by its path as the specification's tables write it, carried as that system writes it. The field's description names the system or list it comes from.",
    )


class IntegerId(SpecRootModel[conint(ge=-9007199254740991, le=9007199254740991)]):
    root: conint(ge=-9007199254740991, le=9007199254740991) = Field(
        ...,
        description='An identifier that an integer spells, as AdCOM 1.0 writes a `VideoPlacement`\'s `podid`, "Unique identifier indicating that an impression opportunity belongs to a video ad pod". A receiver compares two of them for equality and does nothing else with them, never ordering them, never adding them, and never reading one as a number of things. No value is reserved, so a negative integer identifies a thing like any other, and the only bound is the integers an I-JSON receiver reads exactly.',
    )


class Measure(SpecRootModel[confloat(ge=0.0)]):
    root: confloat(ge=0.0) = Field(
        ...,
        description="What a metric that isn't a rate measures, a number never negative and not always whole, such as 1,200,000 audience impacts for DOOH or a modelled audience of 14.2 impacts per play.",
    )


class MediaOffset(SpecRootModel[conint(ge=0, le=9007199254740991)]):
    root: conint(ge=0, le=9007199254740991) = Field(
        ...,
        description='A point within a piece of media, in whole seconds from its start and never negative, such as the second of a video at which a mid-roll ad starts.',
    )


class MinuteOffset(SpecRootModel[int]):
    root: int = Field(
        ...,
        description='A local clock\'s offset from UTC in whole minutes, signed, where a negative value is west of UTC, as AdCOM 1.0 writes a `Geo`\'s `utcoffset`, "local time as the number +/- of minutes from UTC". A receiver reads it beside a point in time and never as a length of time.',
    )


class Text(SpecRootModel[str]):
    root: str = Field(
        ...,
        description='Prose for people and agents to read, on which the specification states no lexical constraint.',
    )


class VendorCode(SpecRootModel[conint(ge=500)]):
    root: conint(ge=500) = Field(
        ...,
        description='A code that an AdCOM 1.0 list reserves for vendors, 500 or more, as List API Frameworks reserves "500+ Vendor-specific codes". It extends a vocabulary of the list\'s codes.',
    )

# The published node each type was generated from. Every verdict and every check reads it
# off the class, so no table, filename or name-keyed lookup stands between a type and the
# schema it has to answer for.
Count.SCHEMA = 'https://jsonspecs.com/adcom/schemas/kernel/1/kernel.json#/$defs/Count'
Degrees.SCHEMA = 'https://jsonspecs.com/adcom/schemas/kernel/1/kernel.json#/$defs/Degrees'
Domain.SCHEMA = 'https://jsonspecs.com/adcom/schemas/kernel/1/kernel.json#/$defs/Domain'
DurationSeconds.SCHEMA = 'https://jsonspecs.com/adcom/schemas/kernel/1/kernel.json#/$defs/DurationSeconds'
EpochMilliseconds.SCHEMA = 'https://jsonspecs.com/adcom/schemas/kernel/1/kernel.json#/$defs/EpochMilliseconds'
ExtendedDuration.SCHEMA = 'https://jsonspecs.com/adcom/schemas/kernel/1/kernel.json#/$defs/ExtendedDuration'
ExternalId.SCHEMA = 'https://jsonspecs.com/adcom/schemas/kernel/1/kernel.json#/$defs/ExternalId'
IntegerId.SCHEMA = 'https://jsonspecs.com/adcom/schemas/kernel/1/kernel.json#/$defs/IntegerId'
Measure.SCHEMA = 'https://jsonspecs.com/adcom/schemas/kernel/1/kernel.json#/$defs/Measure'
MediaOffset.SCHEMA = 'https://jsonspecs.com/adcom/schemas/kernel/1/kernel.json#/$defs/MediaOffset'
MinuteOffset.SCHEMA = 'https://jsonspecs.com/adcom/schemas/kernel/1/kernel.json#/$defs/MinuteOffset'
Text.SCHEMA = 'https://jsonspecs.com/adcom/schemas/kernel/1/kernel.json#/$defs/Text'
VendorCode.SCHEMA = 'https://jsonspecs.com/adcom/schemas/kernel/1/kernel.json#/$defs/VendorCode'
