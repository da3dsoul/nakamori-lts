# lib.shoko.v3.lib.shoko.v3.models.common_tag.CommonTag

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ID** | decimal.Decimal, int,  | decimal.Decimal,  | Tag id. Relative to it&#x27;s source for now. | [optional] value must be a 32 bit integer
**ParentID** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The parent tag id, if any. Relative to it&#x27;s source for now. | [optional] value must be a 32 bit integer
**Name** | None, str,  | NoneClass, str,  | The tag itself. | [optional] 
**Description** | None, str,  | NoneClass, str,  | What does the tag mean/what&#x27;s it for. | [optional] 
**IsVerified** | None, bool,  | NoneClass, BoolClass,  | True if the tag has been verified. | [optional] 
**IsSpoiler** | bool,  | BoolClass,  | True if the tag is considered a spoiler for all series it appears on. | [optional] 
**IsLocalSpoiler** | None, bool,  | NoneClass, BoolClass,  | True if the tag is considered a spoiler for that particular series it is  set on. | [optional] 
**Weight** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | How relevant is it to the series | [optional] value must be a 32 bit integer
**LastUpdated** | None, str, datetime,  | NoneClass, str,  | When the tag info was last updated. | [optional] value must conform to RFC-3339 date-time
**Source** | None, str,  | NoneClass, str,  | Source. Anidb, User, etc. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

