/**
 * Generated from a published JSON Schema tree; don't edit it by hand.
 *
 * From https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json
 */

import type { Count, Degrees, Domain, DurationSeconds, EpochMilliseconds, Ext, ExtendedDuration, ExternalId, IntegerFlag, IntegerId, Measure, MinuteOffset, Text } from "../../../kernel/1/kernel.js";
import type { AgentType, ApiFramework, AuditStatusCode, CategoryTaxonomy, ClickType, CompanionType, ConnectionType, ContentContext, CreativeAttribute, CreativeSubtypeAudioVideo, CreativeSubtypeDisplay, DeliveryMethod, DeviceType, DisplayContextType, DisplayPlacementType, EventTrackingMethod, EventType, ExpandableDirection, FeedType, IdMatchMethod, IpLocationService, LinearityMode, LocationType, MediaRating, NativeDataAssetType, NativeImageAssetType, OperatingSystem, PlacementPosition, PlaybackCessationMode, PlaybackMethod, PlcmtSubtypeVideo, PodSequence, ProductionQuality, SizeUnit, SlotPositionInPod, StartDelayMode, UserAgentSource, VolumeNormalizationMode } from "../../lists/1/lists.js";

export interface Ad {
  /**
   * Advertiser domain; top two levels only (e.g., “ford.com”). This can be an array for the case of
   * rotating creatives.
   */
  readonly adomain?: readonly Domain[];
  /**
   * Set of attributes describing the creative. Refer to List: Creative Attributes.
   */
  readonly attr?: readonly CreativeAttribute[];
  /**
   * Media Subtype Object that indicates this is an audio ad and provides additional detail as such.
   * Refer to Object: Audio. * Required if no other media subtype object is specified.
   */
  readonly audio?: Audio;
  /**
   * An object depicting the audit status of the ad; typically part of a quality/safety review
   * process. Refer to Object: Audit.
   */
  readonly audit?: Audit;
  /**
   * When the product of the ad is an app, the unique ID of that app as a bundle or package name
   * (e.g., “com.foo.mygame”). This should NOT be an app store ID (e.g., no iTunes store IDs). This
   * can be an array of for the case of rotating creatives.
   */
  readonly bundle?: readonly ExternalId[];
  /**
   * Array of content categories describing the ad using IDs from the taxonomy indicated in
   * `cattax`. Implementer should ensure compliance with regional legislation around data usage and
   * sharing.
   */
  readonly cat?: readonly ExternalId[];
  /**
   * The taxonomy in use for the `cat` attribute. Refer to List: Category Taxonomies.
   *
   * @default 2
   */
  readonly cattax?: CategoryTaxonomy;
  /**
   * Media Subtype Object that indicates this is a display ad and provides additional detail as
   * such. Refer to Object: Display. * Required if no other media subtype object is specified.
   */
  readonly display?: Display;
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * ID of the creative; unique at least throughout the scope of a vendor (e.g., an exchange or
   * buying platform). Note that multiple instances of the same ad when used in transactions must
   * have the same ID.
   */
  readonly id: ExternalId;
  /**
   * Timestamp of the original instantiation of this ad (i.e., this object or any of its children)
   * in Unix format (i.e., milliseconds since the epoch).
   */
  readonly init?: EpochMilliseconds;
  /**
   * URL without cache-busting to an image that is representative of the ad content for cursory
   * level ad quality checking.
   */
  readonly iurl?: Text;
  /**
   * Language of the creative using ISO-639-1-alpha-2. In practice, vendors using this object may
   * elect an alternate standard (e.g., BCP-47) in which case this must be communicated beforehand.
   * The non-standard code “xx” may also be used if the creative has no linguistic content (e.g., a
   * banner with just a company logo).
   */
  readonly lang?: ExternalId;
  /**
   * Timestamp of most recent modification to this ad (i.e., this object or any of its children
   * other than the `Audit` object) in Unix format (i.e., milliseconds since the epoch).
   */
  readonly lastmod?: EpochMilliseconds;
  /**
   * Media rating per IQG guidelines. Refer to List: Media Ratings.
   */
  readonly mrating?: MediaRating;
  /**
   * Flag to indicate if the creative is secure (i.e., uses HTTPS for all assets and markup), where
   * 0 = no, 1 = yes. There is no default and thus if omitted, the secure state is unknown. However,
   * as a practical matter, the safe assumption is to treat unknown as non-secure.
   */
  readonly secure?: IntegerFlag;
  /**
   * Media Subtype Object that indicates this is a video ad and provides additional detail as such.
   * Refer to Object: Video. * Required if no other media subtype object is specified.
   */
  readonly video?: Video;
}

/**
 * Amp Rendering Treatment
 *
 * The codes of `DisplayPlacement.ampren`, each with the label the text gives it
 */
export type AmpRenderingTreatment = 1 | 2;

/**
 * The codes of AmpRenderingTreatment, each under the name the published schema carries for it.
 */
export const AmpRenderingTreatmentCodes = {
  /**
   * early loading
   */
  EARLY_LOADING: 1,
  /**
   * standard loading
   */
  STANDARD_LOADING: 2,
} as const satisfies Readonly<Record<string, AmpRenderingTreatment>>;

export interface App {
  /**
   * Bundle or package name of the app (e.g., “com.foo.mygame”) and should NOT be app store IDs
   * (e.g., not iTunes store IDs).
   */
  readonly bundle?: ExternalId;
  /**
   * Array of content categories describing the app using IDs from the taxonomy indicated in
   * `cattax`.
   */
  readonly cat?: readonly ExternalId[];
  /**
   * The taxonomy in use for the `cat`, `sectcat` and `pagecat` attributes. Refer to List: Category
   * Taxonomies.
   */
  readonly cattax?: CategoryTaxonomy;
  /**
   * Details about the content within the distribution channel. Refer to Object: Content.
   */
  readonly content?: Content;
  /**
   * Domain of the app (e.g., “mygame.foo.com”).
   */
  readonly domain?: Domain;
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * Vendor-specific unique identifier of the distribution channel.
   */
  readonly id?: ExternalId;
  /**
   * This field is deprecated, use 'kwarray' instead.
   */
  readonly keywords?: Text;
  /**
   * Array of keywords about the app. Only one of 'keywords' or 'kwarray' may be present.
   */
  readonly kwarray?: readonly Text[];
  /**
   * Displayable name of the distribution channel.
   */
  readonly name?: Text;
  /**
   * Array of content categories describing the current page or view of the app using IDs from the
   * taxonomy indicated in `cattax`.
   */
  readonly pagecat?: readonly ExternalId[];
  /**
   * Indicator of whether or not this is a paid app, where 0 = free, 1 = paid.
   *
   * @default 0
   */
  readonly paid?: IntegerFlag;
  /**
   * Indicates if the app has a privacy policy, where 0 = no, 1 = yes.
   */
  readonly privpolicy?: IntegerFlag;
  /**
   * Details about the publisher of the distribution channel. Refer to Object: Publisher.
   */
  readonly pub?: Publisher;
  /**
   * Array of content categories describing the current section of the app using IDs from the
   * taxonomy indicated in `cattax`.
   */
  readonly sectcat?: readonly ExternalId[];
  /**
   * The ID of the app in an app store (e.g., Apple iTunes, Google Play).
   */
  readonly storeid?: ExternalId;
  /**
   * App store URL for an installed app; for IQG 2.1 compliance.
   */
  readonly storeurl?: Text;
  /**
   * Application version.
   */
  readonly ver?: ExternalId;
}

export interface Asset {
  /**
   * Asset Subtype Object that indicates this is a data asset and provides additional detail as
   * such. Refer to Object: DataAsset. * Required if no other asset subtype object is specified.
   */
  readonly data?: DataAsset;
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * The value of `AssetFormat.id` if this ad references a specific native placement defined by a
   * `Placement` object and its structure.
   */
  readonly id?: Count;
  /**
   * Asset Subtype Object that indicates this is an image asset and provides additional detail as
   * such. Refer to Object: ImageAsset. * Required if no other asset subtype object is specified.
   */
  readonly image?: ImageAsset;
  /**
   * Asset Subtype Object that indicates this is a link asset and provides additional detail as
   * such. Refer to Object: LinkAsset. * Required if no other asset subtype object is specified.
   */
  readonly link?: LinkAsset;
  /**
   * Indicates if the asset is required to be displayed, where 0 = no, 1 = yes.
   *
   * @default 0
   */
  readonly req?: IntegerFlag;
  /**
   * Asset Subtype Object that indicates this is a title asset and provides additional detail as
   * such. Refer to Object: TitleAsset. * Required if no other asset subtype object is specified.
   */
  readonly title?: TitleAsset;
  /**
   * Asset Subtype Object that indicates this is a video asset and provides additional detail as
   * such. Refer to Object: VideoAsset. * Required if no other asset subtype object is specified.
   */
  readonly video?: VideoAsset;
}

