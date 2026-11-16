"""Every integer-coded vocabulary of the published tree, each code under its published name.

**This module is written by the target and not by the generator it drives.** A code's
name is a decision the schema stage made and published on the code's own branch, and no
surveyed generator reads it, so a delegated vocabulary would carry a name nobody decided
(target rules § 6). Every name here is the published one, written verbatim.

An open vocabulary also needs a type an application can extend, which an alternation is
not. Each vocabulary therefore has branch classes: its listed codes, and, where the list
reserves codes it does not state, its extension point. A branch subclasses its base, so
the bases take their branches in this module's trailer rather than in their own bodies.

A primitive whose values are a few titled codes and which publishes a name for none of
them is written here too, because the generator renders it as an enumeration whose
members it names from the titles -- which is a name nobody decided. Its values are its
codes and it carries no name for any of them.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import ClassVar, Literal

from ._runtime import SpecRootModel, Vocabulary
from ._scalars import MediaOffset, VendorCode

__all__ = [
    'AgentType',
    'AgentTypeCode',
    'AgentTypeExtension',
    'AmpRenderingTreatment',
    'AmpRenderingTreatmentCode',
    'ApiFramework',
    'ApiFrameworkCode',
    'ApiFrameworkExtension',
    'AuditStatusCode',
    'AuditStatusCodeCode',
    'AuditStatusCodeExtension',
    'AutoRefreshTrigger',
    'AutoRefreshTriggerCode',
    'CategoryTaxonomy',
    'CategoryTaxonomyCode',
    'CategoryTaxonomyExtension',
    'ClickType',
    'ClickTypeCode',
    'ClickTypeExtension',
    'CompanionType',
    'CompanionTypeCode',
    'ConnectionType',
    'ConnectionTypeCode',
    'ContentContext',
    'ContentContextCode',
    'CreativeAttribute',
    'CreativeAttributeCode',
    'CreativeAttributeExtension',
    'CreativeSubtypeAudioVideo',
    'CreativeSubtypeAudioVideoCode',
    'CreativeSubtypeDisplay',
    'CreativeSubtypeDisplayCode',
    'DeliveryMethod',
    'DeliveryMethodCode',
    'DeviceType',
    'DeviceTypeCode',
    'DisplayContextType',
    'DisplayContextTypeCode',
    'DisplayContextTypeExtension',
    'DisplayPlacementType',
    'DisplayPlacementTypeCode',
    'DisplayPlacementTypeExtension',
    'DoohMultiplierMeasurementSourceType',
    'DoohMultiplierMeasurementSourceTypeCode',
    'DoohPlacementMobility',
    'DoohPlacementMobilityCode',
    'DoohVenueTaxonomy',
    'DoohVenueTaxonomyCode',
    'EventTrackingMethod',
    'EventTrackingMethodCode',
    'EventTrackingMethodExtension',
    'EventType',
    'EventTypeCode',
    'EventTypeExtension',
    'ExpandableDirection',
    'ExpandableDirectionCode',
    'FeedType',
    'FeedTypeCode',
    'FeedTypeExtension',
    'IdMatchMethod',
    'IdMatchMethodCode',
    'IdMatchMethodExtension',
    'IntegerFlag',
    'IpLocationService',
    'IpLocationServiceCode',
    'LinearityMode',
    'LinearityModeCode',
    'LocationType',
    'LocationTypeCode',
    'MediaRating',
    'MediaRatingCode',
    'NativeDataAssetType',
    'NativeDataAssetTypeCode',
    'NativeDataAssetTypeExtension',
    'NativeImageAssetType',
    'NativeImageAssetTypeCode',
    'NativeImageAssetTypeExtension',
    'OperatingSystem',
    'OperatingSystemCode',
    'OperatingSystemExtension',
    'PlacementPosition',
    'PlacementPositionCode',
    'PlaybackCessationMode',
    'PlaybackCessationModeCode',
    'PlaybackMethod',
    'PlaybackMethodCode',
    'PlcmtSubtypeVideo',
    'PlcmtSubtypeVideoCode',
    'PodDeduplicationSetting',
    'PodDeduplicationSettingCode',
    'PodSequence',
    'PodSequenceCode',
    'ProductionQuality',
    'ProductionQualityCode',
    'ServerSideAdInsertionMode',
    'ServerSideAdInsertionModeCode',
    'SizeUnit',
    'SizeUnitCode',
    'SlotPositionInPod',
    'SlotPositionInPodCode',
    'StartDelayMode',
    'StartDelayModeCode',
    'StartDelayModeExtension',
    'UserAgentSource',
    'UserAgentSourceCode',
    'VolumeNormalizationMode',
    'VolumeNormalizationModeCode',
]


class IntegerFlag(SpecRootModel[Literal[0, 1]]):
    """The values of IntegerFlag.

    A yes or no written as an integer, `0` for no and `1` for yes, as AdCOM 1.0 and OpenRTB 2.6
    write their flags, such as a placement's `instl`. A receiver reads it as a flag, never as a
    count, and a field that takes it keeps the integer its text writes.

    Its values are the codes 0 (No), 1 (Yes) and no others. The schema publishes no name for any
    of them, so this type carries none: a name is a decision and this is not the stage that
    makes it.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/kernel/1/kernel.json#/$defs/IntegerFlag'

    root: Literal[0, 1]


class AgentType(Vocabulary[Literal[1, 2, 3] | VendorCode]):
    """List: Agent Types

    The codes of List: Agent Types

    The list reserves codes it does not state, so this vocabulary is open: a value is one of the
    codes below or a value of VendorCode. AgentTypeExtension is the extension point, and an
    application names its own code by subclassing it.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/AgentType'

    BROWSER_OR_DEVICE_ID: ClassVar[Literal[1]] = 1
    """Browser or device ID

    An ID which is tied to a specific web browser or device (cookie-based, probabilistic, or
    other).
    """
    IN_APP_IMPRESSIONS: ClassVar[Literal[2]] = 2
    """In-app impressions

    In-app impressions, which will typically contain a type of device ID (or rather, the
    privacy-compliant versions of device IDs).
    """
    PERSON_BASED_ID: ClassVar[Literal[3]] = 3
    """Person-based ID

    A person-based ID, i.e., that is the same across devices.
    """

    CODES: ClassVar[Mapping[int, str]] = {
        1: 'BROWSER_OR_DEVICE_ID',
        2: 'IN_APP_IMPRESSIONS',
        3: 'PERSON_BASED_ID',
    }


class AgentTypeCode(AgentType):
    """One of the codes List: Agent Types states."""
    root: Literal[1, 2, 3]


class AgentTypeExtension(AgentType):
    """Vendor-specific: a value of VendorCode, which is this vocabulary's extension point.

    Vendor-specific codes.

    An application carries its own code by subclassing this class and naming the code in its own
    `CODES`. The published schema already admits the value, so the verdict does not change.
    """
    root: VendorCode


class ApiFramework(Vocabulary[Literal[1, 2, 3, 4, 5, 6, 7, 8, 9] | VendorCode]):
    """List: API Frameworks

    The codes of List: API Frameworks

    The list reserves codes it does not state, so this vocabulary is open: a value is one of the
    codes below or a value of VendorCode. ApiFrameworkExtension is the extension point, and an
    application names its own code by subclassing it.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/ApiFramework'

    VPAID_1_0: ClassVar[Literal[1]] = 1
    """VPAID 1.0"""
    VPAID_2_0: ClassVar[Literal[2]] = 2
    """VPAID 2.0"""
    MRAID_1_0: ClassVar[Literal[3]] = 3
    """MRAID 1.0"""
    ORMMA: ClassVar[Literal[4]] = 4
    """ORMMA"""
    MRAID_2_0: ClassVar[Literal[5]] = 5
    """MRAID 2.0"""
    MRAID_3_0: ClassVar[Literal[6]] = 6
    """MRAID 3.0"""
    OMID_1_0: ClassVar[Literal[7]] = 7
    """OMID 1.0"""
    SIMID_1_0: ClassVar[Literal[8]] = 8
    """SIMID 1.0"""
    SIMID_1_1: ClassVar[Literal[9]] = 9
    """SIMID 1.1"""

    CODES: ClassVar[Mapping[int, str]] = {
        1: 'VPAID_1_0',
        2: 'VPAID_2_0',
        3: 'MRAID_1_0',
        4: 'ORMMA',
        5: 'MRAID_2_0',
        6: 'MRAID_3_0',
        7: 'OMID_1_0',
        8: 'SIMID_1_0',
        9: 'SIMID_1_1',
    }


class ApiFrameworkCode(ApiFramework):
    """One of the codes List: API Frameworks states."""
    root: Literal[1, 2, 3, 4, 5, 6, 7, 8, 9]


class ApiFrameworkExtension(ApiFramework):
    """Vendor-specific: a value of VendorCode, which is this vocabulary's extension point.

    Vendor-specific codes.

    An application carries its own code by subclassing this class and naming the code in its own
    `CODES`. The published schema already admits the value, so the verdict does not change.
    """
    root: VendorCode


class AuditStatusCode(Vocabulary[Literal[1, 2, 3, 4, 5, 6] | VendorCode]):
    """List: Audit Status Codes

    The codes of List: Audit Status Codes

    The list reserves codes it does not state, so this vocabulary is open: a value is one of the
    codes below or a value of VendorCode. AuditStatusCodeExtension is the extension point, and
    an application names its own code by subclassing it.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/AuditStatusCode'

    PENDING_AUDIT: ClassVar[Literal[1]] = 1
    """Pending Audit

    Pending Audit: An audit has not yet been completed on this ad. A recommendation cannot be
    made to use this ad, but vendors' policies may override.
    """
    PRE_APPROVED: ClassVar[Literal[2]] = 2
    """Pre-Approved

    Pre-Approved: An audit has not yet been completed on this ad. Subject to vendors' policies,
    it can be recommended for use. However, once the audit has been completed, its status will
    change and it may or may not be approved for continued use.
    """
    APPROVED: ClassVar[Literal[3]] = 3
    """Approved

    Approved: The audit is complete and the ad is approved for use. Note, however, that some
    attributes (e.g., `adomain`, `cat`, `attr`, etc.) may have been changed in the process by
    the auditor.
    """
    DENIED: ClassVar[Literal[4]] = 4
    """Denied

    Denied: The audit is complete, but the ad has been found unacceptable in some material
    aspect and is disapproved for use.
    """
    CHANGED_RESUBMISSION_REQUESTED: ClassVar[Literal[5]] = 5
    """Changed; Resubmission Requested

    Changed; Resubmission Requested: A version of the ad has been detected in use that is
    materially different from the version that was previously audited, which may result in
    rejection during use until the ad is resubmitted for audit and approved. Vendors need to
    communicate offline as to the criteria that constitutes a material change.
    """
    EXPIRED: ClassVar[Literal[6]] = 6
    """Expired

    Expired: The ad has been marked as expired by the vendor. Vendors need to communicate
    offline as to the expected bidding behavior for ads with this status.
    """

    CODES: ClassVar[Mapping[int, str]] = {
        1: 'PENDING_AUDIT',
        2: 'PRE_APPROVED',
        3: 'APPROVED',
        4: 'DENIED',
        5: 'CHANGED_RESUBMISSION_REQUESTED',
        6: 'EXPIRED',
    }


class AuditStatusCodeCode(AuditStatusCode):
    """One of the codes List: Audit Status Codes states."""
    root: Literal[1, 2, 3, 4, 5, 6]


class AuditStatusCodeExtension(AuditStatusCode):
    """Vendor-specific: a value of VendorCode, which is this vocabulary's extension point.

    Vendor-specific codes.

    An application carries its own code by subclassing this class and naming the code in its own
    `CODES`. The published schema already admits the value, so the verdict does not change.
    """
    root: VendorCode


class AutoRefreshTrigger(Vocabulary[Literal[0, 1, 2, 3]]):
    """List: Auto Refresh Triggers

    The codes of List: Auto Refresh Triggers

    The list states every code it has, so this vocabulary is closed: no other value is accepted.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/AutoRefreshTrigger'

    UNKNOWN: ClassVar[Literal[0]] = 0
    """UNKNOWN"""
    USER_ACTION: ClassVar[Literal[1]] = 1
    """User Action

    User Action: Refresh triggered by user-initiated action such as scrolling.
    """
    EVENT: ClassVar[Literal[2]] = 2
    """Event

    Event: Event-driven content change. For example, ads refresh when the football game score
    changes on the page.
    """
    TIME: ClassVar[Literal[3]] = 3
    """Time

    Time:Time-based refresh. Ads refresh on a predefined time interval even without user
    activity.
    """

    CODES: ClassVar[Mapping[int, str]] = {
        0: 'UNKNOWN',
        1: 'USER_ACTION',
        2: 'EVENT',
        3: 'TIME',
    }


