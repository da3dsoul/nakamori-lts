# lib.shoko.v3.lib.shoko.v3.models.input_create_user_body.InputCreateUserBody

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Password** | str,  | str,  | The new password. | 
**Username** | None, str,  | NoneClass, str,  | The user&#x27;s new name. Must not be empty or only white-spaces. | [optional] 
**IsAdmin** | None, bool,  | NoneClass, BoolClass,  | Change the user admin status. The viewer must have admin access  yo change this. | [optional] 
**[CommunitySites](#CommunitySites)** | list, tuple, None,  | tuple, NoneClass,  | The updated list of services that the user can use. The viewer  must have admin access to change these. | [optional] 
**[RestrictedTags](#RestrictedTags)** | list, tuple, None,  | tuple, NoneClass,  | The updated restricted tags for the user. The viewer must have  admin access to change these. | [optional] 
**Avatar** | None, str,  | NoneClass, str,  | The new user&#x27;s avatar image, base64 encoded. Set to an empty  string to remove the current avatar image. | [optional] 

# CommunitySites

The updated list of services that the user can use. The viewer  must have admin access to change these.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The updated list of services that the user can use. The viewer  must have admin access to change these. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EnumsCommunitySites**](EnumsCommunitySites.md) | [**EnumsCommunitySites**](EnumsCommunitySites.md) | [**EnumsCommunitySites**](EnumsCommunitySites.md) |  | 

# RestrictedTags

The updated restricted tags for the user. The viewer must have  admin access to change these.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The updated restricted tags for the user. The viewer must have  admin access to change these. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

