# lib.shoko.v3.lib.shoko.v3.models.series_tv_db.SeriesTvDB

The TvDB Data model for series

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The TvDB Data model for series | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Title** | str,  | str,  | TvDB only supports one title | 
**ID** | decimal.Decimal, int,  | decimal.Decimal,  | TvDB ID | value must be a 32 bit integer
**AirDate** | None, str, datetime,  | NoneClass, str,  | Air date (2013-02-27, shut up avael) | [optional] value must conform to RFC-3339 date-time
**EndDate** | None, str, datetime,  | NoneClass, str,  | End date, can be null. Null means that it&#x27;s still airing (2013-02-27) | [optional] value must conform to RFC-3339 date-time
**Description** | None, str,  | NoneClass, str,  | Description | [optional] 
**Season** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | TvDB Season. This value is not guaranteed to be even kind of accurate  TvDB matchings and links affect this. Null means no match. 0 means specials | [optional] value must be a 32 bit integer
**[Posters](#Posters)** | list, tuple, None,  | tuple, NoneClass,  | Posters | [optional] 
**[Fanarts](#Fanarts)** | list, tuple, None,  | tuple, NoneClass,  | Fanarts | [optional] 
**[Banners](#Banners)** | list, tuple, None,  | tuple, NoneClass,  | Banners | [optional] 
**Rating** | [**CommonRating**](CommonRating.md) | [**CommonRating**](CommonRating.md) |  | [optional] 

# Posters

Posters

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | Posters | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CommonImage**](CommonImage.md) | [**CommonImage**](CommonImage.md) | [**CommonImage**](CommonImage.md) |  | 

# Fanarts

Fanarts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | Fanarts | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CommonImage**](CommonImage.md) | [**CommonImage**](CommonImage.md) | [**CommonImage**](CommonImage.md) |  | 

# Banners

Banners

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | Banners | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CommonImage**](CommonImage.md) | [**CommonImage**](CommonImage.md) | [**CommonImage**](CommonImage.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

