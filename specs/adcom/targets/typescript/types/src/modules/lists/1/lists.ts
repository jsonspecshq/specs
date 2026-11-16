/**
 * Generated from a published JSON Schema tree; don't edit it by hand.
 *
 * From https://jsonspecs.com/adcom/schemas/modules/lists/1/lists.json
 */

import type { MediaOffset, VendorCode } from "../../../kernel/1/kernel.js";

/**
 * The key every extension brand is stamped under. It is `declare const` and is never exported as a
 * value, so no consumer can build a branded value by writing the member: the constructors above are
 * the only way in, and each applies what the published bytes admit.
 */
declare const EXTENSION: unique symbol;

/**
 * List: Agent Types
 *
 * The codes of List: Agent Types
 */
export type AgentType = 1 | 2 | 3 | AgentTypeExtension;

/**
 * The codes of AgentType, each under the name the published schema carries for it.
 */
export const AgentTypeCodes = {
  /**
   * Browser or device ID
   *
   * An ID which is tied to a specific web browser or device (cookie-based, probabilistic, or
   * other).
   */
  BROWSER_OR_DEVICE_ID: 1,
  /**
   * In-app impressions
   *
   * In-app impressions, which will typically contain a type of device ID (or rather, the
   * privacy-compliant versions of device IDs).
   */
  IN_APP_IMPRESSIONS: 2,
  /**
   * Person-based ID
   *
   * A person-based ID, i.e., that is the same across devices.
   */
  PERSON_BASED_ID: 3,
} as const satisfies Readonly<Record<string, AgentType>>;

/**
 * Vendor-specific: a VendorCode the list admits beside its own codes. Vendor-specific codes.
 *
 * It is a brand, so a bare `number` is not one of these: a union of literals widened by `number`
 * collapses to `number` and the listed codes stop constraining anything. Build one with
 * `agentTypeExtension`.
 */
export type AgentTypeExtension = VendorCode & { readonly [EXTENSION]: "AgentType" };

/**
 * Whether a `number` is one of this vocabulary's extension values. The test is what VendorCode and
 * this branch state in the published schema.
 */
export const isAgentTypeExtension = (value: number): value is AgentTypeExtension => Number.isInteger(value) && value >= 500;

/**
 * Builds a AgentTypeExtension, or throws. The only way to reach this vocabulary's extension values.
 *
 * @throws TypeError where `isAgentTypeExtension` is false
 */
export const agentTypeExtension = (value: number): AgentTypeExtension => {
  if (!isAgentTypeExtension(value)) throw new TypeError(`${JSON.stringify(value)} is no AgentType extension value`);
  return value;
};

/**
 * List: API Frameworks
 *
 * The codes of List: API Frameworks
 */
export type ApiFramework = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | ApiFrameworkExtension;

/**
 * The codes of ApiFramework, each under the name the published schema carries for it.
 */
export const ApiFrameworkCodes = {
  /**
   * VPAID 1.0
   */
  VPAID_1_0: 1,
  /**
   * VPAID 2.0
   */
  VPAID_2_0: 2,
  /**
   * MRAID 1.0
   */
  MRAID_1_0: 3,
  /**
   * ORMMA
   */
  ORMMA: 4,
  /**
   * MRAID 2.0
   */
  MRAID_2_0: 5,
  /**
   * MRAID 3.0
   */
  MRAID_3_0: 6,
  /**
   * OMID 1.0
   */
  OMID_1_0: 7,
  /**
   * SIMID 1.0
   */
  SIMID_1_0: 8,
  /**
   * SIMID 1.1
   */
  SIMID_1_1: 9,
} as const satisfies Readonly<Record<string, ApiFramework>>;

/**
 * Vendor-specific: a VendorCode the list admits beside its own codes. Vendor-specific codes.
 *
 * It is a brand, so a bare `number` is not one of these: a union of literals widened by `number`
 * collapses to `number` and the listed codes stop constraining anything. Build one with
 * `apiFrameworkExtension`.
 */
export type ApiFrameworkExtension = VendorCode & { readonly [EXTENSION]: "ApiFramework" };

/**
 * Whether a `number` is one of this vocabulary's extension values. The test is what VendorCode and
 * this branch state in the published schema.
 */
export const isApiFrameworkExtension = (value: number): value is ApiFrameworkExtension => Number.isInteger(value) && value >= 500;

/**
 * Builds a ApiFrameworkExtension, or throws. The only way to reach this vocabulary's extension
 * values.
 *
 * @throws TypeError where `isApiFrameworkExtension` is false
 */
export const apiFrameworkExtension = (value: number): ApiFrameworkExtension => {
  if (!isApiFrameworkExtension(value)) throw new TypeError(`${JSON.stringify(value)} is no ApiFramework extension value`);
  return value;
};

/**
 * List: Audit Status Codes
 *
 * The codes of List: Audit Status Codes
 */
export type AuditStatusCode = 1 | 2 | 3 | 4 | 5 | 6 | AuditStatusCodeExtension;

/**
 * The codes of AuditStatusCode, each under the name the published schema carries for it.
 */
export const AuditStatusCodeCodes = {
  /**
   * Pending Audit
   *
   * Pending Audit: An audit has not yet been completed on this ad. A recommendation cannot be made
   * to use this ad, but vendors' policies may override.
   */
  PENDING_AUDIT: 1,
  /**
   * Pre-Approved
   *
   * Pre-Approved: An audit has not yet been completed on this ad. Subject to vendors' policies, it
   * can be recommended for use. However, once the audit has been completed, its status will change
   * and it may or may not be approved for continued use.
   */
  PRE_APPROVED: 2,
  /**
   * Approved
   *
   * Approved: The audit is complete and the ad is approved for use. Note, however, that some
   * attributes (e.g., `adomain`, `cat`, `attr`, etc.) may have been changed in the process by the
   * auditor.
   */
  APPROVED: 3,
  /**
   * Denied
   *
   * Denied: The audit is complete, but the ad has been found unacceptable in some material aspect
   * and is disapproved for use.
   */
  DENIED: 4,
  /**
   * Changed; Resubmission Requested
   *
   * Changed; Resubmission Requested: A version of the ad has been detected in use that is
   * materially different from the version that was previously audited, which may result in
   * rejection during use until the ad is resubmitted for audit and approved. Vendors need to
   * communicate offline as to the criteria that constitutes a material change.
   */
  CHANGED_RESUBMISSION_REQUESTED: 5,
  /**
   * Expired
   *
   * Expired: The ad has been marked as expired by the vendor. Vendors need to communicate offline
   * as to the expected bidding behavior for ads with this status.
   */
  EXPIRED: 6,
} as const satisfies Readonly<Record<string, AuditStatusCode>>;

/**
 * Vendor-specific: a VendorCode the list admits beside its own codes. Vendor-specific codes.
 *
 * It is a brand, so a bare `number` is not one of these: a union of literals widened by `number`
 * collapses to `number` and the listed codes stop constraining anything. Build one with
 * `auditStatusCodeExtension`.
 */
export type AuditStatusCodeExtension = VendorCode & { readonly [EXTENSION]: "AuditStatusCode" };

/**
 * Whether a `number` is one of this vocabulary's extension values. The test is what VendorCode and
 * this branch state in the published schema.
 */
export const isAuditStatusCodeExtension = (value: number): value is AuditStatusCodeExtension => Number.isInteger(value) && value >= 500;

/**
 * Builds a AuditStatusCodeExtension, or throws. The only way to reach this vocabulary's extension
 * values.
 *
 * @throws TypeError where `isAuditStatusCodeExtension` is false
 */
export const auditStatusCodeExtension = (value: number): AuditStatusCodeExtension => {
  if (!isAuditStatusCodeExtension(value)) throw new TypeError(`${JSON.stringify(value)} is no AuditStatusCode extension value`);
  return value;
};

/**
 * List: Auto Refresh Triggers
 *
 * The codes of List: Auto Refresh Triggers
 */
export type AutoRefreshTrigger = 0 | 1 | 2 | 3;

/**
 * The codes of AutoRefreshTrigger, each under the name the published schema carries for it.
 */
export const AutoRefreshTriggerCodes = {
  /**
   * UNKNOWN
   */
  UNKNOWN: 0,
  /**
   * User Action
   *
   * User Action: Refresh triggered by user-initiated action such as scrolling.
   */
  USER_ACTION: 1,
  /**
   * Event
   *
   * Event: Event-driven content change. For example, ads refresh when the football game score
   * changes on the page.
   */
  EVENT: 2,
  /**
   * Time
   *
   * Time:Time-based refresh. Ads refresh on a predefined time interval even without user activity.
   */
  TIME: 3,
} as const satisfies Readonly<Record<string, AutoRefreshTrigger>>;

/**
 * List: Category Taxonomies
 *
 * The codes of List: Category Taxonomies
 */
export type CategoryTaxonomy = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | CategoryTaxonomyExtension;

/**
 * The codes of CategoryTaxonomy, each under the name the published schema carries for it.
 */
