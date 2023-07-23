# lib.shoko.v3.lib.shoko.v3.models.group_group_ids.GroupGroupIDs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ID** | decimal.Decimal, int,  | decimal.Decimal,  | The Shoko internal ID, for easy lookup | value must be a 32 bit integer
**DefaultSeries** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The ID of the user selected default series, if it has one.                The value of this field will be reflected in Shoko.Server.API.v3.Models.Shoko.Group.GroupIDs.MainSeries if it is set. | [optional] value must be a 32 bit integer
**MainSeries** | decimal.Decimal, int,  | decimal.Decimal,  | The ID of the main series for the group. | [optional] value must be a 32 bit integer
**ParentGroup** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The ID of the direct parent group, if it has one. | [optional] value must be a 32 bit integer
**TopLevelGroup** | decimal.Decimal, int,  | decimal.Decimal,  | The ID of the top-level (ancestor) group this group belongs to.  If the current group is a top-level group then it refers to  itself. | [optional] value must be a 32 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