export interface AssetFormat {
  /**
   * Asset Format Subtype Object that indicates this is specifying a data asset and provides
   * additional detail as such. Refer to Object: DataAssetFormat. * Required if no other asset
   * format subtype object is specified.
   */
  readonly data?: DataAssetFormat;
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * Asset ID, unique within the scope of this placement specification.
   */
  readonly id: Count;
  /**
   * Asset Format Subtype Object that indicates this is specifying an image asset and provides
   * additional detail as such. Refer to Object: ImageAssetFormat. * Required if no other asset
   * format subtype object is specified.
   */
  readonly img?: ImageAssetFormat;
  /**
   * Indicator of whether or not this asset is required, where 0 = no, 1 = yes.
   *
   * @default 0
   */
  readonly req?: IntegerFlag;
  /**
   * Asset Format Subtype Object that indicates this is specifying a title asset and provides
   * additional detail as such. Refer to Object: TitleAssetFormat. * Required if no other asset
   * format subtype object is specified.
   */
  readonly title?: TitleAssetFormat;
  /**
   * Asset Format Subtype Object, which leverages the `VideoPlacement` object, that indicates this
   * is specifying a video asset and provides additional detail as such. Refer to Object:
   * VideoPlacement. * Required if no other asset format subtype object is specified.
   */
  readonly video?: VideoPlacement;
}

export interface Audio {
  /**
   * Audio markup (e.g., DAAST). Note that including both `adm` and `curl` is not recommended.
   */
  readonly adm?: Text;
  /**
   * API required by the ad if applicable. Refer to List: API Frameworks.
   */
  readonly api?: readonly ApiFramework[];
  /**
   * Subtype of audio creative. Refer to List: Creative Subtypes - Audio/Video.
   */
  readonly ctype?: CreativeSubtypeAudioVideo;
  /**
   * Optional means of retrieving markup by reference; a URL that returns audio markup (e.g.,
   * DAAST). If this ad is matched to a Placement specification, the `Placement.curlx` attribute
   * indicates if this markup retrieval option is supported. Note that including both `adm` and
   * `curl` is not recommended.
   */
  readonly curl?: Text;
  /**
   * Duration of the audio creative in seconds.
   */
  readonly dur?: DurationSeconds;
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * Mime type(s) of the ad creative(s) (e.g., “audio/mp4”).
   */
  readonly mime?: readonly ExternalId[];
}

export interface AudioPlacement {
  /**
   * List of supported APIs for this placement. If an API is not explicitly listed, it is assumed to
   * be unsupported. Refer to List: API Frameworks.
   */
  readonly api?: readonly ApiFramework[];
  /**
   * Array of objects indicating that companion ads are available and providing the specifications
   * thereof. Refer to Object: Companion.
   */
  readonly comp?: readonly Companion[];
  /**
   * Supported companion ad types; recommended if companion ads are specified in `comp`. Refer to
   * List: Companion Types.
   */
  readonly comptype?: readonly CompanionType[];
  /**
   * Creative subtypes permitted for this placement. Refer to List: Creative Subtypes - Audio/Video.
   */
  readonly ctype?: readonly CreativeSubtypeAudioVideo[];
  /**
   * Indicates the start delay in seconds for pre-roll, mid-roll, or post-roll placements. For
   * additional generic values, refer to List: Start Delay Modes.
   */
  readonly delay?: StartDelayMode;
  /**
   * Array of supported creative delivery methods. If omitted, all can be assumed. Refer to List:
   * Delivery Methods.
   */
  readonly delivery?: readonly DeliveryMethod[];
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * Type of audio feed of this placement. Refer to List: Feed Types.
   */
  readonly feed?: FeedType;
  /**
   * Maximum bit rate of the creative in Kbps.
   */
  readonly maxbitr?: Count;
  /**
   * Maximum creative duration in seconds. This field is mutually exclusive with rqddurs; only one
   * of maxdur and rqddurs may be in a bid request.
   */
  readonly maxdur?: DurationSeconds;
  /**
   * Maximum extended creative duration if extension is allowed. If 0, extension is not allowed. If
   * -1, extension is allowed and there is no time limit imposed. If greater than 0, then the value
   * represents the number of seconds of extended play supported beyond the `maxdur` value.
   */
  readonly maxext?: ExtendedDuration;
  /**
   * The maximum number of ads that can be played in an ad pod.
   */
  readonly maxseq?: Count;
  /**
   * Array of supported mime types (e.g., “audio/mp4”). If omitted, all types are assumed.
   */
  readonly mime?: readonly ExternalId[];
  /**
   * Minimum bit rate of the creative in Kbps.
   */
  readonly minbitr?: Count;
  /**
   * Minimum CPM per second. This is a price floor for the “dynamic” portion of a video ad pod,
   * relative to the duration of bids an advertiser may submit.
   */
  readonly mincpmpersec?: Measure;
  /**
   * Minimum creative duration in seconds. This field is mutually exclusive with rqddurs; only one
   * of mindur and rqddurs may be in a bid request.
   */
  readonly mindur?: DurationSeconds;
  /**
   * Volume normalization mode of this placement. Refer to List: Volume Normalization Modes.
   */
  readonly nvol?: VolumeNormalizationMode;
  /**
   * Directions in which the creative (overlay) is permitted to expand. Refer to List: Expandable
   * Directions.
   */
  readonly overlayexpdir?: readonly ExpandableDirection[];
  /**
   * The event that causes playback to end for this placement. Refer to List: Playback Cessation
   * Modes.
   */
  readonly playend?: PlaybackCessationMode;
  /**
   * Playback method(s) in use for this placement. Refer to List: Playback Methods.
   */
  readonly playmethod?: readonly PlaybackMethod[];
  /**
   * Indicates the total amount of time in seconds that advertisers may fill for a “dynamic” video
   * ad pod, or the dynamic portion of a “hybrid” ad pod. This field is required only for the
   * dynamic portion(s) of video ad pods. This field refers to the length of the entire ad break,
   * whereas mindur/maxdur/rqddurs are constraints relating to the slots that make up the pod.
   */
  readonly poddur?: DurationSeconds;
  /**
   * Unique identifier indicating that an impression opportunity belongs to a video ad pod. If
   * multiple impression opportunities within a bid request share the same podid, this indicates
   * that those impression opportunities belong to the same video ad pod.
   */
  readonly podid?: IntegerId;
  /**
   * The sequence (position) of the video ad pod within a content stream. Refer to List: List: Pod
   * Sequence for guidance on the use of this field.
   *
   * @default 0
   */
  readonly podseq?: PodSequence;
  /**
   * Precise acceptable durations for video creatives in seconds. This field specifically targets
   * the Live TV use case where non-exact ad durations would result in undesirable 'dead air'. This
   * field is mutually exclusive with mindur and maxdur; if rqddurs is specified, mindur and maxdur
   * must not be specified and vice versa.
   */
  readonly rqddurs?: readonly DurationSeconds[];
  /**
   * Indicates if the placement imposes ad skippability, where 0 = no, 1 = yes.
   */
  readonly skip?: IntegerFlag;
  /**
   * Number of seconds a creative must play before the placement enables skipping; only applicable
   * if the ad is skippable.
   *
   * @default 0
   */
  readonly skipafter?: Count;
  /**
   * The placement allows creatives of total duration greater than this number of seconds to be
   * skipped; only applicable if the ad is skippable.
   *
   * @default 0
   */
  readonly skipmin?: DurationSeconds;
  /**
   * For video ad pods, this value indicates that the seller can guarantee delivery against the
   * indicated slot position in the pod. Refer to List: List: Slot Position in Pod for guidance on
   * the use of this field.
   *
   * @default 0
   */
  readonly slotinpod?: SlotPositionInPod;
}

export interface Audit {
  /**
   * Correction object wherein the auditor can specify changes to attributes of the `Ad` object or
   * its children they believe to be proper. For example, if the original `Ad` indicated a category
   * of “IAB3”, but the auditor deems the correct category to be “IAB13”, then `corr` could include
   * a sparse `Ad` object including just the `cat` array indicating “IAB13”.
   */
  readonly corr?: Corr;
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * One or more human-readable explanations as to reasons for rejection or any changes to fields
   * for ad quality reasons (e.g., `adomain`, `cat`, `attr`, etc.).
   */
  readonly feedback?: readonly Text[];
  /**
   * Timestamp of the original instantiation of this object in Unix format (i.e., milliseconds since
   * the epoch).
   */
  readonly init?: EpochMilliseconds;
  /**
   * Timestamp of most recent modification to this object in Unix format (i.e., milliseconds since
   * the epoch).
   */
  readonly lastmod?: EpochMilliseconds;
  /**
   * The audit status of the ad. Refer to List: Audit Status Codes.
   */
  readonly status?: AuditStatusCode;
}