export const CategoryTaxonomyCodes = {
  /**
   * IAB Tech Lab Content Category Taxonomy 1.0
   *
   * IAB Tech Lab Content Category Taxonomy 1.0: Deprecated, and recommend NOT be used since it does
   * not have SCD flags.
   */
  CONTENT_CATEGORY_TAXONOMY_1_0: 1,
  /**
   * IAB Tech Lab Content Category Taxonomy 2.0
   *
   * IAB Tech Lab Content Category Taxonomy 2.0: Deprecated, and recommend NOT be used since it does
   * not have SCD flags.
   */
  CONTENT_CATEGORY_TAXONOMY_2_0: 2,
  /**
   * IAB Tech Lab Ad Product Taxonomy 1.0
   *
   * IAB Tech Lab Ad Product Taxonomy 1.0.
   */
  IAB_TECH_LAB_AD_PRODUCT_TAXONOMY_1_0: 3,
  /**
   * IAB Tech Lab Audience Taxonomy 1.1
   */
  IAB_TECH_LAB_AUDIENCE_TAXONOMY_1_1: 4,
  /**
   * IAB Tech Lab Content Taxonomy 2.1
   */
  IAB_TECH_LAB_CONTENT_TAXONOMY_2_1: 5,
  /**
   * IAB Tech Lab Content Taxonomy 2.2
   */
  IAB_TECH_LAB_CONTENT_TAXONOMY_2_2: 6,
  /**
   * IAB Tech Lab Content Taxonomy 3.0
   */
  IAB_TECH_LAB_CONTENT_TAXONOMY_3_0: 7,
  /**
   * IAB Tech Lab Ad Product Taxonomy 2.0
   */
  IAB_TECH_LAB_AD_PRODUCT_TAXONOMY_2_0: 8,
  /**
   * IAB Tech Lab Content Taxonomy 3.1
   */
  IAB_TECH_LAB_CONTENT_TAXONOMY_3_1: 9,
} as const satisfies Readonly<Record<string, CategoryTaxonomy>>;

/**
 * Vendor-specific: a VendorCode the list admits beside its own codes. Vendor-specific codes.
 *
 * It is a brand, so a bare `number` is not one of these: a union of literals widened by `number`
 * collapses to `number` and the listed codes stop constraining anything. Build one with
 * `categoryTaxonomyExtension`.
 */
export type CategoryTaxonomyExtension = VendorCode & { readonly [EXTENSION]: "CategoryTaxonomy" };

/**
 * Whether a `number` is one of this vocabulary's extension values. The test is what VendorCode and
 * this branch state in the published schema.
 */
export const isCategoryTaxonomyExtension = (value: number): value is CategoryTaxonomyExtension => Number.isInteger(value) && value >= 500;

/**
 * Builds a CategoryTaxonomyExtension, or throws. The only way to reach this vocabulary's extension
 * values.
 *
 * @throws TypeError where `isCategoryTaxonomyExtension` is false
 */
export const categoryTaxonomyExtension = (value: number): CategoryTaxonomyExtension => {
  if (!isCategoryTaxonomyExtension(value)) throw new TypeError(`${JSON.stringify(value)} is no CategoryTaxonomy extension value`);
  return value;
};

/**
 * List: Click Types
 *
 * The codes of List: Click Types
 */
export type ClickType = 0 | 1 | 2 | 3 | ClickTypeExtension;

/**
 * The codes of ClickType, each under the name the published schema carries for it.
 */
export const ClickTypeCodes = {
  /**
   * Non-Clickable
   */
  NON_CLICKABLE: 0,
  /**
   * Clickable - Details Unknown
   */
  CLICKABLE_DETAILS_UNKNOWN: 1,
  /**
   * Clickable - Embedded Browser/Webview
   */
  CLICKABLE_EMBEDDED_BROWSER_WEBVIEW: 2,
  /**
   * Clickable - Native Browser
   */
  CLICKABLE_NATIVE_BROWSER: 3,
} as const satisfies Readonly<Record<string, ClickType>>;

/**
 * Vendor-specific: a VendorCode the list admits beside its own codes. Vendor-specific codes.
 *
 * It is a brand, so a bare `number` is not one of these: a union of literals widened by `number`
 * collapses to `number` and the listed codes stop constraining anything. Build one with
 * `clickTypeExtension`.
 */
export type ClickTypeExtension = VendorCode & { readonly [EXTENSION]: "ClickType" };

/**
 * Whether a `number` is one of this vocabulary's extension values. The test is what VendorCode and
 * this branch state in the published schema.
 */
export const isClickTypeExtension = (value: number): value is ClickTypeExtension => Number.isInteger(value) && value >= 500;

/**
 * Builds a ClickTypeExtension, or throws. The only way to reach this vocabulary's extension values.
 *
 * @throws TypeError where `isClickTypeExtension` is false
 */
export const clickTypeExtension = (value: number): ClickTypeExtension => {
  if (!isClickTypeExtension(value)) throw new TypeError(`${JSON.stringify(value)} is no ClickType extension value`);
  return value;
};

/**
 * List: Companion Types
 *
 * The codes of List: Companion Types
 */
export type CompanionType = 1 | 2 | 3;

/**
 * The codes of CompanionType, each under the name the published schema carries for it.
 */
export const CompanionTypeCodes = {
  /**
   * Static Resource
   */
  STATIC_RESOURCE: 1,
  /**
   * HTML Resource
   */
  HTML_RESOURCE: 2,
  /**
   * iframe Resource
   */
  IFRAME_RESOURCE: 3,
} as const satisfies Readonly<Record<string, CompanionType>>;

/**
 * List: Connection Types
 *
 * The codes of List: Connection Types
 */
export type ConnectionType = 1 | 2 | 3 | 4 | 5 | 6 | 7;

/**
 * The codes of ConnectionType, each under the name the published schema carries for it.
 */
export const ConnectionTypeCodes = {
  /**
   * Ethernet; Wired Connection
   */
  ETHERNET_WIRED_CONNECTION: 1,
  /**
   * WIFI
   */
  WIFI: 2,
  /**
   * Cellular Network - Unknown Generation
   */
  CELLULAR_NETWORK_UNKNOWN_GENERATION: 3,
  /**
   * Cellular Network - 2G
   */
  CELLULAR_NETWORK_2G: 4,
  /**
   * Cellular Network - 3G
   */
  CELLULAR_NETWORK_3G: 5,
  /**
   * Cellular Network - 4G
   */
  CELLULAR_NETWORK_4G: 6,
  /**
   * Cellular Network - 5G
   */
  CELLULAR_NETWORK_5G: 7,
} as const satisfies Readonly<Record<string, ConnectionType>>;

/**
 * List: Content Contexts
 *
 * The codes of List: Content Contexts
 */
export type ContentContext = 1 | 2 | 3 | 4 | 5 | 6 | 7;

/**
 * The codes of ContentContext, each under the name the published schema carries for it.
 */
export const ContentContextCodes = {
  /**
   * Video
   *
   * Video (i.e., video file or stream such as Internet TV broadcasts)
   */
  VIDEO: 1,
  /**
   * Game
   *
   * Game (i.e., an interactive software game)
   */
  GAME: 2,
  /**
   * Music
   *
   * Music (i.e., audio file or stream such as Internet radio broadcasts)
   */
  MUSIC: 3,
  /**
   * Application
   *
   * Application (i.e., an interactive software application)
   */
  APPLICATION: 4,
  /**
   * Text
   *
   * Text (i.e., primarily textual document such as a web page, eBook, or news article)
   */
  TEXT: 5,
  /**
   * Other
   *
   * Other (i.e., none of the other categories applies)
   */
  OTHER: 6,
  /**
   * Unknown
   */
  UNKNOWN: 7,
} as const satisfies Readonly<Record<string, ContentContext>>;

/**
 * List: Creative Attributes
 *
 * The codes of List: Creative Attributes
 */
export type CreativeAttribute = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | CreativeAttributeExtension;

/**
 * The codes of CreativeAttribute, each under the name the published schema carries for it.
 */
