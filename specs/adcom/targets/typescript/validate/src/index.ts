/**
 * The validation layer of this published schema tree, in two passes.
 *
 * **The schema pass** is `check`: one compiled validator per named type, run over the bytes this
 * package carries. It is the floor, and it is what verdict parity is measured on — whatever the
 * types do or do not carry, this pass accepts and rejects what the published schema accepts and
 * rejects.
 *
 * **The model pass** is `decode`: the same verdict, and on acceptance the payload typed as the name
 * the caller asked for. It is a choice the application makes, because a caller who has already
 * validated at its edge pays nothing for it.
 *
 * A type here is a projection of already-validated bytes, which is why `decode` asserts and does
 * not convert: nothing in this layer rewrites a payload, so what a caller holds is the bytes that
 * were graded.
 */

import type * as types from "@jsonspecshq/adcom-types";
import { engine, type Engine, type Issue, type Verdict } from "./engine.js";
import { DOCUMENTS, TYPES, type TypeName } from "./schemas.js";

export type { Engine, Issue, Verdict } from "./engine.js";
export { TYPES, type TypeName } from "./schemas.js";

/**
 * The lock this package was generated from, so a consumer can say which version of the
 * specification a verdict is of. A target emits one artifact per lock (target rules § 12).
 */
export const LOCK = "main";

/**
 * The static type each name stands for.
 *
 * It is written out rather than derived, because TypeScript cannot index a module's exported types
 * by a string. The names are the schema's `$defs` keys and this map is the one place the two
 * packages meet.
 */
export interface TypeMap {
  readonly Ad: types.Ad;
  readonly AgentType: types.AgentType;
  readonly AmpRenderingTreatment: types.AmpRenderingTreatment;
  readonly ApiFramework: types.ApiFramework;
  readonly App: types.App;
  readonly Asset: types.Asset;
  readonly AssetFormat: types.AssetFormat;
  readonly Audio: types.Audio;
  readonly AudioPlacement: types.AudioPlacement;
  readonly Audit: types.Audit;
  readonly AuditStatusCode: types.AuditStatusCode;
  readonly AutoRefreshTrigger: types.AutoRefreshTrigger;
  readonly Banner: types.Banner;
  readonly BrandVersion: types.BrandVersion;
  readonly CategoryTaxonomy: types.CategoryTaxonomy;
  readonly Channel: types.Channel;
  readonly ClickType: types.ClickType;
  readonly Companion: types.Companion;
  readonly CompanionType: types.CompanionType;
  readonly ConnectionType: types.ConnectionType;
  readonly Content: types.Content;
  readonly ContentContext: types.ContentContext;
  readonly Corr: types.Corr;
  readonly Count: types.Count;
  readonly CreativeAttribute: types.CreativeAttribute;
  readonly CreativeSubtypeAudioVideo: types.CreativeSubtypeAudioVideo;
  readonly CreativeSubtypeDisplay: types.CreativeSubtypeDisplay;
  readonly Data: types.Data;
  readonly DataAsset: types.DataAsset;
  readonly DataAssetFormat: types.DataAssetFormat;
  readonly Degrees: types.Degrees;
  readonly DeliveryMethod: types.DeliveryMethod;
  readonly Device: types.Device;
  readonly DeviceType: types.DeviceType;
  readonly Display: types.Display;
  readonly DisplayContextType: types.DisplayContextType;
  readonly DisplayFormat: types.DisplayFormat;
  readonly DisplayPlacement: types.DisplayPlacement;
  readonly DisplayPlacementType: types.DisplayPlacementType;
  readonly Domain: types.Domain;
  readonly Dooh: types.Dooh;
  readonly DoohMultiplierMeasurementSourceType: types.DoohMultiplierMeasurementSourceType;
  readonly DoohPlacementMobility: types.DoohPlacementMobility;
  readonly DoohVenueTaxonomy: types.DoohVenueTaxonomy;
  readonly DurationSeconds: types.DurationSeconds;
  readonly EpochMilliseconds: types.EpochMilliseconds;
  readonly Event: types.Event;
  readonly EventSpec: types.EventSpec;
  readonly EventTrackingMethod: types.EventTrackingMethod;
  readonly EventType: types.EventType;
  readonly ExpandableDirection: types.ExpandableDirection;
  readonly Ext: types.Ext;
  readonly ExtendedDuration: types.ExtendedDuration;
  readonly ExtendedIdentifierUids: types.ExtendedIdentifierUids;
  readonly ExtendedIdentifiers: types.ExtendedIdentifiers;
  readonly ExternalId: types.ExternalId;
  readonly FeedType: types.FeedType;
  readonly Geo: types.Geo;
  readonly IdMatchMethod: types.IdMatchMethod;
  readonly ImageAsset: types.ImageAsset;
  readonly ImageAssetFormat: types.ImageAssetFormat;
  readonly IntegerFlag: types.IntegerFlag;
  readonly IntegerId: types.IntegerId;
  readonly IpLocationService: types.IpLocationService;
  readonly LinearityMode: types.LinearityMode;
  readonly LinkAsset: types.LinkAsset;
  readonly LocationType: types.LocationType;
  readonly Measure: types.Measure;
  readonly MediaOffset: types.MediaOffset;
  readonly MediaRating: types.MediaRating;
  readonly MinuteOffset: types.MinuteOffset;
  readonly Native: types.Native;
  readonly NativeDataAssetType: types.NativeDataAssetType;
  readonly NativeFormat: types.NativeFormat;
  readonly NativeImageAssetType: types.NativeImageAssetType;
  readonly Network: types.Network;
  readonly OperatingSystem: types.OperatingSystem;
  readonly Placement: types.Placement;
  readonly PlacementPosition: types.PlacementPosition;
  readonly PlaybackCessationMode: types.PlaybackCessationMode;
  readonly PlaybackMethod: types.PlaybackMethod;
  readonly PlcmtSubtypeVideo: types.PlcmtSubtypeVideo;
  readonly PodDeduplicationSetting: types.PodDeduplicationSetting;
  readonly PodSequence: types.PodSequence;
  readonly Producer: types.Producer;
  readonly ProductionQuality: types.ProductionQuality;
  readonly Publisher: types.Publisher;
  readonly Regs: types.Regs;
  readonly Restrictions: types.Restrictions;
  readonly Segment: types.Segment;
  readonly ServerSideAdInsertionMode: types.ServerSideAdInsertionMode;
  readonly Site: types.Site;
  readonly SizeUnit: types.SizeUnit;
  readonly SlotPositionInPod: types.SlotPositionInPod;
  readonly StartDelayMode: types.StartDelayMode;
  readonly Text: types.Text;
  readonly TitleAsset: types.TitleAsset;
  readonly TitleAssetFormat: types.TitleAssetFormat;
  readonly User: types.User;
  readonly UserAgent: types.UserAgent;
  readonly UserAgentSource: types.UserAgentSource;
  readonly VendorCode: types.VendorCode;
  readonly Video: types.Video;
  readonly VideoAsset: types.VideoAsset;
  readonly VideoPlacement: types.VideoPlacement;
  readonly VolumeNormalizationMode: types.VolumeNormalizationMode;
}