class AutoRefreshTriggerCode(AutoRefreshTrigger):
    """One of the codes List: Auto Refresh Triggers states."""
    root: Literal[0, 1, 2, 3]


class CategoryTaxonomy(Vocabulary[Literal[1, 2, 3, 4, 5, 6, 7, 8, 9] | VendorCode]):
    """List: Category Taxonomies

    The codes of List: Category Taxonomies

    The list reserves codes it does not state, so this vocabulary is open: a value is one of the
    codes below or a value of VendorCode. CategoryTaxonomyExtension is the extension point, and
    an application names its own code by subclassing it.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/CategoryTaxonomy'

    CONTENT_CATEGORY_TAXONOMY_1_0: ClassVar[Literal[1]] = 1
    """IAB Tech Lab Content Category Taxonomy 1.0

    IAB Tech Lab Content Category Taxonomy 1.0: Deprecated, and recommend NOT be used since it
    does not have SCD flags.
    """
    CONTENT_CATEGORY_TAXONOMY_2_0: ClassVar[Literal[2]] = 2
    """IAB Tech Lab Content Category Taxonomy 2.0

    IAB Tech Lab Content Category Taxonomy 2.0: Deprecated, and recommend NOT be used since it
    does not have SCD flags.
    """
    IAB_TECH_LAB_AD_PRODUCT_TAXONOMY_1_0: ClassVar[Literal[3]] = 3
    """IAB Tech Lab Ad Product Taxonomy 1.0

    IAB Tech Lab Ad Product Taxonomy 1.0.
    """
    IAB_TECH_LAB_AUDIENCE_TAXONOMY_1_1: ClassVar[Literal[4]] = 4
    """IAB Tech Lab Audience Taxonomy 1.1"""
    IAB_TECH_LAB_CONTENT_TAXONOMY_2_1: ClassVar[Literal[5]] = 5
    """IAB Tech Lab Content Taxonomy 2.1"""
    IAB_TECH_LAB_CONTENT_TAXONOMY_2_2: ClassVar[Literal[6]] = 6
    """IAB Tech Lab Content Taxonomy 2.2"""
    IAB_TECH_LAB_CONTENT_TAXONOMY_3_0: ClassVar[Literal[7]] = 7
    """IAB Tech Lab Content Taxonomy 3.0"""
    IAB_TECH_LAB_AD_PRODUCT_TAXONOMY_2_0: ClassVar[Literal[8]] = 8
    """IAB Tech Lab Ad Product Taxonomy 2.0"""
    IAB_TECH_LAB_CONTENT_TAXONOMY_3_1: ClassVar[Literal[9]] = 9
    """IAB Tech Lab Content Taxonomy 3.1"""

    CODES: ClassVar[Mapping[int, str]] = {
        1: 'CONTENT_CATEGORY_TAXONOMY_1_0',
        2: 'CONTENT_CATEGORY_TAXONOMY_2_0',
        3: 'IAB_TECH_LAB_AD_PRODUCT_TAXONOMY_1_0',
        4: 'IAB_TECH_LAB_AUDIENCE_TAXONOMY_1_1',
        5: 'IAB_TECH_LAB_CONTENT_TAXONOMY_2_1',
        6: 'IAB_TECH_LAB_CONTENT_TAXONOMY_2_2',
        7: 'IAB_TECH_LAB_CONTENT_TAXONOMY_3_0',
        8: 'IAB_TECH_LAB_AD_PRODUCT_TAXONOMY_2_0',
        9: 'IAB_TECH_LAB_CONTENT_TAXONOMY_3_1',
    }


class CategoryTaxonomyCode(CategoryTaxonomy):
    """One of the codes List: Category Taxonomies states."""
    root: Literal[1, 2, 3, 4, 5, 6, 7, 8, 9]


class CategoryTaxonomyExtension(CategoryTaxonomy):
    """Vendor-specific: a value of VendorCode, which is this vocabulary's extension point.

    Vendor-specific codes.

    An application carries its own code by subclassing this class and naming the code in its own
    `CODES`. The published schema already admits the value, so the verdict does not change.
    """
    root: VendorCode


class ClickType(Vocabulary[Literal[0, 1, 2, 3] | VendorCode]):
    """List: Click Types

    The codes of List: Click Types

    The list reserves codes it does not state, so this vocabulary is open: a value is one of the
    codes below or a value of VendorCode. ClickTypeExtension is the extension point, and an
    application names its own code by subclassing it.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/ClickType'

    NON_CLICKABLE: ClassVar[Literal[0]] = 0
    """Non-Clickable"""
    CLICKABLE_DETAILS_UNKNOWN: ClassVar[Literal[1]] = 1
    """Clickable - Details Unknown"""
    CLICKABLE_EMBEDDED_BROWSER_WEBVIEW: ClassVar[Literal[2]] = 2
    """Clickable - Embedded Browser/Webview"""
    CLICKABLE_NATIVE_BROWSER: ClassVar[Literal[3]] = 3
    """Clickable - Native Browser"""

    CODES: ClassVar[Mapping[int, str]] = {
        0: 'NON_CLICKABLE',
        1: 'CLICKABLE_DETAILS_UNKNOWN',
        2: 'CLICKABLE_EMBEDDED_BROWSER_WEBVIEW',
        3: 'CLICKABLE_NATIVE_BROWSER',
    }


class ClickTypeCode(ClickType):
    """One of the codes List: Click Types states."""
    root: Literal[0, 1, 2, 3]


class ClickTypeExtension(ClickType):
    """Vendor-specific: a value of VendorCode, which is this vocabulary's extension point.

    Vendor-specific codes.

    An application carries its own code by subclassing this class and naming the code in its own
    `CODES`. The published schema already admits the value, so the verdict does not change.
    """
    root: VendorCode


class CompanionType(Vocabulary[Literal[1, 2, 3]]):
    """List: Companion Types

    The codes of List: Companion Types

    The list states every code it has, so this vocabulary is closed: no other value is accepted.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/CompanionType'

    STATIC_RESOURCE: ClassVar[Literal[1]] = 1
    """Static Resource"""
    HTML_RESOURCE: ClassVar[Literal[2]] = 2
    """HTML Resource"""
    IFRAME_RESOURCE: ClassVar[Literal[3]] = 3
    """iframe Resource"""

    CODES: ClassVar[Mapping[int, str]] = {
        1: 'STATIC_RESOURCE',
        2: 'HTML_RESOURCE',
        3: 'IFRAME_RESOURCE',
    }


class CompanionTypeCode(CompanionType):
    """One of the codes List: Companion Types states."""
    root: Literal[1, 2, 3]


class ConnectionType(Vocabulary[Literal[1, 2, 3, 4, 5, 6, 7]]):
    """List: Connection Types

    The codes of List: Connection Types

    The list states every code it has, so this vocabulary is closed: no other value is accepted.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/ConnectionType'

    ETHERNET_WIRED_CONNECTION: ClassVar[Literal[1]] = 1
    """Ethernet; Wired Connection"""
    WIFI: ClassVar[Literal[2]] = 2
    """WIFI"""
    CELLULAR_NETWORK_UNKNOWN_GENERATION: ClassVar[Literal[3]] = 3
    """Cellular Network - Unknown Generation"""
    CELLULAR_NETWORK_2G: ClassVar[Literal[4]] = 4
    """Cellular Network - 2G"""
    CELLULAR_NETWORK_3G: ClassVar[Literal[5]] = 5
    """Cellular Network - 3G"""
    CELLULAR_NETWORK_4G: ClassVar[Literal[6]] = 6
    """Cellular Network - 4G"""
    CELLULAR_NETWORK_5G: ClassVar[Literal[7]] = 7
    """Cellular Network - 5G"""

    CODES: ClassVar[Mapping[int, str]] = {
        1: 'ETHERNET_WIRED_CONNECTION',
        2: 'WIFI',
        3: 'CELLULAR_NETWORK_UNKNOWN_GENERATION',
        4: 'CELLULAR_NETWORK_2G',
        5: 'CELLULAR_NETWORK_3G',
        6: 'CELLULAR_NETWORK_4G',
        7: 'CELLULAR_NETWORK_5G',
    }


class ConnectionTypeCode(ConnectionType):
    """One of the codes List: Connection Types states."""
    root: Literal[1, 2, 3, 4, 5, 6, 7]


class ContentContext(Vocabulary[Literal[1, 2, 3, 4, 5, 6, 7]]):
    """List: Content Contexts

    The codes of List: Content Contexts

    The list states every code it has, so this vocabulary is closed: no other value is accepted.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/ContentContext'

    VIDEO: ClassVar[Literal[1]] = 1
    """Video

    Video (i.e., video file or stream such as Internet TV broadcasts)
    """
    GAME: ClassVar[Literal[2]] = 2
    """Game

    Game (i.e., an interactive software game)
    """
    MUSIC: ClassVar[Literal[3]] = 3
    """Music

    Music (i.e., audio file or stream such as Internet radio broadcasts)
    """
    APPLICATION: ClassVar[Literal[4]] = 4
    """Application

    Application (i.e., an interactive software application)
    """
    TEXT: ClassVar[Literal[5]] = 5
    """Text

    Text (i.e., primarily textual document such as a web page, eBook, or news article)
    """
    OTHER: ClassVar[Literal[6]] = 6
    """Other

    Other (i.e., none of the other categories applies)
    """
    UNKNOWN: ClassVar[Literal[7]] = 7
    """Unknown"""

    CODES: ClassVar[Mapping[int, str]] = {
        1: 'VIDEO',
        2: 'GAME',
        3: 'MUSIC',
        4: 'APPLICATION',
        5: 'TEXT',
        6: 'OTHER',
        7: 'UNKNOWN',
    }


class ContentContextCode(ContentContext):
    """One of the codes List: Content Contexts states."""
    root: Literal[1, 2, 3, 4, 5, 6, 7]


class CreativeAttribute(Vocabulary[Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23] | VendorCode]):
    """List: Creative Attributes

    The codes of List: Creative Attributes

    The list reserves codes it does not state, so this vocabulary is open: a value is one of the
    codes below or a value of VendorCode. CreativeAttributeExtension is the extension point, and
    an application names its own code by subclassing it.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/CreativeAttribute'

    AUDIO_AD_AUTOPLAY: ClassVar[Literal[1]] = 1
    """Audio Ad (Autoplay)"""
    AUDIO_AD_USER_INITIATED: ClassVar[Literal[2]] = 2
    """Audio Ad (User Initiated)"""
    EXPANDABLE_AUTOMATIC: ClassVar[Literal[3]] = 3
    """Expandable (Automatic)"""
    EXPANDABLE_USER_INITIATED_CLICK: ClassVar[Literal[4]] = 4
    """Expandable (User Initiated - Click)"""
    EXPANDABLE_USER_INITIATED_ROLLOVER: ClassVar[Literal[5]] = 5
    """Expandable (User Initiated - Rollover)"""
    IN_BANNER_VIDEO_AD_AUTOPLAY: ClassVar[Literal[6]] = 6
    """In-Banner Video Ad (Autoplay)"""
    IN_BANNER_VIDEO_AD_USER_INITIATED: ClassVar[Literal[7]] = 7
    """In-Banner Video Ad (User Initiated)"""
    POP: ClassVar[Literal[8]] = 8
    """Pop

    Pop (e.g., Over, Under, or Upon Exit)
    """
    PROVOCATIVE_OR_SUGGESTIVE_IMAGERY: ClassVar[Literal[9]] = 9
    """Provocative or Suggestive Imagery"""
    SHAKY_FLASHING_OR_EXTREME_ANIMATION: ClassVar[Literal[10]] = 10
    """Shaky, Flashing, or Extreme Animation

    Shaky, Flashing, Flickering, Extreme Animation, Smileys
    """
    SURVEYS: ClassVar[Literal[11]] = 11
    """Surveys"""
    TEXT_ONLY: ClassVar[Literal[12]] = 12
    """Text Only"""
    USER_INTERACTIVE: ClassVar[Literal[13]] = 13
    """User Interactive

    User Interactive (e.g., Embedded Games)
    """
    WINDOWS_DIALOG_OR_ALERT_STYLE: ClassVar[Literal[14]] = 14
    """Windows Dialog or Alert Style"""
    HAS_AUDIO_ON_OFF_BUTTON: ClassVar[Literal[15]] = 15
    """Has Audio On/Off Button"""
    AD_PROVIDES_SKIP_BUTTON: ClassVar[Literal[16]] = 16
    """Ad Provides Skip Button

    Ad Provides Skip Button (e.g. VPAID-rendered skip button on pre-roll video)
    """
    ADOBE_FLASH: ClassVar[Literal[17]] = 17
    """Adobe Flash"""
    RESPONSIVE_SIZELESS_FLUID: ClassVar[Literal[18]] = 18
    """Responsive; Sizeless; Fluid

    Responsive; Sizeless; Fluid (i.e., creatives that dynamically resize to environment)
    """
    CONTAINS_ADVERTISER_QR_CODE: ClassVar[Literal[19]] = 19
    """Contains advertiser QR Code"""
    SUPPORT_ALPHA_CHANNEL_TRANSPARENCY: ClassVar[Literal[20]] = 20
    """Support alpha channel transparency"""
    STATIC_VISUAL: ClassVar[Literal[21]] = 21
    """Static Visual

    Static Visual. Creative contains no perceptible motion and renders as a static visual, even
    if delivered in a video file format (e.g., MP4). No animated elements or time-based visual
    transitions are present.
    """
    LIMITED_MOTION: ClassVar[Literal[22]] = 22
    """Limited Motion

    Limited Motion (Cinemagraph). Creative contains subtle or localized motion within an
    otherwise static composition. Motion is minimal, looped, and does not constitute full-scene
    animation or continuous narrative progression.
    """
    FULL_MOTION_VIDEO: ClassVar[Literal[23]] = 23
    """Full-Motion Video

    Full-Motion Video. Creative contains continuous or scene-level motion typical of standard
    video assets, including dynamic visual transitions, camera movement, or narrative
    progression across frames.
    """

    CODES: ClassVar[Mapping[int, str]] = {
        1: 'AUDIO_AD_AUTOPLAY',
        2: 'AUDIO_AD_USER_INITIATED',
        3: 'EXPANDABLE_AUTOMATIC',
        4: 'EXPANDABLE_USER_INITIATED_CLICK',
        5: 'EXPANDABLE_USER_INITIATED_ROLLOVER',
        6: 'IN_BANNER_VIDEO_AD_AUTOPLAY',
        7: 'IN_BANNER_VIDEO_AD_USER_INITIATED',
        8: 'POP',
        9: 'PROVOCATIVE_OR_SUGGESTIVE_IMAGERY',
        10: 'SHAKY_FLASHING_OR_EXTREME_ANIMATION',
        11: 'SURVEYS',
        12: 'TEXT_ONLY',
        13: 'USER_INTERACTIVE',
        14: 'WINDOWS_DIALOG_OR_ALERT_STYLE',
        15: 'HAS_AUDIO_ON_OFF_BUTTON',
        16: 'AD_PROVIDES_SKIP_BUTTON',
        17: 'ADOBE_FLASH',
        18: 'RESPONSIVE_SIZELESS_FLUID',
        19: 'CONTAINS_ADVERTISER_QR_CODE',
        20: 'SUPPORT_ALPHA_CHANNEL_TRANSPARENCY',
        21: 'STATIC_VISUAL',
        22: 'LIMITED_MOTION',
        23: 'FULL_MOTION_VIDEO',
    }