export const CreativeAttributeCodes = {
  /**
   * Audio Ad (Autoplay)
   */
  AUDIO_AD_AUTOPLAY: 1,
  /**
   * Audio Ad (User Initiated)
   */
  AUDIO_AD_USER_INITIATED: 2,
  /**
   * Expandable (Automatic)
   */
  EXPANDABLE_AUTOMATIC: 3,
  /**
   * Expandable (User Initiated - Click)
   */
  EXPANDABLE_USER_INITIATED_CLICK: 4,
  /**
   * Expandable (User Initiated - Rollover)
   */
  EXPANDABLE_USER_INITIATED_ROLLOVER: 5,
  /**
   * In-Banner Video Ad (Autoplay)
   */
  IN_BANNER_VIDEO_AD_AUTOPLAY: 6,
  /**
   * In-Banner Video Ad (User Initiated)
   */
  IN_BANNER_VIDEO_AD_USER_INITIATED: 7,
  /**
   * Pop
   *
   * Pop (e.g., Over, Under, or Upon Exit)
   */
  POP: 8,
  /**
   * Provocative or Suggestive Imagery
   */
  PROVOCATIVE_OR_SUGGESTIVE_IMAGERY: 9,
  /**
   * Shaky, Flashing, or Extreme Animation
   *
   * Shaky, Flashing, Flickering, Extreme Animation, Smileys
   */
  SHAKY_FLASHING_OR_EXTREME_ANIMATION: 10,
  /**
   * Surveys
   */
  SURVEYS: 11,
  /**
   * Text Only
   */
  TEXT_ONLY: 12,
  /**
   * User Interactive
   *
   * User Interactive (e.g., Embedded Games)
   */
  USER_INTERACTIVE: 13,
  /**
   * Windows Dialog or Alert Style
   */
  WINDOWS_DIALOG_OR_ALERT_STYLE: 14,
  /**
   * Has Audio On/Off Button
   */
  HAS_AUDIO_ON_OFF_BUTTON: 15,
  /**
   * Ad Provides Skip Button
   *
   * Ad Provides Skip Button (e.g. VPAID-rendered skip button on pre-roll video)
   */
  AD_PROVIDES_SKIP_BUTTON: 16,
  /**
   * Adobe Flash
   */
  ADOBE_FLASH: 17,
  /**
   * Responsive; Sizeless; Fluid
   *
   * Responsive; Sizeless; Fluid (i.e., creatives that dynamically resize to environment)
   */
  RESPONSIVE_SIZELESS_FLUID: 18,
  /**
   * Contains advertiser QR Code
   */
  CONTAINS_ADVERTISER_QR_CODE: 19,
  /**
   * Support alpha channel transparency
   */
  SUPPORT_ALPHA_CHANNEL_TRANSPARENCY: 20,
  /**
   * Static Visual
   *
   * Static Visual. Creative contains no perceptible motion and renders as a static visual, even if
   * delivered in a video file format (e.g., MP4). No animated elements or time-based visual
   * transitions are present.
   */
  STATIC_VISUAL: 21,
  /**
   * Limited Motion
   *
   * Limited Motion (Cinemagraph). Creative contains subtle or localized motion within an otherwise
   * static composition. Motion is minimal, looped, and does not constitute full-scene animation or
   * continuous narrative progression.
   */
  LIMITED_MOTION: 22,
  /**
   * Full-Motion Video
   *
   * Full-Motion Video. Creative contains continuous or scene-level motion typical of standard video
   * assets, including dynamic visual transitions, camera movement, or narrative progression across
   * frames.
   */
  FULL_MOTION_VIDEO: 23,
} as const satisfies Readonly<Record<string, CreativeAttribute>>;

/**
 * Vendor-specific: a VendorCode the list admits beside its own codes. Vendor-specific codes.
 *
 * It is a brand, so a bare `number` is not one of these: a union of literals widened by `number`
 * collapses to `number` and the listed codes stop constraining anything. Build one with
 * `creativeAttributeExtension`.
 */
export type CreativeAttributeExtension = VendorCode & { readonly [EXTENSION]: "CreativeAttribute" };

/**
 * Whether a `number` is one of this vocabulary's extension values. The test is what VendorCode and
 * this branch state in the published schema.
 */
export const isCreativeAttributeExtension = (value: number): value is CreativeAttributeExtension => Number.isInteger(value) && value >= 500;

/**
 * Builds a CreativeAttributeExtension, or throws. The only way to reach this vocabulary's extension
 * values.
 *
 * @throws TypeError where `isCreativeAttributeExtension` is false
 */
export const creativeAttributeExtension = (value: number): CreativeAttributeExtension => {
  if (!isCreativeAttributeExtension(value)) throw new TypeError(`${JSON.stringify(value)} is no CreativeAttribute extension value`);
  return value;
};

/**
 * List: Creative Subtypes - Audio/Video
 *
 * The codes of List: Creative Subtypes - Audio/Video
 */
export type CreativeSubtypeAudioVideo = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16;

/**
 * The codes of CreativeSubtypeAudioVideo, each under the name the published schema carries for it.
 */
export const CreativeSubtypeAudioVideoCodes = {
  /**
   * VAST 1.0
   */
  VAST_1_0: 1,
  /**
   * VAST 2.0
   */
  VAST_2_0: 2,
  /**
   * VAST 3.0
   */
  VAST_3_0: 3,
  /**
   * VAST 1.0 Wrapper
   */
  VAST_1_0_WRAPPER: 4,
  /**
   * VAST 2.0 Wrapper
   */
  VAST_2_0_WRAPPER: 5,
  /**
   * VAST 3.0 Wrapper
   */
  VAST_3_0_WRAPPER: 6,
  /**
   * VAST 4.0
   */
  VAST_4_0: 7,
  /**
   * VAST 4.0 Wrapper
   */
  VAST_4_0_WRAPPER: 8,
  /**
   * DAAST 1.0
   */
  DAAST_1_0: 9,
  /**
   * DAAST 1.0 Wrapper
   */
  DAAST_1_0_WRAPPER: 10,
  /**
   * VAST 4.1
   */
  VAST_4_1: 11,
  /**
   * VAST 4.1 Wrapper
   */
  VAST_4_1_WRAPPER: 12,
  /**
   * VAST 4.2
   */
  VAST_4_2: 13,
  /**
   * VAST 4.2 Wrapper
   */
  VAST_4_2_WRAPPER: 14,
  /**
   * VAST 4.3
   */
  VAST_4_3: 15,
  /**
   * VAST 4.3 Wrapper
   */
  VAST_4_3_WRAPPER: 16,
} as const satisfies Readonly<Record<string, CreativeSubtypeAudioVideo>>;

/**
 * List: Creative Subtypes - Display
 *
 * The codes of List: Creative Subtypes - Display
 */
export type CreativeSubtypeDisplay = 1 | 2 | 3 | 4;

/**
 * The codes of CreativeSubtypeDisplay, each under the name the published schema carries for it.
 */
export const CreativeSubtypeDisplayCodes = {
  /**
   * HTML
   */
  HTML: 1,
  /**
   * AMPHTML
   */
  AMPHTML: 2,
  /**
   * Structured Image Object
   */
  STRUCTURED_IMAGE_OBJECT: 3,
  /**
   * Structured Native Object
   */
  STRUCTURED_NATIVE_OBJECT: 4,
} as const satisfies Readonly<Record<string, CreativeSubtypeDisplay>>;

/**
 * List: Delivery Methods
 *
 * The codes of List: Delivery Methods
 */
export type DeliveryMethod = 1 | 2 | 3;

/**
 * The codes of DeliveryMethod, each under the name the published schema carries for it.
 */
export const DeliveryMethodCodes = {
  /**
   * Streaming
   */
  STREAMING: 1,
  /**
   * Progressive
   */
  PROGRESSIVE: 2,
  /**
   * Download
   */
  DOWNLOAD: 3,
} as const satisfies Readonly<Record<string, DeliveryMethod>>;

/**
 * List: Device Types
 *
 * The codes of List: Device Types
 */
export type DeviceType = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8;

/**
 * The codes of DeviceType, each under the name the published schema carries for it.
 */
export const DeviceTypeCodes = {
  /**
   * Mobile/Tablet - General
   */
  MOBILE_TABLET_GENERAL: 1,
  /**
   * Personal Computer
   */
  PERSONAL_COMPUTER: 2,
  /**
   * Connected TV
   */
  CONNECTED_TV: 3,
  /**
   * Phone
   */
  PHONE: 4,
  /**
   * Tablet
   */
  TABLET: 5,
  /**
   * Connected Device
   */
  CONNECTED_DEVICE: 6,
  /**
   * Set Top Box
   */
  SET_TOP_BOX: 7,
  /**
   * OOH Device
   */
  OOH_DEVICE: 8,
} as const satisfies Readonly<Record<string, DeviceType>>;

/**
 * List: Display Context Types
 *
 * The codes of List: Display Context Types
 */
export type DisplayContextType = 10 | 11 | 12 | 13 | 14 | 15 | 20 | 21 | 22 | 30 | 31 | 32 | DisplayContextTypeExtension;

/**
 * The codes of DisplayContextType, each under the name the published schema carries for it.
 */
export const DisplayContextTypeCodes = {
  /**
   * Content-centric context
   *
   * Content-centric context (e.g., newsfeed, article, image gallery, video gallery, etc.).
   */
  CONTENT_CENTRIC_CONTEXT: 10,
  /**
   * Primarily article content
   *
   * - Primarily article content, which could include images, etc. as part of the article.
   */
  PRIMARILY_ARTICLE_CONTENT: 11,
  /**
   * Primarily video content
   *
   * - Primarily video content.
   */
  PRIMARILY_VIDEO_CONTENT: 12,
  /**
   * Primarily audio content
   *
   * - Primarily audio content.
   */
  PRIMARILY_AUDIO_CONTENT: 13,
  /**
   * Primarily image content
   *
   * - Primarily image content.
   */
  PRIMARILY_IMAGE_CONTENT: 14,
  /**
   * User-generated content
   *
   * - User-generated content (e.g., forums, comments, etc.).
   */
  USER_GENERATED_CONTENT: 15,
  /**
   * Social-centric context
   *
   * Social-centric context (e.g., social network feed, email, chat, etc.).
   */
  SOCIAL_CENTRIC_CONTEXT: 20,
  /**
   * Primarily email content
   *
   * - Primarily email content.
   */
  PRIMARILY_EMAIL_CONTENT: 21,
  /**
   * Primarily chat/IM content
   *
   * - Primarily chat/IM content.
   */
  PRIMARILY_CHAT_IM_CONTENT: 22,
  /**
   * Product context
   *
   * Product context (e.g., product listings, details, recommendations, reviews, etc.).
   */
  PRODUCT_CONTEXT: 30,
  /**
   * App store/marketplace
   *
   * - App store/marketplace.
   */
  APP_STORE_MARKETPLACE: 31,
  /**
   * Product reviews site primarily
   *
   * - Product reviews site primarily, which may sell product secondarily.
   */
  PRODUCT_REVIEWS_SITE_PRIMARILY: 32,
} as const satisfies Readonly<Record<string, DisplayContextType>>;

