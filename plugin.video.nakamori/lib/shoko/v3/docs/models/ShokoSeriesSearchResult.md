# lib.shoko.v3.lib.shoko.v3.models.shoko_series_search_result.ShokoSeriesSearchResult

An Extended Series Model with Values for Search Results

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An Extended Series Model with Values for Search Results | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Size** | decimal.Decimal, int,  | decimal.Decimal,  | number of direct children (number of series in group, eps in series, etc) | value must be a 32 bit integer
**Name** | str,  | str,  | The server&#x27;s title. This will use overrides, the naming settings, MainTitle if all else fails. This is a guaranteed fallback | 
**ExactMatch** | bool,  | BoolClass,  | Indicates whether the search result is an exact match to the query. | [optional] 
**Index** | decimal.Decimal, int,  | decimal.Decimal,  | Represents the position of the match within the sanitized string.  This property is only applicable when ExactMatch is set to true.  A lower value indicates a match that occurs earlier in the string. | [optional] value must be a 32 bit integer
**Distance** | decimal.Decimal, int, float,  | decimal.Decimal,  | Represents the similarity measure between the sanitized query and the sanitized matched result.  This may be the sorensen-dice distance or the tag weight when comparing tags for a series.  A lower value indicates a more similar match. | [optional] value must be a 64 bit float
**LengthDifference** | decimal.Decimal, int,  | decimal.Decimal,  | Represents the absolute difference in length between the sanitized query and the sanitized matched result.  A lower value indicates a match with a more similar length to the query. | [optional] value must be a 32 bit integer
**Match** | None, str,  | NoneClass, str,  | Contains the original matched substring from the original string. | [optional] 
**IDs** | [**ShokoSeriesIDs**](ShokoSeriesIDs.md) | [**ShokoSeriesIDs**](ShokoSeriesIDs.md) |  | [optional] 
**Images** | [**CommonImages**](CommonImages.md) | [**CommonImages**](CommonImages.md) |  | [optional] 
**UserRating** | [**CommonRating**](CommonRating.md) | [**CommonRating**](CommonRating.md) |  | [optional] 
**[AirsOn](#AirsOn)** | list, tuple, None,  | tuple, NoneClass,  | The inferred days of the week this series airs on. | [optional] 
**[Links](#Links)** | list, tuple, None,  | tuple, NoneClass,  | links to series pages on various sites | [optional] 
**Sizes** | [**ShokoSeriesSizes**](ShokoSeriesSizes.md) | [**ShokoSeriesSizes**](ShokoSeriesSizes.md) |  | [optional] 
**Created** | str, datetime,  | str,  | The time when the series was created, during the process of the first file being added | [optional] value must conform to RFC-3339 date-time
**Updated** | str, datetime,  | str,  | The time when the series was last updated | [optional] value must conform to RFC-3339 date-time
**AniDB** | [**SeriesAniDBWithDate**](SeriesAniDBWithDate.md) | [**SeriesAniDBWithDate**](SeriesAniDBWithDate.md) |  | [optional] 
**[TvDB](#TvDB)** | list, tuple, None,  | tuple, NoneClass,  | The Shoko.Server.API.v3.Models.Shoko.Series.TvDB entries, if Shoko.Server.API.v3.Models.Common.DataSource.TvDB  is included in the data to add. | [optional] 

# AirsOn

The inferred days of the week this series airs on.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The inferred days of the week this series airs on. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SystemDayOfWeek**](SystemDayOfWeek.md) | [**SystemDayOfWeek**](SystemDayOfWeek.md) | [**SystemDayOfWeek**](SystemDayOfWeek.md) |  | 

# Links

links to series pages on various sites

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | links to series pages on various sites | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SeriesResource**](SeriesResource.md) | [**SeriesResource**](SeriesResource.md) | [**SeriesResource**](SeriesResource.md) |  | 

# TvDB

The Shoko.Server.API.v3.Models.Shoko.Series.TvDB entries, if Shoko.Server.API.v3.Models.Common.DataSource.TvDB  is included in the data to add.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The Shoko.Server.API.v3.Models.Shoko.Series.TvDB entries, if Shoko.Server.API.v3.Models.Common.DataSource.TvDB  is included in the data to add. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SeriesTvDB**](SeriesTvDB.md) | [**SeriesTvDB**](SeriesTvDB.md) | [**SeriesTvDB**](SeriesTvDB.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