class CreativeAttributeCode(CreativeAttribute):
    """One of the codes List: Creative Attributes states."""
    root: Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]


class CreativeAttributeExtension(CreativeAttribute):
    """Vendor-specific: a value of VendorCode, which is this vocabulary's extension point.

    Vendor-specific codes.

    An application carries its own code by subclassing this class and naming the code in its own
    `CODES`. The published schema already admits the value, so the verdict does not change.
    """
    root: VendorCode


class CreativeSubtypeAudioVideo(Vocabulary[Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]]):
    """List: Creative Subtypes - Audio/Video

    The codes of List: Creative Subtypes - Audio/Video

    The list states every code it has, so this vocabulary is closed: no other value is accepted.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/CreativeSubtypeAudioVideo'

    VAST_1_0: ClassVar[Literal[1]] = 1
    """VAST 1.0"""
    VAST_2_0: ClassVar[Literal[2]] = 2
    """VAST 2.0"""
    VAST_3_0: ClassVar[Literal[3]] = 3
    """VAST 3.0"""
    VAST_1_0_WRAPPER: ClassVar[Literal[4]] = 4
    """VAST 1.0 Wrapper"""
    VAST_2_0_WRAPPER: ClassVar[Literal[5]] = 5
    """VAST 2.0 Wrapper"""
    VAST_3_0_WRAPPER: ClassVar[Literal[6]] = 6
    """VAST 3.0 Wrapper"""
    VAST_4_0: ClassVar[Literal[7]] = 7
    """VAST 4.0"""
    VAST_4_0_WRAPPER: ClassVar[Literal[8]] = 8
    """VAST 4.0 Wrapper"""
    DAAST_1_0: ClassVar[Literal[9]] = 9
    """DAAST 1.0"""
    DAAST_1_0_WRAPPER: ClassVar[Literal[10]] = 10
    """DAAST 1.0 Wrapper"""
    VAST_4_1: ClassVar[Literal[11]] = 11
    """VAST 4.1"""
    VAST_4_1_WRAPPER: ClassVar[Literal[12]] = 12
    """VAST 4.1 Wrapper"""
    VAST_4_2: ClassVar[Literal[13]] = 13
    """VAST 4.2"""
    VAST_4_2_WRAPPER: ClassVar[Literal[14]] = 14
    """VAST 4.2 Wrapper"""
    VAST_4_3: ClassVar[Literal[15]] = 15
    """VAST 4.3"""
    VAST_4_3_WRAPPER: ClassVar[Literal[16]] = 16
    """VAST 4.3 Wrapper"""

    CODES: ClassVar[Mapping[int, str]] = {
        1: 'VAST_1_0',
        2: 'VAST_2_0',
        3: 'VAST_3_0',
        4: 'VAST_1_0_WRAPPER',
        5: 'VAST_2_0_WRAPPER',
        6: 'VAST_3_0_WRAPPER',
        7: 'VAST_4_0',
        8: 'VAST_4_0_WRAPPER',
        9: 'DAAST_1_0',
        10: 'DAAST_1_0_WRAPPER',
        11: 'VAST_4_1',
        12: 'VAST_4_1_WRAPPER',
        13: 'VAST_4_2',
        14: 'VAST_4_2_WRAPPER',
        15: 'VAST_4_3',
        16: 'VAST_4_3_WRAPPER',
    }


class CreativeSubtypeAudioVideoCode(CreativeSubtypeAudioVideo):
    """One of the codes List: Creative Subtypes - Audio/Video states."""
    root: Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


class CreativeSubtypeDisplay(Vocabulary[Literal[1, 2, 3, 4]]):
    """List: Creative Subtypes - Display

    The codes of List: Creative Subtypes - Display

    The list states every code it has, so this vocabulary is closed: no other value is accepted.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/CreativeSubtypeDisplay'

    HTML: ClassVar[Literal[1]] = 1
    """HTML"""
    AMPHTML: ClassVar[Literal[2]] = 2
    """AMPHTML"""
    STRUCTURED_IMAGE_OBJECT: ClassVar[Literal[3]] = 3
    """Structured Image Object"""
    STRUCTURED_NATIVE_OBJECT: ClassVar[Literal[4]] = 4
    """Structured Native Object"""

    CODES: ClassVar[Mapping[int, str]] = {
        1: 'HTML',
        2: 'AMPHTML',
        3: 'STRUCTURED_IMAGE_OBJECT',
        4: 'STRUCTURED_NATIVE_OBJECT',
    }


class CreativeSubtypeDisplayCode(CreativeSubtypeDisplay):
    """One of the codes List: Creative Subtypes - Display states."""
    root: Literal[1, 2, 3, 4]


class DeliveryMethod(Vocabulary[Literal[1, 2, 3]]):
    """List: Delivery Methods

    The codes of List: Delivery Methods

    The list states every code it has, so this vocabulary is closed: no other value is accepted.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/DeliveryMethod'

    STREAMING: ClassVar[Literal[1]] = 1
    """Streaming"""
    PROGRESSIVE: ClassVar[Literal[2]] = 2
    """Progressive"""
    DOWNLOAD: ClassVar[Literal[3]] = 3
    """Download"""

    CODES: ClassVar[Mapping[int, str]] = {
        1: 'STREAMING',
        2: 'PROGRESSIVE',
        3: 'DOWNLOAD',
    }


class DeliveryMethodCode(DeliveryMethod):
    """One of the codes List: Delivery Methods states."""
    root: Literal[1, 2, 3]


class DeviceType(Vocabulary[Literal[1, 2, 3, 4, 5, 6, 7, 8]]):
    """List: Device Types

    The codes of List: Device Types

    The list states every code it has, so this vocabulary is closed: no other value is accepted.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/DeviceType'

    MOBILE_TABLET_GENERAL: ClassVar[Literal[1]] = 1
    """Mobile/Tablet - General"""
    PERSONAL_COMPUTER: ClassVar[Literal[2]] = 2
    """Personal Computer"""
    CONNECTED_TV: ClassVar[Literal[3]] = 3
    """Connected TV"""
    PHONE: ClassVar[Literal[4]] = 4
    """Phone"""
    TABLET: ClassVar[Literal[5]] = 5
    """Tablet"""
    CONNECTED_DEVICE: ClassVar[Literal[6]] = 6
    """Connected Device"""
    SET_TOP_BOX: ClassVar[Literal[7]] = 7
    """Set Top Box"""
    OOH_DEVICE: ClassVar[Literal[8]] = 8
    """OOH Device"""

    CODES: ClassVar[Mapping[int, str]] = {
        1: 'MOBILE_TABLET_GENERAL',
        2: 'PERSONAL_COMPUTER',
        3: 'CONNECTED_TV',
        4: 'PHONE',
        5: 'TABLET',
        6: 'CONNECTED_DEVICE',
        7: 'SET_TOP_BOX',
        8: 'OOH_DEVICE',
    }


class DeviceTypeCode(DeviceType):
    """One of the codes List: Device Types states."""
    root: Literal[1, 2, 3, 4, 5, 6, 7, 8]