/**
 * Vendor-specific: a VendorCode the list admits beside its own codes. Vendor-specific codes.
 *
 * It is a brand, so a bare `number` is not one of these: a union of literals widened by `number`
 * collapses to `number` and the listed codes stop constraining anything. Build one with
 * `displayContextTypeExtension`.
 */
export type DisplayContextTypeExtension = VendorCode & { readonly [EXTENSION]: "DisplayContextType" };

/**
 * Whether a `number` is one of this vocabulary's extension values. The test is what VendorCode and
 * this branch state in the published schema.
 */
export const isDisplayContextTypeExtension = (value: number): value is DisplayContextTypeExtension => Number.isInteger(value) && value >= 500;

/**
 * Builds a DisplayContextTypeExtension, or throws. The only way to reach this vocabulary's
 * extension values.
 *
 * @throws TypeError where `isDisplayContextTypeExtension` is false
 */
export const displayContextTypeExtension = (value: number): DisplayContextTypeExtension => {
  if (!isDisplayContextTypeExtension(value)) throw new TypeError(`${JSON.stringify(value)} is no DisplayContextType extension value`);
  return value;
};

/**
 * List: Display Placement Types
 *
 * The codes of List: Display Placement Types
 */
export type DisplayPlacementType = 1 | 2 | 3 | 4 | DisplayPlacementTypeExtension;

/**
 * The codes of DisplayPlacementType, each under the name the published schema carries for it.
 */
export const DisplayPlacementTypeCodes = {
  /**
   * In the feed of content
   *
   * In the feed of content (e.g., as an item inside the organic feed, grid, listing, carousel,
   * etc.).
   */
  IN_THE_FEED_OF_CONTENT: 1,
  /**
   * In the atomic unit of the content
   *
   * In the atomic unit of the content (e.g., in the article page or single image page).
   */
  IN_THE_ATOMIC_UNIT_OF_THE_CONTENT: 2,
  /**
   * Outside the core content
   *
   * Outside the core content (e.g., in the ads section on the right rail, as a banner-style
   * placement near the content, etc.).
   */
  OUTSIDE_THE_CORE_CONTENT: 3,
  /**
   * Recommendation widget
   *
   * Recommendation widget; most commonly presented below article content.
   */
  RECOMMENDATION_WIDGET: 4,
} as const satisfies Readonly<Record<string, DisplayPlacementType>>;

/**
 * Vendor-specific: a VendorCode the list admits beside its own codes. Vendor-specific codes.
 *
 * It is a brand, so a bare `number` is not one of these: a union of literals widened by `number`
 * collapses to `number` and the listed codes stop constraining anything. Build one with
 * `displayPlacementTypeExtension`.
 */
export type DisplayPlacementTypeExtension = VendorCode & { readonly [EXTENSION]: "DisplayPlacementType" };

/**
 * Whether a `number` is one of this vocabulary's extension values. The test is what VendorCode and
 * this branch state in the published schema.
 */
export const isDisplayPlacementTypeExtension = (value: number): value is DisplayPlacementTypeExtension => Number.isInteger(value) && value >= 500;

/**
 * Builds a DisplayPlacementTypeExtension, or throws. The only way to reach this vocabulary's
 * extension values.
 *
 * @throws TypeError where `isDisplayPlacementTypeExtension` is false
 */
export const displayPlacementTypeExtension = (value: number): DisplayPlacementTypeExtension => {
  if (!isDisplayPlacementTypeExtension(value)) throw new TypeError(`${JSON.stringify(value)} is no DisplayPlacementType extension value`);
  return value;
};

/**
 * List: DOOH Multiplier Measurement Source Types
 *
 * The codes of List: DOOH Multiplier Measurement Source Types
 */
export type DoohMultiplierMeasurementSourceType = 0 | 1 | 2 | 3;

/**
 * The codes of DoohMultiplierMeasurementSourceType, each under the name the published schema
 * carries for it.
 */
export const DoohMultiplierMeasurementSourceTypeCodes = {
  /**
   * Unknown
   */
  UNKNOWN: 0,
  /**
   * Measurement Vendor Provided
   */
  MEASUREMENT_VENDOR_PROVIDED: 1,
  /**
   * Publisher Provided
   */
  PUBLISHER_PROVIDED: 2,
  /**
   * Exchange Provided
   */
  EXCHANGE_PROVIDED: 3,
} as const satisfies Readonly<Record<string, DoohMultiplierMeasurementSourceType>>;

/**
 * List: DOOH Venue Taxonomies
 *
 * The codes of List: DOOH Venue Taxonomies
 */
export type DoohVenueTaxonomy = 0 | 1 | 2 | 3 | 4 | 5;

/**
 * The codes of DoohVenueTaxonomy, each under the name the published schema carries for it.
 */
export const DoohVenueTaxonomyCodes = {
  /**
   * AdCom DOOH Venue Types (deprecated)
   */
  ADCOM_DOOH_VENUE_TYPES_DEPRECATED: 0,
  /**
   * OpenOOH Venue Taxonomy 1.0
   *
   * OpenOOH Venue Taxonomy 1.0
   * https://github.com/openooh/venue-taxonomy/blob/main/specification-1.0.md
   */
  OPENOOH_VENUE_TAXONOMY_1_0: 1,
  /**
   * DPAA Device Venue Types
   *
   * DPAA Device Venue Types
   * https://github.com/InteractiveAdvertisingBureau/AdCOM/blob/master/AdCOM%20v1.0%20FINAL.md#list--dooh-venue-types-
   */
  DPAA_DEVICE_VENUE_TYPES: 2,
  /**
   * DMI Categorization of Venues 1.1
   *
   * DMI Categorization of Venues 1.1
   * https://www.dmi-org.com/download/DMI_Standards_for_DOOH_Venues.pdf
   */
  DMI_CATEGORIZATION_OF_VENUES_1_1: 3,
  /**
   * OMA taxonomy Jan 2022
   *
   * OMA taxonomy Jan 2022 https://www.oma.org.au/industry-standards
   */
  OMA_TAXONOMY_JAN_2022: 4,
  /**
   * OpenOOH Venue Taxonomy 1.1
   *
   * OpenOOH Venue Taxonomy 1.1
   * https://github.com/openooh/venue-taxonomy/blob/main/specification-1.1.md
   */
  OPENOOH_VENUE_TAXONOMY_1_1: 5,
} as const satisfies Readonly<Record<string, DoohVenueTaxonomy>>;

/**
 * List: Event Tracking Methods
 *
 * The codes of List: Event Tracking Methods
 */
export type EventTrackingMethod = 1 | 2 | EventTrackingMethodExtension;

/**
 * The codes of EventTrackingMethod, each under the name the published schema carries for it.
 */
export const EventTrackingMethodCodes = {
  /**
   * Image-Pixel
   *
   * Image-Pixel: URL provided will be inserted as a 1x1 pixel at the time of the event.
   */
  IMAGE_PIXEL: 1,
  /**
   * JavaScript
   *
   * JavaScript: URL provided will be inserted as a JavaScript tag at the time of the event.
   */
  JAVASCRIPT: 2,
} as const satisfies Readonly<Record<string, EventTrackingMethod>>;

/**
 * Vendor-specific: a VendorCode the list admits beside its own codes. Vendor-specific codes.
 *
 * It is a brand, so a bare `number` is not one of these: a union of literals widened by `number`
 * collapses to `number` and the listed codes stop constraining anything. Build one with
 * `eventTrackingMethodExtension`.
 */
export type EventTrackingMethodExtension = VendorCode & { readonly [EXTENSION]: "EventTrackingMethod" };

/**
 * Whether a `number` is one of this vocabulary's extension values. The test is what VendorCode and
 * this branch state in the published schema.
 */
export const isEventTrackingMethodExtension = (value: number): value is EventTrackingMethodExtension => Number.isInteger(value) && value >= 500;

/**
 * Builds a EventTrackingMethodExtension, or throws. The only way to reach this vocabulary's
 * extension values.
 *
 * @throws TypeError where `isEventTrackingMethodExtension` is false
 */
export const eventTrackingMethodExtension = (value: number): EventTrackingMethodExtension => {
  if (!isEventTrackingMethodExtension(value)) throw new TypeError(`${JSON.stringify(value)} is no EventTrackingMethod extension value`);
  return value;
};

/**
 * List: Event Types
 *
 * The codes of List: Event Types
 */
export type EventType = 1 | 2 | 3 | 4 | 5 | EventTypeExtension;

/**
 * The codes of EventType, each under the name the published schema carries for it.
 */
