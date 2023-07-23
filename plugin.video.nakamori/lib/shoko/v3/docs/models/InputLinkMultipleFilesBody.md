# lib.shoko.v3.lib.shoko.v3.models.input_link_multiple_files_body.InputLinkMultipleFilesBody

Link a file to multiple episodes.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Link a file to multiple episodes. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**EpisodeID** | decimal.Decimal, int,  | decimal.Decimal,  | The episode identifier. | value must be a 32 bit integer
**[FileIDs](#FileIDs)** | list, tuple,  | tuple,  | An array of file identifiers to link in batch. | 

# FileIDs

An array of file identifiers to link in batch.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of file identifiers to link in batch. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

