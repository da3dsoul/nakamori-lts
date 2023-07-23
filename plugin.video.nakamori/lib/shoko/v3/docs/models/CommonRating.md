# lib.shoko.v3.lib.shoko.v3.models.common_rating.CommonRating

Rating object. Shared between sources, episodes vs series, etc

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Rating object. Shared between sources, episodes vs series, etc | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Value** | decimal.Decimal, int, float,  | decimal.Decimal,  | rating | value must be a 64 bit float
**MaxValue** | decimal.Decimal, int,  | decimal.Decimal,  | out of what? Assuming int, as the max should be | value must be a 32 bit integer
**Source** | str,  | str,  | AniDB, etc | 
**Votes** | decimal.Decimal, int,  | decimal.Decimal,  | number of votes | [optional] value must be a 32 bit integer
**Type** | None, str,  | NoneClass, str,  | for temporary vs permanent, or any other situations that may arise later | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

