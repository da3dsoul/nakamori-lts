# lib.shoko.v3.lib.shoko.v3.models.input_create_or_update_filter_body.InputCreateOrUpdateFilterBody

Used for creating new filters, updating existing filters, and/or  updating the live filter.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Used for creating new filters, updating existing filters, and/or  updating the live filter. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Name** | None, str,  | NoneClass, str,  | The filter name. | [optional] 
**ParentID** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The id of the parent filter. If you want to add/move this filter  as a sub-filter to an existing directory filter. | [optional] value must be a 32 bit integer
**IsDirectory** | bool,  | BoolClass,  | Indicates the filter should be a directory filter. | [optional] 
**IsInverted** | bool,  | BoolClass,  | Indicates that the filter is inverted and all conditions applied  to it will be used to exclude groups and series instead of  include them. | [optional] 
**IsHidden** | bool,  | BoolClass,  | Indicates the filter should be hidden unless explictly requested. This will hide the filter from the normal UIs. | [optional] 
**ApplyAtSeriesLevel** | bool,  | BoolClass,  | Inidcates the filter should be applied at the series level.  Filter conditions like like Seasons, Years, Tags, etc only count series individually, rather than by group. | [optional] 
**[Conditions](#Conditions)** | list, tuple, None,  | tuple, NoneClass,  | List of Conditions. Order doesn&#x27;t matter. | [optional] 
**[Sorting](#Sorting)** | list, tuple, None,  | tuple, NoneClass,  | The sorting criteria. Order matters. | [optional] 

# Conditions

List of Conditions. Order doesn't matter.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | List of Conditions. Order doesn&#x27;t matter. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FilterFilterCondition**](FilterFilterCondition.md) | [**FilterFilterCondition**](FilterFilterCondition.md) | [**FilterFilterCondition**](FilterFilterCondition.md) |  | 

# Sorting

The sorting criteria. Order matters.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The sorting criteria. Order matters. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FilterSortingCriteria**](FilterSortingCriteria.md) | [**FilterSortingCriteria**](FilterSortingCriteria.md) | [**FilterSortingCriteria**](FilterSortingCriteria.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

