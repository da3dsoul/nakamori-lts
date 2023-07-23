# lib.shoko.v3.lib.shoko.v3.models.shoko_episode.ShokoEpisode

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Size** | decimal.Decimal, int,  | decimal.Decimal,  | number of direct children (number of series in group, eps in series, etc) | value must be a 32 bit integer
**Name** | str,  | str,  | The server&#x27;s title. This will use overrides, the naming settings, MainTitle if all else fails. This is a guaranteed fallback | 
**IDs** | [**EpisodeEpisodeIDs**](EpisodeEpisodeIDs.md) | [**EpisodeEpisodeIDs**](EpisodeEpisodeIDs.md) |  | [optional] 
**Duration** | str,  | str,  | The duration of the episode. | [optional] 
**ResumePosition** | None, str,  | NoneClass, str,  | Where to resume the next playback for the most recently watched file, if  any. Otherwise &#x60;null&#x60; if no files for the episode have any resume  positions. | [optional] 
**Watched** | None, str, datetime,  | NoneClass, str,  | The last watched date and time for the current user for the most  recently watched file, if any. Or &#x60;null&#x60; if it is considered  \&quot;unwatched.\&quot; | [optional] value must conform to RFC-3339 date-time
**WatchCount** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of times the episode have been watched (till completion) by  the user across all files. | [optional] value must be a 32 bit integer
**IsHidden** | bool,  | BoolClass,  | Episode is marked as \&quot;ignored.\&quot; Which means it won&#x27;t be show up in the  api unless explictly requested, and will not count against the unwatched  counts and missing counts for the series. | [optional] 
**AniDB** | [**EpisodeAniDB**](EpisodeAniDB.md) | [**EpisodeAniDB**](EpisodeAniDB.md) |  | [optional] 
**[TvDB](#TvDB)** | list, tuple, None,  | tuple, NoneClass,  | The Shoko.Server.API.v3.Models.Shoko.Episode.TvDB entries, if Shoko.Server.API.v3.Models.Common.DataSource.TvDB  is included in the data to add. | [optional] 

# TvDB

The Shoko.Server.API.v3.Models.Shoko.Episode.TvDB entries, if Shoko.Server.API.v3.Models.Common.DataSource.TvDB  is included in the data to add.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The Shoko.Server.API.v3.Models.Shoko.Episode.TvDB entries, if Shoko.Server.API.v3.Models.Common.DataSource.TvDB  is included in the data to add. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EpisodeTvDB**](EpisodeTvDB.md) | [**EpisodeTvDB**](EpisodeTvDB.md) | [**EpisodeTvDB**](EpisodeTvDB.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