class DisplayContextType(Vocabulary[Literal[10, 11, 12, 13, 14, 15, 20, 21, 22, 30, 31, 32] | VendorCode]):
    """List: Display Context Types

    The codes of List: Display Context Types

    The list reserves codes it does not state, so this vocabulary is open: a value is one of the
    codes below or a value of VendorCode. DisplayContextTypeExtension is the extension point,
    and an application names its own code by subclassing it.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/DisplayContextType'

    CONTENT_CENTRIC_CONTEXT: ClassVar[Literal[10]] = 10
    """Content-centric context

    Content-centric context (e.g., newsfeed, article, image gallery, video gallery, etc.).
    """
    PRIMARILY_ARTICLE_CONTENT: ClassVar[Literal[11]] = 11
    """Primarily article content

    - Primarily article content, which could include images, etc. as part of the article.
    """
    PRIMARILY_VIDEO_CONTENT: ClassVar[Literal[12]] = 12
    """Primarily video content

    - Primarily video content.
    """
    PRIMARILY_AUDIO_CONTENT: ClassVar[Literal[13]] = 13
    """Primarily audio content

    - Primarily audio content.
    """
    PRIMARILY_IMAGE_CONTENT: ClassVar[Literal[14]] = 14
    """Primarily image content

    - Primarily image content.
    """
    USER_GENERATED_CONTENT: ClassVar[Literal[15]] = 15
    """User-generated content

    - User-generated content (e.g., forums, comments, etc.).
    """
    SOCIAL_CENTRIC_CONTEXT: ClassVar[Literal[20]] = 20
    """Social-centric context

    Social-centric context (e.g., social network feed, email, chat, etc.).
    """
    PRIMARILY_EMAIL_CONTENT: ClassVar[Literal[21]] = 21
    """Primarily email content

    - Primarily email content.
    """
    PRIMARILY_CHAT_IM_CONTENT: ClassVar[Literal[22]] = 22
    """Primarily chat/IM content

    - Primarily chat/IM content.
    """
    PRODUCT_CONTEXT: ClassVar[Literal[30]] = 30
    """Product context

    Product context (e.g., product listings, details, recommendations, reviews, etc.).
    """
    APP_STORE_MARKETPLACE: ClassVar[Literal[31]] = 31
    """App store/marketplace

    - App store/marketplace.
    """
    PRODUCT_REVIEWS_SITE_PRIMARILY: ClassVar[Literal[32]] = 32
    """Product reviews site primarily

    - Product reviews site primarily, which may sell product secondarily.
    """

    CODES: ClassVar[Mapping[int, str]] = {
        10: 'CONTENT_CENTRIC_CONTEXT',
        11: 'PRIMARILY_ARTICLE_CONTENT',
        12: 'PRIMARILY_VIDEO_CONTENT',
        13: 'PRIMARILY_AUDIO_CONTENT',
        14: 'PRIMARILY_IMAGE_CONTENT',
        15: 'USER_GENERATED_CONTENT',
        20: 'SOCIAL_CENTRIC_CONTEXT',
        21: 'PRIMARILY_EMAIL_CONTENT',
        22: 'PRIMARILY_CHAT_IM_CONTENT',
        30: 'PRODUCT_CONTEXT',
        31: 'APP_STORE_MARKETPLACE',
        32: 'PRODUCT_REVIEWS_SITE_PRIMARILY',
    }


class DisplayContextTypeCode(DisplayContextType):
    """One of the codes List: Display Context Types states."""
    root: Literal[10, 11, 12, 13, 14, 15, 20, 21, 22, 30, 31, 32]


class DisplayContextTypeExtension(DisplayContextType):
    """Vendor-specific: a value of VendorCode, which is this vocabulary's extension point.

    Vendor-specific codes.

    An application carries its own code by subclassing this class and naming the code in its own
    `CODES`. The published schema already admits the value, so the verdict does not change.
    """
    root: VendorCode


class DisplayPlacementType(Vocabulary[Literal[1, 2, 3, 4] | VendorCode]):
    """List: Display Placement Types

    The codes of List: Display Placement Types

    The list reserves codes it does not state, so this vocabulary is open: a value is one of the
    codes below or a value of VendorCode. DisplayPlacementTypeExtension is the extension point,
    and an application names its own code by subclassing it.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/DisplayPlacementType'

    IN_THE_FEED_OF_CONTENT: ClassVar[Literal[1]] = 1
    """In the feed of content

    In the feed of content (e.g., as an item inside the organic feed, grid, listing, carousel,
    etc.).
    """
    IN_THE_ATOMIC_UNIT_OF_THE_CONTENT: ClassVar[Literal[2]] = 2
    """In the atomic unit of the content

    In the atomic unit of the content (e.g., in the article page or single image page).
    """
    OUTSIDE_THE_CORE_CONTENT: ClassVar[Literal[3]] = 3
    """Outside the core content

    Outside the core content (e.g., in the ads section on the right rail, as a banner-style
    placement near the content, etc.).
    """
    RECOMMENDATION_WIDGET: ClassVar[Literal[4]] = 4
    """Recommendation widget

    Recommendation widget; most commonly presented below article content.
    """

    CODES: ClassVar[Mapping[int, str]] = {
        1: 'IN_THE_FEED_OF_CONTENT',
        2: 'IN_THE_ATOMIC_UNIT_OF_THE_CONTENT',
        3: 'OUTSIDE_THE_CORE_CONTENT',
        4: 'RECOMMENDATION_WIDGET',
    }


class DisplayPlacementTypeCode(DisplayPlacementType):
    """One of the codes List: Display Placement Types states."""
    root: Literal[1, 2, 3, 4]


class DisplayPlacementTypeExtension(DisplayPlacementType):
    """Vendor-specific: a value of VendorCode, which is this vocabulary's extension point.

    Vendor-specific codes.

    An application carries its own code by subclassing this class and naming the code in its own
    `CODES`. The published schema already admits the value, so the verdict does not change.
    """
    root: VendorCode


class DoohMultiplierMeasurementSourceType(Vocabulary[Literal[0, 1, 2, 3]]):
    """List: DOOH Multiplier Measurement Source Types

    The codes of List: DOOH Multiplier Measurement Source Types

    The list states every code it has, so this vocabulary is closed: no other value is accepted.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/DoohMultiplierMeasurementSourceType'

    UNKNOWN: ClassVar[Literal[0]] = 0
    """Unknown"""
    MEASUREMENT_VENDOR_PROVIDED: ClassVar[Literal[1]] = 1
    """Measurement Vendor Provided"""
    PUBLISHER_PROVIDED: ClassVar[Literal[2]] = 2
    """Publisher Provided"""
    EXCHANGE_PROVIDED: ClassVar[Literal[3]] = 3
    """Exchange Provided"""

    CODES: ClassVar[Mapping[int, str]] = {
        0: 'UNKNOWN',
        1: 'MEASUREMENT_VENDOR_PROVIDED',
        2: 'PUBLISHER_PROVIDED',
        3: 'EXCHANGE_PROVIDED',
    }


class DoohMultiplierMeasurementSourceTypeCode(DoohMultiplierMeasurementSourceType):
    """One of the codes List: DOOH Multiplier Measurement Source Types states."""
    root: Literal[0, 1, 2, 3]


class DoohVenueTaxonomy(Vocabulary[Literal[0, 1, 2, 3, 4, 5]]):
    """List: DOOH Venue Taxonomies

    The codes of List: DOOH Venue Taxonomies

    The list states every code it has, so this vocabulary is closed: no other value is accepted.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/DoohVenueTaxonomy'

    ADCOM_DOOH_VENUE_TYPES_DEPRECATED: ClassVar[Literal[0]] = 0
    """AdCom DOOH Venue Types (deprecated)"""
    OPENOOH_VENUE_TAXONOMY_1_0: ClassVar[Literal[1]] = 1
    """OpenOOH Venue Taxonomy 1.0

    OpenOOH Venue Taxonomy 1.0
    https://github.com/openooh/venue-taxonomy/blob/main/specification-1.0.md
    """
    DPAA_DEVICE_VENUE_TYPES: ClassVar[Literal[2]] = 2
    """DPAA Device Venue Types

    DPAA Device Venue Types
    https://github.com/InteractiveAdvertisingBureau/AdCOM/blob/master/AdCOM%20v1.0%20FINAL.md#list--dooh-venue-types-
    """
    DMI_CATEGORIZATION_OF_VENUES_1_1: ClassVar[Literal[3]] = 3
    """DMI Categorization of Venues 1.1

    DMI Categorization of Venues 1.1
    https://www.dmi-org.com/download/DMI_Standards_for_DOOH_Venues.pdf
    """
    OMA_TAXONOMY_JAN_2022: ClassVar[Literal[4]] = 4
    """OMA taxonomy Jan 2022

    OMA taxonomy Jan 2022 https://www.oma.org.au/industry-standards
    """
    OPENOOH_VENUE_TAXONOMY_1_1: ClassVar[Literal[5]] = 5
    """OpenOOH Venue Taxonomy 1.1

    OpenOOH Venue Taxonomy 1.1
    https://github.com/openooh/venue-taxonomy/blob/main/specification-1.1.md
    """

    CODES: ClassVar[Mapping[int, str]] = {
        0: 'ADCOM_DOOH_VENUE_TYPES_DEPRECATED',
        1: 'OPENOOH_VENUE_TAXONOMY_1_0',
        2: 'DPAA_DEVICE_VENUE_TYPES',
        3: 'DMI_CATEGORIZATION_OF_VENUES_1_1',
        4: 'OMA_TAXONOMY_JAN_2022',
        5: 'OPENOOH_VENUE_TAXONOMY_1_1',
    }


class DoohVenueTaxonomyCode(DoohVenueTaxonomy):
    """One of the codes List: DOOH Venue Taxonomies states."""
    root: Literal[0, 1, 2, 3, 4, 5]


class EventTrackingMethod(Vocabulary[Literal[1, 2] | VendorCode]):
    """List: Event Tracking Methods

    The codes of List: Event Tracking Methods

    The list reserves codes it does not state, so this vocabulary is open: a value is one of the
    codes below or a value of VendorCode. EventTrackingMethodExtension is the extension point,
    and an application names its own code by subclassing it.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/EventTrackingMethod'

    IMAGE_PIXEL: ClassVar[Literal[1]] = 1
    """Image-Pixel

    Image-Pixel: URL provided will be inserted as a 1x1 pixel at the time of the event.
    """
    JAVASCRIPT: ClassVar[Literal[2]] = 2
    """JavaScript

    JavaScript: URL provided will be inserted as a JavaScript tag at the time of the event.
    """

    CODES: ClassVar[Mapping[int, str]] = {
        1: 'IMAGE_PIXEL',
        2: 'JAVASCRIPT',
    }


class EventTrackingMethodCode(EventTrackingMethod):
    """One of the codes List: Event Tracking Methods states."""
    root: Literal[1, 2]


class EventTrackingMethodExtension(EventTrackingMethod):
    """Vendor-specific: a value of VendorCode, which is this vocabulary's extension point.

    Vendor-specific codes.

    An application carries its own code by subclassing this class and naming the code in its own
    `CODES`. The published schema already admits the value, so the verdict does not change.
    """
    root: VendorCode


class EventType(Vocabulary[Literal[1, 2, 3, 4, 5] | VendorCode]):
    """List: Event Types

    The codes of List: Event Types

    The list reserves codes it does not state, so this vocabulary is open: a value is one of the
    codes below or a value of VendorCode. EventTypeExtension is the extension point, and an
    application names its own code by subclassing it.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/EventType'

    LOADED: ClassVar[Literal[1]] = 1
    """loaded

    loaded: Delivered as a part of the creative markup. Creative may be pre-cached or
    pre-loaded; prior to initial rendering.
    """
    IMPRESSION: ClassVar[Literal[2]] = 2
    """impression

    impression: Ad impression per IAB/MRC Ad Impression Measurement Guidelines.
    """
    VIEWABLE_MRC50: ClassVar[Literal[3]] = 3
    """viewable-mrc50

    viewable-mrc50: Visible impression using MRC definition of 50% in view for 1 second.
    """
    VIEWABLE_MRC100: ClassVar[Literal[4]] = 4
    """viewable-mrc100

    viewable-mrc100: 100% in view for 1 second (i.e., the GroupM standard).
    """
    VIEWABLE_VIDEO50: ClassVar[Literal[5]] = 5
    """viewable-video50

    viewable-video50: Visible impression for video using MRC definition of 50% in view for 2
    seconds.
    """

    CODES: ClassVar[Mapping[int, str]] = {
        1: 'LOADED',
        2: 'IMPRESSION',
        3: 'VIEWABLE_MRC50',
        4: 'VIEWABLE_MRC100',
        5: 'VIEWABLE_VIDEO50',
    }


class EventTypeCode(EventType):
    """One of the codes List: Event Types states."""
    root: Literal[1, 2, 3, 4, 5]


class EventTypeExtension(EventType):
    """Vendor-specific: a value of VendorCode, which is this vocabulary's extension point.

    Vendor-specific codes.

    An application carries its own code by subclassing this class and naming the code in its own
    `CODES`. The published schema already admits the value, so the verdict does not change.
    """
    root: VendorCode


class ExpandableDirection(Vocabulary[Literal[1, 2, 3, 4, 5, 6]]):
    """List: Expandable Directions

    The codes of List: Expandable Directions

    The list states every code it has, so this vocabulary is closed: no other value is accepted.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/ExpandableDirection'

    LEFT: ClassVar[Literal[1]] = 1
    """Left"""
    RIGHT: ClassVar[Literal[2]] = 2
    """Right"""
    UP: ClassVar[Literal[3]] = 3
    """Up"""
    DOWN: ClassVar[Literal[4]] = 4
    """Down"""
    FULL_SCREEN: ClassVar[Literal[5]] = 5
    """Full Screen"""
    RESIZE_MINIMIZE_MAKE_SMALLER: ClassVar[Literal[6]] = 6
    """Resize/Minimize (make smaller)"""

    CODES: ClassVar[Mapping[int, str]] = {
        1: 'LEFT',
        2: 'RIGHT',
        3: 'UP',
        4: 'DOWN',
        5: 'FULL_SCREEN',
        6: 'RESIZE_MINIMIZE_MAKE_SMALLER',
    }


class ExpandableDirectionCode(ExpandableDirection):
    """One of the codes List: Expandable Directions states."""
    root: Literal[1, 2, 3, 4, 5, 6]


class FeedType(Vocabulary[Literal[1, 2, 3, 4, 5, 6, 7] | VendorCode]):
    """List: Feed Types

    The codes of List: Feed Types

    The list reserves codes it does not state, so this vocabulary is open: a value is one of the
    codes below or a value of VendorCode. FeedTypeExtension is the extension point, and an
    application names its own code by subclassing it.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/FeedType'

    MUSIC_STREAMING_SERVICE: ClassVar[Literal[1]] = 1
    """Music streaming service

    AOD: Music streaming service
    """
    FM_AM_BROADCAST: ClassVar[Literal[2]] = 2
    """FM/AM broadcast

    LIVE: FM/AM broadcast (live content broadcast over the air but also available via online
    streaming)
    """
    PODCAST: ClassVar[Literal[3]] = 3
    """Podcast

    AOD: Podcast (original, pre-recorded content distributed as episodes in a series)
    """
    CATCH_UP_RADIO: ClassVar[Literal[4]] = 4
    """Catch-up radio

    AOD: Catch-up radio (recorded segment of a radio show that was originally broadcast live)
    """
    WEB_RADIO: ClassVar[Literal[5]] = 5
    """Web radio

    LIVE: Web radio (live content only available via online streaming, not as AM/FM broadcast)
    """
    VIDEO_GAME_BACKGROUND_AUDIO: ClassVar[Literal[6]] = 6
    """Video game (background audio in video games)

    MISC: Video game (background audio in video games)
    """
    TEXT_TO_SPEECH: ClassVar[Literal[7]] = 7
    """Text to speech

    MISC: Text to speech (audio books, website plugin that can read article)
    """

    CODES: ClassVar[Mapping[int, str]] = {
        1: 'MUSIC_STREAMING_SERVICE',
        2: 'FM_AM_BROADCAST',
        3: 'PODCAST',
        4: 'CATCH_UP_RADIO',
        5: 'WEB_RADIO',
        6: 'VIDEO_GAME_BACKGROUND_AUDIO',
        7: 'TEXT_TO_SPEECH',
    }


