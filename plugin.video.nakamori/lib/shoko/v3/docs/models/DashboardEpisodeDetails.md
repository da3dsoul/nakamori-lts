# lib.shoko.v3.lib.shoko.v3.models.dashboard_episode_details.DashboardEpisodeDetails

Episode details for displaying on the dashboard.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Episode details for displaying on the dashboard. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**IDs** | [**DashboardEpisodeDetailsIDs**](DashboardEpisodeDetailsIDs.md) | [**DashboardEpisodeDetailsIDs**](DashboardEpisodeDetailsIDs.md) |  | [optional] 
**Title** | None, str,  | NoneClass, str,  | Episode title. | [optional] 
**Number** | decimal.Decimal, int,  | decimal.Decimal,  | Episode number. | [optional] value must be a 32 bit integer
**Type** | str,  | str,  | Episode type. | [optional] 
**AirDate** | None, str, datetime,  | NoneClass, str,  | Air Date. | [optional] value must conform to RFC-3339 date-time
**Duration** | str,  | str,  | The duration of the episode. | [optional] 
**ResumePosition** | None, str,  | NoneClass, str,  | Where to resume the next playback. | [optional] 
**Watched** | None, str, datetime,  | NoneClass, str,  | If the file/episode is considered watched. | [optional] value must conform to RFC-3339 date-time
**SeriesTitle** | None, str,  | NoneClass, str,  | Series title. | [optional] 
**SeriesPoster** | [**CommonImage**](CommonImage.md) | [**CommonImage**](CommonImage.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

