# lib.shoko.v3.lib.shoko.v3.models.file_file_user_stats.FileFileUserStats

User stats for the file.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | User stats for the file. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ResumePosition** | None, str,  | NoneClass, str,  | Where to resume the next playback. | [optional] 
**WatchedCount** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of times the file have been watched. | [optional] value must be a 32 bit integer
**LastWatchedAt** | None, str, datetime,  | NoneClass, str,  | When the file was last watched. Will be null if the full is  currently marked as unwatched. | [optional] value must conform to RFC-3339 date-time
**LastUpdatedAt** | str, datetime,  | str,  | When the entry was last updated. | [optional] value must conform to RFC-3339 date-time

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

