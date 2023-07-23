# lib.shoko.v3.lib.shoko.v3.models.dashboard_collection_stats.DashboardCollectionStats

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**FileCount** | decimal.Decimal, int,  | decimal.Decimal,  | Number of Files in the collection (visible to the current user) | [optional] value must be a 32 bit integer
**SeriesCount** | decimal.Decimal, int,  | decimal.Decimal,  | Number of Series in the Collection (visible to the current user) | [optional] value must be a 32 bit integer
**GroupCount** | decimal.Decimal, int,  | decimal.Decimal,  | The number of Groups in the Collection (visible to the current user) | [optional] value must be a 32 bit integer
**FileSize** | decimal.Decimal, int,  | decimal.Decimal,  | Total amount of space the collection takes (of what&#x27;s visible to the current user) | [optional] value must be a 64 bit integer
**FinishedSeries** | decimal.Decimal, int,  | decimal.Decimal,  | Number of Series Completely Watched | [optional] value must be a 32 bit integer
**WatchedEpisodes** | decimal.Decimal, int,  | decimal.Decimal,  | Number of Episodes Watched | [optional] value must be a 32 bit integer
**WatchedHours** | decimal.Decimal, int, float,  | decimal.Decimal,  | Watched Hours, rounded to one place | [optional] value must be a 64 bit float
**PercentDuplicate** | decimal.Decimal, int, float,  | decimal.Decimal,  | The percentage of files that are either duplicates or belong to the same episode | [optional] value must be a 64 bit float
**MissingEpisodes** | decimal.Decimal, int,  | decimal.Decimal,  | The Number of missing episodes, regardless of where they are from or available | [optional] value must be a 32 bit integer
**MissingEpisodesCollecting** | decimal.Decimal, int,  | decimal.Decimal,  | The number of missing episodes from groups we are collecting. This should not be used as a rule, as it&#x27;s not very reliable | [optional] value must be a 32 bit integer
**UnrecognizedFiles** | decimal.Decimal, int,  | decimal.Decimal,  | Number of Unrecognized Files | [optional] value must be a 32 bit integer
**SeriesWithMissingLinks** | decimal.Decimal, int,  | decimal.Decimal,  | The number of series missing both the TvDB and MovieDB Links | [optional] value must be a 32 bit integer
**EpisodesWithMultipleFiles** | decimal.Decimal, int,  | decimal.Decimal,  | The number of Episodes with more than one File (not marked as a variation) | [optional] value must be a 32 bit integer
**FilesWithDuplicateLocations** | decimal.Decimal, int,  | decimal.Decimal,  | The number of files that exist in more than one location | [optional] value must be a 32 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

