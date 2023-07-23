# lib.shoko.v3.lib.shoko.v3.models.debug_controller_anidb_udp_request.DebugControllerAnidbUdpRequest

An abstraction for an AniDB UDP API Request.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An abstraction for an AniDB UDP API Request. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Action** | str,  | str,  | The action to run. | 
**Unsafe** | bool,  | BoolClass,  | Run the action without checking if we&#x27;re banned and what-not. | [optional] 
**[Payload](#Payload)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Extra payload to use with the action. | [optional] 

# Payload

Extra payload to use with the action.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Extra payload to use with the action. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

