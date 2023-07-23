# lib.shoko.v3.lib.shoko.v3.models.shoko_group.ShokoGroup

Group object, stores all of the group info. Groups are Shoko Internal Objects, so they are handled a bit differently

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Group object, stores all of the group info. Groups are Shoko Internal Objects, so they are handled a bit differently | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Size** | decimal.Decimal, int,  | decimal.Decimal,  | number of direct children (number of series in group, eps in series, etc) | value must be a 32 bit integer
**Name** | str,  | str,  | The server&#x27;s title. This will use overrides, the naming settings, MainTitle if all else fails. This is a guaranteed fallback | 
**IDs** | [**GroupGroupIDs**](GroupGroupIDs.md) | [**GroupGroupIDs**](GroupGroupIDs.md) |  | [optional] 
**SortName** | None, str,  | NoneClass, str,  | The sort name for the group. | [optional] 
**Description** | None, str,  | NoneClass, str,  | A short description of the group. | [optional] 
**HasCustomName** | bool,  | BoolClass,  | Indicates the group has a custom name set, different from the default  name of the main series in the group. | [optional] 
**HasCustomDescription** | bool,  | BoolClass,  | Indicates the group has a custom description set, different from the  default description of the main series in the group. | [optional] 
**Images** | [**CommonImages**](CommonImages.md) | [**CommonImages**](CommonImages.md) |  | [optional] 
**Sizes** | [**ShokoGroupSizes**](ShokoGroupSizes.md) | [**ShokoGroupSizes**](ShokoGroupSizes.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

