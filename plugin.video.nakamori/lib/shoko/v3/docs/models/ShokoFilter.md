# lib.shoko.v3.lib.shoko.v3.models.shoko_filter.ShokoFilter

A Filter. This is how Shoko serves and organizes Series/Groups. They can be  used to keep track of what you're watching and many other things.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A Filter. This is how Shoko serves and organizes Series/Groups. They can be  used to keep track of what you&#x27;re watching and many other things. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Size** | decimal.Decimal, int,  | decimal.Decimal,  | number of direct children (number of series in group, eps in series, etc) | value must be a 32 bit integer
**Name** | str,  | str,  | The server&#x27;s title. This will use overrides, the naming settings, MainTitle if all else fails. This is a guaranteed fallback | 
**IDs** | [**FilterFilterIDs**](FilterFilterIDs.md) | [**FilterFilterIDs**](FilterFilterIDs.md) |  | [optional] 
**IsLocked** | bool,  | BoolClass,  | Indicates the filter cannot be edited by a user. | [optional] 
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