class FeedTypeCode(FeedType):
    """One of the codes List: Feed Types states."""
    root: Literal[1, 2, 3, 4, 5, 6, 7]


class FeedTypeExtension(FeedType):
    """Vendor-specific: a value of VendorCode, which is this vocabulary's extension point.

    MISC: Vendor-specific codes.

    An application carries its own code by subclassing this class and naming the code in its own
    `CODES`. The published schema already admits the value, so the verdict does not change.
    """
    root: VendorCode


class IdMatchMethod(Vocabulary[Literal[0, 1, 2, 3, 4, 5] | VendorCode]):
    """List: ID Match Methods

    The codes of List: ID Match Methods

    The list reserves codes it does not state, so this vocabulary is open: a value is one of the
    codes below or a value of VendorCode. IdMatchMethodExtension is the extension point, and an
    application names its own code by subclassing it.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/IdMatchMethod'

    UNKNOWN: ClassVar[Literal[0]] = 0
    """Unknown"""
    NO_MATCH: ClassVar[Literal[1]] = 1
    """No Match

    No Match: No matching has occurred. The associated ID came directly from a 3rd-party cookie
    or OS-provided resettable device ID for advertising (IFA).
    """
    BROWSER_COOKIE_SYNC: ClassVar[Literal[2]] = 2
    """Browser Cookie Sync

    Browser Cookie Sync: Real time cookie sync as described in Appendix: Cookie Based ID Syncing
    of OpenRTB 2.x
    """
    AUTHENTICATED: ClassVar[Literal[3]] = 3
    """Authenticated

    Authenticated: ID match was based on user authentication such as an email login or hashed
    PII
    """
    OBSERVED: ClassVar[Literal[4]] = 4
    """Observed

    Observed: ID match was based on a 1st party observation, but without user authentication
    (e.g. GUID, SharedID, Session IDs, CHIPS or other 1st party cookies contained in
    localStorage)
    """
    INFERENCE: ClassVar[Literal[5]] = 5
    """Inference

    Inference: ID match was inferred from linkage based on non-authenticated features across
    multiple browsers or devices (e.g. IP address and/or UserAgent)
    """

    CODES: ClassVar[Mapping[int, str]] = {
        0: 'UNKNOWN',
        1: 'NO_MATCH',
        2: 'BROWSER_COOKIE_SYNC',
        3: 'AUTHENTICATED',
        4: 'OBSERVED',
        5: 'INFERENCE',
    }


class IdMatchMethodCode(IdMatchMethod):
    """One of the codes List: ID Match Methods states."""
    root: Literal[0, 1, 2, 3, 4, 5]


class IdMatchMethodExtension(IdMatchMethod):
    """Vendor-specific: a value of VendorCode, which is this vocabulary's extension point.

    Vendor Specific

    An application carries its own code by subclassing this class and naming the code in its own
    `CODES`. The published schema already admits the value, so the verdict does not change.
    """
    root: VendorCode


class IpLocationService(Vocabulary[Literal[1, 2, 3, 4, 511, 512]]):
    """List: IP Location Services

    The codes of List: IP Location Services

    The list states every code it has, so this vocabulary is closed: no other value is accepted.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/IpLocationService'

    IP2LOCATION: ClassVar[Literal[1]] = 1
    """ip2location"""
    NEUSTAR_QUOVA: ClassVar[Literal[2]] = 2
    """Neustar (Quova)"""
    MAXMIND: ClassVar[Literal[3]] = 3
    """MaxMind"""
    NETACUITY_DIGITAL_ELEMENT: ClassVar[Literal[4]] = 4
    """NetAcuity (Digital Element)"""
    CODE_51DEGREES_HIGH_CONFIDENCE: ClassVar[Literal[511]] = 511
    """51Degrees (High Confidence)"""
    CODE_51DEGREES_MEDIUM_CONFIDENCE: ClassVar[Literal[512]] = 512
    """51Degrees (Medium Confidence)"""

    CODES: ClassVar[Mapping[int, str]] = {
        1: 'IP2LOCATION',
        2: 'NEUSTAR_QUOVA',
        3: 'MAXMIND',
        4: 'NETACUITY_DIGITAL_ELEMENT',
        511: 'CODE_51DEGREES_HIGH_CONFIDENCE',
        512: 'CODE_51DEGREES_MEDIUM_CONFIDENCE',
    }


class IpLocationServiceCode(IpLocationService):
    """One of the codes List: IP Location Services states."""
    root: Literal[1, 2, 3, 4, 511, 512]


class LinearityMode(Vocabulary[Literal[1, 2]]):
    """List: Linearity Modes

    The codes of List: Linearity Modes

    The list states every code it has, so this vocabulary is closed: no other value is accepted.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/LinearityMode'

    LINEAR: ClassVar[Literal[1]] = 1
    """Linear"""
    NON_LINEAR: ClassVar[Literal[2]] = 2
    """Non-Linear

    Non-Linear (i.e., Overlay)
    """

    CODES: ClassVar[Mapping[int, str]] = {
        1: 'LINEAR',
        2: 'NON_LINEAR',
    }


class LinearityModeCode(LinearityMode):
    """One of the codes List: Linearity Modes states."""
    root: Literal[1, 2]


class LocationType(Vocabulary[Literal[1, 2, 3]]):
    """List: Location Types

    The codes of List: Location Types

    The list states every code it has, so this vocabulary is closed: no other value is accepted.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/LocationType'

    GPS_LOCATION_SERVICES: ClassVar[Literal[1]] = 1
    """GPS/Location Services"""
    IP_ADDRESS: ClassVar[Literal[2]] = 2
    """IP Address"""
    USER_PROVIDED: ClassVar[Literal[3]] = 3
    """User Provided

    User Provided (e.g., registration data)
    """

    CODES: ClassVar[Mapping[int, str]] = {
        1: 'GPS_LOCATION_SERVICES',
        2: 'IP_ADDRESS',
        3: 'USER_PROVIDED',
    }


class LocationTypeCode(LocationType):
    """One of the codes List: Location Types states."""
    root: Literal[1, 2, 3]


class MediaRating(Vocabulary[Literal[1, 2, 3]]):
    """List: Media Ratings

    The codes of List: Media Ratings

    The list states every code it has, so this vocabulary is closed: no other value is accepted.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/MediaRating'

    ALL_AUDIENCES: ClassVar[Literal[1]] = 1
    """All Audiences"""
    EVERYONE_OVER_AGE_12: ClassVar[Literal[2]] = 2
    """Everyone Over Age 12"""
    MATURE_AUDIENCES: ClassVar[Literal[3]] = 3
    """Mature Audiences"""

    CODES: ClassVar[Mapping[int, str]] = {
        1: 'ALL_AUDIENCES',
        2: 'EVERYONE_OVER_AGE_12',
        3: 'MATURE_AUDIENCES',
    }


class MediaRatingCode(MediaRating):
    """One of the codes List: Media Ratings states."""
    root: Literal[1, 2, 3]


class NativeDataAssetType(Vocabulary[Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] | VendorCode]):
    """List: Native Data Asset Types

    The codes of List: Native Data Asset Types

    The list reserves codes it does not state, so this vocabulary is open: a value is one of the
    codes below or a value of VendorCode. NativeDataAssetTypeExtension is the extension point,
    and an application names its own code by subclassing it.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/NativeDataAssetType'

    SPONSORED: ClassVar[Literal[1]] = 1
    """sponsored

    sponsored: "Sponsored By" message which should contain the brand name of the sponsor.
    Recommended maximum length of at least 25 characters.
    """
    DESC: ClassVar[Literal[2]] = 2
    """desc

    desc: Descriptive text associated with the product or service being advertised. Long text
    lengths may be truncated or ellipsed when rendered. Recommended maximum length of at least
    140 characters.
    """
    RATING: ClassVar[Literal[3]] = 3
    """rating

    rating: Numeric rating of the product (e.g., an app's rating). Recommended integer range of
    0-5.
    """
    LIKES: ClassVar[Literal[4]] = 4
    """likes

    likes: Number of social ratings or "likes" of the product.
    """
    DOWNLOADS: ClassVar[Literal[5]] = 5
    """downloads

    downloads: Number downloads and/or installs of the product.
    """
    PRICE: ClassVar[Literal[6]] = 6
    """price

    price: Price of the product, app, or in-app purchase. Value should include currency symbol
    in localized format (e.g., "$10").
    """
    SALEPRICE: ClassVar[Literal[7]] = 7
    """saleprice

    saleprice: Sale price that can be used together with "price" to indicate a comparative
    discounted price. Value should include currency symbol in localized format (e.g., "$8.50").
    """
    PHONE: ClassVar[Literal[8]] = 8
    """phone

    phone: A formatted phone number.
    """
    ADDRESS: ClassVar[Literal[9]] = 9
    """address

    address: A formatted address.
    """
    DESC2: ClassVar[Literal[10]] = 10
    """desc2

    desc2: Additional descriptive text associated with the product.
    """
    DISPLAYURL: ClassVar[Literal[11]] = 11
    """displayurl

    displayurl: Display URL for the ad. To be used when sponsoring entity doesn't own the
    content (e.g., "Sponsored by Brand on Site", where Site is specified in this data asset).
    """
    CTATEXT: ClassVar[Literal[12]] = 12
    """ctatext

    ctatext: Description of the call to action (CTA) button for the destination URL. Recommended
    maximum length of at least 15 characters.
    """

    CODES: ClassVar[Mapping[int, str]] = {
        1: 'SPONSORED',
        2: 'DESC',
        3: 'RATING',
        4: 'LIKES',
        5: 'DOWNLOADS',
        6: 'PRICE',
        7: 'SALEPRICE',
        8: 'PHONE',
        9: 'ADDRESS',
        10: 'DESC2',
        11: 'DISPLAYURL',
        12: 'CTATEXT',
    }


class NativeDataAssetTypeCode(NativeDataAssetType):
    """One of the codes List: Native Data Asset Types states."""
    root: Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


class NativeDataAssetTypeExtension(NativeDataAssetType):
    """Vendor-specific: a value of VendorCode, which is this vocabulary's extension point.

    Vendor-specific codes.

    An application carries its own code by subclassing this class and naming the code in its own
    `CODES`. The published schema already admits the value, so the verdict does not change.
    """
    root: VendorCode