export interface Banner {
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * A URL that will return the image.
   */
  readonly img: Text;
  /**
   * Destination link if the image is activated (e.g., clicked); not applicable in some contexts
   * (e.g., DOOH) and its inclusion does not guarantee it will be supported. Refer to Object:
   * LinkAsset.
   */
  readonly link?: LinkAsset;
}

export interface BrandVersion {
  /**
   * A brand identifier, for example, “Chrome” or “Windows”. The value may be sourced from the
   * User-Agent Client Hints headers, representing either the user agent brand (from the
   * Sec-CH-UA-Full-Version header) or the platform brand (from the Sec-CH-UA-Platform header).
   */
  readonly brand?: Text;
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * A sequence of version components, in descending hierarchical order (major, minor, micro, …)
   */
  readonly version?: readonly ExternalId[];
}

export interface Channel {
  /**
   * The primary domain of the channel (e.g., “abc7ny.com” in the case of the local channel
   * WABC-TV). It is recommended to include the top private domain (PSL+1) for DSP targeting
   * normalization purposes.
   */
  readonly domain?: Domain;
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * A unique identifier assigned by the publisher. This may not be a unique identifier across all
   * supply sources.
   */
  readonly id?: ExternalId;
  /**
   * Channel the content is on (e.g., a local channel like "WABC-TV").
   */
  readonly name?: Text;
}

export interface Companion {
  /**
   * Display specification object representing the companion ad. Refer to Object: DisplayPlacement.
   */
  readonly display?: DisplayPlacement;
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * Identifier of the companion ad; unique within this placement.
   */
  readonly id?: ExternalId;
  /**
   * Indicates the companion ad rendering mode relative to the associated video or audio ad, where 0
   * = concurrent, 1 = end-card. For a given placement, typically only one companion at most should
   * be designated as an end card.
   */
  readonly vcm?: IntegerFlag;
}

export interface Content {
  /**
   * Album to which the content belongs; typically for audio.
   */
  readonly album?: Text;
  /**
   * Artist credited with the content.
   */
  readonly artist?: Text;
  /**
   * Array of IAB Tech Lab content categories that describe the content. The taxonomy to be used is
   * defined by the cattax field. If no cattax field is supplied Content Category Taxonomy 1.0 is
   * assumed.
   */
  readonly cat?: readonly ExternalId[];
  /**
   * The taxonomy in use. Refer to list List: Category Taxonomies in AdCOM 1.0 for values.
   *
   * @default 1
   */
  readonly cattax?: CategoryTaxonomy;
  /**
   * Details about the channel (Section 3.2.24) the content is on.
   */
  readonly channel?: Channel;
  /**
   * Type of content (game, video, text, etc.). Refer to List: Content Contexts in AdCOM 1.0.
   */
  readonly context?: ContentContext;
  /**
   * Additional content data. Each `Data` object (Section 3.2.21) represents a different data
   * source.
   */
  readonly data?: readonly Data[];
  /**
   * Indicator of whether the content is embeddable (e.g., an embeddable video player), where 0 =
   * no, 1 = yes.
   */
  readonly embed?: IntegerFlag;
  /**
   * Episode number.
   */
  readonly episode?: Count;
  /**
   * Placeholder for vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * An enumeration indicating whether this broadcast is the first time the content is available to
   * an audience where: 0 = not first time being broadcast 1 = first time being broadcast
   */
  readonly firstbroadcast?: IntegerFlag;
  /**
   * Genre that best describes the content (e.g., rock, pop, etc).
   */
  readonly genre?: Text;
  /**
   * Unique ID(s) for the genre of the content as listed in the taxonomy defined by the gtax field.
   * If no gtax field is supplied, subset of rows listed in CTV Genre Mapping of Content Category
   * Taxonomy 3.1 are assumed. See Section 7.13 of Implementation Guidance for additional detail.
   */
  readonly genres?: readonly ExternalId[];
  /**
   * The taxonomy in use. Refer to list List: Category Taxonomies in AdCOM 1.0 for values. If no
   * gtax field is supplied rows listed, Content Category Taxonomy 3.1 is assumed
   *
   * @default 9
   */
  readonly gtax?: CategoryTaxonomy;
  /**
   * Publisher-provided ID uniquely identifying the content.
   */
  readonly id?: ExternalId;
  /**
   * International Standard Recording Code conforming to ISO- 3901.
   */
  readonly isrc?: ExternalId;
  /**
   * Comma separated list of keywords describing the content. Only one of `keywords` or `kwarray`
   * may be present.
   */
  readonly keywords?: Text;
  /**
   * Array of keywords about the site. Only one of `keywords` or `kwarray` may be present.
   */
  readonly kwarray?: readonly Text[];
  /**
   * Content language using ISO-639-1-alpha-2. Only one of `lang` or `langb` should be present.
   */
  readonly lang?: ExternalId;
  /**
   * Content language using IETF BCP 47. Only one of `lang` or `langb` should be present.
   */
  readonly langb?: ExternalId;
  /**
   * Length of content in seconds; appropriate for video or audio.
   */
  readonly len?: DurationSeconds;
  /**
   * An enumeration indicating the method of broadcast of the content where: 0 = the broadcast is
   * not scheduled (e.g. it is VOD or otherwise user initiated). 1 = the broadcast is scheduled
   * (also referred to as linear viewing).
   */
  readonly live?: IntegerFlag;
  /**
   * Media rating per IQG guidelines. Refer to List: Media Ratings in AdCOM 1.0.
   */
  readonly mrating?: MediaRating;
  /**
   * Details about the network (Section 3.2.23) the content is on.
   */
  readonly network?: Network;
  /**
   * Production quality. Refer to List: Production Qualities in AdCOM 1.0.
   */
  readonly prodq?: ProductionQuality;
  /**
   * Details about the content `Producer` (Section 3.2.17).
   */
  readonly producer?: Producer;
  /**
   * Content rating (e.g., MPAA).
   */
  readonly rating?: Text;
  /**
   * An enumeration indicating if the event is happening in real time while it is being watched
   * where: 0 = not happening in real time (e.g., a replay). 1 = yes, happening in real time (e.g.,
   * a live sports game).
   */
  readonly realtime?: IntegerFlag;
  /**
   * Content season (e.g., “Season 3”).
   */
  readonly season?: Text;
  /**
   * Content series. Video Examples: “The Office” (television), “Star Wars” (movie), or “Arby ‘N’
   * The Chief” (made for web). Non-Video Example: “Ecocentric” (Time Magazine blog).
   */
  readonly series?: Text;
  /**
   * 0 = indirect, 1 = direct.
   */
  readonly srcrel?: IntegerFlag;
  /**
   * Content title. Video Examples: “Search Committee” (television), “A New Hope” (movie), or
   * “Endgame” (made for web). Non-Video Example: “Why an Antarctic Glacier Is Melting So Quickly”
   * (Time magazine article).
   */
  readonly title?: Text;
  /**
   * User rating of the content (e.g., number of stars, likes, etc.).
   */
  readonly urating?: Text;
  /**
   * URL of the content, for buy-side contextualization or review.
   */
  readonly url?: Text;
}

/**
 * Its content is set by the `Ad` object and its children, of which it carries the attributes the
 * auditor states are proper, so a correction is a sparse `Ad` (Object: Audit, `corr`)
 */
export interface Corr {
  /**
   * The members the specification leaves to the parties to define. This node states no
   * `additionalProperties: false`, so a member it does not name is admitted and a receiver keeps
   * it.
   */
  readonly [member: string]: unknown;
}

export interface Data {
  /**
   * An array of Extended Content IDs, representing one or more identifiers for the video or audio
   * content from the ID source specified in the `name` field of the `data` object.
   */
  readonly cids?: readonly ExternalId[];
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * Vendor-specific ID for the data provider.
   */
  readonly id?: ExternalId;
  /**
   * Vendor-specific displayable name for the data provider.
   */
  readonly name?: Text;
  /**
   * Array of `Segment` objects that contain the actual data values. Refer to Object: Segment.
   */
  readonly segment?: readonly Segment[];
}

export interface DataAsset {
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * The length of the `value` contents. This length should conform to recommendations provided in
   * List: Native Data Asset Types
   */
  readonly len?: Count;
  /**
   * The type of data represented by this asset. Refer to List: Native Data Asset Types.
   */
  readonly type?: NativeDataAssetType;
  /**
   * A formatted string of data to be displayed (e.g., “5 stars”, “3.4 stars out of 5”, “$10”,
   * etc.).
   */
  readonly value: Text;
}

export interface DataAssetFormat {
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * The maximum allowed length of the data value.
   */
  readonly len?: Count;
  /**
   * The type of data asset supported. Refer to List: Native Data Asset Types.
   */
  readonly type: NativeDataAssetType;
}

