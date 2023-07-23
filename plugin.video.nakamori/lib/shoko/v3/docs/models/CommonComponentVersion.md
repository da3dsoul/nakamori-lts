# lib.shoko.v3.lib.shoko.v3.models.common_component_version.CommonComponentVersion

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Version** | None, str,  | NoneClass, str,  | Version number. | [optional] 
**Commit** | None, str,  | NoneClass, str,  | Commit SHA. | [optional] 
**ReleaseChannel** | [**CommonReleaseChannel**](CommonReleaseChannel.md) | [**CommonReleaseChannel**](CommonReleaseChannel.md) |  | [optional] 
**ReleaseDate** | None, str, datetime,  | NoneClass, str,  | Release date. | [optional] value must conform to RFC-3339 date-time
**Tag** | None, str,  | NoneClass, str,  | Git Tag. | [optional] 
**Description** | None, str,  | NoneClass, str,  | A short description about this release/version. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