export const EventTypeCodes = {
  /**
   * loaded
   *
   * loaded: Delivered as a part of the creative markup. Creative may be pre-cached or pre-loaded;
   * prior to initial rendering.
   */
  LOADED: 1,
  /**
   * impression
   *
   * impression: Ad impression per IAB/MRC Ad Impression Measurement Guidelines.
   */
  IMPRESSION: 2,
  /**
   * viewable-mrc50
   *
   * viewable-mrc50: Visible impression using MRC definition of 50% in view for 1 second.
   */
  VIEWABLE_MRC50: 3,
  /**
   * viewable-mrc100
   *
   * viewable-mrc100: 100% in view for 1 second (i.e., the GroupM standard).
   */
  VIEWABLE_MRC100: 4,
  /**
   * viewable-video50
   *
   * viewable-video50: Visible impression for video using MRC definition of 50% in view for 2
   * seconds.
   */
  VIEWABLE_VIDEO50: 5,
} as const satisfies Readonly<Record<string, EventType>>;

/**
 * Vendor-specific: a VendorCode the list admits beside its own codes. Vendor-specific codes.
 *
 * It is a brand, so a bare `number` is not one of these: a union of literals widened by `number`
 * collapses to `number` and the listed codes stop constraining anything. Build one with
 * `eventTypeExtension`.
 */
export type EventTypeExtension = VendorCode & { readonly [EXTENSION]: "EventType" };

/**
 * Whether a `number` is one of this vocabulary's extension values. The test is what VendorCode and
 * this branch state in the published schema.
 */
export const isEventTypeExtension = (value: number): value is EventTypeExtension => Number.isInteger(value) && value >= 500;

/**
 * Builds a EventTypeExtension, or throws. The only way to reach this vocabulary's extension values.
 *
 * @throws TypeError where `isEventTypeExtension` is false
 */
export const eventTypeExtension = (value: number): EventTypeExtension => {
  if (!isEventTypeExtension(value)) throw new TypeError(`${JSON.stringify(value)} is no EventType extension value`);
  return value;
};

/**
 * List: Expandable Directions
 *
 * The codes of List: Expandable Directions
 */
export type ExpandableDirection = 1 | 2 | 3 | 4 | 5 | 6;

/**
 * The codes of ExpandableDirection, each under the name the published schema carries for it.
 */
export const ExpandableDirectionCodes = {
  /**
   * Left
   */
  LEFT: 1,
  /**
   * Right
   */
  RIGHT: 2,
  /**
   * Up
   */
  UP: 3,
  /**
   * Down
   */
  DOWN: 4,
  /**
   * Full Screen
   */
  FULL_SCREEN: 5,
  /**
   * Resize/Minimize (make smaller)
   */
  RESIZE_MINIMIZE_MAKE_SMALLER: 6,
} as const satisfies Readonly<Record<string, ExpandableDirection>>;

/**
 * List: Feed Types
 *
 * The codes of List: Feed Types
 */
export type FeedType = 1 | 2 | 3 | 4 | 5 | 6 | 7 | FeedTypeExtension;

/**
 * The codes of FeedType, each under the name the published schema carries for it.
 */
export const FeedTypeCodes = {
  /**
   * Music streaming service
   *
   * AOD: Music streaming service
   */
  MUSIC_STREAMING_SERVICE: 1,
  /**
   * FM/AM broadcast
   *
   * LIVE: FM/AM broadcast (live content broadcast over the air but also available via online
   * streaming)
   */
  FM_AM_BROADCAST: 2,
  /**
   * Podcast
   *
   * AOD: Podcast (original, pre-recorded content distributed as episodes in a series)
   */
  PODCAST: 3,
  /**
   * Catch-up radio
   *
   * AOD: Catch-up radio (recorded segment of a radio show that was originally broadcast live)
   */
  CATCH_UP_RADIO: 4,
  /**
   * Web radio
   *
   * LIVE: Web radio (live content only available via online streaming, not as AM/FM broadcast)
   */
  WEB_RADIO: 5,
  /**
   * Video game (background audio in video games)
   *
   * MISC: Video game (background audio in video games)
   */
  VIDEO_GAME_BACKGROUND_AUDIO: 6,
  /**
   * Text to speech
   *
   * MISC: Text to speech (audio books, website plugin that can read article)
   */
  TEXT_TO_SPEECH: 7,
} as const satisfies Readonly<Record<string, FeedType>>;

/**
 * Vendor-specific: a VendorCode the list admits beside its own codes. MISC: Vendor-specific codes.
 *
 * It is a brand, so a bare `number` is not one of these: a union of literals widened by `number`
 * collapses to `number` and the listed codes stop constraining anything. Build one with
 * `feedTypeExtension`.
 */
export type FeedTypeExtension = VendorCode & { readonly [EXTENSION]: "FeedType" };

/**
 * Whether a `number` is one of this vocabulary's extension values. The test is what VendorCode and
 * this branch state in the published schema.
 */
export const isFeedTypeExtension = (value: number): value is FeedTypeExtension => Number.isInteger(value) && value >= 500;

/**
 * Builds a FeedTypeExtension, or throws. The only way to reach this vocabulary's extension values.
 *
 * @throws TypeError where `isFeedTypeExtension` is false
 */
export const feedTypeExtension = (value: number): FeedTypeExtension => {
  if (!isFeedTypeExtension(value)) throw new TypeError(`${JSON.stringify(value)} is no FeedType extension value`);
  return value;
};

/**
 * List: ID Match Methods
 *
 * The codes of List: ID Match Methods
 */
export type IdMatchMethod = 0 | 1 | 2 | 3 | 4 | 5 | IdMatchMethodExtension;

/**
 * The codes of IdMatchMethod, each under the name the published schema carries for it.
 */
export const IdMatchMethodCodes = {
  /**
   * Unknown
   */
  UNKNOWN: 0,
  /**
   * No Match
   *
   * No Match: No matching has occurred. The associated ID came directly from a 3rd-party cookie or
   * OS-provided resettable device ID for advertising (IFA).
   */
  NO_MATCH: 1,
  /**
   * Browser Cookie Sync
   *
   * Browser Cookie Sync: Real time cookie sync as described in Appendix: Cookie Based ID Syncing of
   * OpenRTB 2.x
   */
  BROWSER_COOKIE_SYNC: 2,
  /**
   * Authenticated
   *
   * Authenticated: ID match was based on user authentication such as an email login or hashed PII
   */
  AUTHENTICATED: 3,
  /**
   * Observed
   *
   * Observed: ID match was based on a 1st party observation, but without user authentication (e.g.
   * GUID, SharedID, Session IDs, CHIPS or other 1st party cookies contained in localStorage)
   */
  OBSERVED: 4,
  /**
   * Inference
   *
   * Inference: ID match was inferred from linkage based on non-authenticated features across
   * multiple browsers or devices (e.g. IP address and/or UserAgent)
   */
  INFERENCE: 5,
} as const satisfies Readonly<Record<string, IdMatchMethod>>;

/**
 * Vendor-specific: a VendorCode the list admits beside its own codes. Vendor Specific
 *
 * It is a brand, so a bare `number` is not one of these: a union of literals widened by `number`
 * collapses to `number` and the listed codes stop constraining anything. Build one with
 * `idMatchMethodExtension`.
 */
export type IdMatchMethodExtension = VendorCode & { readonly [EXTENSION]: "IdMatchMethod" };

/**
 * Whether a `number` is one of this vocabulary's extension values. The test is what VendorCode and
 * this branch state in the published schema.
 */
export const isIdMatchMethodExtension = (value: number): value is IdMatchMethodExtension => Number.isInteger(value) && value >= 500;

/**
 * Builds a IdMatchMethodExtension, or throws. The only way to reach this vocabulary's extension
 * values.
 *
 * @throws TypeError where `isIdMatchMethodExtension` is false
 */
export const idMatchMethodExtension = (value: number): IdMatchMethodExtension => {
  if (!isIdMatchMethodExtension(value)) throw new TypeError(`${JSON.stringify(value)} is no IdMatchMethod extension value`);
  return value;
};

/**
 * List: IP Location Services
 *
 * The codes of List: IP Location Services
 */
export type IpLocationService = 1 | 2 | 3 | 4 | 511 | 512;

/**
 * The codes of IpLocationService, each under the name the published schema carries for it.
 */
export const IpLocationServiceCodes = {
  /**
   * ip2location
   */
  IP2LOCATION: 1,
  /**
   * Neustar (Quova)
   */
  NEUSTAR_QUOVA: 2,
  /**
   * MaxMind
   */
  MAXMIND: 3,
  /**
   * NetAcuity (Digital Element)
   */
  NETACUITY_DIGITAL_ELEMENT: 4,
  /**
   * 51Degrees (High Confidence)
   */
  CODE_51DEGREES_HIGH_CONFIDENCE: 511,
  /**
   * 51Degrees (Medium Confidence)
   */
  CODE_51DEGREES_MEDIUM_CONFIDENCE: 512,
} as const satisfies Readonly<Record<string, IpLocationService>>;

/**
 * List: Linearity Modes
 *
 * The codes of List: Linearity Modes
 */
export type LinearityMode = 1 | 2;

/**
 * The codes of LinearityMode, each under the name the published schema carries for it.
 */
