# lib.shoko.v3.lib.shoko.v3.models.shoko_import_folder.ShokoImportFolder

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Size** | decimal.Decimal, int,  | decimal.Decimal,  | number of direct children (number of series in group, eps in series, etc) | value must be a 32 bit integer
**Name** | str,  | str,  | The server&#x27;s title. This will use overrides, the naming settings, MainTitle if all else fails. This is a guaranteed fallback | 
**ID** | decimal.Decimal, int,  | decimal.Decimal,  | Import Folder ID | [optional] value must be a 32 bit integer
**WatchForNewFiles** | bool,  | BoolClass,  | Is the Folder watched by the filesystem watcher | [optional] 
**DropFolderType** | [**ShokoDropFolderType**](ShokoDropFolderType.md) | [**ShokoDropFolderType**](ShokoDropFolderType.md) |  | [optional] 
**Path** | None, str,  | NoneClass, str,  | Path on the server where the import folder exists. For docker, it&#x27;s inside the container, so it&#x27;ll look excessively simple | [optional] 
**FileSize** | decimal.Decimal, int,  | decimal.Decimal,  | Total FileSize of the contents of the ImportFolder | [optional] value must be a 64 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