class NativeImageAssetType(Vocabulary[Literal[1, 3] | VendorCode]):
    """List: Native Image Asset Types

    The codes of List: Native Image Asset Types

    The list reserves codes it does not state, so this vocabulary is open: a value is one of the
    codes below or a value of VendorCode. NativeImageAssetTypeExtension is the extension point,
    and an application names its own code by subclassing it.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/NativeImageAssetType'

    ICON: ClassVar[Literal[1]] = 1
    """Icon

    Icon: Icon image. Maximum height at least 50 device independent pixels (DIPS); aspect ratio
    1:1.
    """
    MAIN: ClassVar[Literal[3]] = 3
    """Main

    Main: Large image preview for the ad. At least one of 2 size variants required: Small:
    Maximum height at least 200 DIPS; maximum width at least 200, 267, or 382 DIPS (i.e., aspect
    ratios of 1:1, 4:3, or 1.91:1, respectively). Large: Maximum height at least 627 DIPS;
    maximum width at least 627, 836, or 1198 DIPS (i.e., aspect ratios of 1:1, 4:3, or 1.91:1,
    respectively).
    """

    CODES: ClassVar[Mapping[int, str]] = {
        1: 'ICON',
        3: 'MAIN',
    }


class NativeImageAssetTypeCode(NativeImageAssetType):
    """One of the codes List: Native Image Asset Types states."""
    root: Literal[1, 3]


class NativeImageAssetTypeExtension(NativeImageAssetType):
    """Vendor-specific: a value of VendorCode, which is this vocabulary's extension point.

    Vendor-specific codes.

    An application carries its own code by subclassing this class and naming the code in its own
    `CODES`. The published schema already admits the value, so the verdict does not change.
    """
    root: VendorCode


class OperatingSystem(Vocabulary[Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28] | VendorCode]):
    """List: Operating Systems

    The codes of List: Operating Systems

    The list reserves codes it does not state, so this vocabulary is open: a value is one of the
    codes below or a value of VendorCode. OperatingSystemExtension is the extension point, and
    an application names its own code by subclassing it.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/OperatingSystem'

    OTHER_NOT_LISTED: ClassVar[Literal[0]] = 0
    """Other Not Listed"""
    CODE_3DS_SYSTEM_SOFTWARE: ClassVar[Literal[1]] = 1
    """3DS System Software"""
    ANDROID: ClassVar[Literal[2]] = 2
    """Android"""
    APPLE_TV_SOFTWARE: ClassVar[Literal[3]] = 3
    """Apple TV Software"""
    ASHA: ClassVar[Literal[4]] = 4
    """Asha"""
    BADA: ClassVar[Literal[5]] = 5
    """Bada"""
    BLACKBERRY: ClassVar[Literal[6]] = 6
    """BlackBerry"""
    BREW: ClassVar[Literal[7]] = 7
    """BREW"""
    CHROMEOS: ClassVar[Literal[8]] = 8
    """ChromeOS"""
    DARWIN: ClassVar[Literal[9]] = 9
    """Darwin"""
    FIREOS: ClassVar[Literal[10]] = 10
    """FireOS"""
    FIREFOXOS: ClassVar[Literal[11]] = 11
    """FirefoxOS"""
    HELENOS: ClassVar[Literal[12]] = 12
    """HelenOS"""
    IOS: ClassVar[Literal[13]] = 13
    """iOS"""
    LINUX: ClassVar[Literal[14]] = 14
    """Linux"""
    MACOS: ClassVar[Literal[15]] = 15
    """MacOS"""
    MEEGO: ClassVar[Literal[16]] = 16
    """MeeGo"""
    MORPHOS: ClassVar[Literal[17]] = 17
    """MorphOS"""
    NETBSD: ClassVar[Literal[18]] = 18
    """NetBSD"""
    NUCLEUSPLUS: ClassVar[Literal[19]] = 19
    """NucleusPLUS"""
    PS_VITA_SYSTEM_SOFTWARE: ClassVar[Literal[20]] = 20
    """PS Vita System Software"""
    PS3_SYSTEM_SOFTWARE: ClassVar[Literal[21]] = 21
    """PS3 System Software"""
    PS4_SOFTWARE: ClassVar[Literal[22]] = 22
    """PS4 Software"""
    PSP_SYSTEM_SOFTWARE: ClassVar[Literal[23]] = 23
    """PSP System Software"""
    SYMBIAN: ClassVar[Literal[24]] = 24
    """Symbian"""
    TIZEN: ClassVar[Literal[25]] = 25
    """Tizen"""
    WATCHOS: ClassVar[Literal[26]] = 26
    """WatchOS"""
    WEBOS: ClassVar[Literal[27]] = 27
    """WebOS"""
    WINDOWS: ClassVar[Literal[28]] = 28
    """Windows"""

    CODES: ClassVar[Mapping[int, str]] = {
        0: 'OTHER_NOT_LISTED',
        1: 'CODE_3DS_SYSTEM_SOFTWARE',
        2: 'ANDROID',
        3: 'APPLE_TV_SOFTWARE',
        4: 'ASHA',
        5: 'BADA',
        6: 'BLACKBERRY',
        7: 'BREW',
        8: 'CHROMEOS',
        9: 'DARWIN',
        10: 'FIREOS',
        11: 'FIREFOXOS',
        12: 'HELENOS',
        13: 'IOS',
        14: 'LINUX',
        15: 'MACOS',
        16: 'MEEGO',
        17: 'MORPHOS',
        18: 'NETBSD',
        19: 'NUCLEUSPLUS',
        20: 'PS_VITA_SYSTEM_SOFTWARE',
        21: 'PS3_SYSTEM_SOFTWARE',
        22: 'PS4_SOFTWARE',
        23: 'PSP_SYSTEM_SOFTWARE',
        24: 'SYMBIAN',
        25: 'TIZEN',
        26: 'WATCHOS',
        27: 'WEBOS',
        28: 'WINDOWS',
    }


class OperatingSystemCode(OperatingSystem):
    """One of the codes List: Operating Systems states."""
    root: Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]


class OperatingSystemExtension(OperatingSystem):
    """Vendor-specific: a value of VendorCode, which is this vocabulary's extension point.

    Vendor-specific codes.

    An application carries its own code by subclassing this class and naming the code in its own
    `CODES`. The published schema already admits the value, so the verdict does not change.
    """
    root: VendorCode


class PlacementPosition(Vocabulary[Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]]):
    """List: Placement Positions

    The codes of List: Placement Positions

    The list states every code it has, so this vocabulary is closed: no other value is accepted.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/PlacementPosition'

    UNKNOWN: ClassVar[Literal[0]] = 0
    """Unknown"""
    ABOVE_THE_FOLD: ClassVar[Literal[1]] = 1
    """Above The Fold"""
    LOCKED: ClassVar[Literal[2]] = 2
    """Locked

    Locked (i.e., fixed position)
    """
    BELOW_THE_FOLD: ClassVar[Literal[3]] = 3
    """Below The Fold"""
    HEADER: ClassVar[Literal[4]] = 4
    """Header"""
    FOOTER: ClassVar[Literal[5]] = 5
    """Footer"""
    SIDEBAR: ClassVar[Literal[6]] = 6
    """Sidebar"""
    FULLSCREEN: ClassVar[Literal[7]] = 7
    """Fullscreen"""
    PARTIAL_SCREEN: ClassVar[Literal[8]] = 8
    """Partial Screen"""
    TOP_LEFT: ClassVar[Literal[9]] = 9
    """Top Left"""
    TOP_RIGHT: ClassVar[Literal[10]] = 10
    """Top Right"""
    FRAME_THE_CONTENT: ClassVar[Literal[11]] = 11
    """Frame the content"""
    DOUBLE_BOX: ClassVar[Literal[12]] = 12
    """Double box"""
    DOUBLE_BOX_WITH_BACKGROUND: ClassVar[Literal[13]] = 13
    """Double box with background"""
    BOTTOM_LEFT: ClassVar[Literal[14]] = 14
    """Bottom Left"""
    BOTTOM_RIGHT: ClassVar[Literal[15]] = 15
    """Bottom Right"""
    L_SHAPE: ClassVar[Literal[16]] = 16
    """L shape"""
    REVERSED_L_SHAPE: ClassVar[Literal[17]] = 17
    """Reversed L shape"""

    CODES: ClassVar[Mapping[int, str]] = {
        0: 'UNKNOWN',
        1: 'ABOVE_THE_FOLD',
        2: 'LOCKED',
        3: 'BELOW_THE_FOLD',
        4: 'HEADER',
        5: 'FOOTER',
        6: 'SIDEBAR',
        7: 'FULLSCREEN',
        8: 'PARTIAL_SCREEN',
        9: 'TOP_LEFT',
        10: 'TOP_RIGHT',
        11: 'FRAME_THE_CONTENT',
        12: 'DOUBLE_BOX',
        13: 'DOUBLE_BOX_WITH_BACKGROUND',
        14: 'BOTTOM_LEFT',
        15: 'BOTTOM_RIGHT',
        16: 'L_SHAPE',
        17: 'REVERSED_L_SHAPE',
    }


class PlacementPositionCode(PlacementPosition):
    """One of the codes List: Placement Positions states."""
    root: Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]


class PlaybackCessationMode(Vocabulary[Literal[1, 2, 3]]):
    """List: Playback Cessation Modes

    The codes of List: Playback Cessation Modes

    The list states every code it has, so this vocabulary is closed: no other value is accepted.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/PlaybackCessationMode'

    ON_VIDEO_COMPLETION: ClassVar[Literal[1]] = 1
    """On Video Completion or when Terminated by User"""
    ON_LEAVING_VIEWPORT: ClassVar[Literal[2]] = 2
    """On Leaving Viewport or when Terminated by User"""
    ON_LEAVING_VIEWPORT_CONTINUES_FLOATING: ClassVar[Literal[3]] = 3
    """On Leaving Viewport Continues as Floating Unit

    On Leaving Viewport Continues as a Floating/Slider Unit until Video Completion or when
    Terminated by User
    """

    CODES: ClassVar[Mapping[int, str]] = {
        1: 'ON_VIDEO_COMPLETION',
        2: 'ON_LEAVING_VIEWPORT',
        3: 'ON_LEAVING_VIEWPORT_CONTINUES_FLOATING',
    }


class PlaybackCessationModeCode(PlaybackCessationMode):
    """One of the codes List: Playback Cessation Modes states."""
    root: Literal[1, 2, 3]


