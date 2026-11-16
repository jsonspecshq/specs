"""The delegated object types: every type of the published tree whose value is an object.

An object references the scalars and the vocabularies, both written before it. The tree states a cycle among these types, which the forward references and the rebuild at the end of this module close.

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

from ._runtime import SpecModel
from ._scalars import (
    Count,
    Degrees,
    Domain,
    DurationSeconds,
    EpochMilliseconds,
    ExtendedDuration,
    ExternalId,
    IntegerId,
    Measure,
    MediaOffset,
    MinuteOffset,
    Text,
    VendorCode,
)
from ._vocabularies import (
    AgentType,
    AmpRenderingTreatment,
    ApiFramework,
    AuditStatusCode,
    AutoRefreshTrigger,
    CategoryTaxonomy,
    ClickType,
    CompanionType,
    ConnectionType,
    ContentContext,
    CreativeAttribute,
    CreativeSubtypeAudioVideo,
    CreativeSubtypeDisplay,
    DeliveryMethod,
    DeviceType,
    DisplayContextType,
    DisplayPlacementType,
    DoohMultiplierMeasurementSourceType,
    DoohPlacementMobility,
    DoohVenueTaxonomy,
    EventTrackingMethod,
    EventType,
    ExpandableDirection,
    FeedType,
    IdMatchMethod,
    IntegerFlag,
    IpLocationService,
    LinearityMode,
    LocationType,
    MediaRating,
    NativeDataAssetType,
    NativeImageAssetType,
    OperatingSystem,
    PlacementPosition,
    PlaybackCessationMode,
    PlaybackMethod,
    PlcmtSubtypeVideo,
    PodDeduplicationSetting,
    PodSequence,
    ProductionQuality,
    ServerSideAdInsertionMode,
    SizeUnit,
    SlotPositionInPod,
    StartDelayMode,
    UserAgentSource,
    VolumeNormalizationMode,
)


class Ext(SpecModel):
    model_config = ConfigDict(
        extra='allow',
    )


class Audio(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    adm: Text | None = Field(
        None,
        description='Audio markup (e.g., DAAST). Note that including both `adm` and `curl` is not recommended.',
    )
    api: list[ApiFramework] | None = Field(
        None,
        description='API required by the ad if applicable. Refer to List: API Frameworks.',
    )
    ctype: CreativeSubtypeAudioVideo | None = Field(
        None,
        description='Subtype of audio creative. Refer to List: Creative Subtypes - Audio/Video.',
    )
    curl: Text | None = Field(
        None,
        description='Optional means of retrieving markup by reference; a URL that returns audio markup (e.g., DAAST). If this ad is matched to a Placement specification, the `Placement.curlx` attribute indicates if this markup retrieval option is supported. Note that including both `adm` and `curl` is not recommended.',
    )
    dur: DurationSeconds | None = Field(
        None, description='Duration of the audio creative in seconds.'
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    mime: list[ExternalId] | None = Field(
        None, description='Mime type(s) of the ad creative(s) (e.g., “audio/mp4”).'
    )


class BrandVersion(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    brand: Text | None = Field(
        None,
        description='A brand identifier, for example, “Chrome” or “Windows”. The value may be sourced from the User-Agent Client Hints headers, representing either the user agent brand (from the Sec-CH-UA-Full-Version header) or the platform brand (from the Sec-CH-UA-Platform header).',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    version: list[ExternalId] | None = Field(
        None,
        description='A sequence of version components, in descending hierarchical order (major, minor, micro, …)',
    )


class Channel(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    domain: Domain | None = Field(
        None,
        description='The primary domain of the channel (e.g., “abc7ny.com” in the case of the local channel WABC-TV). It is recommended to include the top private domain (PSL+1) for DSP targeting normalization purposes.',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    id: ExternalId | None = Field(
        None,
        description='A unique identifier assigned by the publisher. This may not be a unique identifier across all supply sources.',
    )
    name: Text | None = Field(
        None,
        description='Channel the content is on (e.g., a local channel like "WABC-TV").',
    )


class Corr(SpecModel):
    model_config = ConfigDict(
        extra='allow',
    )


class DataAsset(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    len: Count | None = Field(
        None,
        description='The length of the `value` contents. This length should conform to recommendations provided in List: Native Data Asset Types',
    )
    type: NativeDataAssetType | None = Field(
        None,
        description='The type of data represented by this asset. Refer to List: Native Data Asset Types.',
    )
    value: Text = Field(
        ...,
        description='A formatted string of data to be displayed (e.g., “5 stars”, “3.4 stars out of 5”, “$10”, etc.).',
    )


class DataAssetFormat(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    len: Count | None = Field(
        None, description='The maximum allowed length of the data value.'
    )
    type: NativeDataAssetType = Field(
        ...,
        description='The type of data asset supported. Refer to List: Native Data Asset Types.',
    )


class DisplayFormat(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    expdir: list[ExpandableDirection] | None = Field(
        None,
        description='Directions in which the creative is permitted to expand. Refer to List: Expandable Directions.',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    h: Count | None = Field(
        None,
        description='Absolute height of the creative in units specified by `DisplayPlacement.unit`. Note that mixing absolute and relative sizes is not recommended.',
    )
    hratio: Count | None = Field(
        None,
        description='Relative height of the creative when expressing size as a ratio. Note that mixing absolute and relative sizes is not recommended.',
    )
    w: Count | None = Field(
        None,
        description='Absolute width of the creative in units specified by `DisplayPlacement.unit`. Note that mixing absolute and relative sizes is not recommended.',
    )
    wratio: Count | None = Field(
        None,
        description='Relative width of the creative when expressing size as a ratio. Note that mixing absolute and relative sizes is not recommended.',
    )


class Event(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    api: list[ApiFramework] | None = Field(
        None,
        description='The APIs being used by the tracker; only relevant when the tracking method is JavaScript. Refer to List: API Frameworks.',
    )
    cdata: Ext | None = Field(
        None,
        description='An array of key-value pairs to support vendor-specific data required for custom tracking. For example, the account number of a buyer with a tracking company might be represented as: {"acct": "123"}.',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    method: EventTrackingMethod = Field(
        ...,
        description='Method of tracking requested. Refer to List: Event Tracking Methods.',
    )
    type: EventType = Field(
        ..., description='Type of event to track. Refer to List: Event Types.'
    )
    url: Text | None = Field(
        None,
        description='The URL of the tracking pixel or JavaScript tag, respectively. * Required for Image-Pixel or JavaScript methods.',
    )


class EventSpec(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    api: list[ApiFramework] | None = Field(
        None,
        description='Event tracking APIs available for use; only relevant for JavaScript method trackers. Refer to List: API Frameworks.',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    jstrk: list[Domain] | None = Field(
        None,
        description='Array of domains, top two levels only (e.g., “tracker.com”), that constitute a restriction list of JavaScript trackers. The sense of the restrictions is determined by `wjs`.',
    )
    method: list[EventTrackingMethod] | None = Field(
        None,
        description='Array of supported event tracking methods for this event type. Refer to List: Event Tracking Methods.',
    )
    pxtrk: list[Domain] | None = Field(
        None,
        description='Array of domains, top two levels only (e.g., “tracker.com”), that constitute a restriction list of pixel image trackers. The sense of the restrictions is determined by `wpx`.',
    )
    type: EventType = Field(
        ...,
        description='Type of supported ad tracking event. Refer to List: Event Types.',
    )
    wjs: IntegerFlag | None = Field(
        1,
        description='Sense of the `jstrk` restriction list, where 0 = block list, 1 = allow list.',
    )
    wpx: IntegerFlag | None = Field(
        1,
        description='Sense of the `pxtrk` restriction list, where 0 = block list, 1 = allow list.',
    )


class ExtendedIdentifierUids(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    atype: AgentType | None = Field(
        None,
        description='Type of user agent the match is from. It is highly recommended to set this, as many DSPs separate app-native IDs from browser-based IDs and require a type value for ID resolution. Refer to List: Agent Types.',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    id: ExternalId | None = Field(
        None, description='Cookie or platform-native identifier.'
    )


class ExtendedIdentifiers(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    inserter: Domain | None = Field(
        None,
        description='The canonical domain name of the entity (publisher, publisher monetization company, SSP, Exchange, Header Wrapper, etc.) that caused the ID array element to be added. This may be the operational domain of the system, if that is different from the parent corporate domain, to facilitate WHOIS and reverse IP lookups to establish clear ownership of the delegate system. This should be the same value as used to identify sellers in an ads.txt file if one exists. For ad tech intermediaries, this would be the domain as used in ads.txt. For publishers, this would match the domain in the `site` or `app` object.',
    )
    matcher: Text | None = Field(
        None,
        description='Technology providing the match method as defined in `mm`. In some cases, this may be the same value as inserter. When blank, it is assumed that the `matcher` is equal to the `source` May be omitted when mm=0, 1, or 2.',
    )
    mm: IdMatchMethod | None = Field(
        None,
        description='Match method used by the `matcher`. Refer to List: ID Match Methods.',
    )
    source: Domain | None = Field(
        None,
        description='Source domain of the UID provider. Should be the root domain name of the provider, not the URL. For example, "liveramp.com" not "https://liveramp.com/connect"',
    )
    uids: list[ExtendedIdentifierUids] | None = Field(
        None,
        description='Array of extended ID UID objects from the given `source`. Refer to Object: Extended Identifier UIDs.',
    )


class Geo(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    accur: Count | None = Field(
        None,
        description="Estimated location accuracy in meters; recommended when lat/lon are specified and derived from a device's location services (i.e., type = 1). Note that this is the accuracy as reported from the device. Consult OS specific documentation (e.g., Android, iOS) for exact interpretation.",
    )
    city: ExternalId | None = Field(
        None,
        description='City using United Nations Code for Trade & Transport Locations “UN/LOCODE” with the space between country and city suppressed (e.g., Boston MA, USA = “USBOS”). Refer to UN/LOCODE Code List.',
    )
    country: ExternalId | None = Field(
        None,
        description='Country code using ISO-3166-1-alpha-2. Note that alpha-3 codes may be encountered and vendors are encouraged to be tolerant of them.',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    ipserv: IpLocationService | None = Field(
        None,
        description='Service or provider used to determine geolocation from IP address if applicable (i.e., `type` = 2). Refer to List: IP Location Services.',
    )
    lastfix: Count | None = Field(
        None,
        description='Number of seconds since this geolocation fix was established. Note that devices may cache location data across multiple fetches. Ideally, this value should be from the time the actual fix was taken.',
    )
    lat: Degrees | None = Field(
        None, description='Latitude from -90.0 to +90.0, where negative is south.'
    )
    lon: Degrees | None = Field(
        None, description='Longitude from -180.0 to +180.0, where negative is west.'
    )
    metro: ExternalId | None = Field(
        None,
        description="Regional marketing areas such as Nielsen's DMA codes or other similar taxonomy to be agreed among vendors prior to use. Note that DMA is a trademarked asset of The Nielsen Company. Vendors are encouraged to ensure their use of DMAs is properly licensed.",
    )
    region: ExternalId | None = Field(
        None, description='Region code using ISO-3166-2; 2-letter state code if USA.'
    )
    type: LocationType | None = Field(
        None,
        description='Source of location data; recommended when passing lat/lon. Refer to List: Location Types.',
    )
    utcoffset: MinuteOffset | None = Field(
        None, description='Local time as the number +/- of minutes from UTC.'
    )
    zip: ExternalId | None = Field(None, description='ZIP or postal code.')


class ImageAsset(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    h: Count | None = Field(
        None,
        description='Height of the image asset in device independent pixels (DIPS).',
    )
    type: NativeImageAssetType | None = Field(
        None,
        description='The type of image represented by this asset. Refer to List: Native Image Asset Types.',
    )
    url: Text = Field(..., description='A URL that returns the image for the asset.')
    w: Count | None = Field(
        None,
        description='Width of the image asset in device independent pixels (DIPS).',
    )


class ImageAssetFormat(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    h: Count | None = Field(
        None,
        description='Absolute height of the image asset in device independent pixels (DIPS). Note that mixing absolute and relative sizes is not recommended.',
    )
    hmin: Count | None = Field(
        None,
        description='The minimum requested absolute height of the image in device independent pixels (DIPS). This option should be used for any scaling of images by the client.',
    )
    hratio: Count | None = Field(
        None,
        description='Relative height of the image asset when expressing size as a ratio. Note that mixing absolute and relative sizes is not recommended.',
    )
    mime: list[ExternalId] | None = Field(
        None,
        description='Array of supported mime types (e.g., “image/jpeg”, “image/gif”). If omitted, all types are assumed.',
    )
    type: NativeImageAssetType | None = Field(
        None,
        description='The type of image asset supported. Refer to List: Native Image Asset Types.',
    )
    w: Count | None = Field(
        None,
        description='Absolute width of the image asset in device independent pixels (DIPS). Note that mixing absolute and relative sizes is not recommended.',
    )
    wmin: Count | None = Field(
        None,
        description='The minimum requested absolute width of the image in device independent pixels (DIPS). This option should be used for any scaling of images by the client.',
    )
    wratio: Count | None = Field(
        None,
        description='Relative width of the image asset when expressing size as a ratio. Note that mixing absolute and relative sizes is not recommended.',
    )


class LinkAsset(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    trkr: list[Text] | None = Field(
        None, description='List of third-party tracker URLs to be fired on click.'
    )
    url: Text = Field(..., description='Landing URL of the clickable link.')
    urlfb: Text | None = Field(
        None,
        description='Fallback URL for deep-link to be used if the URL specified in `url` is not supported by the device.',
    )


class Network(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    domain: Domain | None = Field(
        None,
        description='The primary domain of the network (e.g., “abc.com” in the case of the network ABC). It is recommended to include the top private domain (PSL+1) for DSP targeting normalization purposes.',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    id: ExternalId | None = Field(
        None,
        description='A unique identifier assigned by the publisher. This may not be a unique identifier across all supply sources.',
    )
    name: Text | None = Field(
        None, description='Network the content is on (e.g., a TV network like "ABC").'
    )


class Producer(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    cat: list[ExternalId] | None = Field(
        None,
        description='Array of content categories that describe the producer using IDs from the taxonomy indicated in `cattax`.',
    )
    cattax: CategoryTaxonomy | None = Field(
        None,
        description='The taxonomy in use for the `cat` attribute. Refer to List: Category Taxonomies.',
    )
    domain: Domain | None = Field(
        None, description='Highest level domain of the producer (e.g., “producer.com”).'
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    id: ExternalId | None = Field(
        None,
        description='Vendor-specific unique producer identifier. Useful if content is syndicated and may be posted on a site using embed tags.',
    )
    name: Text | None = Field(None, description='Displayable name of the producer.')


class Publisher(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    cat: list[ExternalId] | None = Field(
        None,
        description='Array of content categories that describe the publisher using IDs from the taxonomy indicated in `cattax`. Implementer should ensure compliance with regional legislation around data usage and sharing.',
    )
    cattax: CategoryTaxonomy | None = Field(
        None,
        description='The taxonomy in use for the `cat` attribute. Refer to ![image](https://github.com/InteractiveAdvertisingBureau/AdCOM/assets/114763292/e80e72e1-e099-4aff-b466-a5e91eb9f62f).',
    )
    domain: Domain | None = Field(
        None,
        description='Highest level domain of the publisher (e.g., “publisher.com”).',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    id: ExternalId | None = Field(
        None,
        description='Vendor-specific unique publisher identifier, as used in ads.txt files.',
    )
    name: Text | None = Field(None, description='Displayable name of the publisher.')


class Regs(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    coppa: IntegerFlag | None = Field(
        None,
        description="Flag indicating if COPPA regulations apply, where 0 = no, 1 = yes. The Children's Online Privacy Protection Act (COPPA) was established by the U.S. Federal Trade Commission.",
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    gdpr: IntegerFlag | None = Field(
        None,
        description='Flag indicating if GDPR regulations apply, where 0 = no, 1 = yes. The General Data Protection Regulation (GDPR) is a regulation of the European Union.',
    )
    gpp: ExternalId | None = Field(
        None,
        description='Contains the Global Privacy Platform’s consent string. See the Global Privacy Platform specification for more details.',
    )
    gpp_sid: list[Count] | None = Field(
        None,
        description='Array of the section(s) of the string which should be applied for this transaction. Generally will contain one and only one value, but there are edge cases where more than one may apply. GPP Section 3 (Header) and 4 (Signal Integrity) do not need to be included. See the GPP Section Information for more details.',
    )


class Restrictions(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    acat: list[ExternalId] | None = Field(
        None,
        description='Allowed content categories using IDs from the taxonomy indicated in `cattax`. Only one of `acat` or `bcat` should be present.',
    )
    badv: list[Domain] | None = Field(
        None,
        description='Block list of advertisers by their domains (e.g., “ford.com”).',
    )
    bapp: list[ExternalId] | None = Field(
        None,
        description='Block list of apps for which ads are disallowed. These should be bundle or package names (e.g., “com.foo.mygame”) and should NOT be app store IDs (e.g., not iTunes store IDs).',
    )
    battr: list[CreativeAttribute] | None = Field(
        None,
        description='Block list of creative attributes. Refer to List: Creative Attributes.',
    )
    bcat: list[ExternalId] | None = Field(
        None,
        description='Block list of content categories using IDs from the taxonomy indicated in `cattax`. Only one of `acat` or `bcat` should be present.',
    )
    cattax: CategoryTaxonomy | None = Field(
        2,
        description='The taxonomy in use for the `bcat` attribute. Refer to List: Category Taxonomies.',
        validate_default=True,
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')


class Segment(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    id: ExternalId | None = Field(
        None, description='ID of the data segment specific to the data provider.'
    )
    name: Text | None = Field(
        None,
        description='Displayable name of the data segment specific to the data provider.',
    )
    value: Text | None = Field(
        None, description='String representation of the data segment value.'
    )


class TitleAsset(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    len: Count | None = Field(
        None, description='The length of the contents of the `text` attribute.'
    )
    text: Text = Field(..., description='The text content of the text element.')


class TitleAssetFormat(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    len: Count = Field(
        ...,
        description='The maximum allowed length of the title value. Recommended lengths are 25, 90, or 140.',
    )


class UserAgent(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    architecture: ExternalId | None = Field(
        None,
        description='Device’s major binary architecture, e.g. “x86” or “arm”. Implementers should retrieve this value from the Sec-CH-UA-Arch header*.',
    )
    bitness: ExternalId | None = Field(
        None,
        description='Device’s bitness, e.g. “64” for 64-bit architecture. Implementers should retrieve this value from the Sec-CH-UA-Bitness header *.',
    )
    browsers: list[BrandVersion] | None = Field(
        None,
        description='Each BrandVersion object identifies a browser or similar software component. Refer to Object: BrandVersion. Implementers should send brands and versions derived from the Sec-CH-UA-Full-Version-List header*.',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    mobile: IntegerFlag | None = Field(
        None,
        description='1 if the agent prefers a “mobile” version of the content, if available, i.e. optimized for small screens or touch input. 0 if the agent prefers the “desktop” or “full” content. Implementers should derive this value from the Sec-CH-UA-Mobile header *.',
    )
    model: Text | None = Field(
        None,
        description='Device model. Implementers should retrieve this value from the Sec-CH-UA-Model header *.',
    )
    platform: BrandVersion | None = Field(
        None,
        description='Refer to Object: BrandVersion that identifies the user agent’s execution platform / OS. Implementers should send a brand derived from the Sec-CH-UA-Platform header, and version derived from the Sec-CH-UA-Platform-Version header *.',
    )
    source: UserAgentSource | None = Field(
        0,
        description='The source of data used to create this object. Refer to List: User-Agent Source',
    )


class Video(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    adm: Text | None = Field(
        None,
        description='Video markup (e.g., VAST). Note that including both `adm` and `curl` is not recommended.',
    )
    api: list[ApiFramework] | None = Field(
        None,
        description='API required by the ad if applicable. Refer to List: API Frameworks.',
    )
    ctype: CreativeSubtypeAudioVideo | None = Field(
        None,
        description='Subtype of video creative. Refer to List: Creative Subtypes - Audio/Video.',
    )
    curl: Text | None = Field(
        None,
        description='Optional means of retrieving markup by reference; a URL that returns video markup (e.g., VAST). If this ad is matched to a Placement specification, the `Placement.curlx` attribute indicates if this markup retrieval option is supported. Note that including both `adm` and `curl` is not recommended.',
    )
    dur: DurationSeconds | None = Field(
        None, description='Duration of the video creative in seconds.'
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    mime: list[ExternalId] | None = Field(
        None, description='Mime type(s) of the ad creative(s) (e.g., “video/mp4”).'
    )


class VideoAsset(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    adm: Text | None = Field(
        None,
        description='Video markup (e.g., VAST document) for the asset. * Exactly one of `adm` and `curl` is required. Including both is not recommended.',
    )
    curl: Text | None = Field(
        None,
        description='A URL that returns the video markup (e.g., VAST document) for the asset. If this ad is matched to a placement specification, the `Placement.curlx` attribute indicates if this markup retrieval option is supported. * Exactly one of `adm` and `curl` is required. Including both is not recommended.',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')


class Asset(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    data: DataAsset | None = Field(
        None,
        description='Asset Subtype Object that indicates this is a data asset and provides additional detail as such. Refer to Object: DataAsset. * Required if no other asset subtype object is specified.',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    id: Count | None = Field(
        None,
        description='The value of `AssetFormat.id` if this ad references a specific native placement defined by a `Placement` object and its structure.',
    )
    image: ImageAsset | None = Field(
        None,
        description='Asset Subtype Object that indicates this is an image asset and provides additional detail as such. Refer to Object: ImageAsset. * Required if no other asset subtype object is specified.',
    )
    link: LinkAsset | None = Field(
        None,
        description='Asset Subtype Object that indicates this is a link asset and provides additional detail as such. Refer to Object: LinkAsset. * Required if no other asset subtype object is specified.',
    )
    req: IntegerFlag | None = Field(
        0,
        description='Indicates if the asset is required to be displayed, where 0 = no, 1 = yes.',
    )
    title: TitleAsset | None = Field(
        None,
        description='Asset Subtype Object that indicates this is a title asset and provides additional detail as such. Refer to Object: TitleAsset. * Required if no other asset subtype object is specified.',
    )
    video: VideoAsset | None = Field(
        None,
        description='Asset Subtype Object that indicates this is a video asset and provides additional detail as such. Refer to Object: VideoAsset. * Required if no other asset subtype object is specified.',
    )


class Audit(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    corr: Corr | None = Field(
        None,
        description='Correction object wherein the auditor can specify changes to attributes of the `Ad` object or its children they believe to be proper. For example, if the original `Ad` indicated a category of “IAB3”, but the auditor deems the correct category to be “IAB13”, then `corr` could include a sparse `Ad` object including just the `cat` array indicating “IAB13”.',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    feedback: list[Text] | None = Field(
        None,
        description='One or more human-readable explanations as to reasons for rejection or any changes to fields for ad quality reasons (e.g., `adomain`, `cat`, `attr`, etc.).',
    )
    init: EpochMilliseconds | None = Field(
        None,
        description='Timestamp of the original instantiation of this object in Unix format (i.e., milliseconds since the epoch).',
    )
    lastmod: EpochMilliseconds | None = Field(
        None,
        description='Timestamp of most recent modification to this object in Unix format (i.e., milliseconds since the epoch).',
    )
    status: AuditStatusCode | None = Field(
        None,
        description='The audit status of the ad. Refer to List: Audit Status Codes.',
    )


class Banner(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    img: Text = Field(..., description='A URL that will return the image.')
    link: LinkAsset | None = Field(
        None,
        description='Destination link if the image is activated (e.g., clicked); not applicable in some contexts (e.g., DOOH) and its inclusion does not guarantee it will be supported. Refer to Object: LinkAsset.',
    )


class Data(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    cids: list[ExternalId] | None = Field(
        None,
        description='An array of Extended Content IDs, representing one or more identifiers for the video or audio content from the ID source specified in the `name` field of the `data` object.',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    id: ExternalId | None = Field(
        None, description='Vendor-specific ID for the data provider.'
    )
    name: Text | None = Field(
        None, description='Vendor-specific displayable name for the data provider.'
    )
    segment: list[Segment] | None = Field(
        None,
        description='Array of `Segment` objects that contain the actual data values. Refer to Object: Segment.',
    )


class Device(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    carrier: Text | None = Field(
        None,
        description='Carrier or ISP (e.g., “VERIZON”) using exchange curated string names which should be published to bidders beforehand.',
    )
    contype: ConnectionType | None = Field(
        None, description='Network connection type. Refer to List: Connection Types.'
    )
    dnt: IntegerFlag | None = Field(
        None,
        description='Standard “Do Not Track” flag as set in the header by the browser, where 0 = tracking is unrestricted, 1 = do not track.',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    geo: Geo | None = Field(
        None,
        description="Location of the device (i.e., typically the user's current location). Refer to Object: Geo.",
    )
    geofetch: IntegerFlag | None = Field(
        None,
        description='Indicates if the geolocation API will be available to JavaScript code running in display ad, where 0 = no, 1 = yes.',
    )
    h: Count | None = Field(
        None, description='Physical height of the screen in pixels.'
    )
    hwv: ExternalId | None = Field(
        None, description='Hardware version of the device (e.g., “5S” for iPhone 5S).'
    )
    ifa: ExternalId | None = Field(
        None,
        description='ID sanctioned for advertiser use in the clear (i.e., not hashed).',
    )
    ip: ExternalId | None = Field(None, description='IPv4 address closest to device.')
    iptr: IntegerFlag | None = Field(
        None,
        description='Indicator of truncation of any of the IP attributes (i.e., `ip`, `ipv6`, `xff`), where 0 = no, 1 = yes (e.g., from 1.2.3.4 to 1.2.3.0). Refer to https://tools.ietf.org/html/rfc6235#section-4.1.1 for more information on IP truncation.',
    )
    ipv6: ExternalId | None = Field(
        None, description='IP address closest to device as IPv6.'
    )
    js: IntegerFlag | None = Field(
        None, description='Support for JavaScript, where 0 = no, 1 = yes.'
    )
    lang: ExternalId | None = Field(
        None,
        description='Browser language using ISO-639-1-alpha-2. Only one of lang or langb should be present.',
    )
    langb: ExternalId | None = Field(
        None,
        description='Browser language using IETF BCP 47. Only one of lang or langb should be present.',
    )
    lmt: IntegerFlag | None = Field(
        None,
        description='“Limit Ad Tracking” signal commercially endorsed (e.g., iOS, Android), where 0 = tracking is unrestricted, 1 = tracking must be limited per commercial guidelines.',
    )
    make: Text | None = Field(None, description='Device make (e.g., "Apple").')
    mccmnc: ExternalId | None = Field(
        None,
        description='Mobile carrier as the concatenated MCC-MNC code (e.g., “310-005” identifies Verizon Wireless CDMA in the USA). Refer to https://en.wikipedia.org/wiki/Mobile_country_code for further information and references. Note that the dash between the MCC and MNC parts is required to remove parsing ambiguity. The MCC-MNC values represent the SIM installed on the device and do not change when a device is roaming. Roaming may be inferred by a combination of the MCC-MNC, geo, IP and other data signals.',
    )
    mccmncsim: ExternalId | None = Field(
        None,
        description='MCC and MNC of the SIM card using the same format as `mccmnc`. When both values are available, a difference between them reveals that a user is roaming.',
    )
    model: Text | None = Field(
        None,
        description='Device model (e.g., “iPhone10,1” when the specific device model is known, “iPhone” otherwise). The value obtained from the device O/S should be used when available.',
    )
    os: OperatingSystem | None = Field(
        None, description='Device operating system. Refer to List: Operating Systems.'
    )
    osv: ExternalId | None = Field(
        None, description='Device operating system version (e.g., “3.1.2”).'
    )
    ppi: Count | None = Field(
        None, description='Screen size as pixels per linear inch.'
    )
    pxratio: Measure | None = Field(
        None, description='The ratio of physical pixels to device independent pixels.'
    )
    sua: UserAgent | None = Field(
        None,
        description='Structured user agent information defined by a Object: UserAgent. If both `ua` and `sua` are present in the bid request, `sua` should be considered the more accurate representation of the device attributes. This is because the `ua` may contain a frozen or reduced UserAgent string.',
    )
    type: DeviceType | None = Field(
        None, description='The general type of device. Refer to List: Device Types.'
    )
    ua: Text | None = Field(
        None,
        description='Browser user agent string. This field represents a raw user agent string from the browser. For backwards compatibility, exchanges are recommended to always populate `ua` with the User-Agent string, when available from the end user’s device, even if an alternative representation, such as the User-Agent Client-Hints, is available and gets used to populate `sua`. No inferred or approximated user agents are expected in this field. If both `ua` and `sua` are present in the bid request, `sua` should be considered the more accurate representation of the device attributes. This is because the `ua` may contain a frozen or reduced UserAgent string.',
    )
    w: Count | None = Field(None, description='Physical width of the screen in pixels.')
    xff: ExternalId | None = Field(
        None, description='The value of the “x-forwarded-for” header.'
    )


class Native(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    asset: list[Asset] | None = Field(
        None,
        description='Array of assets that comprise the native ad. Refer to Object: Asset.',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    link: LinkAsset | None = Field(
        None,
        description="Default destination link for the native ad overall; used if an asset is activated (e.g., clicked) that doesn't specify it's own destination link. Refer to Object: LinkAsset.",
    )


class User(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    buyeruid: ExternalId | None = Field(
        None,
        description='Buyer-specific ID for the user as mapped by an exchange for the buyer. At least one of `id` or `buyeruid` is strongly recommended. Unless prior arrangements have been made between the buyer and the seller directly, the value in this field is expected to be derived from an ID sync. (see [Appendix: Cookie Based ID Syncing)](https://github.com/InteractiveAdvertisingBureau/openrtb2.x/blob/main/2.6.md#appendixc)',
    )
    consent: ExternalId | None = Field(
        None,
        description='GDPR consent string if applicable, complying with the comply with the IAB standard Consent String Format in the Transparency and Consent Framework technical specifications.',
    )
    data: list[Data] | None = Field(
        None,
        description='Additional user data. Each `Data` object represents a different data source. Refer to Object: Data.',
    )
    eids: list[ExtendedIdentifiers] | None = Field(
        None,
        description='Extended (third-party) identifiers for this user. Refer to Object: Extended Identifiers.',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    gender: Text | None = Field(None, description='Deprecated as of OpenRTB 2.6')
    geo: Geo | None = Field(
        None,
        description="Location of the user's home base (i.e., not necessarily their current location). Refer to Object: Geo.",
    )
    id: ExternalId | None = Field(
        None,
        description='Exchange-specific ID for the user At least one of `id` or `buyeruid` is strongly recommended. Unless prior arrangements have been made between the buyer and the seller directly, the value in this field is expected to be derived from an ID sync. (see [Appendix: Cookie Based ID Syncing)](https://github.com/InteractiveAdvertisingBureau/openrtb2.x/blob/main/2.6.md#appendixc)',
    )
    keywords: Text | None = Field(
        None, description="This field is deprecated, use 'kwarray' instead."
    )
    kwarray: list[Text] | None = Field(
        None,
        description="Array of keywords describing the content. Only one of 'keywords' or 'kwarray' may be present.",
    )
    yob: Count | None = Field(None, description='Deprecated as of OpenRTB 2.6')


class Content(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    album: Text | None = Field(
        None, description='Album to which the content belongs; typically for audio.'
    )
    artist: Text | None = Field(None, description='Artist credited with the content.')
    cat: list[ExternalId] | None = Field(
        None,
        description='Array of IAB Tech Lab content categories that describe the content. The taxonomy to be used is defined by the cattax field. If no cattax field is supplied Content Category Taxonomy 1.0 is assumed.',
    )
    cattax: CategoryTaxonomy | None = Field(
        1,
        description='The taxonomy in use. Refer to list List: Category Taxonomies in AdCOM 1.0 for values.',
        validate_default=True,
    )
    channel: Channel | None = Field(
        None,
        description='Details about the channel (Section 3.2.24) the content is on.',
    )
    context: ContentContext | None = Field(
        None,
        description='Type of content (game, video, text, etc.). Refer to List: Content Contexts in AdCOM 1.0.',
    )
    data: list[Data] | None = Field(
        None,
        description='Additional content data. Each `Data` object (Section 3.2.21) represents a different data source.',
    )
    embed: IntegerFlag | None = Field(
        None,
        description='Indicator of whether the content is embeddable (e.g., an embeddable video player), where 0 = no, 1 = yes.',
    )
    episode: Count | None = Field(None, description='Episode number.')
    ext: Ext | None = Field(
        None, description='Placeholder for vendor-specific extensions.'
    )
    firstbroadcast: IntegerFlag | None = Field(
        None,
        description='An enumeration indicating whether this broadcast is the first time the content is available to an audience where: 0 = not first time being broadcast 1 = first time being broadcast',
    )
    genre: Text | None = Field(
        None,
        description='Genre that best describes the content (e.g., rock, pop, etc).',
    )
    genres: list[ExternalId] | None = Field(
        None,
        description='Unique ID(s) for the genre of the content as listed in the taxonomy defined by the gtax field. If no gtax field is supplied, subset of rows listed in CTV Genre Mapping of Content Category Taxonomy 3.1 are assumed. See Section 7.13 of Implementation Guidance for additional detail.',
    )
    gtax: CategoryTaxonomy | None = Field(
        9,
        description='The taxonomy in use. Refer to list List: Category Taxonomies in AdCOM 1.0 for values. If no gtax field is supplied rows listed, Content Category Taxonomy 3.1 is assumed',
        validate_default=True,
    )
    id: ExternalId | None = Field(
        None, description='Publisher-provided ID uniquely identifying the content.'
    )
    isrc: ExternalId | None = Field(
        None,
        description='International Standard Recording Code conforming to ISO- 3901.',
    )
    keywords: Text | None = Field(
        None,
        description='Comma separated list of keywords describing the content. Only one of `keywords` or `kwarray` may be present.',
    )
    kwarray: list[Text] | None = Field(
        None,
        description='Array of keywords about the site. Only one of `keywords` or `kwarray` may be present.',
    )
    lang: ExternalId | None = Field(
        None,
        description='Content language using ISO-639-1-alpha-2. Only one of `lang` or `langb` should be present.',
    )
    langb: ExternalId | None = Field(
        None,
        description='Content language using IETF BCP 47. Only one of `lang` or `langb` should be present.',
    )
    len: DurationSeconds | None = Field(
        None,
        description='Length of content in seconds; appropriate for video or audio.',
    )
    live: IntegerFlag | None = Field(
        None,
        description='An enumeration indicating the method of broadcast of the content where: 0 = the broadcast is not scheduled (e.g. it is VOD or otherwise user initiated). 1 = the broadcast is scheduled (also referred to as linear viewing).',
    )
    mrating: MediaRating | None = Field(
        None,
        description='Media rating per IQG guidelines. Refer to List: Media Ratings in AdCOM 1.0.',
    )
    network: Network | None = Field(
        None,
        description='Details about the network (Section 3.2.23) the content is on.',
    )
    prodq: ProductionQuality | None = Field(
        None,
        description='Production quality. Refer to List: Production Qualities in AdCOM 1.0.',
    )
    producer: Producer | None = Field(
        None, description='Details about the content `Producer` (Section 3.2.17).'
    )
    rating: Text | None = Field(None, description='Content rating (e.g., MPAA).')
    realtime: IntegerFlag | None = Field(
        None,
        description='An enumeration indicating if the event is happening in real time while it is being watched where: 0 = not happening in real time (e.g., a replay). 1 = yes, happening in real time (e.g., a live sports game).',
    )
    season: Text | None = Field(None, description='Content season (e.g., “Season 3”).')
    series: Text | None = Field(
        None,
        description='Content series. Video Examples: “The Office” (television), “Star Wars” (movie), or “Arby ‘N’ The Chief” (made for web). Non-Video Example: “Ecocentric” (Time Magazine blog).',
    )
    srcrel: IntegerFlag | None = Field(None, description='0 = indirect, 1 = direct.')
    title: Text | None = Field(
        None,
        description='Content title. Video Examples: “Search Committee” (television), “A New Hope” (movie), or “Endgame” (made for web). Non-Video Example: “Why an Antarctic Glacier Is Melting So Quickly” (Time magazine article).',
    )
    urating: Text | None = Field(
        None,
        description='User rating of the content (e.g., number of stars, likes, etc.).',
    )
    url: Text | None = Field(
        None,
        description='URL of the content, for buy-side contextualization or review.',
    )


class Display(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    adm: Text | None = Field(
        None,
        description='General display markup (e.g., HTML, AMPHTML) if not using a structured alternative (e.g., `banner`, `native`). Note that including both `adm` and `curl` is not recommended.',
    )
    api: list[ApiFramework] | None = Field(
        None,
        description='API required by the ad if applicable. Refer to List: API Frameworks.',
    )
    banner: Banner | None = Field(
        None,
        description='Structured banner image object, recommended for simple banner creatives. Refer to Object: Banner.',
    )
    ctype: CreativeSubtypeDisplay | None = Field(
        None,
        description='Subtype of display creative. Refer to List: Creative Subtypes - Display.',
    )
    curl: Text | None = Field(
        None,
        description='Optional means of retrieving display markup by reference; a URL that can return HTML, AMPHTML, or a collection native `Asset` object and their subordinates). If this ad is matched to a Placement specification, the `Placement.curlx` attribute indicates if this markup retrieval option is supported. Note that including both `adm` and `curl` is not recommended.',
    )
    event: list[Event] | None = Field(
        None,
        description='Array of events that the advertiser or buying platform wants to track. Refer to Object: Event.',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    h: Count | None = Field(
        None,
        description='Absolute height of the creative in device independent pixels (DIPS), typically for non-native ads. Note that mixing absolute and relative sizes is not recommended.',
    )
    hratio: Count | None = Field(
        None,
        description='Relative height of the creative when expressing size as a ratio, typically for non-native ads. Note that mixing absolute and relative sizes is not recommended.',
    )
    mime: ExternalId | None = Field(
        None, description='Mime type of the ad (e.g., “image/jpeg”).'
    )
    native: Native | None = Field(
        None,
        description='Structured native object, recommended for native ads. Refer to Object: Native.',
    )
    priv: Text | None = Field(
        None,
        description="URL of a page informing the user about a buyer's targeting activity.",
    )
    w: Count | None = Field(
        None,
        description='Absolute width of the creative in device independent pixels (DIPS), typically for non-native ads. Note that mixing absolute and relative sizes is not recommended.',
    )
    wratio: Count | None = Field(
        None,
        description='Relative width of the creative when expressing size as a ratio, typically for non-native ads. Note that mixing absolute and relative sizes is not recommended.',
    )


class Dooh(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    content: Content | None = Field(
        None,
        description='Details about the content within the distribution channel. Refer to Object: Content.',
    )
    dpi: Count | None = Field(
        None,
        description='Minimum DPI for text-based creative elements to display clearly.',
    )
    etime: DurationSeconds | None = Field(
        None,
        description='The exposure time in seconds per view that the creative will be displayed before refreshing to the next creative.',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    fixed: DoohPlacementMobility | None = Field(
        None,
        description='Indicates whether the DOOH placement is in a fixed location (e.g., kiosk, billboard, elevator) or is movable (e.g., taxi), where 1 = fixed, 2 = movable.',
    )
    id: ExternalId | None = Field(
        None,
        description='Vendor-specific unique identifier of the distribution channel.',
    )
    name: Text | None = Field(
        None, description='Displayable name of the distribution channel.'
    )
    pub: Publisher | None = Field(
        None,
        description='Details about the publisher of the distribution channel. Refer to Object: Publisher.',
    )
    venue: Count | None = Field(
        None,
        description='The type of out-of-home venue. Refer to List: DOOH Venue TypesList: DOOH Venue Types.',
    )


class Site(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    amp: IntegerFlag | None = Field(
        None,
        description='Indicates if the page is built with AMP HTML, where 0 = no, 1 = yes.',
    )
    cat: list[ExternalId] | None = Field(
        None,
        description='Array of content categories describing the site using IDs from the taxonomy indicated in `cattax`.',
    )
    cattax: CategoryTaxonomy | None = Field(
        None,
        description='The taxonomy in use for the `cat`, `sectcat` and `pagecat` attributes. Refer to List: Category Taxonomies.',
    )
    content: Content | None = Field(
        None,
        description='Details about the content within the distribution channel. Refer to Object: Content.',
    )
    domain: Domain | None = Field(
        None, description='Domain of the site (e.g., “mysite.foo.com”).'
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    id: ExternalId | None = Field(
        None,
        description='Vendor-specific unique identifier of the distribution channel.',
    )
    keywords: Text | None = Field(
        None, description="This field is deprecated, use 'kwarray' instead."
    )
    kwarray: list[Text] | None = Field(
        None,
        description="Array of keywords about the site. Only one of 'keywords' or 'kwarray' may be present.",
    )
    mobile: IntegerFlag | None = Field(
        None,
        description='Indicates if the site has been programmed to optimize layout when viewed on mobile devices, where 0 = no, 1 = yes.',
    )
    name: Text | None = Field(
        None, description='Displayable name of the distribution channel.'
    )
    page: Text | None = Field(None, description='URL of the page within the site.')
    pagecat: list[ExternalId] | None = Field(
        None,
        description='Array of content categories describing the current page or view of the site using IDs from the taxonomy indicated in `cattax`.',
    )
    privpolicy: IntegerFlag | None = Field(
        None,
        description='Indicates if the site has a privacy policy, where 0 = no, 1 = yes.',
    )
    pub: Publisher | None = Field(
        None,
        description='Details about the publisher of the distribution channel. Refer to Object: Publisher.',
    )
    ref: Text | None = Field(
        None, description='Referrer URL that caused navigation to the current page.'
    )
    search: Text | None = Field(
        None, description='Search string that caused navigation to the current page.'
    )
    sectcat: list[ExternalId] | None = Field(
        None,
        description='Array of content categories describing the current section of the site using IDs from the taxonomy indicated in `cattax`.',
    )


class Ad(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    adomain: list[Domain] | None = Field(
        None,
        description='Advertiser domain; top two levels only (e.g., “ford.com”). This can be an array for the case of rotating creatives.',
    )
    attr: list[CreativeAttribute] | None = Field(
        None,
        description='Set of attributes describing the creative. Refer to List: Creative Attributes.',
    )
    audio: Audio | None = Field(
        None,
        description='Media Subtype Object that indicates this is an audio ad and provides additional detail as such. Refer to Object: Audio. * Required if no other media subtype object is specified.',
    )
    audit: Audit | None = Field(
        None,
        description='An object depicting the audit status of the ad; typically part of a quality/safety review process. Refer to Object: Audit.',
    )
    bundle: list[ExternalId] | None = Field(
        None,
        description='When the product of the ad is an app, the unique ID of that app as a bundle or package name (e.g., “com.foo.mygame”). This should NOT be an app store ID (e.g., no iTunes store IDs). This can be an array of for the case of rotating creatives.',
    )
    cat: list[ExternalId] | None = Field(
        None,
        description='Array of content categories describing the ad using IDs from the taxonomy indicated in `cattax`. Implementer should ensure compliance with regional legislation around data usage and sharing.',
    )
    cattax: CategoryTaxonomy | None = Field(
        2,
        description='The taxonomy in use for the `cat` attribute. Refer to List: Category Taxonomies.',
        validate_default=True,
    )
    display: Display | None = Field(
        None,
        description='Media Subtype Object that indicates this is a display ad and provides additional detail as such. Refer to Object: Display. * Required if no other media subtype object is specified.',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    id: ExternalId = Field(
        ...,
        description='ID of the creative; unique at least throughout the scope of a vendor (e.g., an exchange or buying platform). Note that multiple instances of the same ad when used in transactions must have the same ID.',
    )
    init: EpochMilliseconds | None = Field(
        None,
        description='Timestamp of the original instantiation of this ad (i.e., this object or any of its children) in Unix format (i.e., milliseconds since the epoch).',
    )
    iurl: Text | None = Field(
        None,
        description='URL without cache-busting to an image that is representative of the ad content for cursory level ad quality checking.',
    )
    lang: ExternalId | None = Field(
        None,
        description='Language of the creative using ISO-639-1-alpha-2. In practice, vendors using this object may elect an alternate standard (e.g., BCP-47) in which case this must be communicated beforehand. The non-standard code “xx” may also be used if the creative has no linguistic content (e.g., a banner with just a company logo).',
    )
    lastmod: EpochMilliseconds | None = Field(
        None,
        description='Timestamp of most recent modification to this ad (i.e., this object or any of its children other than the `Audit` object) in Unix format (i.e., milliseconds since the epoch).',
    )
    mrating: MediaRating | None = Field(
        None,
        description='Media rating per IQG guidelines. Refer to List: Media Ratings.',
    )
    secure: IntegerFlag | None = Field(
        None,
        description='Flag to indicate if the creative is secure (i.e., uses HTTPS for all assets and markup), where 0 = no, 1 = yes. There is no default and thus if omitted, the secure state is unknown. However, as a practical matter, the safe assumption is to treat unknown as non-secure.',
    )
    video: Video | None = Field(
        None,
        description='Media Subtype Object that indicates this is a video ad and provides additional detail as such. Refer to Object: Video. * Required if no other media subtype object is specified.',
    )


class App(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    bundle: ExternalId | None = Field(
        None,
        description='Bundle or package name of the app (e.g., “com.foo.mygame”) and should NOT be app store IDs (e.g., not iTunes store IDs).',
    )
    cat: list[ExternalId] | None = Field(
        None,
        description='Array of content categories describing the app using IDs from the taxonomy indicated in `cattax`.',
    )
    cattax: CategoryTaxonomy | None = Field(
        None,
        description='The taxonomy in use for the `cat`, `sectcat` and `pagecat` attributes. Refer to List: Category Taxonomies.',
    )
    content: Content | None = Field(
        None,
        description='Details about the content within the distribution channel. Refer to Object: Content.',
    )
    domain: Domain | None = Field(
        None, description='Domain of the app (e.g., “mygame.foo.com”).'
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    id: ExternalId | None = Field(
        None,
        description='Vendor-specific unique identifier of the distribution channel.',
    )
    keywords: Text | None = Field(
        None, description="This field is deprecated, use 'kwarray' instead."
    )
    kwarray: list[Text] | None = Field(
        None,
        description="Array of keywords about the app. Only one of 'keywords' or 'kwarray' may be present.",
    )
    name: Text | None = Field(
        None, description='Displayable name of the distribution channel.'
    )
    pagecat: list[ExternalId] | None = Field(
        None,
        description='Array of content categories describing the current page or view of the app using IDs from the taxonomy indicated in `cattax`.',
    )
    paid: IntegerFlag | None = Field(
        0,
        description='Indicator of whether or not this is a paid app, where 0 = free, 1 = paid.',
    )
    privpolicy: IntegerFlag | None = Field(
        None,
        description='Indicates if the app has a privacy policy, where 0 = no, 1 = yes.',
    )
    pub: Publisher | None = Field(
        None,
        description='Details about the publisher of the distribution channel. Refer to Object: Publisher.',
    )
    sectcat: list[ExternalId] | None = Field(
        None,
        description='Array of content categories describing the current section of the app using IDs from the taxonomy indicated in `cattax`.',
    )
    storeid: ExternalId | None = Field(
        None,
        description='The ID of the app in an app store (e.g., Apple iTunes, Google Play).',
    )
    storeurl: Text | None = Field(
        None, description='App store URL for an installed app; for IQG 2.1 compliance.'
    )
    ver: ExternalId | None = Field(None, description='Application version.')


class AssetFormat(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    data: DataAssetFormat | None = Field(
        None,
        description='Asset Format Subtype Object that indicates this is specifying a data asset and provides additional detail as such. Refer to Object: DataAssetFormat. * Required if no other asset format subtype object is specified.',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    id: Count = Field(
        ...,
        description='Asset ID, unique within the scope of this placement specification.',
    )
    img: ImageAssetFormat | None = Field(
        None,
        description='Asset Format Subtype Object that indicates this is specifying an image asset and provides additional detail as such. Refer to Object: ImageAssetFormat. * Required if no other asset format subtype object is specified.',
    )
    req: IntegerFlag | None = Field(
        0,
        description='Indicator of whether or not this asset is required, where 0 = no, 1 = yes.',
    )
    title: TitleAssetFormat | None = Field(
        None,
        description='Asset Format Subtype Object that indicates this is specifying a title asset and provides additional detail as such. Refer to Object: TitleAssetFormat. * Required if no other asset format subtype object is specified.',
    )
    video: VideoPlacement | None = Field(
        None,
        description='Asset Format Subtype Object, which leverages the `VideoPlacement` object, that indicates this is specifying a video asset and provides additional detail as such. Refer to Object: VideoPlacement. * Required if no other asset format subtype object is specified.',
    )


class AudioPlacement(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    api: list[ApiFramework] | None = Field(
        None,
        description='List of supported APIs for this placement. If an API is not explicitly listed, it is assumed to be unsupported. Refer to List: API Frameworks.',
    )
    comp: list[Companion] | None = Field(
        None,
        description='Array of objects indicating that companion ads are available and providing the specifications thereof. Refer to Object: Companion.',
    )
    comptype: list[CompanionType] | None = Field(
        None,
        description='Supported companion ad types; recommended if companion ads are specified in `comp`. Refer to List: Companion Types.',
    )
    ctype: list[CreativeSubtypeAudioVideo] | None = Field(
        None,
        description='Creative subtypes permitted for this placement. Refer to List: Creative Subtypes - Audio/Video.',
    )
    delay: StartDelayMode | None = Field(
        None,
        description='Indicates the start delay in seconds for pre-roll, mid-roll, or post-roll placements. For additional generic values, refer to List: Start Delay Modes.',
    )
    delivery: list[DeliveryMethod] | None = Field(
        None,
        description='Array of supported creative delivery methods. If omitted, all can be assumed. Refer to List: Delivery Methods.',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    feed: FeedType | None = Field(
        None,
        description='Type of audio feed of this placement. Refer to List: Feed Types.',
    )
    maxbitr: Count | None = Field(
        None, description='Maximum bit rate of the creative in Kbps.'
    )
    maxdur: DurationSeconds | None = Field(
        None,
        description='Maximum creative duration in seconds. This field is mutually exclusive with rqddurs; only one of maxdur and rqddurs may be in a bid request.',
    )
    maxext: ExtendedDuration | None = Field(
        None,
        description='Maximum extended creative duration if extension is allowed. If 0, extension is not allowed. If -1, extension is allowed and there is no time limit imposed. If greater than 0, then the value represents the number of seconds of extended play supported beyond the `maxdur` value.',
    )
    maxseq: Count | None = Field(
        None, description='The maximum number of ads that can be played in an ad pod.'
    )
    mime: list[ExternalId] | None = Field(
        None,
        description='Array of supported mime types (e.g., “audio/mp4”). If omitted, all types are assumed.',
    )
    minbitr: Count | None = Field(
        None, description='Minimum bit rate of the creative in Kbps.'
    )
    mincpmpersec: Measure | None = Field(
        None,
        description='Minimum CPM per second. This is a price floor for the “dynamic” portion of a video ad pod, relative to the duration of bids an advertiser may submit.',
    )
    mindur: DurationSeconds | None = Field(
        None,
        description='Minimum creative duration in seconds. This field is mutually exclusive with rqddurs; only one of mindur and rqddurs may be in a bid request.',
    )
    nvol: VolumeNormalizationMode | None = Field(
        None,
        description='Volume normalization mode of this placement. Refer to List: Volume Normalization Modes.',
    )
    overlayexpdir: list[ExpandableDirection] | None = Field(
        None,
        description='Directions in which the creative (overlay) is permitted to expand. Refer to List: Expandable Directions.',
    )
    playend: PlaybackCessationMode | None = Field(
        None,
        description='The event that causes playback to end for this placement. Refer to List: Playback Cessation Modes.',
    )
    playmethod: list[PlaybackMethod] | None = Field(
        None,
        description='Playback method(s) in use for this placement. Refer to List: Playback Methods.',
    )
    poddur: DurationSeconds | None = Field(
        None,
        description='Indicates the total amount of time in seconds that advertisers may fill for a “dynamic” video ad pod, or the dynamic portion of a “hybrid” ad pod. This field is required only for the dynamic portion(s) of video ad pods. This field refers to the length of the entire ad break, whereas mindur/maxdur/rqddurs are constraints relating to the slots that make up the pod.',
    )
    podid: IntegerId | None = Field(
        None,
        description='Unique identifier indicating that an impression opportunity belongs to a video ad pod. If multiple impression opportunities within a bid request share the same podid, this indicates that those impression opportunities belong to the same video ad pod.',
    )
    podseq: PodSequence | None = Field(
        0,
        description='The sequence (position) of the video ad pod within a content stream. Refer to List: List: Pod Sequence for guidance on the use of this field.',
    )
    rqddurs: list[DurationSeconds] | None = Field(
        None,
        description="Precise acceptable durations for video creatives in seconds. This field specifically targets the Live TV use case where non-exact ad durations would result in undesirable 'dead air'. This field is mutually exclusive with mindur and maxdur; if rqddurs is specified, mindur and maxdur must not be specified and vice versa.",
    )
    skip: IntegerFlag | None = Field(
        None,
        description='Indicates if the placement imposes ad skippability, where 0 = no, 1 = yes.',
    )
    skipafter: Count | None = Field(
        0,
        description='Number of seconds a creative must play before the placement enables skipping; only applicable if the ad is skippable.',
        validate_default=True,
    )
    skipmin: DurationSeconds | None = Field(
        0,
        description='The placement allows creatives of total duration greater than this number of seconds to be skipped; only applicable if the ad is skippable.',
        validate_default=True,
    )
    slotinpod: SlotPositionInPod | None = Field(
        0,
        description='For video ad pods, this value indicates that the seller can guarantee delivery against the indicated slot position in the pod. Refer to List: List: Slot Position in Pod for guidance on the use of this field.',
    )


class Companion(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    display: DisplayPlacement | None = Field(
        None,
        description='Display specification object representing the companion ad. Refer to Object: DisplayPlacement.',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    id: ExternalId | None = Field(
        None,
        description='Identifier of the companion ad; unique within this placement.',
    )
    vcm: IntegerFlag | None = Field(
        None,
        description='Indicates the companion ad rendering mode relative to the associated video or audio ad, where 0 = concurrent, 1 = end-card. For a given placement, typically only one companion at most should be designated as an end card.',
    )


class DisplayPlacement(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    ampren: AmpRenderingTreatment | None = Field(
        None,
        description='AMPHTML rendering treatment for AMP ads in this placement, where 1 = early loading, 2 = standard loading.',
    )
    api: list[ApiFramework] | None = Field(
        None,
        description='List of supported APIs. If an API is not explicitly listed, it is assumed to be unsupported. Refer to List: API Frameworks.',
    )
    clktype: ClickType | None = Field(
        1,
        description='Indicates the click type of this placement. Refer to List: Click Types.',
        validate_default=True,
    )
    context: DisplayContextType | None = Field(
        None,
        description='The context of the placement. Refer to List: Display Context Types.',
    )
    ctype: list[CreativeSubtypeDisplay] | None = Field(
        None,
        description='Creative subtypes permitted. Refer to List: Creative Subtypes - Display.',
    )
    displayfmt: list[DisplayFormat] | None = Field(
        None,
        description='Array of objects that govern the attributes (e.g., sizes) of a banner display placement. Refer to Object: DisplayFormat.',
    )
    event: list[EventSpec] | None = Field(
        None,
        description='Array of supported ad tracking events. Refer to Object: EventSpec.',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    h: Count | None = Field(
        None,
        description='Width of the placement in units specified by `unit`. Note that this size applies to the placement itself; permitted creative sizes are specified elsewhere (e.g., `DisplayFormat`, `ImageAssetFormat`, etc.).',
    )
    ifrbust: list[ExternalId] | None = Field(
        None,
        description='Array of iframe busters supported by this placement. The meaning of strings in this attribute must be coordinated beforehand among vendors.',
    )
    instl: IntegerFlag | None = Field(
        0,
        description='Indicates if this is an interstitial placement, where 0 = no, 1 = yes.',
    )
    mime: list[ExternalId] | None = Field(
        None,
        description='Array of supported mime types (e.g., “image/jpeg”, “image/gif”). If omitted, all types are assumed.',
    )
    nativefmt: NativeFormat | None = Field(
        None,
        description='This object specified the required and permitted assets and attributes of a native display placement. Refer to Object: NativeFormat.',
    )
    pos: PlacementPosition | None = Field(
        None,
        description='Placement position on screen. Refer to List: Placement Positions.',
    )
    priv: IntegerFlag | None = Field(
        0,
        description='Indicator of whether or not the placement supports a buyer-specific privacy notice URL, where 0 = no, 1 = yes.',
    )
    ptype: DisplayPlacementType | None = Field(
        None,
        description='The display placement type. Refer to List: Display Placement Types.',
    )
    topframe: IntegerFlag | None = Field(
        None,
        description='Indicates if the placement will be loaded into an iframe or not, where 0 = unfriendly iframe or unknown, 1 = top frame, friendly iframe, or SafeFrame. A value of "1" can be understood to mean that expandable ads are technically capable of being delivered.',
    )
    unit: SizeUnit | None = Field(
        1,
        description='Unit of size used for placement size (i.e., `w` and `h` attributes). Refer to List: Size Units.',
    )
    w: Count | None = Field(
        None,
        description='Width of the placement in units specified by `unit`. Note that this size applies to the placement itself; permitted creative sizes are specified elsewhere (e.g., `DisplayFormat`, `ImageAssetFormat`, etc.).',
    )


class NativeFormat(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    asset: list[AssetFormat] = Field(
        ...,
        description='Array of objects that specify the set of native assets and their permitted formats. Refer to Object: AssetFormat.',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')


class Placement(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    admx: IntegerFlag | None = Field(
        None,
        description='Indicates if including markup is supported (i.e., the various `adm` attributes throughout the `Placement` structure), where 0 = no, 1 = yes.',
    )
    audio: AudioPlacement | None = Field(
        None,
        description='Placement Subtype Object that indicates that this may be an audio placement and provides additional detail related thereto. Refer to Object: AudioPlacement. * At least one placement subtype object is required.',
    )
    curlx: IntegerFlag | None = Field(
        None,
        description='Indicates if retrieving markup via URL reference is supported (i.e., the various `curl` attributes throughout the `Placement` structure), where 0 = no, 1 = yes.',
    )
    display: DisplayPlacement | None = Field(
        None,
        description='Placement Subtype Object that indicates that this may be a display placement and provides additional detail related thereto. Refer to Object: DisplayPlacement. * At least one placement subtype object is required.',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    reward: IntegerFlag | None = Field(
        0,
        description='Indicates whether the user recieves a reward for viewing the ad, where 0 = no, 1 = yes. Typcially video ad implementations allow users to read an additional news article for free, receive an extra life in a game, or get a sponsored ad-free music session. The reward is typically distributed after the video ad is completed.',
    )
    sdk: Text | None = Field(
        None,
        description='Name of ad mediation partner, SDK technology, or player responsible for rendering ad (typically video, audio, or mobile); used by some ad servers to customize ad code by partner.',
    )
    sdkver: ExternalId | None = Field(
        None, description='Version of the SDK specified in the `sdk` attribute.'
    )
    secure: IntegerFlag | None = Field(
        None,
        description='Flag to indicate if the creative is secure (i.e., uses HTTPS for all assets and markup), where 0 = no, 1 = yes. There is no default and thus if omitted, the secure state is unknown. However, as a practical matter, the safe assumption is to treat unknown as non-secure.',
    )
    ssai: ServerSideAdInsertionMode | None = Field(
        0,
        description='Indicates if server-side ad insertion (e.g., stitching an ad into an audio or video stream) is in use and the impact of this on asset and tracker retrieval, where 0 = status unknown, 1 = all client-side (i.e., not server-side), 2 = assets stitched server-side but tracking pixels fired client-side, 3 = all server-side.',
    )
    tagid: ExternalId | None = Field(
        None,
        description='Identifier for specific ad placement or ad tag; unique within a distribution channel.',
    )
    video: VideoPlacement | None = Field(
        None,
        description='Placement Subtype Object that indicates that this may be a video placement and provides additional detail related thereto. Refer to Object: VideoPlacement. * At least one placement subtype object is required.',
    )
    wlang: list[ExternalId] | None = Field(
        None,
        description='Allow list of permitted languages of the creative using ISO-639-1-alpha-2. In practice, vendors using this object may elect an alternate standard (e.g., BCP-47) in which case this must be communicated beforehand. Omission of this attribute indicates there are no restrictions.',
    )


class VideoPlacement(SpecModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    api: list[ApiFramework] | None = Field(
        None,
        description='List of supported APIs for this placement. If an API is not explicitly listed, it is assumed to be unsupported. Refer to List: API Frameworks.',
    )
    boxing: IntegerFlag | None = Field(
        1,
        description='Indicates if letterboxing of 4:3 creatives into a 16:9 window is allowed, where 0 = no, 1 = yes.',
    )
    clktype: ClickType | None = Field(
        None,
        description='Indicates the click type of the placement. Refer to List: Click Types.',
    )
    comp: list[Companion] | None = Field(
        None,
        description='Array of objects indicating that companion ads are available and providing the specifications thereof. Refer to Object: Companion.',
    )
    comptype: list[CompanionType] | None = Field(
        None,
        description='Supported companion ad types; recommended if companion ads are specified in `comp`. Refer to List: Companion Types.',
    )
    ctype: list[CreativeSubtypeAudioVideo] | None = Field(
        None,
        description='Creative subtypes permitted for this placement. Refer to List: Creative Subtypes - Audio/Video.',
    )
    delay: StartDelayMode | None = Field(
        None,
        description='Indicates the start delay in seconds for pre-roll, mid-roll, or post-roll placements. For additional generic values, refer to List: Start Delay Modes.',
    )
    delivery: list[DeliveryMethod] | None = Field(
        None,
        description='Array of supported creative delivery methods. If omitted, all can be assumed. Refer to List: Delivery Methods.',
    )
    expdir: list[ExpandableDirection] | None = Field(
        None,
        description='Directions in which the creative (video placement) is permitted to expand. Refer to List: Expandable Directions.',
    )
    ext: Ext | None = Field(None, description='Optional vendor-specific extensions.')
    h: Count | None = Field(
        None, description='Height of the placement in units specified by `unit`.'
    )
    linear: LinearityMode | None = Field(
        None,
        description='Indicates if the creative must be linear, nonlinear, etc. If none specified, no restrictions are assumed. Refer to List: Linearity Modes. Note that this field describes the expected VAST response and not whether a placement is in-stream, out-stream, etc. For that, see `ptype`.',
    )
    maxbitr: Count | None = Field(
        None, description='Maximum bit rate of the creative in Kbps.'
    )
    maxdur: DurationSeconds | None = Field(
        None,
        description='Maximum creative duration in seconds. This field is mutually exclusive with rqddurs; only one of maxdur and rqddurs may be in a bid request.',
    )
    maxext: ExtendedDuration | None = Field(
        0,
        description='Maximum extended creative duration if extension is allowed. If 0, extension is not allowed. If -1, extension is allowed and there is no time limit imposed. If greater than 0, then the value represents the number of seconds of extended play supported beyond the `maxdur` value.',
        validate_default=True,
    )
    maxseq: Count | None = Field(
        None, description='The maximum number of ads that can be played in an ad pod.'
    )
    mime: list[ExternalId] | None = Field(
        None,
        description='Array of supported mime types (e.g., “video/mp4”). If omitted, all types are assumed.',
    )
    minbitr: Count | None = Field(
        None, description='Minimum bit rate of the creative in Kbps.'
    )
    mincpmpersec: Measure | None = Field(
        None,
        description='Minimum CPM per second. This is a price floor for the “dynamic” portion of a video ad pod, relative to the duration of bids an advertiser may submit.',
    )
    mindur: DurationSeconds | None = Field(
        None,
        description='Minimum creative duration in seconds. This field is mutually exclusive with rqddurs; only one of mindur and rqddurs may be in a bid request.',
    )
    overlayexpdir: list[ExpandableDirection] | None = Field(
        None,
        description='Directions in which the creative (video overlay) is permitted to expand. This is primarily used for non-linear videos. Refer to List: Expandable Directions.',
    )
    playend: PlaybackCessationMode | None = Field(
        None,
        description='The event that causes playback to end for this placement. Refer to List: Playback Cessation Modes.',
    )
    playmethod: list[PlaybackMethod] | None = Field(
        None,
        description='Playback method(s) in use for this placement. Refer to List: Playback Methods.',
    )
    poddur: DurationSeconds | None = Field(
        None,
        description='Indicates the total amount of time in seconds that advertisers may fill for a “dynamic” video ad pod, or the dynamic portion of a “hybrid” ad pod. This field is required only for the dynamic portion(s) of video ad pods. This field refers to the length of the entire ad break, whereas mindur/maxdur/rqddurs are constraints relating to the slots that make up the pod.',
    )
    podid: IntegerId | None = Field(
        None,
        description='Unique identifier indicating that an impression opportunity belongs to a video ad pod. If multiple impression opportunities within a bid request share the same podid, this indicates that those impression opportunities belong to the same video ad pod.',
    )
    podseq: PodSequence | None = Field(
        0,
        description='The sequence (position) of the video ad pod within a content stream. Refer to List: List: Pod Sequence for guidance on the use of this field.',
    )
    pos: PlacementPosition | None = Field(
        None,
        description='Placement position on screen. Refer to List: Placement Positions.',
    )
    ptype: PlcmtSubtypeVideo | None = Field(
        None, description='Placement subtype. Refer to List: Plcmt Subtypes - Video.'
    )
    rqddurs: list[DurationSeconds] | None = Field(
        None,
        description="Precise acceptable durations for video creatives in seconds. This field specifically targets the Live TV use case where non-exact ad durations would result in undesirable 'dead air'. This field is mutually exclusive with mindur and maxdur; if rqddurs is specified, mindur and maxdur must not be specified and vice versa.",
    )
    skip: IntegerFlag | None = Field(
        None,
        description='Indicates if the placement imposes ad skippability, where 0 = no, 1 = yes.',
    )
    skipafter: Count | None = Field(
        0,
        description='Number of seconds a creative must play before the placement enables skipping; only applicable if the ad is skippable.',
        validate_default=True,
    )
    skipmin: DurationSeconds | None = Field(
        0,
        description='The placement allows creatives of total duration greater than this number of seconds to be skipped; only applicable if the ad is skippable.',
        validate_default=True,
    )
    slotinpod: SlotPositionInPod | None = Field(
        0,
        description='For video ad pods, this value indicates that the seller can guarantee delivery against the indicated slot position in the pod. Refer to List: List: Slot Position in Pod for guidance on the use of this field.',
    )
    unit: SizeUnit | None = Field(
        1,
        description='Units of size used for `w` and `h` attributes. Refer to List: Size Units.',
    )
    w: Count | None = Field(
        None, description='Width of the placement in units specified by `unit`.'
    )


AssetFormat.model_rebuild()
AudioPlacement.model_rebuild()
Companion.model_rebuild()
DisplayPlacement.model_rebuild()
Placement.model_rebuild()

# The published node each type was generated from. Every verdict and every check reads it
# off the class, so no table, filename or name-keyed lookup stands between a type and the
# schema it has to answer for.
Ad.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/Ad'
App.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/App'
Asset.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/Asset'
AssetFormat.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/AssetFormat'
Audio.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/Audio'
AudioPlacement.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/AudioPlacement'
Audit.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/Audit'
Banner.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/Banner'
BrandVersion.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/BrandVersion'
Channel.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/Channel'
Companion.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/Companion'
Content.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/Content'
Corr.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/Corr'
Data.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/Data'
DataAsset.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/DataAsset'
DataAssetFormat.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/DataAssetFormat'
Device.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/Device'
Display.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/Display'
DisplayFormat.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/DisplayFormat'
DisplayPlacement.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/DisplayPlacement'
Dooh.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/Dooh'
Event.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/Event'
EventSpec.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/EventSpec'
Ext.SCHEMA = 'https://jsonspecs.com/adcom/schemas/kernel/1/kernel.json#/$defs/Ext'
ExtendedIdentifierUids.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/ExtendedIdentifierUids'
ExtendedIdentifiers.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/ExtendedIdentifiers'
Geo.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/Geo'
ImageAsset.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/ImageAsset'
ImageAssetFormat.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/ImageAssetFormat'
LinkAsset.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/LinkAsset'
Native.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/Native'
NativeFormat.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/NativeFormat'
Network.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/Network'
Placement.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/Placement'
Producer.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/Producer'
Publisher.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/Publisher'
Regs.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/Regs'
Restrictions.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/Restrictions'
Segment.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/Segment'
Site.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/Site'
TitleAsset.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/TitleAsset'
TitleAssetFormat.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/TitleAssetFormat'
User.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/User'
UserAgent.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/UserAgent'
Video.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/Video'
VideoAsset.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/VideoAsset'
VideoPlacement.SCHEMA = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/VideoPlacement'

# The tree states a cycle, so a type above may name one below it. Each is rebuilt once
# every name in this module is bound, which is what resolves the forward references.
Ad.model_rebuild()
App.model_rebuild()
Asset.model_rebuild()
AssetFormat.model_rebuild()
Audio.model_rebuild()
AudioPlacement.model_rebuild()
Audit.model_rebuild()
Banner.model_rebuild()
BrandVersion.model_rebuild()
Channel.model_rebuild()
Companion.model_rebuild()
Content.model_rebuild()
Corr.model_rebuild()
Data.model_rebuild()
DataAsset.model_rebuild()
DataAssetFormat.model_rebuild()
Device.model_rebuild()
Display.model_rebuild()
DisplayFormat.model_rebuild()
DisplayPlacement.model_rebuild()
Dooh.model_rebuild()
Event.model_rebuild()
EventSpec.model_rebuild()
Ext.model_rebuild()
ExtendedIdentifierUids.model_rebuild()
ExtendedIdentifiers.model_rebuild()
Geo.model_rebuild()
ImageAsset.model_rebuild()
ImageAssetFormat.model_rebuild()
LinkAsset.model_rebuild()
Native.model_rebuild()
NativeFormat.model_rebuild()
Network.model_rebuild()
Placement.model_rebuild()
Producer.model_rebuild()
Publisher.model_rebuild()
Regs.model_rebuild()
Restrictions.model_rebuild()
Segment.model_rebuild()
Site.model_rebuild()
TitleAsset.model_rebuild()
TitleAssetFormat.model_rebuild()
User.model_rebuild()
UserAgent.model_rebuild()
Video.model_rebuild()
VideoAsset.model_rebuild()
VideoPlacement.model_rebuild()