export const LinearityModeCodes = {
  /**
   * Linear
   */
  LINEAR: 1,
  /**
   * Non-Linear
   *
   * Non-Linear (i.e., Overlay)
   */
  NON_LINEAR: 2,
} as const satisfies Readonly<Record<string, LinearityMode>>;

/**
 * List: Location Types
 *
 * The codes of List: Location Types
 */
export type LocationType = 1 | 2 | 3;

/**
 * The codes of LocationType, each under the name the published schema carries for it.
 */
export const LocationTypeCodes = {
  /**
   * GPS/Location Services
   */
  GPS_LOCATION_SERVICES: 1,
  /**
   * IP Address
   */
  IP_ADDRESS: 2,
  /**
   * User Provided
   *
   * User Provided (e.g., registration data)
   */
  USER_PROVIDED: 3,
} as const satisfies Readonly<Record<string, LocationType>>;

/**
 * List: Media Ratings
 *
 * The codes of List: Media Ratings
 */
export type MediaRating = 1 | 2 | 3;

/**
 * The codes of MediaRating, each under the name the published schema carries for it.
 */
export const MediaRatingCodes = {
  /**
   * All Audiences
   */
  ALL_AUDIENCES: 1,
  /**
   * Everyone Over Age 12
   */
  EVERYONE_OVER_AGE_12: 2,
  /**
   * Mature Audiences
   */
  MATURE_AUDIENCES: 3,
} as const satisfies Readonly<Record<string, MediaRating>>;

/**
 * List: Native Data Asset Types
 *
 * The codes of List: Native Data Asset Types
 */
export type NativeDataAssetType = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | NativeDataAssetTypeExtension;

/**
 * The codes of NativeDataAssetType, each under the name the published schema carries for it.
 */
export const NativeDataAssetTypeCodes = {
  /**
   * sponsored
   *
   * sponsored: "Sponsored By" message which should contain the brand name of the sponsor.
   * Recommended maximum length of at least 25 characters.
   */
  SPONSORED: 1,
  /**
   * desc
   *
   * desc: Descriptive text associated with the product or service being advertised. Long text
   * lengths may be truncated or ellipsed when rendered. Recommended maximum length of at least 140
   * characters.
   */
  DESC: 2,
  /**
   * rating
   *
   * rating: Numeric rating of the product (e.g., an app's rating). Recommended integer range of
   * 0-5.
   */
  RATING: 3,
  /**
   * likes
   *
   * likes: Number of social ratings or "likes" of the product.
   */
  LIKES: 4,
  /**
   * downloads
   *
   * downloads: Number downloads and/or installs of the product.
   */
  DOWNLOADS: 5,
  /**
   * price
   *
   * price: Price of the product, app, or in-app purchase. Value should include currency symbol in
   * localized format (e.g., "$10").
   */
  PRICE: 6,
  /**
   * saleprice
   *
   * saleprice: Sale price that can be used together with "price" to indicate a comparative
   * discounted price. Value should include currency symbol in localized format (e.g., "$8.50").
   */
  SALEPRICE: 7,
  /**
   * phone
   *
   * phone: A formatted phone number.
   */
  PHONE: 8,
  /**
   * address
   *
   * address: A formatted address.
   */
  ADDRESS: 9,
  /**
   * desc2
   *
   * desc2: Additional descriptive text associated with the product.
   */
  DESC2: 10,
  /**
   * displayurl
   *
   * displayurl: Display URL for the ad. To be used when sponsoring entity doesn't own the content
   * (e.g., "Sponsored by Brand on Site", where Site is specified in this data asset).
   */
  DISPLAYURL: 11,
  /**
   * ctatext
   *
   * ctatext: Description of the call to action (CTA) button for the destination URL. Recommended
   * maximum length of at least 15 characters.
   */
  CTATEXT: 12,
} as const satisfies Readonly<Record<string, NativeDataAssetType>>;

/**
 * Vendor-specific: a VendorCode the list admits beside its own codes. Vendor-specific codes.
 *
 * It is a brand, so a bare `number` is not one of these: a union of literals widened by `number`
 * collapses to `number` and the listed codes stop constraining anything. Build one with
 * `nativeDataAssetTypeExtension`.
 */
export type NativeDataAssetTypeExtension = VendorCode & { readonly [EXTENSION]: "NativeDataAssetType" };

/**
 * Whether a `number` is one of this vocabulary's extension values. The test is what VendorCode and
 * this branch state in the published schema.
 */
export const isNativeDataAssetTypeExtension = (value: number): value is NativeDataAssetTypeExtension => Number.isInteger(value) && value >= 500;

/**
 * Builds a NativeDataAssetTypeExtension, or throws. The only way to reach this vocabulary's
 * extension values.
 *
 * @throws TypeError where `isNativeDataAssetTypeExtension` is false
 */
export const nativeDataAssetTypeExtension = (value: number): NativeDataAssetTypeExtension => {
  if (!isNativeDataAssetTypeExtension(value)) throw new TypeError(`${JSON.stringify(value)} is no NativeDataAssetType extension value`);
  return value;
};

/**
 * List: Native Image Asset Types
 *
 * The codes of List: Native Image Asset Types
 */
export type NativeImageAssetType = 1 | 3 | NativeImageAssetTypeExtension;

/**
 * The codes of NativeImageAssetType, each under the name the published schema carries for it.
 */
export const NativeImageAssetTypeCodes = {
  /**
   * Icon
   *
   * Icon: Icon image. Maximum height at least 50 device independent pixels (DIPS); aspect ratio
   * 1:1.
   */
  ICON: 1,
  /**
   * Main
   *
   * Main: Large image preview for the ad. At least one of 2 size variants required: Small: Maximum
   * height at least 200 DIPS; maximum width at least 200, 267, or 382 DIPS (i.e., aspect ratios of
   * 1:1, 4:3, or 1.91:1, respectively). Large: Maximum height at least 627 DIPS; maximum width at
   * least 627, 836, or 1198 DIPS (i.e., aspect ratios of 1:1, 4:3, or 1.91:1, respectively).
   */
  MAIN: 3,
} as const satisfies Readonly<Record<string, NativeImageAssetType>>;

/**
 * Vendor-specific: a VendorCode the list admits beside its own codes. Vendor-specific codes.
 *
 * It is a brand, so a bare `number` is not one of these: a union of literals widened by `number`
 * collapses to `number` and the listed codes stop constraining anything. Build one with
 * `nativeImageAssetTypeExtension`.
 */
export type NativeImageAssetTypeExtension = VendorCode & { readonly [EXTENSION]: "NativeImageAssetType" };

/**
 * Whether a `number` is one of this vocabulary's extension values. The test is what VendorCode and
 * this branch state in the published schema.
 */
export const isNativeImageAssetTypeExtension = (value: number): value is NativeImageAssetTypeExtension => Number.isInteger(value) && value >= 500;

/**
 * Builds a NativeImageAssetTypeExtension, or throws. The only way to reach this vocabulary's
 * extension values.
 *
 * @throws TypeError where `isNativeImageAssetTypeExtension` is false
 */
export const nativeImageAssetTypeExtension = (value: number): NativeImageAssetTypeExtension => {
  if (!isNativeImageAssetTypeExtension(value)) throw new TypeError(`${JSON.stringify(value)} is no NativeImageAssetType extension value`);
  return value;
};

/**
 * List: Operating Systems
 *
 * The codes of List: Operating Systems
 */
export type OperatingSystem = 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | OperatingSystemExtension;

/**
 * The codes of OperatingSystem, each under the name the published schema carries for it.
 */
export const OperatingSystemCodes = {
  /**
   * Other Not Listed
   */
  OTHER_NOT_LISTED: 0,
  /**
   * 3DS System Software
   */
  CODE_3DS_SYSTEM_SOFTWARE: 1,
  /**
   * Android
   */
  ANDROID: 2,
  /**
   * Apple TV Software
   */
  APPLE_TV_SOFTWARE: 3,
  /**
   * Asha
   */
  ASHA: 4,
  /**
   * Bada
   */
  BADA: 5,
  /**
   * BlackBerry
   */
  BLACKBERRY: 6,
  /**
   * BREW
   */
  BREW: 7,
  /**
   * ChromeOS
   */
  CHROMEOS: 8,
  /**
   * Darwin
   */
  DARWIN: 9,
  /**
   * FireOS
   */
  FIREOS: 10,
  /**
   * FirefoxOS
   */
  FIREFOXOS: 11,
  /**
   * HelenOS
   */
  HELENOS: 12,
  /**
   * iOS
   */
  IOS: 13,
  /**
   * Linux
   */
  LINUX: 14,
  /**
   * MacOS
   */
  MACOS: 15,
  /**
   * MeeGo
   */
  MEEGO: 16,
  /**
   * MorphOS
   */
  MORPHOS: 17,
  /**
   * NetBSD
   */
  NETBSD: 18,
  /**
   * NucleusPLUS
   */
  NUCLEUSPLUS: 19,
  /**
   * PS Vita System Software
   */
  PS_VITA_SYSTEM_SOFTWARE: 20,
  /**
   * PS3 System Software
   */
  PS3_SYSTEM_SOFTWARE: 21,
  /**
   * PS4 Software
   */
  PS4_SOFTWARE: 22,
  /**
   * PSP System Software
   */
  PSP_SYSTEM_SOFTWARE: 23,
  /**
   * Symbian
   */
  SYMBIAN: 24,
  /**
   * Tizen
   */
  TIZEN: 25,
  /**
   * WatchOS
   */
  WATCHOS: 26,
  /**
   * WebOS
   */
  WEBOS: 27,
  /**
   * Windows
   */
  WINDOWS: 28,
} as const satisfies Readonly<Record<string, OperatingSystem>>;

