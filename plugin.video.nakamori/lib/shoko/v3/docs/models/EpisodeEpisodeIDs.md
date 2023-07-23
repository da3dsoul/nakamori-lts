# lib.shoko.v3.lib.shoko.v3.models.episode_episode_ids.EpisodeEpisodeIDs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ID** | decimal.Decimal, int,  | decimal.Decimal,  | The Shoko internal ID, for easy lookup | value must be a 32 bit integer
**AniDB** | decimal.Decimal, int,  | decimal.Decimal,  | The AniDB ID | value must be a 32 bit integer
**ParentSeries** | decimal.Decimal, int,  | decimal.Decimal,  | The id of the parent Shoko.Server.API.v3.Models.Shoko.Series. | [optional] value must be a 32 bit integer
**[TvDB](#TvDB)** | list, tuple, None,  | tuple, NoneClass,  | The TvDB IDs | [optional] 

# TvDB

The TvDB IDs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The TvDB IDs | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

