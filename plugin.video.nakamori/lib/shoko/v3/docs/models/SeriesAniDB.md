# lib.shoko.v3.lib.shoko.v3.models.series_ani_db.SeriesAniDB

Basic anidb data across all anidb types.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Basic anidb data across all anidb types. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Type** | str,  | str,  | Series type. Series, OVA, Movie, etc | 
**Poster** | [**CommonImage**](CommonImage.md) | [**CommonImage**](CommonImage.md) |  | 
**Title** | str,  | str,  | Main Title, usually matches x-jat | 
**ID** | decimal.Decimal, int,  | decimal.Decimal,  | AniDB ID | value must be a 32 bit integer
**[Titles](#Titles)** | list, tuple,  | tuple,  | There should always be at least one of these, the Shoko.Server.API.v3.Models.Shoko.Series.AniDB.Title. | 
**ShokoID** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Shoko.Server.API.v3.Models.Shoko.Series ID if the series is available locally. | [optional] value must be a 32 bit integer
**Description** | None, str,  | NoneClass, str,  | Description. | [optional] 
**Restricted** | bool,  | BoolClass,  | Restricted content. Mainly porn. | [optional] 
**EpisodeCount** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Number of Shoko.Server.API.v3.Models.Shoko.EpisodeType.Normal episodes contained within the series if it&#x27;s known. | [optional] value must be a 32 bit integer
**Rating** | [**CommonRating**](CommonRating.md) | [**CommonRating**](CommonRating.md) |  | [optional] 
**UserApproval** | [**CommonRating**](CommonRating.md) | [**CommonRating**](CommonRating.md) |  | [optional] 
**Relation** | [**DataModelsRelationType**](DataModelsRelationType.md) | [**DataModelsRelationType**](DataModelsRelationType.md) |  | [optional] 

# Titles

There should always be at least one of these, the Shoko.Server.API.v3.Models.Shoko.Series.AniDB.Title.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | There should always be at least one of these, the Shoko.Server.API.v3.Models.Shoko.Series.AniDB.Title. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CommonTitle**](CommonTitle.md) | [**CommonTitle**](CommonTitle.md) | [**CommonTitle**](CommonTitle.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

