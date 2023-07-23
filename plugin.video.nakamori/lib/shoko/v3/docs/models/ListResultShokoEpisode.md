# lib.shoko.v3.lib.shoko.v3.models.list_result_shoko_episode.ListResultShokoEpisode

A list with the total count of <typeparamref name=\"T\" /> entries that  match the filter and a sliced or the full list of <typeparamref name=\"T\" />  entries.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A list with the total count of &lt;typeparamref name&#x3D;\&quot;T\&quot; /&gt; entries that  match the filter and a sliced or the full list of &lt;typeparamref name&#x3D;\&quot;T\&quot; /&gt;  entries. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Total** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of &lt;typeparamref name&#x3D;\&quot;T\&quot; /&gt; entries that matched the  applied filter. | [optional] value must be a 32 bit integer
**[List](#List)** | list, tuple, None,  | tuple, NoneClass,  | A sliced page or the whole list of &lt;typeparamref name&#x3D;\&quot;T\&quot; /&gt; entries. | [optional] 

# List

A sliced page or the whole list of <typeparamref name=\"T\" /> entries.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | A sliced page or the whole list of &lt;typeparamref name&#x3D;\&quot;T\&quot; /&gt; entries. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShokoEpisode**](ShokoEpisode.md) | [**ShokoEpisode**](ShokoEpisode.md) | [**ShokoEpisode**](ShokoEpisode.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

