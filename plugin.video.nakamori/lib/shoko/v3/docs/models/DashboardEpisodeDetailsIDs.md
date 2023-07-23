# lib.shoko.v3.lib.shoko.v3.models.dashboard_episode_details_ids.DashboardEpisodeDetailsIDs

Object holding ids related to the episode.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object holding ids related to the episode. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ID** | decimal.Decimal, int,  | decimal.Decimal,  | The related Shoko.Server.API.v3.Models.Shoko.Episode.AniDB id for the entry. | [optional] value must be a 32 bit integer
**Series** | decimal.Decimal, int,  | decimal.Decimal,  | The related Shoko.Server.API.v3.Models.Shoko.Series.AniDB id for the entry. | [optional] value must be a 32 bit integer
**ShokoFile** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The related Shoko Shoko.Server.API.v3.Models.Shoko.File id if a file is available  and/or appropriate. | [optional] value must be a 32 bit integer
**ShokoEpisode** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The related Shoko Shoko.Server.API.v3.Models.Shoko.Episode id if the episode is  available locally. | [optional] value must be a 32 bit integer
**ShokoSeries** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The related Shoko Shoko.Server.API.v3.Models.Shoko.Series id if the series is  available locally. | [optional] value must be a 32 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

