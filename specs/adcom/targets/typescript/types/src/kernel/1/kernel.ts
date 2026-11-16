/**
 * Generated from a published JSON Schema tree; don't edit it by hand.
 *
 * From https://jsonspecs.com/adcom/schemas/kernel/1/kernel.json
 */

/**
 * A whole number of things, never negative and at most 2^53 − 1, such as impressions, options, or a
 * proposal's revisions, which its `version` counts.
 */
export type Count = number;

/**
 * A geographic coordinate in signed decimal degrees, a latitude or a longitude, where the sign
 * gives the hemisphere, as AdCOM 1.0 writes a `Geo`'s `lat` from −90.0 to +90.0 and its `lon` from
 * −180.0 to +180.0. A receiver reads it as a number and never rounds it to a whole degree. The type
 * states no bound, because the two bounds are the coordinate's and not the kind's, and one type
 * carrying both would accept a latitude of 150.
 */
export type Degrees = number;

/**
 * A domain name, written as lowercase A-labels with at least two labels, a top-level label that
 * starts with a letter, and no trailing dot, such as `examplepub.example`.
 */
export type Domain = string;

/**
 * A length of time in whole seconds, never negative, as AdCOM 1.0 writes a `Video`'s `dur`,
 * "Duration of the video creative in seconds", and a `Content`'s `len`, "Length of content in
 * seconds". The unit is seconds and never milliseconds, so `30` is half a minute. It is a length
 * and not a point, so a receiver adds two of them and never compares one with an instant, and it is
 * not a number of things, so nothing counts it. It carries no sentinel, because a field that states
 * "no limit" in the same value is `ExtendedDuration`.
 */
export type DurationSeconds = number;

/**
 * A point in time written as a whole number of milliseconds since the Unix epoch,
 * `1970-01-01T00:00:00Z`, as AdCOM 1.0 writes an `Ad`'s `init`, "Timestamp of the original
 * instantiation of this ad … in Unix format (i.e., milliseconds since the epoch)". The unit is
 * milliseconds and never seconds, so `1793664000000` is 2026-11-03 and the same instant written in
 * seconds, `1793664000`, is a thousand times smaller and reads as 1970-01-21. The value is signed,
 * because an instant before the epoch is a negative number of milliseconds, and it runs from −(2^53
 * − 1) to 2^53 − 1, the integers an I-JSON receiver reads exactly. A receiver compares two of them
 * as instants, as it compares two Timestamps, and never adds them or reads one as a number of
 * things.
 */
export type EpochMilliseconds = number;

/**
 * An object for members the specification leaves to the parties to define, such as the Deals API's
 * `ext` on each of its objects. It takes any members, and a receiver keeps the ones it doesn't
 * know.
 */
export interface Ext {
  /**
   * The members the specification leaves to the parties to define. This node states no
   * `additionalProperties: false`, so a member it does not name is admitted and a receiver keeps
   * it.
   */
  readonly [member: string]: unknown;
}

/**
 * A length of extended play in whole seconds, where `0` states that no extension is allowed and
 * `-1` that an extension is allowed with no limit, as AdCOM 1.0 writes a `VideoPlacement`'s
 * `maxext`. So the value is never below −1, and a receiver reads `-1` as "no limit" rather than as
 * a length.
 */
export type ExtendedDuration = number;

/**
 * The identity of a record, a code, or a version that another system or list defines, such as a
 * registry entry, a DSP seat, a geo code, a content category, a published document's version, or a
 * field of the specification, named by its path as the specification's tables write it, carried as
 * that system writes it. The field's description names the system or list it comes from.
 */
export type ExternalId = string;

/**
 * A yes or no written as an integer, `0` for no and `1` for yes, as AdCOM 1.0 and OpenRTB 2.6 write
 * their flags, such as a placement's `instl`. A receiver reads it as a flag, never as a count, and
 * a field that takes it keeps the integer its text writes.
 */
export type IntegerFlag = 0 | 1;

/**
 * An identifier that an integer spells, as AdCOM 1.0 writes a `VideoPlacement`'s `podid`, "Unique
 * identifier indicating that an impression opportunity belongs to a video ad pod". A receiver
 * compares two of them for equality and does nothing else with them, never ordering them, never
 * adding them, and never reading one as a number of things. No value is reserved, so a negative
 * integer identifies a thing like any other, and the only bound is the integers an I-JSON receiver
 * reads exactly.
 */
export type IntegerId = number;

/**
 * What a metric that isn't a rate measures, a number never negative and not always whole, such as
 * 1,200,000 audience impacts for DOOH or a modelled audience of 14.2 impacts per play.
 */
export type Measure = number;

/**
 * A point within a piece of media, in whole seconds from its start and never negative, such as the
 * second of a video at which a mid-roll ad starts.
 */
export type MediaOffset = number;

/**
 * A local clock's offset from UTC in whole minutes, signed, where a negative value is west of UTC,
 * as AdCOM 1.0 writes a `Geo`'s `utcoffset`, "local time as the number +/- of minutes from UTC". A
 * receiver reads it beside a point in time and never as a length of time.
 */
export type MinuteOffset = number;

/**
 * Prose for people and agents to read, on which the specification states no lexical constraint.
 */
export type Text = string;

/**
 * A code that an AdCOM 1.0 list reserves for vendors, 500 or more, as List API Frameworks reserves
 * "500+ Vendor-specific codes". It extends a vocabulary of the list's codes.
 */
export type VendorCode = number;