/**
 * Vendor-specific: a VendorCode the list admits beside its own codes. Vendor-specific codes.
 *
 * It is a brand, so a bare `number` is not one of these: a union of literals widened by `number`
 * collapses to `number` and the listed codes stop constraining anything. Build one with
 * `operatingSystemExtension`.
 */
export type OperatingSystemExtension = VendorCode & { readonly [EXTENSION]: "OperatingSystem" };

/**
 * Whether a `number` is one of this vocabulary's extension values. The test is what VendorCode and
 * this branch state in the published schema.
 */
export const isOperatingSystemExtension = (value: number): value is OperatingSystemExtension => Number.isInteger(value) && value >= 500;

/**
 * Builds a OperatingSystemExtension, or throws. The only way to reach this vocabulary's extension
 * values.
 *
 * @throws TypeError where `isOperatingSystemExtension` is false
 */
export const operatingSystemExtension = (value: number): OperatingSystemExtension => {
  if (!isOperatingSystemExtension(value)) throw new TypeError(`${JSON.stringify(value)} is no OperatingSystem extension value`);
  return value;
};

/**
 * List: Placement Positions
 *
 * The codes of List: Placement Positions
 */
export type PlacementPosition = 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17;

/**
 * The codes of PlacementPosition, each under the name the published schema carries for it.
 */
export const PlacementPositionCodes = {
  /**
   * Unknown
   */
  UNKNOWN: 0,
  /**
   * Above The Fold
   */
  ABOVE_THE_FOLD: 1,
  /**
   * Locked
   *
   * Locked (i.e., fixed position)
   */
  LOCKED: 2,
  /**
   * Below The Fold
   */
  BELOW_THE_FOLD: 3,
  /**
   * Header
   */
  HEADER: 4,
  /**
   * Footer
   */
  FOOTER: 5,
  /**
   * Sidebar
   */
  SIDEBAR: 6,
  /**
   * Fullscreen
   */
  FULLSCREEN: 7,
  /**
   * Partial Screen
   */
  PARTIAL_SCREEN: 8,
  /**
   * Top Left
   */
  TOP_LEFT: 9,
  /**
   * Top Right
   */
  TOP_RIGHT: 10,
  /**
   * Frame the content
   */
  FRAME_THE_CONTENT: 11,
  /**
   * Double box
   */
  DOUBLE_BOX: 12,
  /**
   * Double box with background
   */
  DOUBLE_BOX_WITH_BACKGROUND: 13,
  /**
   * Bottom Left
   */
  BOTTOM_LEFT: 14,
  /**
   * Bottom Right
   */
  BOTTOM_RIGHT: 15,
  /**
   * L shape
   */
  L_SHAPE: 16,
  /**
   * Reversed L shape
   */
  REVERSED_L_SHAPE: 17,
} as const satisfies Readonly<Record<string, PlacementPosition>>;

/**
 * List: Playback Cessation Modes
 *
 * The codes of List: Playback Cessation Modes
 */
export type PlaybackCessationMode = 1 | 2 | 3;

/**
 * The codes of PlaybackCessationMode, each under the name the published schema carries for it.
 */
export const PlaybackCessationModeCodes = {
  /**
   * On Video Completion or when Terminated by User
   */
  ON_VIDEO_COMPLETION: 1,
  /**
   * On Leaving Viewport or when Terminated by User
   */
  ON_LEAVING_VIEWPORT: 2,
  /**
   * On Leaving Viewport Continues as Floating Unit
   *
   * On Leaving Viewport Continues as a Floating/Slider Unit until Video Completion or when
   * Terminated by User
   */
  ON_LEAVING_VIEWPORT_CONTINUES_FLOATING: 3,
} as const satisfies Readonly<Record<string, PlaybackCessationMode>>;

/**
 * List: Playback Methods
 *
 * The codes of List: Playback Methods
 */
export type PlaybackMethod = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11;

/**
 * The codes of PlaybackMethod, each under the name the published schema carries for it.
 */
export const PlaybackMethodCodes = {
  /**
   * Initiates Automatically with Sound On
   *
   * Initiates without any specific user interaction with Sound On
   */
  INITIATES_AUTOMATICALLY_WITH_SOUND_ON: 1,
  /**
   * Initiates Automatically with Sound Off
   *
   * Initiates without any specific user interaction Sound Off by Default
   */
  INITIATES_AUTOMATICALLY_WITH_SOUND_OFF: 2,
  /**
   * Initiates on Click with Sound On
   */
  INITIATES_ON_CLICK_WITH_SOUND_ON: 3,
  /**
   * Initiates on Mouse-Over with Sound On
   *
   * Initiates on Mouse-Over or cursor over with Sound On
   */
  INITIATES_ON_MOUSE_OVER_WITH_SOUND_ON: 4,
  /**
   * Initiates on Entering Viewport with Sound On
   *
   * Initiates on Entering Viewport or scrolling into view with Sound On
   */
  INITIATES_ON_ENTERING_VIEWPORT_SOUND_ON: 5,
  /**
   * Initiates on Entering Viewport with Sound Off
   *
   * Initiates on Entering Viewport or scrolling into view with Sound Off by Default
   */
  INITIATES_ON_ENTERING_VIEWPORT_SOUND_OFF: 6,
  /**
   * Continuous Playback
   *
   * Continuous Playback - Media playback is set to play additional media automatically without user
   * interaction. The media player will keep playing additional media (playlist or generated) for
   * the user until the user actively stops this from happening.
   */
  CONTINUOUS_PLAYBACK: 7,
  /**
   * Initiated by user pausing content, Sound on
   */
  INITIATED_BY_CONTENT_PAUSE_SOUND_ON: 8,
  /**
   * Initiated by user pausing content, Sound off
   */
  INITIATED_BY_CONTENT_PAUSE_SOUND_OFF: 9,
  /**
   * Initiated by idling, Sound on
   *
   * Initiated by idling (e.g. screensaver), Sound on
   */
  INITIATED_BY_IDLING_SOUND_ON: 10,
  /**
   * Initiated by idling, Sound off
   *
   * Initiated by idling (e.g. screensaver), Sound off
   */
  INITIATED_BY_IDLING_SOUND_OFF: 11,
} as const satisfies Readonly<Record<string, PlaybackMethod>>;

/**
 * List: Plcmt Subtypes - Video
 *
 * The codes of List: Plcmt Subtypes - Video
 */
export type PlcmtSubtypeVideo = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9;

/**
 * The codes of PlcmtSubtypeVideo, each under the name the published schema carries for it.
 */
export const PlcmtSubtypeVideoCodes = {
  /**
   * Instream
   *
   * Instream: Pre-roll, mid-roll, and post-roll ads that are played before, during or after the
   * streaming video content that the consumer has requested. Instream video must be set to “sound
   * on” by default at player start, or have explicitly clear user intent to watch the video
   * content. While there may be other content surrounding the player, the video content must be the
   * focus of the user’s visit. It should remain the primary content on the page and the only video
   * player in-view capable of audio when playing. If the player converts to floating/sticky
   * subsequent ad calls should accurately convey the updated player size.
   */
  INSTREAM: 1,
  /**
   * Accompanying Content
   *
   * Accompanying Content: Pre-roll, mid-roll, and post-roll ads that are played before, during, or
   * after streaming video content. The video player loads and plays before, between, or after
   * paragraphs of text or graphical content, and starts playing only when it enters the viewport.
   * Accompanying content should only start playback upon entering the viewport. It may convert to a
   * floating/sticky player as it scrolls off the page.
   */
  ACCOMPANYING_CONTENT: 2,
  /**
   * Interstitial
   *
   * Interstitial:Video ads that are played without video content. During playback, it must be the
   * primary focus of the page and take up the majority of the viewport and cannot be scrolled out
   * of view. This can be in placements like in-app video or slideshows.
   */
  INTERSTITIAL: 3,
  /**
   * No Content/Standalone
   *
   * No Content/Standalone: Video ads that are played without streaming video content. This can be
   * in placements like slideshows, native feeds, in-content or sticky/floating.
   */
  NO_CONTENT_STANDALONE: 4,
  /**
   * Pause
   *
   * Pause: An ad present in streaming video content that the consumer has requested. While there
   * may be other content surrounding the player, the video content must be the focus of the user’s
   * visit. It should remain the primary content on the page and the only video player in-view.
   */
  PAUSE: 5,
  /**
   * Screensaver
   *
   * Screensaver: An ad present, when OS/App Screen Saver are initiated.
   */
  SCREENSAVER: 6,
  /**
   * Overlay
   *
   * Overlay: Ads occurring during program content and outside of the traditional ad break. The ad
   * format places ad creatives over top of the program content, often as a banner or picture in
   * picture execution. While there may be other content surrounding the player with the overlay,
   * the player with the overlay must be the focus of the user’s visit. It should remain the primary
   * content on the page and the primary video player in-view.
   */
  OVERLAY: 7,
  /**
   * Squeezeback
   *
   * Squeezeback: Ads Alongside or Adjacent to Content, also known as L-Shape Ads & Double Box, are
   * ads that occur during program content and outside of the traditional ad break. The program
   * content is resized to allow for placement of an ad on the screen. In a squeezeback, none of the
   * content is covered by the ad, instead it shares screen space with the ad. This is the major
   * distinction between squeezeback and overlay. While there may be other content surrounding the
   * player with the squeezeback, the player with the squeezeback must be the focus of the user’s
   * visit. It should remain the primary content on the page and the primary video player in-view.
   */
  SQUEEZEBACK: 8,
  /**
   * In-scene
   *
   * In-scene: A form of advertising that integrates branded elements directly within the content
   * itself, rather than appearing as separate pre-roll, mid-roll, overlay, or display formats. In
   * Scene Advertising is composited into the video content and blends the brand naturally into the
   * scene, environment, or storyline, ensuring contextual relevance and viewer immersion without
   * interrupting the user experience. In-scene ads typically consist of product placements or
   * virtual out of A insertions. At this time, the standardization focuses on the out of home
   * insertions in non-live content. While there may be other content surrounding the player with
   * the in-scene ad, the player with the in-scene ad must be the focus of the user’s visit. It
   * should remain the primary content on the page and the primary video player in-view.
   */
  IN_SCENE: 9,
} as const satisfies Readonly<Record<string, PlcmtSubtypeVideo>>;

