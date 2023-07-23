# lib.shoko.v3.lib.shoko.v3.models.input_create_or_update_group_body.InputCreateOrUpdateGroupBody

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ParentID** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The Shoko.Server.API.v3.Models.Shoko.Group parent ID. Omit it or set it to 0 to  create a new top-level group. | [optional] value must be a 32 bit integer
**DefaultSeriesID** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Manually select the default series for the group. | [optional] value must be a 32 bit integer
**[SeriesIDs](#SeriesIDs)** | list, tuple, None,  | tuple, NoneClass,  | All the series to put into the group. | [optional] 
**[ChildIDs](#ChildIDs)** | list, tuple, None,  | tuple, NoneClass,  | All groups to put into the group as sub-groups. | [optional] 
**Name** | None, str,  | NoneClass, str,  | The group&#x27;s custom name. | [optional] 
**SortName** | None, str,  | NoneClass, str,  | The group&#x27;s custom sort name. | [optional] 
**Description** | None, str,  | NoneClass, str,  | The group&#x27;s custom description. | [optional] 
**HasCustomName** | None, bool,  | NoneClass, BoolClass,  | Indicates the group should use a custom name. | [optional] 
**HasCustomDescription** | None, bool,  | NoneClass, BoolClass,  | Indicates the group should use a custom description. | [optional] 

# SeriesIDs

All the series to put into the group.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | All the series to put into the group. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# ChildIDs

All groups to put into the group as sub-groups.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | All groups to put into the group as sub-groups. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

