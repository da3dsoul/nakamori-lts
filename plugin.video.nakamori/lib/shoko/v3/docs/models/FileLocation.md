# lib.shoko.v3.lib.shoko.v3.models.file_location.FileLocation

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**IsAccessible** | bool,  | BoolClass,  | Can the server access the file right now | 
**ImportFolderID** | decimal.Decimal, int,  | decimal.Decimal,  | The Import Folder that this file resides in | [optional] value must be a 32 bit integer
**RelativePath** | None, str,  | NoneClass, str,  | The relative path from the import folder&#x27;s path on the server. The Filename can be easily extracted from this. Using the ImportFolder, you can get the full server path of the file or map it if the client has remote access to the filesystem. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