/**
 * List: Pod Deduplication Settings
 *
 * The codes of List: Pod Deduplication Settings
 */
export type PodDeduplicationSetting = 1 | 2 | 3 | 4 | 5;

/**
 * The codes of PodDeduplicationSetting, each under the name the published schema carries for it.
 */
export const PodDeduplicationSettingCodes = {
  /**
   * Deduplicated on adomain
   */
  DEDUPLICATED_ON_ADOMAIN: 1,
  /**
   * Deduplicated on IAB Tech Lab Content Taxonomy
   */
  DEDUPLICATED_ON_CONTENT_TAXONOMY: 2,
  /**
   * Deduplicated on creative ID
   */
  DEDUPLICATED_ON_CREATIVE_ID: 3,
  /**
   * Deduplicated on mediafile URL
   */
  DEDUPLICATED_ON_MEDIAFILE_URL: 4,
  /**
   * No deduplication
   */
  NO_DEDUPLICATION: 5,
} as const satisfies Readonly<Record<string, PodDeduplicationSetting>>;

/**
 * List: Pod Sequence
 *
 * The codes of List: Pod Sequence
 */
export type PodSequence = -1 | 0 | 1;

/**
 * The codes of PodSequence, each under the name the published schema carries for it.
 */
export const PodSequenceCodes = {
  /**
   * Last pod in the content stream
   */
  LAST_POD_IN_THE_CONTENT_STREAM: -1,
  /**
   * Any pod in the content stream
   */
  ANY_POD_IN_THE_CONTENT_STREAM: 0,
  /**
   * First pod in the content stream
   */
  FIRST_POD_IN_THE_CONTENT_STREAM: 1,
} as const satisfies Readonly<Record<string, PodSequence>>;

/**
 * List: Production Qualities
 *
 * The codes of List: Production Qualities
 */
export type ProductionQuality = 0 | 1 | 2 | 3;

/**
 * The codes of ProductionQuality, each under the name the published schema carries for it.
 */
export const ProductionQualityCodes = {
  /**
   * Unknown
   */
  UNKNOWN: 0,
  /**
   * Professionally Produced
   */
  PROFESSIONALLY_PRODUCED: 1,
  /**
   * Prosumer
   */
  PROSUMER: 2,
  /**
   * User Generated (UGC)
   */
  USER_GENERATED_UGC: 3,
} as const satisfies Readonly<Record<string, ProductionQuality>>;

/**
 * List: Size Units
 *
 * The codes of List: Size Units
 */
export type SizeUnit = 1 | 2 | 3;

/**
 * The codes of SizeUnit, each under the name the published schema carries for it.
 */
export const SizeUnitCodes = {
  /**
   * Device Independent Pixels (DIPS)
   */
  DEVICE_INDEPENDENT_PIXELS_DIPS: 1,
  /**
   * Inches
   */
  INCHES: 2,
  /**
   * Centimeters
   */
  CENTIMETERS: 3,
} as const satisfies Readonly<Record<string, SizeUnit>>;

/**
 * List: Slot Position in Pod
 *
 * The codes of List: Slot Position in Pod
 */
export type SlotPositionInPod = -1 | 0 | 1 | 2;

/**
 * The codes of SlotPositionInPod, each under the name the published schema carries for it.
 */
export const SlotPositionInPodCodes = {
  /**
   * Last ad in the pod
   */
  LAST_AD_IN_THE_POD: -1,
  /**
   * Any ad in the pod
   */
  ANY_AD_IN_THE_POD: 0,
  /**
   * First ad in the pod
   */
  FIRST_AD_IN_THE_POD: 1,
  /**
   * First or Last ad in the pod
   */
  FIRST_OR_LAST_AD_IN_THE_POD: 2,
} as const satisfies Readonly<Record<string, SlotPositionInPod>>;

/**
 * List: Start Delay Modes
 *
 * The codes of List: Start Delay Modes, or, for a mid-roll at a given second, the delay in seconds,
 * which the row `>0` stands for
 */
export type StartDelayMode = -2 | -1 | 0 | StartDelayModeExtension;

/**
 * The codes of StartDelayMode, each under the name the published schema carries for it.
 */
export const StartDelayModeCodes = {
  /**
   * Generic Post-Roll
   */
  GENERIC_POST_ROLL: -2,
  /**
   * Generic Mid-Roll
   */
  GENERIC_MID_ROLL: -1,
  /**
   * Pre-Roll
   */
  PRE_ROLL: 0,
} as const satisfies Readonly<Record<string, StartDelayMode>>;

/**
 * Media offset: a MediaOffset the list admits beside its own codes.
 *
 * It is a brand, so a bare `number` is not one of these: a union of literals widened by `number`
 * collapses to `number` and the listed codes stop constraining anything. Build one with
 * `startDelayModeExtension`.
 */
export type StartDelayModeExtension = MediaOffset & { readonly [EXTENSION]: "StartDelayMode" };

/**
 * Whether a `number` is one of this vocabulary's extension values. The test is what MediaOffset and
 * this branch state in the published schema, the code 0 excepted, which has a branch of its own.
 */
export const isStartDelayModeExtension = (value: number): value is StartDelayModeExtension => Number.isInteger(value) && value >= 0 && value <= 9007199254740991 && value !== 0;

/**
 * Builds a StartDelayModeExtension, or throws. The only way to reach this vocabulary's extension
 * values.
 *
 * @throws TypeError where `isStartDelayModeExtension` is false
 */
export const startDelayModeExtension = (value: number): StartDelayModeExtension => {
  if (!isStartDelayModeExtension(value)) throw new TypeError(`${JSON.stringify(value)} is no StartDelayMode extension value`);
  return value;
};

/**
 * List: User-Agent Source
 *
 * The codes of List: User-Agent Source
 */
export type UserAgentSource = 0 | 1 | 2 | 3;

/**
 * The codes of UserAgentSource, each under the name the published schema carries for it.
 */
export const UserAgentSourceCodes = {
  /**
   * Unspecified/unknown
   */
  UNSPECIFIED_UNKNOWN: 0,
  /**
   * Low-Entropy Client Hints
   *
   * User-Agent Client Hints (only low-entropy headers were available)
   */
  LOW_ENTROPY_CLIENT_HINTS: 1,
  /**
   * High-Entropy Client Hints
   *
   * User-Agent Client Hints (with high-entropy headers available)
   */
  HIGH_ENTROPY_CLIENT_HINTS: 2,
  /**
   * Parsed from User-Agent header
   *
   * Parsed from User-Agent header (the same string carried by the ua field)
   */
  PARSED_FROM_USER_AGENT_HEADER: 3,
} as const satisfies Readonly<Record<string, UserAgentSource>>;

/**
 * List: Volume Normalization Modes
 *
 * The codes of List: Volume Normalization Modes
 */
export type VolumeNormalizationMode = 0 | 1 | 2 | 3 | 4;

/**
 * The codes of VolumeNormalizationMode, each under the name the published schema carries for it.
 */
export const VolumeNormalizationModeCodes = {
  /**
   * None
   */
  NONE: 0,
  /**
   * Ad Volume Average Normalized to Content
   */
  AD_VOLUME_AVERAGE_NORMALIZED_TO_CONTENT: 1,
  /**
   * Ad Volume Peak Normalized to Content
   */
  AD_VOLUME_PEAK_NORMALIZED_TO_CONTENT: 2,
  /**
   * Ad Loudness Normalized to Content
   */
  AD_LOUDNESS_NORMALIZED_TO_CONTENT: 3,
  /**
   * Custom Volume Normalization
   */
  CUSTOM_VOLUME_NORMALIZATION: 4,
} as const satisfies Readonly<Record<string, VolumeNormalizationMode>>;
