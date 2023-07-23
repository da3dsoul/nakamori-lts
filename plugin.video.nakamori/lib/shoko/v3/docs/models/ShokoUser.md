# lib.shoko.v3.lib.shoko.v3.models.shoko_user.ShokoUser

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ID** | decimal.Decimal, int,  | decimal.Decimal,  | The UserID, this is used in a lot of v1 and v2 endpoints, and it&#x27;s needed for editing or removing a user | [optional] value must be a 32 bit integer
**Username** | None, str,  | NoneClass, str,  | Pretty Self-explanatory. It&#x27;s the Username of the user | [optional] 
**IsAdmin** | bool,  | BoolClass,  | Is the user an admin. Admins can perform all operations, including modification of users | [optional] 
**[CommunitySites](#CommunitySites)** | list, tuple, None,  | tuple, NoneClass,  | This is a list of services that the user is set to use. AniDB, Trakt, and Plex, for example | [optional] 
**[RestrictedTags](#RestrictedTags)** | list, tuple, None,  | tuple, NoneClass,  | Restricted tags. Any group/series containing any of these tags will be  rendered inaccessible to the user. | [optional] 
**Avatar** | None, str,  | NoneClass, str,  | The user&#x27;s avatar as a base64 encoded data url if available. Otherwise  an empty string. | [optional] 

# CommunitySites

This is a list of services that the user is set to use. AniDB, Trakt, and Plex, for example

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | This is a list of services that the user is set to use. AniDB, Trakt, and Plex, for example | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EnumsCommunitySites**](EnumsCommunitySites.md) | [**EnumsCommunitySites**](EnumsCommunitySites.md) | [**EnumsCommunitySites**](EnumsCommunitySites.md) |  | 

# RestrictedTags

Restricted tags. Any group/series containing any of these tags will be  rendered inaccessible to the user.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | Restricted tags. Any group/series containing any of these tags will be  rendered inaccessible to the user. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

