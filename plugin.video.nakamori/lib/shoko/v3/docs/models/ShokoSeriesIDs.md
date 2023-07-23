# lib.shoko.v3.lib.shoko.v3.models.shoko_series_ids.ShokoSeriesIDs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ID** | decimal.Decimal, int,  | decimal.Decimal,  | The Shoko internal ID, for easy lookup | value must be a 32 bit integer
**AniDB** | decimal.Decimal, int,  | decimal.Decimal,  | The AniDB ID | value must be a 32 bit integer
**ParentGroup** | decimal.Decimal, int,  | decimal.Decimal,  | The ID of the direct parent group, if it has one. | [optional] value must be a 32 bit integer
**TopLevelGroup** | decimal.Decimal, int,  | decimal.Decimal,  | The ID of the top-level (ancestor) group this series belongs to. | [optional] value must be a 32 bit integer
**[TvDB](#TvDB)** | list, tuple, None,  | tuple, NoneClass,  | The TvDB IDs | [optional] 
**[TMDB](#TMDB)** | list, tuple, None,  | tuple, NoneClass,  | The Movie DB IDs | [optional] 
**[MAL](#MAL)** | list, tuple, None,  | tuple, NoneClass,  | The MyAnimeList IDs | [optional] 
**[TraktTv](#TraktTv)** | list, tuple, None,  | tuple, NoneClass,  | The TraktTv IDs | [optional] 
**[AniList](#AniList)** | list, tuple, None,  | tuple, NoneClass,  | The AniList IDs | [optional] 

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

# TMDB

The Movie DB IDs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The Movie DB IDs | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# MAL

The MyAnimeList IDs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The MyAnimeList IDs | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# TraktTv

The TraktTv IDs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The TraktTv IDs | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# AniList

The AniList IDs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The AniList IDs | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