class PlaybackMethod(Vocabulary[Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]):
    """List: Playback Methods

    The codes of List: Playback Methods

    The list states every code it has, so this vocabulary is closed: no other value is accepted.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/PlaybackMethod'

    INITIATES_AUTOMATICALLY_WITH_SOUND_ON: ClassVar[Literal[1]] = 1
    """Initiates Automatically with Sound On

    Initiates without any specific user interaction with Sound On
    """
    INITIATES_AUTOMATICALLY_WITH_SOUND_OFF: ClassVar[Literal[2]] = 2
    """Initiates Automatically with Sound Off

    Initiates without any specific user interaction Sound Off by Default
    """
    INITIATES_ON_CLICK_WITH_SOUND_ON: ClassVar[Literal[3]] = 3
    """Initiates on Click with Sound On"""
    INITIATES_ON_MOUSE_OVER_WITH_SOUND_ON: ClassVar[Literal[4]] = 4
    """Initiates on Mouse-Over with Sound On

    Initiates on Mouse-Over or cursor over with Sound On
    """
    INITIATES_ON_ENTERING_VIEWPORT_SOUND_ON: ClassVar[Literal[5]] = 5
    """Initiates on Entering Viewport with Sound On

    Initiates on Entering Viewport or scrolling into view with Sound On
    """
    INITIATES_ON_ENTERING_VIEWPORT_SOUND_OFF: ClassVar[Literal[6]] = 6
    """Initiates on Entering Viewport with Sound Off

    Initiates on Entering Viewport or scrolling into view with Sound Off by Default
    """
    CONTINUOUS_PLAYBACK: ClassVar[Literal[7]] = 7
    """Continuous Playback

    Continuous Playback - Media playback is set to play additional media automatically without
    user interaction. The media player will keep playing additional media (playlist or
    generated) for the user until the user actively stops this from happening.
    """
    INITIATED_BY_CONTENT_PAUSE_SOUND_ON: ClassVar[Literal[8]] = 8
    """Initiated by user pausing content, Sound on"""
    INITIATED_BY_CONTENT_PAUSE_SOUND_OFF: ClassVar[Literal[9]] = 9
    """Initiated by user pausing content, Sound off"""
    INITIATED_BY_IDLING_SOUND_ON: ClassVar[Literal[10]] = 10
    """Initiated by idling, Sound on

    Initiated by idling (e.g. screensaver), Sound on
    """
    INITIATED_BY_IDLING_SOUND_OFF: ClassVar[Literal[11]] = 11
    """Initiated by idling, Sound off

    Initiated by idling (e.g. screensaver), Sound off
    """

    CODES: ClassVar[Mapping[int, str]] = {
        1: 'INITIATES_AUTOMATICALLY_WITH_SOUND_ON',
        2: 'INITIATES_AUTOMATICALLY_WITH_SOUND_OFF',
        3: 'INITIATES_ON_CLICK_WITH_SOUND_ON',
        4: 'INITIATES_ON_MOUSE_OVER_WITH_SOUND_ON',
        5: 'INITIATES_ON_ENTERING_VIEWPORT_SOUND_ON',
        6: 'INITIATES_ON_ENTERING_VIEWPORT_SOUND_OFF',
        7: 'CONTINUOUS_PLAYBACK',
        8: 'INITIATED_BY_CONTENT_PAUSE_SOUND_ON',
        9: 'INITIATED_BY_CONTENT_PAUSE_SOUND_OFF',
        10: 'INITIATED_BY_IDLING_SOUND_ON',
        11: 'INITIATED_BY_IDLING_SOUND_OFF',
    }


class PlaybackMethodCode(PlaybackMethod):
    """One of the codes List: Playback Methods states."""
    root: Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


class PlcmtSubtypeVideo(Vocabulary[Literal[1, 2, 3, 4, 5, 6, 7, 8, 9]]):
    """List: Plcmt Subtypes - Video

    The codes of List: Plcmt Subtypes - Video

    The list states every code it has, so this vocabulary is closed: no other value is accepted.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/PlcmtSubtypeVideo'

    INSTREAM: ClassVar[Literal[1]] = 1
    """Instream

    Instream: Pre-roll, mid-roll, and post-roll ads that are played before, during or after the
    streaming video content that the consumer has requested. Instream video must be set to
    “sound on” by default at player start, or have explicitly clear user intent to watch the
    video content. While there may be other content surrounding the player, the video content
    must be the focus of the user’s visit. It should remain the primary content on the page and
    the only video player in-view capable of audio when playing. If the player converts to
    floating/sticky subsequent ad calls should accurately convey the updated player size.
    """
    ACCOMPANYING_CONTENT: ClassVar[Literal[2]] = 2
    """Accompanying Content

    Accompanying Content: Pre-roll, mid-roll, and post-roll ads that are played before, during,
    or after streaming video content. The video player loads and plays before, between, or after
    paragraphs of text or graphical content, and starts playing only when it enters the
    viewport. Accompanying content should only start playback upon entering the viewport. It may
    convert to a floating/sticky player as it scrolls off the page.
    """
    INTERSTITIAL: ClassVar[Literal[3]] = 3
    """Interstitial

    Interstitial:Video ads that are played without video content. During playback, it must be
    the primary focus of the page and take up the majority of the viewport and cannot be
    scrolled out of view. This can be in placements like in-app video or slideshows.
    """
    NO_CONTENT_STANDALONE: ClassVar[Literal[4]] = 4
    """No Content/Standalone

    No Content/Standalone: Video ads that are played without streaming video content. This can
    be in placements like slideshows, native feeds, in-content or sticky/floating.
    """
    PAUSE: ClassVar[Literal[5]] = 5
    """Pause

    Pause: An ad present in streaming video content that the consumer has requested. While there
    may be other content surrounding the player, the video content must be the focus of the
    user’s visit. It should remain the primary content on the page and the only video player
    in-view.
    """
    SCREENSAVER: ClassVar[Literal[6]] = 6
    """Screensaver

    Screensaver: An ad present, when OS/App Screen Saver are initiated.
    """
    OVERLAY: ClassVar[Literal[7]] = 7
    """Overlay

    Overlay: Ads occurring during program content and outside of the traditional ad break. The
    ad format places ad creatives over top of the program content, often as a banner or picture
    in picture execution. While there may be other content surrounding the player with the
    overlay, the player with the overlay must be the focus of the user’s visit. It should remain
    the primary content on the page and the primary video player in-view.
    """
    SQUEEZEBACK: ClassVar[Literal[8]] = 8
    """Squeezeback

    Squeezeback: Ads Alongside or Adjacent to Content, also known as L-Shape Ads & Double Box,
    are ads that occur during program content and outside of the traditional ad break. The
    program content is resized to allow for placement of an ad on the screen. In a squeezeback,
    none of the content is covered by the ad, instead it shares screen space with the ad. This
    is the major distinction between squeezeback and overlay. While there may be other content
    surrounding the player with the squeezeback, the player with the squeezeback must be the
    focus of the user’s visit. It should remain the primary content on the page and the primary
    video player in-view.
    """
    IN_SCENE: ClassVar[Literal[9]] = 9
    """In-scene

    In-scene: A form of advertising that integrates branded elements directly within the content
    itself, rather than appearing as separate pre-roll, mid-roll, overlay, or display formats.
    In Scene Advertising is composited into the video content and blends the brand naturally
    into the scene, environment, or storyline, ensuring contextual relevance and viewer
    immersion without interrupting the user experience. In-scene ads typically consist of
    product placements or virtual out of A insertions. At this time, the standardization focuses
    on the out of home insertions in non-live content. While there may be other content
    surrounding the player with the in-scene ad, the player with the in-scene ad must be the
    focus of the user’s visit. It should remain the primary content on the page and the primary
    video player in-view.
    """

    CODES: ClassVar[Mapping[int, str]] = {
        1: 'INSTREAM',
        2: 'ACCOMPANYING_CONTENT',
        3: 'INTERSTITIAL',
        4: 'NO_CONTENT_STANDALONE',
        5: 'PAUSE',
        6: 'SCREENSAVER',
        7: 'OVERLAY',
        8: 'SQUEEZEBACK',
        9: 'IN_SCENE',
    }


class PlcmtSubtypeVideoCode(PlcmtSubtypeVideo):
    """One of the codes List: Plcmt Subtypes - Video states."""
    root: Literal[1, 2, 3, 4, 5, 6, 7, 8, 9]


class PodDeduplicationSetting(Vocabulary[Literal[1, 2, 3, 4, 5]]):
    """List: Pod Deduplication Settings

    The codes of List: Pod Deduplication Settings

    The list states every code it has, so this vocabulary is closed: no other value is accepted.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/PodDeduplicationSetting'

    DEDUPLICATED_ON_ADOMAIN: ClassVar[Literal[1]] = 1
    """Deduplicated on adomain"""
    DEDUPLICATED_ON_CONTENT_TAXONOMY: ClassVar[Literal[2]] = 2
    """Deduplicated on IAB Tech Lab Content Taxonomy"""
    DEDUPLICATED_ON_CREATIVE_ID: ClassVar[Literal[3]] = 3
    """Deduplicated on creative ID"""
    DEDUPLICATED_ON_MEDIAFILE_URL: ClassVar[Literal[4]] = 4
    """Deduplicated on mediafile URL"""
    NO_DEDUPLICATION: ClassVar[Literal[5]] = 5
    """No deduplication"""

    CODES: ClassVar[Mapping[int, str]] = {
        1: 'DEDUPLICATED_ON_ADOMAIN',
        2: 'DEDUPLICATED_ON_CONTENT_TAXONOMY',
        3: 'DEDUPLICATED_ON_CREATIVE_ID',
        4: 'DEDUPLICATED_ON_MEDIAFILE_URL',
        5: 'NO_DEDUPLICATION',
    }


class PodDeduplicationSettingCode(PodDeduplicationSetting):
    """One of the codes List: Pod Deduplication Settings states."""
    root: Literal[1, 2, 3, 4, 5]


class PodSequence(Vocabulary[Literal[-1, 0, 1]]):
    """List: Pod Sequence

    The codes of List: Pod Sequence

    The list states every code it has, so this vocabulary is closed: no other value is accepted.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/PodSequence'

    LAST_POD_IN_THE_CONTENT_STREAM: ClassVar[Literal[-1]] = -1
    """Last pod in the content stream"""
    ANY_POD_IN_THE_CONTENT_STREAM: ClassVar[Literal[0]] = 0
    """Any pod in the content stream"""
    FIRST_POD_IN_THE_CONTENT_STREAM: ClassVar[Literal[1]] = 1
    """First pod in the content stream"""

    CODES: ClassVar[Mapping[int, str]] = {
        -1: 'LAST_POD_IN_THE_CONTENT_STREAM',
        0: 'ANY_POD_IN_THE_CONTENT_STREAM',
        1: 'FIRST_POD_IN_THE_CONTENT_STREAM',
    }


class PodSequenceCode(PodSequence):
    """One of the codes List: Pod Sequence states."""
    root: Literal[-1, 0, 1]


class ProductionQuality(Vocabulary[Literal[0, 1, 2, 3]]):
    """List: Production Qualities

    The codes of List: Production Qualities

    The list states every code it has, so this vocabulary is closed: no other value is accepted.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/ProductionQuality'

    UNKNOWN: ClassVar[Literal[0]] = 0
    """Unknown"""
    PROFESSIONALLY_PRODUCED: ClassVar[Literal[1]] = 1
    """Professionally Produced"""
    PROSUMER: ClassVar[Literal[2]] = 2
    """Prosumer"""
    USER_GENERATED_UGC: ClassVar[Literal[3]] = 3
    """User Generated (UGC)"""

    CODES: ClassVar[Mapping[int, str]] = {
        0: 'UNKNOWN',
        1: 'PROFESSIONALLY_PRODUCED',
        2: 'PROSUMER',
        3: 'USER_GENERATED_UGC',
    }


class ProductionQualityCode(ProductionQuality):
    """One of the codes List: Production Qualities states."""
    root: Literal[0, 1, 2, 3]


class SizeUnit(Vocabulary[Literal[1, 2, 3]]):
    """List: Size Units

    The codes of List: Size Units

    The list states every code it has, so this vocabulary is closed: no other value is accepted.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/SizeUnit'

    DEVICE_INDEPENDENT_PIXELS_DIPS: ClassVar[Literal[1]] = 1
    """Device Independent Pixels (DIPS)"""
    INCHES: ClassVar[Literal[2]] = 2
    """Inches"""
    CENTIMETERS: ClassVar[Literal[3]] = 3
    """Centimeters"""

    CODES: ClassVar[Mapping[int, str]] = {
        1: 'DEVICE_INDEPENDENT_PIXELS_DIPS',
        2: 'INCHES',
        3: 'CENTIMETERS',
    }


class SizeUnitCode(SizeUnit):
    """One of the codes List: Size Units states."""
    root: Literal[1, 2, 3]


class SlotPositionInPod(Vocabulary[Literal[-1, 0, 1, 2]]):
    """List: Slot Position in Pod

    The codes of List: Slot Position in Pod

    The list states every code it has, so this vocabulary is closed: no other value is accepted.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/SlotPositionInPod'

    LAST_AD_IN_THE_POD: ClassVar[Literal[-1]] = -1
    """Last ad in the pod"""
    ANY_AD_IN_THE_POD: ClassVar[Literal[0]] = 0
    """Any ad in the pod"""
    FIRST_AD_IN_THE_POD: ClassVar[Literal[1]] = 1
    """First ad in the pod"""
    FIRST_OR_LAST_AD_IN_THE_POD: ClassVar[Literal[2]] = 2
    """First or Last ad in the pod"""

    CODES: ClassVar[Mapping[int, str]] = {
        -1: 'LAST_AD_IN_THE_POD',
        0: 'ANY_AD_IN_THE_POD',
        1: 'FIRST_AD_IN_THE_POD',
        2: 'FIRST_OR_LAST_AD_IN_THE_POD',
    }


class SlotPositionInPodCode(SlotPositionInPod):
    """One of the codes List: Slot Position in Pod states."""
    root: Literal[-1, 0, 1, 2]


class StartDelayMode(Vocabulary[Literal[-2, -1, 0] | MediaOffset]):
    """List: Start Delay Modes

    The codes of List: Start Delay Modes, or, for a mid-roll at a given second, the delay in
    seconds, which the row `>0` stands for

    The list reserves codes it does not state, so this vocabulary is open: a value is one of the
    codes below or a value of MediaOffset. StartDelayModeExtension is the extension point, and
    an application names its own code by subclassing it.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/StartDelayMode'

    GENERIC_POST_ROLL: ClassVar[Literal[-2]] = -2
    """Generic Post-Roll"""
    GENERIC_MID_ROLL: ClassVar[Literal[-1]] = -1
    """Generic Mid-Roll"""
    PRE_ROLL: ClassVar[Literal[0]] = 0
    """Pre-Roll"""

    CODES: ClassVar[Mapping[int, str]] = {
        -2: 'GENERIC_POST_ROLL',
        -1: 'GENERIC_MID_ROLL',
        0: 'PRE_ROLL',
    }


class StartDelayModeCode(StartDelayMode):
    """One of the codes List: Start Delay Modes states."""
    root: Literal[-2, -1, 0]