export interface Device {
  /**
   * Carrier or ISP (e.g., “VERIZON”) using exchange curated string names which should be published
   * to bidders beforehand.
   */
  readonly carrier?: Text;
  /**
   * Network connection type. Refer to List: Connection Types.
   */
  readonly contype?: ConnectionType;
  /**
   * Standard “Do Not Track” flag as set in the header by the browser, where 0 = tracking is
   * unrestricted, 1 = do not track.
   */
  readonly dnt?: IntegerFlag;
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * Location of the device (i.e., typically the user's current location). Refer to Object: Geo.
   */
  readonly geo?: Geo;
  /**
   * Indicates if the geolocation API will be available to JavaScript code running in display ad,
   * where 0 = no, 1 = yes.
   */
  readonly geofetch?: IntegerFlag;
  /**
   * Physical height of the screen in pixels.
   */
  readonly h?: Count;
  /**
   * Hardware version of the device (e.g., “5S” for iPhone 5S).
   */
  readonly hwv?: ExternalId;
  /**
   * ID sanctioned for advertiser use in the clear (i.e., not hashed).
   */
  readonly ifa?: ExternalId;
  /**
   * IPv4 address closest to device.
   */
  readonly ip?: ExternalId;
  /**
   * Indicator of truncation of any of the IP attributes (i.e., `ip`, `ipv6`, `xff`), where 0 = no,
   * 1 = yes (e.g., from 1.2.3.4 to 1.2.3.0). Refer to
   * https://tools.ietf.org/html/rfc6235#section-4.1.1 for more information on IP truncation.
   */
  readonly iptr?: IntegerFlag;
  /**
   * IP address closest to device as IPv6.
   */
  readonly ipv6?: ExternalId;
  /**
   * Support for JavaScript, where 0 = no, 1 = yes.
   */
  readonly js?: IntegerFlag;
  /**
   * Browser language using ISO-639-1-alpha-2. Only one of lang or langb should be present.
   */
  readonly lang?: ExternalId;
  /**
   * Browser language using IETF BCP 47. Only one of lang or langb should be present.
   */
  readonly langb?: ExternalId;
  /**
   * “Limit Ad Tracking” signal commercially endorsed (e.g., iOS, Android), where 0 = tracking is
   * unrestricted, 1 = tracking must be limited per commercial guidelines.
   */
  readonly lmt?: IntegerFlag;
  /**
   * Device make (e.g., "Apple").
   */
  readonly make?: Text;
  /**
   * Mobile carrier as the concatenated MCC-MNC code (e.g., “310-005” identifies Verizon Wireless
   * CDMA in the USA). Refer to https://en.wikipedia.org/wiki/Mobile_country_code for further
   * information and references. Note that the dash between the MCC and MNC parts is required to
   * remove parsing ambiguity. The MCC-MNC values represent the SIM installed on the device and do
   * not change when a device is roaming. Roaming may be inferred by a combination of the MCC-MNC,
   * geo, IP and other data signals.
   */
  readonly mccmnc?: ExternalId;
  /**
   * MCC and MNC of the SIM card using the same format as `mccmnc`. When both values are available,
   * a difference between them reveals that a user is roaming.
   */
  readonly mccmncsim?: ExternalId;
  /**
   * Device model (e.g., “iPhone10,1” when the specific device model is known, “iPhone” otherwise).
   * The value obtained from the device O/S should be used when available.
   */
  readonly model?: Text;
  /**
   * Device operating system. Refer to List: Operating Systems.
   */
  readonly os?: OperatingSystem;
  /**
   * Device operating system version (e.g., “3.1.2”).
   */
  readonly osv?: ExternalId;
  /**
   * Screen size as pixels per linear inch.
   */
  readonly ppi?: Count;
  /**
   * The ratio of physical pixels to device independent pixels.
   */
  readonly pxratio?: Measure;
  /**
   * Structured user agent information defined by a Object: UserAgent. If both `ua` and `sua` are
   * present in the bid request, `sua` should be considered the more accurate representation of the
   * device attributes. This is because the `ua` may contain a frozen or reduced UserAgent string.
   */
  readonly sua?: UserAgent;
  /**
   * The general type of device. Refer to List: Device Types.
   */
  readonly type?: DeviceType;
  /**
   * Browser user agent string. This field represents a raw user agent string from the browser. For
   * backwards compatibility, exchanges are recommended to always populate `ua` with the User-Agent
   * string, when available from the end user’s device, even if an alternative representation, such
   * as the User-Agent Client-Hints, is available and gets used to populate `sua`. No inferred or
   * approximated user agents are expected in this field. If both `ua` and `sua` are present in the
   * bid request, `sua` should be considered the more accurate representation of the device
   * attributes. This is because the `ua` may contain a frozen or reduced UserAgent string.
   */
  readonly ua?: Text;
  /**
   * Physical width of the screen in pixels.
   */
  readonly w?: Count;
  /**
   * The value of the “x-forwarded-for” header.
   */
  readonly xff?: ExternalId;
}

export interface Display {
  /**
   * General display markup (e.g., HTML, AMPHTML) if not using a structured alternative (e.g.,
   * `banner`, `native`). Note that including both `adm` and `curl` is not recommended.
   */
  readonly adm?: Text;
  /**
   * API required by the ad if applicable. Refer to List: API Frameworks.
   */
  readonly api?: readonly ApiFramework[];
  /**
   * Structured banner image object, recommended for simple banner creatives. Refer to Object:
   * Banner.
   */
  readonly banner?: Banner;
  /**
   * Subtype of display creative. Refer to List: Creative Subtypes - Display.
   */
  readonly ctype?: CreativeSubtypeDisplay;
  /**
   * Optional means of retrieving display markup by reference; a URL that can return HTML, AMPHTML,
   * or a collection native `Asset` object and their subordinates). If this ad is matched to a
   * Placement specification, the `Placement.curlx` attribute indicates if this markup retrieval
   * option is supported. Note that including both `adm` and `curl` is not recommended.
   */
  readonly curl?: Text;
  /**
   * Array of events that the advertiser or buying platform wants to track. Refer to Object: Event.
   */
  readonly event?: readonly Event[];
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * Absolute height of the creative in device independent pixels (DIPS), typically for non-native
   * ads. Note that mixing absolute and relative sizes is not recommended.
   */
  readonly h?: Count;
  /**
   * Relative height of the creative when expressing size as a ratio, typically for non-native ads.
   * Note that mixing absolute and relative sizes is not recommended.
   */
  readonly hratio?: Count;
  /**
   * Mime type of the ad (e.g., “image/jpeg”).
   */
  readonly mime?: ExternalId;
  /**
   * Structured native object, recommended for native ads. Refer to Object: Native.
   */
  readonly native?: Native;
  /**
   * URL of a page informing the user about a buyer's targeting activity.
   */
  readonly priv?: Text;
  /**
   * Absolute width of the creative in device independent pixels (DIPS), typically for non-native
   * ads. Note that mixing absolute and relative sizes is not recommended.
   */
  readonly w?: Count;
  /**
   * Relative width of the creative when expressing size as a ratio, typically for non-native ads.
   * Note that mixing absolute and relative sizes is not recommended.
   */
  readonly wratio?: Count;
}

export interface DisplayFormat {
  /**
   * Directions in which the creative is permitted to expand. Refer to List: Expandable Directions.
   */
  readonly expdir?: readonly ExpandableDirection[];
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * Absolute height of the creative in units specified by `DisplayPlacement.unit`. Note that mixing
   * absolute and relative sizes is not recommended.
   */
  readonly h?: Count;
  /**
   * Relative height of the creative when expressing size as a ratio. Note that mixing absolute and
   * relative sizes is not recommended.
   */
  readonly hratio?: Count;
  /**
   * Absolute width of the creative in units specified by `DisplayPlacement.unit`. Note that mixing
   * absolute and relative sizes is not recommended.
   */
  readonly w?: Count;
  /**
   * Relative width of the creative when expressing size as a ratio. Note that mixing absolute and
   * relative sizes is not recommended.
   */
  readonly wratio?: Count;
}

export interface DisplayPlacement {
  /**
   * AMPHTML rendering treatment for AMP ads in this placement, where 1 = early loading, 2 =
   * standard loading.
   */
  readonly ampren?: AmpRenderingTreatment;
  /**
   * List of supported APIs. If an API is not explicitly listed, it is assumed to be unsupported.
   * Refer to List: API Frameworks.
   */
  readonly api?: readonly ApiFramework[];
  /**
   * Indicates the click type of this placement. Refer to List: Click Types.
   *
   * @default 1
   */
  readonly clktype?: ClickType;
  /**
   * The context of the placement. Refer to List: Display Context Types.
   */
  readonly context?: DisplayContextType;
  /**
   * Creative subtypes permitted. Refer to List: Creative Subtypes - Display.
   */
  readonly ctype?: readonly CreativeSubtypeDisplay[];
  /**
   * Array of objects that govern the attributes (e.g., sizes) of a banner display placement. Refer
   * to Object: DisplayFormat.
   */
  readonly displayfmt?: readonly DisplayFormat[];
  /**
   * Array of supported ad tracking events. Refer to Object: EventSpec.
   */
  readonly event?: readonly EventSpec[];
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * Width of the placement in units specified by `unit`. Note that this size applies to the
   * placement itself; permitted creative sizes are specified elsewhere (e.g., `DisplayFormat`,
   * `ImageAssetFormat`, etc.).
   */
  readonly h?: Count;
  /**
   * Array of iframe busters supported by this placement. The meaning of strings in this attribute
   * must be coordinated beforehand among vendors.
   */
  readonly ifrbust?: readonly ExternalId[];
  /**
   * Indicates if this is an interstitial placement, where 0 = no, 1 = yes.
   *
   * @default 0
   */
  readonly instl?: IntegerFlag;
  /**
   * Array of supported mime types (e.g., “image/jpeg”, “image/gif”). If omitted, all types are
   * assumed.
   */
  readonly mime?: readonly ExternalId[];
  /**
   * This object specified the required and permitted assets and attributes of a native display
   * placement. Refer to Object: NativeFormat.
   */
  readonly nativefmt?: NativeFormat;
  /**
   * Placement position on screen. Refer to List: Placement Positions.
   */
  readonly pos?: PlacementPosition;
  /**
   * Indicator of whether or not the placement supports a buyer-specific privacy notice URL, where 0
   * = no, 1 = yes.
   *
   * @default 0
   */
  readonly priv?: IntegerFlag;
  /**
   * The display placement type. Refer to List: Display Placement Types.
   */
  readonly ptype?: DisplayPlacementType;
  /**
   * Indicates if the placement will be loaded into an iframe or not, where 0 = unfriendly iframe or
   * unknown, 1 = top frame, friendly iframe, or SafeFrame. A value of "1" can be understood to mean
   * that expandable ads are technically capable of being delivered.
   */
  readonly topframe?: IntegerFlag;
  /**
   * Unit of size used for placement size (i.e., `w` and `h` attributes). Refer to List: Size Units.
   *
   * @default 1
   */
  readonly unit?: SizeUnit;
  /**
   * Width of the placement in units specified by `unit`. Note that this size applies to the
   * placement itself; permitted creative sizes are specified elsewhere (e.g., `DisplayFormat`,
   * `ImageAssetFormat`, etc.).
   */
  readonly w?: Count;
}

export interface Dooh {
  /**
   * Details about the content within the distribution channel. Refer to Object: Content.
   */
  readonly content?: Content;
  /**
   * Minimum DPI for text-based creative elements to display clearly.
   */
  readonly dpi?: Count;
  /**
   * The exposure time in seconds per view that the creative will be displayed before refreshing to
   * the next creative.
   */
  readonly etime?: DurationSeconds;
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * Indicates whether the DOOH placement is in a fixed location (e.g., kiosk, billboard, elevator)
   * or is movable (e.g., taxi), where 1 = fixed, 2 = movable.
   */
  readonly fixed?: DoohPlacementMobility;
  /**
   * Vendor-specific unique identifier of the distribution channel.
   */
  readonly id?: ExternalId;
  /**
   * Displayable name of the distribution channel.
   */
  readonly name?: Text;
  /**
   * Details about the publisher of the distribution channel. Refer to Object: Publisher.
   */
  readonly pub?: Publisher;
  /**
   * The type of out-of-home venue. Refer to List: DOOH Venue TypesList: DOOH Venue Types.
   */
  readonly venue?: Count;
}

/**
 * Dooh Placement Mobility
 *
 * The codes of `Dooh.fixed`, each with the label the text gives it
 */
export type DoohPlacementMobility = 1 | 2;

/**
 * The codes of DoohPlacementMobility, each under the name the published schema carries for it.
 */
export const DoohPlacementMobilityCodes = {
  /**
   * fixed
   */
  FIXED: 1,
  /**
   * movable
   */
  MOVABLE: 2,
} as const satisfies Readonly<Record<string, DoohPlacementMobility>>;

export interface Event {
  /**
   * The APIs being used by the tracker; only relevant when the tracking method is JavaScript. Refer
   * to List: API Frameworks.
   */
  readonly api?: readonly ApiFramework[];
  /**
   * An array of key-value pairs to support vendor-specific data required for custom tracking. For
   * example, the account number of a buyer with a tracking company might be represented as:
   * {"acct": "123"}.
   */
  readonly cdata?: Ext;
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * Method of tracking requested. Refer to List: Event Tracking Methods.
   */
  readonly method: EventTrackingMethod;
  /**
   * Type of event to track. Refer to List: Event Types.
   */
  readonly type: EventType;
  /**
   * The URL of the tracking pixel or JavaScript tag, respectively. * Required for Image-Pixel or
   * JavaScript methods.
   */
  readonly url?: Text;
}

export interface EventSpec {
  /**
   * Event tracking APIs available for use; only relevant for JavaScript method trackers. Refer to
   * List: API Frameworks.
   */
  readonly api?: readonly ApiFramework[];
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * Array of domains, top two levels only (e.g., “tracker.com”), that constitute a restriction list
   * of JavaScript trackers. The sense of the restrictions is determined by `wjs`.
   */
  readonly jstrk?: readonly Domain[];
  /**
   * Array of supported event tracking methods for this event type. Refer to List: Event Tracking
   * Methods.
   */
  readonly method?: readonly EventTrackingMethod[];
  /**
   * Array of domains, top two levels only (e.g., “tracker.com”), that constitute a restriction list
   * of pixel image trackers. The sense of the restrictions is determined by `wpx`.
   */
  readonly pxtrk?: readonly Domain[];
  /**
   * Type of supported ad tracking event. Refer to List: Event Types.
   */
  readonly type: EventType;
  /**
   * Sense of the `jstrk` restriction list, where 0 = block list, 1 = allow list.
   *
   * @default 1
   */
  readonly wjs?: IntegerFlag;
  /**
   * Sense of the `pxtrk` restriction list, where 0 = block list, 1 = allow list.
   *
   * @default 1
   */
  readonly wpx?: IntegerFlag;
}

export interface ExtendedIdentifierUids {
  /**
   * Type of user agent the match is from. It is highly recommended to set this, as many DSPs
   * separate app-native IDs from browser-based IDs and require a type value for ID resolution.
   * Refer to List: Agent Types.
   */
  readonly atype?: AgentType;
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * Cookie or platform-native identifier.
   */
  readonly id?: ExternalId;
}

export interface ExtendedIdentifiers {
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * The canonical domain name of the entity (publisher, publisher monetization company, SSP,
   * Exchange, Header Wrapper, etc.) that caused the ID array element to be added. This may be the
   * operational domain of the system, if that is different from the parent corporate domain, to
   * facilitate WHOIS and reverse IP lookups to establish clear ownership of the delegate system.
   * This should be the same value as used to identify sellers in an ads.txt file if one exists. For
   * ad tech intermediaries, this would be the domain as used in ads.txt. For publishers, this would
   * match the domain in the `site` or `app` object.
   */
  readonly inserter?: Domain;
  /**
   * Technology providing the match method as defined in `mm`. In some cases, this may be the same
   * value as inserter. When blank, it is assumed that the `matcher` is equal to the `source` May be
   * omitted when mm=0, 1, or 2.
   */
  readonly matcher?: Text;
  /**
   * Match method used by the `matcher`. Refer to List: ID Match Methods.
   */
  readonly mm?: IdMatchMethod;
  /**
   * Source domain of the UID provider. Should be the root domain name of the provider, not the URL.
   * For example, "liveramp.com" not "https://liveramp.com/connect"
   */
  readonly source?: Domain;
  /**
   * Array of extended ID UID objects from the given `source`. Refer to Object: Extended Identifier
   * UIDs.
   */
  readonly uids?: readonly ExtendedIdentifierUids[];
}

export interface Geo {
  /**
   * Estimated location accuracy in meters; recommended when lat/lon are specified and derived from
   * a device's location services (i.e., type = 1). Note that this is the accuracy as reported from
   * the device. Consult OS specific documentation (e.g., Android, iOS) for exact interpretation.
   */
  readonly accur?: Count;
  /**
   * City using United Nations Code for Trade & Transport Locations “UN/LOCODE” with the space
   * between country and city suppressed (e.g., Boston MA, USA = “USBOS”). Refer to UN/LOCODE Code
   * List.
   */
  readonly city?: ExternalId;
  /**
   * Country code using ISO-3166-1-alpha-2. Note that alpha-3 codes may be encountered and vendors
   * are encouraged to be tolerant of them.
   */
  readonly country?: ExternalId;
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * Service or provider used to determine geolocation from IP address if applicable (i.e., `type` =
   * 2). Refer to List: IP Location Services.
   */
  readonly ipserv?: IpLocationService;
  /**
   * Number of seconds since this geolocation fix was established. Note that devices may cache
   * location data across multiple fetches. Ideally, this value should be from the time the actual
   * fix was taken.
   */
  readonly lastfix?: Count;
  /**
   * Latitude from -90.0 to +90.0, where negative is south.
   */
  readonly lat?: Degrees;
  /**
   * Longitude from -180.0 to +180.0, where negative is west.
   */
  readonly lon?: Degrees;
  /**
   * Regional marketing areas such as Nielsen's DMA codes or other similar taxonomy to be agreed
   * among vendors prior to use. Note that DMA is a trademarked asset of The Nielsen Company.
   * Vendors are encouraged to ensure their use of DMAs is properly licensed.
   */
  readonly metro?: ExternalId;
  /**
   * Region code using ISO-3166-2; 2-letter state code if USA.
   */
  readonly region?: ExternalId;
  /**
   * Source of location data; recommended when passing lat/lon. Refer to List: Location Types.
   */
  readonly type?: LocationType;
  /**
   * Local time as the number +/- of minutes from UTC.
   */
  readonly utcoffset?: MinuteOffset;
  /**
   * ZIP or postal code.
   */
  readonly zip?: ExternalId;
}

export interface ImageAsset {
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * Height of the image asset in device independent pixels (DIPS).
   */
  readonly h?: Count;
  /**
   * The type of image represented by this asset. Refer to List: Native Image Asset Types.
   */
  readonly type?: NativeImageAssetType;
  /**
   * A URL that returns the image for the asset.
   */
  readonly url: Text;
  /**
   * Width of the image asset in device independent pixels (DIPS).
   */
  readonly w?: Count;
}

export interface ImageAssetFormat {
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * Absolute height of the image asset in device independent pixels (DIPS). Note that mixing
   * absolute and relative sizes is not recommended.
   */
  readonly h?: Count;
  /**
   * The minimum requested absolute height of the image in device independent pixels (DIPS). This
   * option should be used for any scaling of images by the client.
   */
  readonly hmin?: Count;
  /**
   * Relative height of the image asset when expressing size as a ratio. Note that mixing absolute
   * and relative sizes is not recommended.
   */
  readonly hratio?: Count;
  /**
   * Array of supported mime types (e.g., “image/jpeg”, “image/gif”). If omitted, all types are
   * assumed.
   */
  readonly mime?: readonly ExternalId[];
  /**
   * The type of image asset supported. Refer to List: Native Image Asset Types.
   */
  readonly type?: NativeImageAssetType;
  /**
   * Absolute width of the image asset in device independent pixels (DIPS). Note that mixing
   * absolute and relative sizes is not recommended.
   */
  readonly w?: Count;
  /**
   * The minimum requested absolute width of the image in device independent pixels (DIPS). This
   * option should be used for any scaling of images by the client.
   */
  readonly wmin?: Count;
  /**
   * Relative width of the image asset when expressing size as a ratio. Note that mixing absolute
   * and relative sizes is not recommended.
   */
  readonly wratio?: Count;
}

export interface LinkAsset {
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * List of third-party tracker URLs to be fired on click.
   */
  readonly trkr?: readonly Text[];
  /**
   * Landing URL of the clickable link.
   */
  readonly url: Text;
  /**
   * Fallback URL for deep-link to be used if the URL specified in `url` is not supported by the
   * device.
   */
  readonly urlfb?: Text;
}

export interface Native {
  /**
   * Array of assets that comprise the native ad. Refer to Object: Asset.
   */
  readonly asset?: readonly Asset[];
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * Default destination link for the native ad overall; used if an asset is activated (e.g.,
   * clicked) that doesn't specify it's own destination link. Refer to Object: LinkAsset.
   */
  readonly link?: LinkAsset;
}

export interface NativeFormat {
  /**
   * Array of objects that specify the set of native assets and their permitted formats. Refer to
   * Object: AssetFormat.
   */
  readonly asset: readonly AssetFormat[];
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
}

export interface Network {
  /**
   * The primary domain of the network (e.g., “abc.com” in the case of the network ABC). It is
   * recommended to include the top private domain (PSL+1) for DSP targeting normalization purposes.
   */
  readonly domain?: Domain;
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * A unique identifier assigned by the publisher. This may not be a unique identifier across all
   * supply sources.
   */
  readonly id?: ExternalId;
  /**
   * Network the content is on (e.g., a TV network like "ABC").
   */
  readonly name?: Text;
}

export interface Placement {
  /**
   * Indicates if including markup is supported (i.e., the various `adm` attributes throughout the
   * `Placement` structure), where 0 = no, 1 = yes.
   */
  readonly admx?: IntegerFlag;
  /**
   * Placement Subtype Object that indicates that this may be an audio placement and provides
   * additional detail related thereto. Refer to Object: AudioPlacement. * At least one placement
   * subtype object is required.
   */
  readonly audio?: AudioPlacement;
  /**
   * Indicates if retrieving markup via URL reference is supported (i.e., the various `curl`
   * attributes throughout the `Placement` structure), where 0 = no, 1 = yes.
   */
  readonly curlx?: IntegerFlag;
  /**
   * Placement Subtype Object that indicates that this may be a display placement and provides
   * additional detail related thereto. Refer to Object: DisplayPlacement. * At least one placement
   * subtype object is required.
   */
  readonly display?: DisplayPlacement;
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * Indicates whether the user recieves a reward for viewing the ad, where 0 = no, 1 = yes.
   * Typcially video ad implementations allow users to read an additional news article for free,
   * receive an extra life in a game, or get a sponsored ad-free music session. The reward is
   * typically distributed after the video ad is completed.
   *
   * @default 0
   */
  readonly reward?: IntegerFlag;
  /**
   * Name of ad mediation partner, SDK technology, or player responsible for rendering ad (typically
   * video, audio, or mobile); used by some ad servers to customize ad code by partner.
   */
  readonly sdk?: Text;
  /**
   * Version of the SDK specified in the `sdk` attribute.
   */
  readonly sdkver?: ExternalId;
  /**
   * Flag to indicate if the creative is secure (i.e., uses HTTPS for all assets and markup), where
   * 0 = no, 1 = yes. There is no default and thus if omitted, the secure state is unknown. However,
   * as a practical matter, the safe assumption is to treat unknown as non-secure.
   */
  readonly secure?: IntegerFlag;
  /**
   * Indicates if server-side ad insertion (e.g., stitching an ad into an audio or video stream) is
   * in use and the impact of this on asset and tracker retrieval, where 0 = status unknown, 1 = all
   * client-side (i.e., not server-side), 2 = assets stitched server-side but tracking pixels fired
   * client-side, 3 = all server-side.
   *
   * @default 0
   */
  readonly ssai?: ServerSideAdInsertionMode;
  /**
   * Identifier for specific ad placement or ad tag; unique within a distribution channel.
   */
  readonly tagid?: ExternalId;
  /**
   * Placement Subtype Object that indicates that this may be a video placement and provides
   * additional detail related thereto. Refer to Object: VideoPlacement. * At least one placement
   * subtype object is required.
   */
  readonly video?: VideoPlacement;
  /**
   * Allow list of permitted languages of the creative using ISO-639-1-alpha-2. In practice, vendors
   * using this object may elect an alternate standard (e.g., BCP-47) in which case this must be
   * communicated beforehand. Omission of this attribute indicates there are no restrictions.
   */
  readonly wlang?: readonly ExternalId[];
}

export interface Producer {
  /**
   * Array of content categories that describe the producer using IDs from the taxonomy indicated in
   * `cattax`.
   */
  readonly cat?: readonly ExternalId[];
  /**
   * The taxonomy in use for the `cat` attribute. Refer to List: Category Taxonomies.
   */
  readonly cattax?: CategoryTaxonomy;
  /**
   * Highest level domain of the producer (e.g., “producer.com”).
   */
  readonly domain?: Domain;
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * Vendor-specific unique producer identifier. Useful if content is syndicated and may be posted
   * on a site using embed tags.
   */
  readonly id?: ExternalId;
  /**
   * Displayable name of the producer.
   */
  readonly name?: Text;
}

export interface Publisher {
  /**
   * Array of content categories that describe the publisher using IDs from the taxonomy indicated
   * in `cattax`. Implementer should ensure compliance with regional legislation around data usage
   * and sharing.
   */
  readonly cat?: readonly ExternalId[];
  /**
   * The taxonomy in use for the `cat` attribute. Refer to
   * ![image](https://github.com/InteractiveAdvertisingBureau/AdCOM/assets/114763292/e80e72e1-e099-4aff-b466-a5e91eb9f62f).
   */
  readonly cattax?: CategoryTaxonomy;
  /**
   * Highest level domain of the publisher (e.g., “publisher.com”).
   */
  readonly domain?: Domain;
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * Vendor-specific unique publisher identifier, as used in ads.txt files.
   */
  readonly id?: ExternalId;
  /**
   * Displayable name of the publisher.
   */
  readonly name?: Text;
}

export interface Regs {
  /**
   * Flag indicating if COPPA regulations apply, where 0 = no, 1 = yes. The Children's Online
   * Privacy Protection Act (COPPA) was established by the U.S. Federal Trade Commission.
   */
  readonly coppa?: IntegerFlag;
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * Flag indicating if GDPR regulations apply, where 0 = no, 1 = yes. The General Data Protection
   * Regulation (GDPR) is a regulation of the European Union.
   */
  readonly gdpr?: IntegerFlag;
  /**
   * Contains the Global Privacy Platform’s consent string. See the Global Privacy Platform
   * specification for more details.
   */
  readonly gpp?: ExternalId;
  /**
   * Array of the section(s) of the string which should be applied for this transaction. Generally
   * will contain one and only one value, but there are edge cases where more than one may apply.
   * GPP Section 3 (Header) and 4 (Signal Integrity) do not need to be included. See the GPP Section
   * Information for more details.
   */
  readonly gpp_sid?: readonly Count[];
}

export interface Restrictions {
  /**
   * Allowed content categories using IDs from the taxonomy indicated in `cattax`. Only one of
   * `acat` or `bcat` should be present.
   */
  readonly acat?: readonly ExternalId[];
  /**
   * Block list of advertisers by their domains (e.g., “ford.com”).
   */
  readonly badv?: readonly Domain[];
  /**
   * Block list of apps for which ads are disallowed. These should be bundle or package names (e.g.,
   * “com.foo.mygame”) and should NOT be app store IDs (e.g., not iTunes store IDs).
   */
  readonly bapp?: readonly ExternalId[];
  /**
   * Block list of creative attributes. Refer to List: Creative Attributes.
   */
  readonly battr?: readonly CreativeAttribute[];
  /**
   * Block list of content categories using IDs from the taxonomy indicated in `cattax`. Only one of
   * `acat` or `bcat` should be present.
   */
  readonly bcat?: readonly ExternalId[];
  /**
   * The taxonomy in use for the `bcat` attribute. Refer to List: Category Taxonomies.
   *
   * @default 2
   */
  readonly cattax?: CategoryTaxonomy;
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
}

export interface Segment {
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * ID of the data segment specific to the data provider.
   */
  readonly id?: ExternalId;
  /**
   * Displayable name of the data segment specific to the data provider.
   */
  readonly name?: Text;
  /**
   * String representation of the data segment value.
   */
  readonly value?: Text;
}

/**
 * Server Side Ad Insertion Mode
 *
 * The codes of `Placement.ssai`, each with the label the text gives it
 */
export type ServerSideAdInsertionMode = 0 | 1 | 2 | 3;

/**
 * The codes of ServerSideAdInsertionMode, each under the name the published schema carries for it.
 */
export const ServerSideAdInsertionModeCodes = {
  /**
   * status unknown
   */
  STATUS_UNKNOWN: 0,
  /**
   * all client-side
   *
   * all client-side (i.e., not server-side)
   */
  ALL_CLIENT_SIDE: 1,
  /**
   * assets stitched server-side but tracking pixels fired client-side
   */
  ASSETS_STITCHED_SERVER_SIDE_BUT_TRACKING_PIXELS: 2,
  /**
   * all server-side
   */
  ALL_SERVER_SIDE: 3,
} as const satisfies Readonly<Record<string, ServerSideAdInsertionMode>>;

export interface Site {
  /**
   * Indicates if the page is built with AMP HTML, where 0 = no, 1 = yes.
   */
  readonly amp?: IntegerFlag;
  /**
   * Array of content categories describing the site using IDs from the taxonomy indicated in
   * `cattax`.
   */
  readonly cat?: readonly ExternalId[];
  /**
   * The taxonomy in use for the `cat`, `sectcat` and `pagecat` attributes. Refer to List: Category
   * Taxonomies.
   */
  readonly cattax?: CategoryTaxonomy;
  /**
   * Details about the content within the distribution channel. Refer to Object: Content.
   */
  readonly content?: Content;
  /**
   * Domain of the site (e.g., “mysite.foo.com”).
   */
  readonly domain?: Domain;
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * Vendor-specific unique identifier of the distribution channel.
   */
  readonly id?: ExternalId;
  /**
   * This field is deprecated, use 'kwarray' instead.
   */
  readonly keywords?: Text;
  /**
   * Array of keywords about the site. Only one of 'keywords' or 'kwarray' may be present.
   */
  readonly kwarray?: readonly Text[];
  /**
   * Indicates if the site has been programmed to optimize layout when viewed on mobile devices,
   * where 0 = no, 1 = yes.
   */
  readonly mobile?: IntegerFlag;
  /**
   * Displayable name of the distribution channel.
   */
  readonly name?: Text;
  /**
   * URL of the page within the site.
   */
  readonly page?: Text;
  /**
   * Array of content categories describing the current page or view of the site using IDs from the
   * taxonomy indicated in `cattax`.
   */
  readonly pagecat?: readonly ExternalId[];
  /**
   * Indicates if the site has a privacy policy, where 0 = no, 1 = yes.
   */
  readonly privpolicy?: IntegerFlag;
  /**
   * Details about the publisher of the distribution channel. Refer to Object: Publisher.
   */
  readonly pub?: Publisher;
  /**
   * Referrer URL that caused navigation to the current page.
   */
  readonly ref?: Text;
  /**
   * Search string that caused navigation to the current page.
   */
  readonly search?: Text;
  /**
   * Array of content categories describing the current section of the site using IDs from the
   * taxonomy indicated in `cattax`.
   */
  readonly sectcat?: readonly ExternalId[];
}

export interface TitleAsset {
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * The length of the contents of the `text` attribute.
   */
  readonly len?: Count;
  /**
   * The text content of the text element.
   */
  readonly text: Text;
}

export interface TitleAssetFormat {
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * The maximum allowed length of the title value. Recommended lengths are 25, 90, or 140.
   */
  readonly len: Count;
}

export interface User {
  /**
   * Buyer-specific ID for the user as mapped by an exchange for the buyer. At least one of `id` or
   * `buyeruid` is strongly recommended. Unless prior arrangements have been made between the buyer
   * and the seller directly, the value in this field is expected to be derived from an ID sync.
   * (see [Appendix: Cookie Based ID
   * Syncing)](https://github.com/InteractiveAdvertisingBureau/openrtb2.x/blob/main/2.6.md#appendixc)
   */
  readonly buyeruid?: ExternalId;
  /**
   * GDPR consent string if applicable, complying with the comply with the IAB standard Consent
   * String Format in the Transparency and Consent Framework technical specifications.
   */
  readonly consent?: ExternalId;
  /**
   * Additional user data. Each `Data` object represents a different data source. Refer to Object:
   * Data.
   */
  readonly data?: readonly Data[];
  /**
   * Extended (third-party) identifiers for this user. Refer to Object: Extended Identifiers.
   */
  readonly eids?: readonly ExtendedIdentifiers[];
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * Deprecated as of OpenRTB 2.6
   */
  readonly gender?: Text;
  /**
   * Location of the user's home base (i.e., not necessarily their current location). Refer to
   * Object: Geo.
   */
  readonly geo?: Geo;
  /**
   * Exchange-specific ID for the user At least one of `id` or `buyeruid` is strongly recommended.
   * Unless prior arrangements have been made between the buyer and the seller directly, the value
   * in this field is expected to be derived from an ID sync. (see [Appendix: Cookie Based ID
   * Syncing)](https://github.com/InteractiveAdvertisingBureau/openrtb2.x/blob/main/2.6.md#appendixc)
   */
  readonly id?: ExternalId;
  /**
   * This field is deprecated, use 'kwarray' instead.
   */
  readonly keywords?: Text;
  /**
   * Array of keywords describing the content. Only one of 'keywords' or 'kwarray' may be present.
   */
  readonly kwarray?: readonly Text[];
  /**
   * Deprecated as of OpenRTB 2.6
   */
  readonly yob?: Count;
}

export interface UserAgent {
  /**
   * Device’s major binary architecture, e.g. “x86” or “arm”. Implementers should retrieve this
   * value from the Sec-CH-UA-Arch header*.
   */
  readonly architecture?: ExternalId;
  /**
   * Device’s bitness, e.g. “64” for 64-bit architecture. Implementers should retrieve this value
   * from the Sec-CH-UA-Bitness header *.
   */
  readonly bitness?: ExternalId;
  /**
   * Each BrandVersion object identifies a browser or similar software component. Refer to Object:
   * BrandVersion. Implementers should send brands and versions derived from the
   * Sec-CH-UA-Full-Version-List header*.
   */
  readonly browsers?: readonly BrandVersion[];
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * 1 if the agent prefers a “mobile” version of the content, if available, i.e. optimized for
   * small screens or touch input. 0 if the agent prefers the “desktop” or “full” content.
   * Implementers should derive this value from the Sec-CH-UA-Mobile header *.
   */
  readonly mobile?: IntegerFlag;
  /**
   * Device model. Implementers should retrieve this value from the Sec-CH-UA-Model header *.
   */
  readonly model?: Text;
  /**
   * Refer to Object: BrandVersion that identifies the user agent’s execution platform / OS.
   * Implementers should send a brand derived from the Sec-CH-UA-Platform header, and version
   * derived from the Sec-CH-UA-Platform-Version header *.
   */
  readonly platform?: BrandVersion;
  /**
   * The source of data used to create this object. Refer to List: User-Agent Source
   *
   * @default 0
   */
  readonly source?: UserAgentSource;
}

export interface Video {
  /**
   * Video markup (e.g., VAST). Note that including both `adm` and `curl` is not recommended.
   */
  readonly adm?: Text;
  /**
   * API required by the ad if applicable. Refer to List: API Frameworks.
   */
  readonly api?: readonly ApiFramework[];
  /**
   * Subtype of video creative. Refer to List: Creative Subtypes - Audio/Video.
   */
  readonly ctype?: CreativeSubtypeAudioVideo;
  /**
   * Optional means of retrieving markup by reference; a URL that returns video markup (e.g., VAST).
   * If this ad is matched to a Placement specification, the `Placement.curlx` attribute indicates
   * if this markup retrieval option is supported. Note that including both `adm` and `curl` is not
   * recommended.
   */
  readonly curl?: Text;
  /**
   * Duration of the video creative in seconds.
   */
  readonly dur?: DurationSeconds;
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * Mime type(s) of the ad creative(s) (e.g., “video/mp4”).
   */
  readonly mime?: readonly ExternalId[];
}

export interface VideoAsset {
  /**
   * Video markup (e.g., VAST document) for the asset. * Exactly one of `adm` and `curl` is
   * required. Including both is not recommended.
   */
  readonly adm?: Text;
  /**
   * A URL that returns the video markup (e.g., VAST document) for the asset. If this ad is matched
   * to a placement specification, the `Placement.curlx` attribute indicates if this markup
   * retrieval option is supported. * Exactly one of `adm` and `curl` is required. Including both is
   * not recommended.
   */
  readonly curl?: Text;
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
}

export interface VideoPlacement {
  /**
   * List of supported APIs for this placement. If an API is not explicitly listed, it is assumed to
   * be unsupported. Refer to List: API Frameworks.
   */
  readonly api?: readonly ApiFramework[];
  /**
   * Indicates if letterboxing of 4:3 creatives into a 16:9 window is allowed, where 0 = no, 1 =
   * yes.
   *
   * @default 1
   */
  readonly boxing?: IntegerFlag;
  /**
   * Indicates the click type of the placement. Refer to List: Click Types.
   */
  readonly clktype?: ClickType;
  /**
   * Array of objects indicating that companion ads are available and providing the specifications
   * thereof. Refer to Object: Companion.
   */
  readonly comp?: readonly Companion[];
  /**
   * Supported companion ad types; recommended if companion ads are specified in `comp`. Refer to
   * List: Companion Types.
   */
  readonly comptype?: readonly CompanionType[];
  /**
   * Creative subtypes permitted for this placement. Refer to List: Creative Subtypes - Audio/Video.
   */
  readonly ctype?: readonly CreativeSubtypeAudioVideo[];
  /**
   * Indicates the start delay in seconds for pre-roll, mid-roll, or post-roll placements. For
   * additional generic values, refer to List: Start Delay Modes.
   */
  readonly delay?: StartDelayMode;
  /**
   * Array of supported creative delivery methods. If omitted, all can be assumed. Refer to List:
   * Delivery Methods.
   */
  readonly delivery?: readonly DeliveryMethod[];
  /**
   * Directions in which the creative (video placement) is permitted to expand. Refer to List:
   * Expandable Directions.
   */
  readonly expdir?: readonly ExpandableDirection[];
  /**
   * Optional vendor-specific extensions.
   */
  readonly ext?: Ext;
  /**
   * Height of the placement in units specified by `unit`.
   */
  readonly h?: Count;
  /**
   * Indicates if the creative must be linear, nonlinear, etc. If none specified, no restrictions
   * are assumed. Refer to List: Linearity Modes. Note that this field describes the expected VAST
   * response and not whether a placement is in-stream, out-stream, etc. For that, see `ptype`.
   */
  readonly linear?: LinearityMode;
  /**
   * Maximum bit rate of the creative in Kbps.
   */
  readonly maxbitr?: Count;
  /**
   * Maximum creative duration in seconds. This field is mutually exclusive with rqddurs; only one
   * of maxdur and rqddurs may be in a bid request.
   */
  readonly maxdur?: DurationSeconds;
  /**
   * Maximum extended creative duration if extension is allowed. If 0, extension is not allowed. If
   * -1, extension is allowed and there is no time limit imposed. If greater than 0, then the value
   * represents the number of seconds of extended play supported beyond the `maxdur` value.
   *
   * @default 0
   */
  readonly maxext?: ExtendedDuration;
  /**
   * The maximum number of ads that can be played in an ad pod.
   */
  readonly maxseq?: Count;
  /**
   * Array of supported mime types (e.g., “video/mp4”). If omitted, all types are assumed.
   */
  readonly mime?: readonly ExternalId[];
  /**
   * Minimum bit rate of the creative in Kbps.
   */
  readonly minbitr?: Count;
  /**
   * Minimum CPM per second. This is a price floor for the “dynamic” portion of a video ad pod,
   * relative to the duration of bids an advertiser may submit.
   */
  readonly mincpmpersec?: Measure;
  /**
   * Minimum creative duration in seconds. This field is mutually exclusive with rqddurs; only one
   * of mindur and rqddurs may be in a bid request.
   */
  readonly mindur?: DurationSeconds;
  /**
   * Directions in which the creative (video overlay) is permitted to expand. This is primarily used
   * for non-linear videos. Refer to List: Expandable Directions.
   */
  readonly overlayexpdir?: readonly ExpandableDirection[];
  /**
   * The event that causes playback to end for this placement. Refer to List: Playback Cessation
   * Modes.
   */
  readonly playend?: PlaybackCessationMode;
  /**
   * Playback method(s) in use for this placement. Refer to List: Playback Methods.
   */
  readonly playmethod?: readonly PlaybackMethod[];
  /**
   * Indicates the total amount of time in seconds that advertisers may fill for a “dynamic” video
   * ad pod, or the dynamic portion of a “hybrid” ad pod. This field is required only for the
   * dynamic portion(s) of video ad pods. This field refers to the length of the entire ad break,
   * whereas mindur/maxdur/rqddurs are constraints relating to the slots that make up the pod.
   */
  readonly poddur?: DurationSeconds;
  /**
   * Unique identifier indicating that an impression opportunity belongs to a video ad pod. If
   * multiple impression opportunities within a bid request share the same podid, this indicates
   * that those impression opportunities belong to the same video ad pod.
   */
  readonly podid?: IntegerId;
  /**
   * The sequence (position) of the video ad pod within a content stream. Refer to List: List: Pod
   * Sequence for guidance on the use of this field.
   *
   * @default 0
   */
  readonly podseq?: PodSequence;
  /**
   * Placement position on screen. Refer to List: Placement Positions.
   */
  readonly pos?: PlacementPosition;
  /**
   * Placement subtype. Refer to List: Plcmt Subtypes - Video.
   */
  readonly ptype?: PlcmtSubtypeVideo;
  /**
   * Precise acceptable durations for video creatives in seconds. This field specifically targets
   * the Live TV use case where non-exact ad durations would result in undesirable 'dead air'. This
   * field is mutually exclusive with mindur and maxdur; if rqddurs is specified, mindur and maxdur
   * must not be specified and vice versa.
   */
  readonly rqddurs?: readonly DurationSeconds[];
  /**
   * Indicates if the placement imposes ad skippability, where 0 = no, 1 = yes.
   */
  readonly skip?: IntegerFlag;
  /**
   * Number of seconds a creative must play before the placement enables skipping; only applicable
   * if the ad is skippable.
   *
   * @default 0
   */
  readonly skipafter?: Count;
  /**
   * The placement allows creatives of total duration greater than this number of seconds to be
   * skipped; only applicable if the ad is skippable.
   *
   * @default 0
   */
  readonly skipmin?: DurationSeconds;
  /**
   * For video ad pods, this value indicates that the seller can guarantee delivery against the
   * indicated slot position in the pod. Refer to List: List: Slot Position in Pod for guidance on
   * the use of this field.
   *
   * @default 0
   */
  readonly slotinpod?: SlotPositionInPod;
  /**
   * Units of size used for `w` and `h` attributes. Refer to List: Size Units.
   *
   * @default 1
   */
  readonly unit?: SizeUnit;
  /**
   * Width of the placement in units specified by `unit`.
   */
  readonly w?: Count;
}
