# lib.shoko.v3.lib.shoko.v3.models.common_vote.CommonVote

Vote object. Shared between sources, episodes vs series, etc.  Normalises the value

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Vote object. Shared between sources, episodes vs series, etc.  Normalises the value | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Value** | decimal.Decimal, int, float,  | decimal.Decimal,  | The user-submitted rating relative to Shoko.Server.API.v3.Models.Common.Vote.MaxValue. | value must be a 64 bit float
**MaxValue** | decimal.Decimal, int,  | decimal.Decimal,  | Max allowed value for the user-submitted rating. Assumes 10 if not set. | [optional] if omitted the server will use the default value of 10value must be a 32 bit integer
**Type** | None, str,  | NoneClass, str,  | for temporary vs permanent, or any other situations that may arise later. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

