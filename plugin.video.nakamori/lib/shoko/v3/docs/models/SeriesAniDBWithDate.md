# lib.shoko.v3.lib.shoko.v3.models.series_ani_db_with_date.SeriesAniDBWithDate

The AniDB Data model for series

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The AniDB Data model for series | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**AirDate** | str, datetime,  | str,  | Air date (2013-02-27, shut up avael). Anything without an air date is going to be missing a lot of info. | value must conform to RFC-3339 date-time
**Type** | str,  | str,  | Series type. Series, OVA, Movie, etc | 
**Poster** | [**CommonImage**](CommonImage.md) | [**CommonImage**](CommonImage.md) |  | 
**Title** | str,  | str,  | Main Title, usually matches x-jat | 
**ID** | decimal.Decimal, int,  | decimal.Decimal,  | AniDB ID | value must be a 32 bit integer
**[Titles](#Titles)** | list, tuple,  | tuple,  | There should always be at least one of these, the Shoko.Server.API.v3.Models.Shoko.Series.AniDB.Title. | 
**EndDate** | None, str, datetime,  | NoneClass, str,  | End date, can be omitted. Omitted means that it&#x27;s still airing (2013-02-27) | [optional] value must conform to RFC-3339 date-time
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

