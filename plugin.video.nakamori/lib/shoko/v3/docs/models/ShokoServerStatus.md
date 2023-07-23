# lib.shoko.v3.lib.shoko.v3.models.shoko_server_status.ShokoServerStatus

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**StartupMessage** | None, str,  | NoneClass, str,  | The progress message for starting up | [optional] 
**State** | [**ServerStatusStartupState**](ServerStatusStartupState.md) | [**ServerStatusStartupState**](ServerStatusStartupState.md) |  | [optional] 
**Uptime** | None, str,  | NoneClass, str,  | Uptime in hh:mm:ss or null if not started. Uses hours may be greater than a day. | [optional] 
**DatabaseBlocked** | [**ServerStateDatabaseBlockedInfo**](ServerStateDatabaseBlockedInfo.md) | [**ServerStateDatabaseBlockedInfo**](ServerStateDatabaseBlockedInfo.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

