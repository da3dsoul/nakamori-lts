# lib.shoko.v3.lib.shoko.v3.models.collection_plex_library.CollectionPlexLibrary

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**RatingKey** | None, str,  | NoneClass, str,  |  | [optional] 
**Key** | None, str,  | NoneClass, str,  |  | [optional] 
**Type** | [**PlexPlexType**](PlexPlexType.md) | [**PlexPlexType**](PlexPlexType.md) |  | [optional] 
**Title** | None, str,  | NoneClass, str,  |  | [optional] 
**ContentRating** | None, str,  | NoneClass, str,  |  | [optional] 
**Summary** | None, str,  | NoneClass, str,  |  | [optional] 
**Index** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**Rating** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  |  | [optional] value must be a 64 bit float
**Year** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**Thumb** | None, str,  | NoneClass, str,  |  | [optional] 
**Art** | None, str,  | NoneClass, str,  |  | [optional] 
**Banner** | None, str,  | NoneClass, str,  |  | [optional] 
**OriginallyAvailableAt** | None, str, datetime,  | NoneClass, str,  |  | [optional] value must conform to RFC-3339 date-time
**LeafCount** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**ViewedLeafCount** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**ChildCount** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**AddedAt** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**UpdatedAt** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**[Genre](#Genre)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 
**[Role](#Role)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 
**SkipChildren** | None, bool,  | NoneClass, BoolClass,  |  | [optional] 
**Theme** | None, str,  | NoneClass, str,  |  | [optional] 
**ViewCount** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**LastViewedAt** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**TitleSort** | None, str,  | NoneClass, str,  |  | [optional] 
**UserRating** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  |  | [optional] value must be a 64 bit integer

# Genre

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PlexTagHolder**](PlexTagHolder.md) | [**PlexTagHolder**](PlexTagHolder.md) | [**PlexTagHolder**](PlexTagHolder.md) |  | 

# Role

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PlexTagHolder**](PlexTagHolder.md) | [**PlexTagHolder**](PlexTagHolder.md) | [**PlexTagHolder**](PlexTagHolder.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