/**
 * The static type the named type is.
 */
export type TypeOf<N extends TypeName> = N extends keyof TypeMap ? TypeMap[N] : never;

/**
 * What `decode` returns: the verdict, and the typed payload where it was accepted.
 */
export type Decoded<N extends TypeName> = { readonly ok: true; readonly value: TypeOf<N> } | { readonly ok: false; readonly issues: readonly Issue[] };

/**
 * A validator over the tree this package carries, each type compiled on first use.
 *
 * The engine is an argument with a default, so an application obliged to run another 2020-12
 * implementation supplies one and keeps this layer. What it may not do is supply one that reaches a
 * different verdict: the floor is verdict parity and no engine declares it away (target rules § 9).
 */
export function validator(using: Engine = engine(DOCUMENTS)) {
  const compiled = new Map<string, (value: unknown) => Verdict>();
  const of = (name: TypeName): ((value: unknown) => Verdict) => {
    const already = compiled.get(name);
    if (already !== undefined) return already;
    const fresh = using.compile(TYPES[name]);
    compiled.set(name, fresh);
    return fresh;
  };
  return {
    /**
     * Which engine reached the verdicts.
     */
    engine: using.name,
    /**
     * The schema pass: the verdict the published document gives this payload.
     */
    check: (name: TypeName, value: unknown): Verdict => of(name)(value),
    /**
     * The model pass: the same verdict, and on acceptance the payload typed as the named type. It
     * asserts and does not convert, so an accepted value is the bytes that were graded.
     */
    decode: <N extends TypeName>(name: N, value: unknown): Decoded<N> => {
      const verdict = of(name)(value);
      return verdict.ok ? { ok: true, value: value as TypeOf<N> } : { ok: false, issues: verdict.issues };
    },
  };
}
