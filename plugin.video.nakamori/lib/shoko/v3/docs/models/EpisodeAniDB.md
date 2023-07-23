# lib.shoko.v3.lib.shoko.v3.models.episode_ani_db.EpisodeAniDB

AniDB specific data for an Episode

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | AniDB specific data for an Episode | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ID** | decimal.Decimal, int,  | decimal.Decimal,  | AniDB Episode ID | [optional] value must be a 32 bit integer
**Type** | str,  | str,  | Episode Type | [optional] 
**EpisodeNumber** | decimal.Decimal, int,  | decimal.Decimal,  | Episode Number | [optional] value must be a 32 bit integer
**AirDate** | None, str, datetime,  | NoneClass, str,  | First Listed Air Date. This may not be when it aired, but an early release date | [optional] value must conform to RFC-3339 date-time
**[Titles](#Titles)** | list, tuple, None,  | tuple, NoneClass,  | Titles for the Episode | [optional] 
**Description** | None, str,  | NoneClass, str,  | AniDB Episode Summary | [optional] 
**Rating** | [**CommonRating**](CommonRating.md) | [**CommonRating**](CommonRating.md) |  | [optional] 

# Titles

Titles for the Episode

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | Titles for the Episode | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CommonTitle**](CommonTitle.md) | [**CommonTitle**](CommonTitle.md) | [**CommonTitle**](CommonTitle.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

