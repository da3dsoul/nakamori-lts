# lib.shoko.v3.lib.shoko.v3.models.input_link_series_multiple_body.InputLinkSeriesMultipleBody

Link multiple files to an episode range in a series.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Link multiple files to an episode range in a series. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**SeriesID** | decimal.Decimal, int,  | decimal.Decimal,  | The series identifier. | value must be a 32 bit integer
**[FileIDs](#FileIDs)** | list, tuple,  | tuple,  | An array of file identifiers to link in batch. | 
**RangeStart** | str,  | str,  | The start of the range of episodes to link to the file. Append a type prefix to use another episode type. | 
**SingleEpisode** | bool,  | BoolClass,  | If true then files will be linked to a single episode instead of a range spanning the amount of files to add. | [optional] if omitted the server will use the default value of False

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

