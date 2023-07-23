# lib.shoko.v3.lib.shoko.v3.models.input_link_series_body.InputLinkSeriesBody

Link a file to an episode range in a series.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Link a file to an episode range in a series. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**RangeEnd** | str,  | str,  | The end of the range of episodes to link to the file. The prefix used should be the same as in Shoko.Server.API.v3.Models.Shoko.File.Input.LinkSeriesBody.RangeStart. | 
**SeriesID** | decimal.Decimal, int,  | decimal.Decimal,  | The series identifier. | value must be a 32 bit integer
**RangeStart** | str,  | str,  | The start of the range of episodes to link to the file. Append a type prefix to use another episode type. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

