# lib.shoko.v3.lib.shoko.v3.models.filter_sorting_criteria.FilterSortingCriteria

Sorting Criteria hold info on how Group Filters sort their items.  It is in a List to follow an OrderBy().ThenBy().ThenBy(), allowing  consistent results with fallbacks.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Sorting Criteria hold info on how Group Filters sort their items.  It is in a List to follow an OrderBy().ThenBy().ThenBy(), allowing  consistent results with fallbacks. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Type** | [**EnumsGroupFilterSorting**](EnumsGroupFilterSorting.md) | [**EnumsGroupFilterSorting**](EnumsGroupFilterSorting.md) |  | 
**IsInverted** | bool,  | BoolClass,  | Assumed Ascending unless this is specified. You must set this if you want highest rating, for example | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