class StartDelayModeExtension(StartDelayMode):
    """Media offset: a value of MediaOffset, which is this vocabulary's extension point.

    A point within a piece of media, in whole seconds from its start and never negative, such as
    the second of a video at which a mid-roll ad starts.

    An application carries its own code by subclassing this class and naming the code in its own
    `CODES`. The published schema already admits the value, so the verdict does not change.
    """
    root: MediaOffset


class UserAgentSource(Vocabulary[Literal[0, 1, 2, 3]]):
    """List: User-Agent Source

    The codes of List: User-Agent Source

    The list states every code it has, so this vocabulary is closed: no other value is accepted.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/UserAgentSource'

    UNSPECIFIED_UNKNOWN: ClassVar[Literal[0]] = 0
    """Unspecified/unknown"""
    LOW_ENTROPY_CLIENT_HINTS: ClassVar[Literal[1]] = 1
    """Low-Entropy Client Hints

    User-Agent Client Hints (only low-entropy headers were available)
    """
    HIGH_ENTROPY_CLIENT_HINTS: ClassVar[Literal[2]] = 2
    """High-Entropy Client Hints

    User-Agent Client Hints (with high-entropy headers available)
    """
    PARSED_FROM_USER_AGENT_HEADER: ClassVar[Literal[3]] = 3
    """Parsed from User-Agent header

    Parsed from User-Agent header (the same string carried by the ua field)
    """

    CODES: ClassVar[Mapping[int, str]] = {
        0: 'UNSPECIFIED_UNKNOWN',
        1: 'LOW_ENTROPY_CLIENT_HINTS',
        2: 'HIGH_ENTROPY_CLIENT_HINTS',
        3: 'PARSED_FROM_USER_AGENT_HEADER',
    }


class UserAgentSourceCode(UserAgentSource):
    """One of the codes List: User-Agent Source states."""
    root: Literal[0, 1, 2, 3]


class VolumeNormalizationMode(Vocabulary[Literal[0, 1, 2, 3, 4]]):
    """List: Volume Normalization Modes

    The codes of List: Volume Normalization Modes

    The list states every code it has, so this vocabulary is closed: no other value is accepted.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json#/$defs/VolumeNormalizationMode'

    NONE: ClassVar[Literal[0]] = 0
    """None"""
    AD_VOLUME_AVERAGE_NORMALIZED_TO_CONTENT: ClassVar[Literal[1]] = 1
    """Ad Volume Average Normalized to Content"""
    AD_VOLUME_PEAK_NORMALIZED_TO_CONTENT: ClassVar[Literal[2]] = 2
    """Ad Volume Peak Normalized to Content"""
    AD_LOUDNESS_NORMALIZED_TO_CONTENT: ClassVar[Literal[3]] = 3
    """Ad Loudness Normalized to Content"""
    CUSTOM_VOLUME_NORMALIZATION: ClassVar[Literal[4]] = 4
    """Custom Volume Normalization"""

    CODES: ClassVar[Mapping[int, str]] = {
        0: 'NONE',
        1: 'AD_VOLUME_AVERAGE_NORMALIZED_TO_CONTENT',
        2: 'AD_VOLUME_PEAK_NORMALIZED_TO_CONTENT',
        3: 'AD_LOUDNESS_NORMALIZED_TO_CONTENT',
        4: 'CUSTOM_VOLUME_NORMALIZATION',
    }


class VolumeNormalizationModeCode(VolumeNormalizationMode):
    """One of the codes List: Volume Normalization Modes states."""
    root: Literal[0, 1, 2, 3, 4]


class AmpRenderingTreatment(Vocabulary[Literal[1, 2]]):
    """Amp Rendering Treatment

    The codes of `DisplayPlacement.ampren`, each with the label the text gives it

    The list states every code it has, so this vocabulary is closed: no other value is accepted.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/AmpRenderingTreatment'

    EARLY_LOADING: ClassVar[Literal[1]] = 1
    """early loading"""
    STANDARD_LOADING: ClassVar[Literal[2]] = 2
    """standard loading"""

    CODES: ClassVar[Mapping[int, str]] = {
        1: 'EARLY_LOADING',
        2: 'STANDARD_LOADING',
    }


class AmpRenderingTreatmentCode(AmpRenderingTreatment):
    """One of the codes Amp Rendering Treatment states."""
    root: Literal[1, 2]


class DoohPlacementMobility(Vocabulary[Literal[1, 2]]):
    """Dooh Placement Mobility

    The codes of `Dooh.fixed`, each with the label the text gives it

    The list states every code it has, so this vocabulary is closed: no other value is accepted.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/DoohPlacementMobility'

    FIXED: ClassVar[Literal[1]] = 1
    """fixed"""
    MOVABLE: ClassVar[Literal[2]] = 2
    """movable"""

    CODES: ClassVar[Mapping[int, str]] = {
        1: 'FIXED',
        2: 'MOVABLE',
    }


class DoohPlacementMobilityCode(DoohPlacementMobility):
    """One of the codes Dooh Placement Mobility states."""
    root: Literal[1, 2]


class ServerSideAdInsertionMode(Vocabulary[Literal[0, 1, 2, 3]]):
    """Server Side Ad Insertion Mode

    The codes of `Placement.ssai`, each with the label the text gives it

    The list states every code it has, so this vocabulary is closed: no other value is accepted.
    """

    SCHEMA: ClassVar[str] = 'https://jsonspecs.com/adcom/schemas/modules/objects/1/objects.json#/$defs/ServerSideAdInsertionMode'

    STATUS_UNKNOWN: ClassVar[Literal[0]] = 0
    """status unknown"""
    ALL_CLIENT_SIDE: ClassVar[Literal[1]] = 1
    """all client-side

    all client-side (i.e., not server-side)
    """
    ASSETS_STITCHED_SERVER_SIDE_BUT_TRACKING_PIXELS: ClassVar[Literal[2]] = 2
    """assets stitched server-side but tracking pixels fired client-side"""
    ALL_SERVER_SIDE: ClassVar[Literal[3]] = 3
    """all server-side"""

    CODES: ClassVar[Mapping[int, str]] = {
        0: 'STATUS_UNKNOWN',
        1: 'ALL_CLIENT_SIDE',
        2: 'ASSETS_STITCHED_SERVER_SIDE_BUT_TRACKING_PIXELS',
        3: 'ALL_SERVER_SIDE',
    }


class ServerSideAdInsertionModeCode(ServerSideAdInsertionMode):
    """One of the codes Server Side Ad Insertion Mode states."""
    root: Literal[0, 1, 2, 3]


# Each base takes its branches and is rebuilt, which is what installs the branch classes
# as the base's own validator: a branch subclasses the base, so it does not exist while
# the base is being built.
AgentType._branch_models = (AgentTypeCode, AgentTypeExtension,)
ApiFramework._branch_models = (ApiFrameworkCode, ApiFrameworkExtension,)
AuditStatusCode._branch_models = (AuditStatusCodeCode, AuditStatusCodeExtension,)
AutoRefreshTrigger._branch_models = (AutoRefreshTriggerCode,)
CategoryTaxonomy._branch_models = (CategoryTaxonomyCode, CategoryTaxonomyExtension,)
ClickType._branch_models = (ClickTypeCode, ClickTypeExtension,)
CompanionType._branch_models = (CompanionTypeCode,)
ConnectionType._branch_models = (ConnectionTypeCode,)
ContentContext._branch_models = (ContentContextCode,)
CreativeAttribute._branch_models = (CreativeAttributeCode, CreativeAttributeExtension,)
CreativeSubtypeAudioVideo._branch_models = (CreativeSubtypeAudioVideoCode,)
CreativeSubtypeDisplay._branch_models = (CreativeSubtypeDisplayCode,)
DeliveryMethod._branch_models = (DeliveryMethodCode,)
DeviceType._branch_models = (DeviceTypeCode,)
DisplayContextType._branch_models = (DisplayContextTypeCode, DisplayContextTypeExtension,)
DisplayPlacementType._branch_models = (DisplayPlacementTypeCode, DisplayPlacementTypeExtension,)
DoohMultiplierMeasurementSourceType._branch_models = (DoohMultiplierMeasurementSourceTypeCode,)
DoohVenueTaxonomy._branch_models = (DoohVenueTaxonomyCode,)
EventTrackingMethod._branch_models = (EventTrackingMethodCode, EventTrackingMethodExtension,)
EventType._branch_models = (EventTypeCode, EventTypeExtension,)
ExpandableDirection._branch_models = (ExpandableDirectionCode,)
FeedType._branch_models = (FeedTypeCode, FeedTypeExtension,)
IdMatchMethod._branch_models = (IdMatchMethodCode, IdMatchMethodExtension,)
IpLocationService._branch_models = (IpLocationServiceCode,)
LinearityMode._branch_models = (LinearityModeCode,)
LocationType._branch_models = (LocationTypeCode,)
MediaRating._branch_models = (MediaRatingCode,)
NativeDataAssetType._branch_models = (NativeDataAssetTypeCode, NativeDataAssetTypeExtension,)
NativeImageAssetType._branch_models = (NativeImageAssetTypeCode, NativeImageAssetTypeExtension,)
OperatingSystem._branch_models = (OperatingSystemCode, OperatingSystemExtension,)
PlacementPosition._branch_models = (PlacementPositionCode,)
PlaybackCessationMode._branch_models = (PlaybackCessationModeCode,)
PlaybackMethod._branch_models = (PlaybackMethodCode,)
PlcmtSubtypeVideo._branch_models = (PlcmtSubtypeVideoCode,)
PodDeduplicationSetting._branch_models = (PodDeduplicationSettingCode,)
PodSequence._branch_models = (PodSequenceCode,)
ProductionQuality._branch_models = (ProductionQualityCode,)
SizeUnit._branch_models = (SizeUnitCode,)
SlotPositionInPod._branch_models = (SlotPositionInPodCode,)
StartDelayMode._branch_models = (StartDelayModeCode, StartDelayModeExtension,)
UserAgentSource._branch_models = (UserAgentSourceCode,)
VolumeNormalizationMode._branch_models = (VolumeNormalizationModeCode,)
AmpRenderingTreatment._branch_models = (AmpRenderingTreatmentCode,)
DoohPlacementMobility._branch_models = (DoohPlacementMobilityCode,)
ServerSideAdInsertionMode._branch_models = (ServerSideAdInsertionModeCode,)
AgentType.model_rebuild(force=True)
ApiFramework.model_rebuild(force=True)
AuditStatusCode.model_rebuild(force=True)
AutoRefreshTrigger.model_rebuild(force=True)
CategoryTaxonomy.model_rebuild(force=True)
ClickType.model_rebuild(force=True)
CompanionType.model_rebuild(force=True)
ConnectionType.model_rebuild(force=True)
ContentContext.model_rebuild(force=True)
CreativeAttribute.model_rebuild(force=True)
CreativeSubtypeAudioVideo.model_rebuild(force=True)
CreativeSubtypeDisplay.model_rebuild(force=True)
DeliveryMethod.model_rebuild(force=True)
DeviceType.model_rebuild(force=True)
DisplayContextType.model_rebuild(force=True)
DisplayPlacementType.model_rebuild(force=True)
DoohMultiplierMeasurementSourceType.model_rebuild(force=True)
DoohVenueTaxonomy.model_rebuild(force=True)
EventTrackingMethod.model_rebuild(force=True)
EventType.model_rebuild(force=True)
ExpandableDirection.model_rebuild(force=True)
FeedType.model_rebuild(force=True)
IdMatchMethod.model_rebuild(force=True)
IpLocationService.model_rebuild(force=True)
LinearityMode.model_rebuild(force=True)
LocationType.model_rebuild(force=True)
MediaRating.model_rebuild(force=True)
NativeDataAssetType.model_rebuild(force=True)
NativeImageAssetType.model_rebuild(force=True)
OperatingSystem.model_rebuild(force=True)
PlacementPosition.model_rebuild(force=True)
PlaybackCessationMode.model_rebuild(force=True)
PlaybackMethod.model_rebuild(force=True)
PlcmtSubtypeVideo.model_rebuild(force=True)
PodDeduplicationSetting.model_rebuild(force=True)
PodSequence.model_rebuild(force=True)
ProductionQuality.model_rebuild(force=True)
SizeUnit.model_rebuild(force=True)
SlotPositionInPod.model_rebuild(force=True)
StartDelayMode.model_rebuild(force=True)
UserAgentSource.model_rebuild(force=True)
VolumeNormalizationMode.model_rebuild(force=True)
AmpRenderingTreatment.model_rebuild(force=True)
DoohPlacementMobility.model_rebuild(force=True)
ServerSideAdInsertionMode.model_rebuild(force=True)
