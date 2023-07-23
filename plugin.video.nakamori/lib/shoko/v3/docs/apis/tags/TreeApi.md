<a id="__pageTop"></a>
# lib.shoko.v3.lib.shoko.v3.api.tags.tree_api.TreeApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**episode_episode_id_file_get**](#episode_episode_id_file_get) | **get** /Episode/{episodeID}/File | Get the Shoko.Server.API.v3.Models.Shoko.Files for the Shoko.Server.API.v3.Models.Shoko.Episode with the given episodeID.
[**filter_filter_id_filter_get**](#filter_filter_id_filter_get) | **get** /Filter/{filterID}/Filter | Get a list of all the sub-Shoko.Server.API.v3.Models.Shoko.Filter for the Shoko.Server.API.v3.Models.Shoko.Filter with the given filterID.
[**filter_filter_id_group_get**](#filter_filter_id_group_get) | **get** /Filter/{filterID}/Group | Get a paginated list of all the top-level Shoko.Server.API.v3.Models.Shoko.Groups for the Shoko.Server.API.v3.Models.Shoko.Filter with the given filterID.
[**filter_filter_id_group_group_id_group_get**](#filter_filter_id_group_group_id_group_get) | **get** /Filter/{filterID}/Group/{groupID}/Group | Get a list of all the sub-Shoko.Server.API.v3.Models.Shoko.Groups belonging to the Shoko.Server.API.v3.Models.Shoko.Group with the given groupID and which are present within the Shoko.Server.API.v3.Models.Shoko.Filter with the given filterID.
[**filter_filter_id_group_group_id_series_get**](#filter_filter_id_group_group_id_series_get) | **get** /Filter/{filterID}/Group/{groupID}/Series | Get a list of all the Shoko.Server.API.v3.Models.Shoko.Series for the Shoko.Server.API.v3.Models.Shoko.Group within the Shoko.Server.API.v3.Models.Shoko.Filter.
[**filter_filter_id_group_letters_get**](#filter_filter_id_group_letters_get) | **get** /Filter/{filterID}/Group/Letters | Get a dictionary with the count for each starting character in each of  the top-level group&#x27;s name with the filter for the given  filterID applied.
[**filter_filter_id_series_get**](#filter_filter_id_series_get) | **get** /Filter/{filterID}/Series | Get a paginated list of all the Shoko.Server.API.v3.Models.Shoko.Series within a Shoko.Server.API.v3.Models.Shoko.Filter.
[**group_group_id_group_get**](#group_group_id_group_get) | **get** /Group/{groupID}/Group | Get a list of sub-Shoko.Server.API.v3.Models.Shoko.Groups a the Shoko.Server.API.v3.Models.Shoko.Group.
[**group_group_id_main_series_get**](#group_group_id_main_series_get) | **get** /Group/{groupID}/MainSeries | Get the main Shoko.Server.API.v3.Models.Shoko.Series in a Shoko.Server.API.v3.Models.Shoko.Group.
[**group_group_id_series_get**](#group_group_id_series_get) | **get** /Group/{groupID}/Series | Get a list of Shoko.Server.API.v3.Models.Shoko.Series within a Shoko.Server.API.v3.Models.Shoko.Group.
[**import_folder_folder_id_file_get**](#import_folder_folder_id_file_get) | **get** /ImportFolder/{folderID}/File | Get all Shoko.Server.API.v3.Models.Shoko.Files in the Shoko.Server.API.v3.Models.Shoko.ImportFolder with the given folderID.
[**series_series_id_episode_get**](#series_series_id_episode_get) | **get** /Series/{seriesID}/Episode | Get the Shoko.Server.API.v3.Models.Shoko.Episodes for the Shoko.Server.API.v3.Models.Shoko.Series with seriesID.
[**series_series_id_file_get**](#series_series_id_file_get) | **get** /Series/{seriesID}/File | Get the Shoko.Server.API.v3.Models.Shoko.Files for the Shoko.Server.API.v3.Models.Shoko.Series with the given seriesID.
[**series_series_id_next_up_episode_get**](#series_series_id_next_up_episode_get) | **get** /Series/{seriesID}/NextUpEpisode | Get the next Shoko.Server.API.v3.Models.Shoko.Episode for the Shoko.Server.API.v3.Models.Shoko.Series with seriesID.

# **episode_episode_id_file_get**
<a id="episode_episode_id_file_get"></a>
> [ShokoFile] episode_episode_id_file_get(episode_id)

Get the Shoko.Server.API.v3.Models.Shoko.Files for the Shoko.Server.API.v3.Models.Shoko.Episode with the given episodeID.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import tree_api
from lib.shoko.v3.lib.shoko.v3.models.shoko_file import ShokoFile
from lib.shoko.v3.lib.shoko.v3.models.common_data_source import CommonDataSource
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = lib.shoko.v3.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Enter a context with an instance of the API client
with lib.shoko.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tree_api.TreeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'episodeID': 1,
    }
    query_params = {
    }
    try:
        # Get the Shoko.Server.API.v3.Models.Shoko.Files for the Shoko.Server.API.v3.Models.Shoko.Episode with the given episodeID.
        api_response = api_instance.episode_episode_id_file_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling TreeApi->episode_episode_id_file_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'episodeID': 1,
    }
    query_params = {
        'includeXRefs': False,
        'includeDataFrom': [
        CommonDataSource("None")
    ],
        'isManuallyLinked': True,
        'includeMediaInfo': False,
    }
    try:
        # Get the Shoko.Server.API.v3.Models.Shoko.Files for the Shoko.Server.API.v3.Models.Shoko.Episode with the given episodeID.
        api_response = api_instance.episode_episode_id_file_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling TreeApi->episode_episode_id_file_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
includeXRefs | IncludeXRefsSchema | | optional
includeDataFrom | IncludeDataFromSchema | | optional
isManuallyLinked | IsManuallyLinkedSchema | | optional
includeMediaInfo | IncludeMediaInfoSchema | | optional


# IncludeXRefsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# IncludeDataFromSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CommonDataSource**]({{complexTypePrefix}}CommonDataSource.md) | [**CommonDataSource**]({{complexTypePrefix}}CommonDataSource.md) | [**CommonDataSource**]({{complexTypePrefix}}CommonDataSource.md) |  | 

# IsManuallyLinkedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# IncludeMediaInfoSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
episodeID | EpisodeIDSchema | | 

# EpisodeIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#episode_episode_id_file_get.ApiResponseFor200) | Success

#### episode_episode_id_file_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShokoFile**]({{complexTypePrefix}}ShokoFile.md) | [**ShokoFile**]({{complexTypePrefix}}ShokoFile.md) | [**ShokoFile**]({{complexTypePrefix}}ShokoFile.md) |  | 

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShokoFile**]({{complexTypePrefix}}ShokoFile.md) | [**ShokoFile**]({{complexTypePrefix}}ShokoFile.md) | [**ShokoFile**]({{complexTypePrefix}}ShokoFile.md) |  | 

# SchemaFor200ResponseBodyTextJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShokoFile**]({{complexTypePrefix}}ShokoFile.md) | [**ShokoFile**]({{complexTypePrefix}}ShokoFile.md) | [**ShokoFile**]({{complexTypePrefix}}ShokoFile.md) |  | 

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **filter_filter_id_filter_get**
<a id="filter_filter_id_filter_get"></a>
> ListResultShokoFilter filter_filter_id_filter_get(filter_id)

Get a list of all the sub-Shoko.Server.API.v3.Models.Shoko.Filter for the Shoko.Server.API.v3.Models.Shoko.Filter with the given filterID.

The Shoko.Server.API.v3.Models.Shoko.Filter must have Shoko.Server.API.v3.Models.Shoko.Filter.IsDirectory set to true to use  this endpoint.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import tree_api
from lib.shoko.v3.lib.shoko.v3.models.list_result_shoko_filter import ListResultShokoFilter
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = lib.shoko.v3.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Enter a context with an instance of the API client
with lib.shoko.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tree_api.TreeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'filterID': 1,
    }
    query_params = {
    }
    try:
        # Get a list of all the sub-Shoko.Server.API.v3.Models.Shoko.Filter for the Shoko.Server.API.v3.Models.Shoko.Filter with the given filterID.
        api_response = api_instance.filter_filter_id_filter_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling TreeApi->filter_filter_id_filter_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'filterID': 1,
    }
    query_params = {
        'pageSize': 50,
        'page': 1,
        'showHidden': False,
    }
    try:
        # Get a list of all the sub-Shoko.Server.API.v3.Models.Shoko.Filter for the Shoko.Server.API.v3.Models.Shoko.Filter with the given filterID.
        api_response = api_instance.filter_filter_id_filter_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling TreeApi->filter_filter_id_filter_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pageSize | PageSizeSchema | | optional
page | PageSchema | | optional
showHidden | ShowHiddenSchema | | optional


# PageSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 50value must be a 32 bit integer

# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1value must be a 32 bit integer

# ShowHiddenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
filterID | FilterIDSchema | | 

# FilterIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#filter_filter_id_filter_get.ApiResponseFor200) | Success

#### filter_filter_id_filter_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ListResultShokoFilter**](../../models/ListResultShokoFilter.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ListResultShokoFilter**](../../models/ListResultShokoFilter.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ListResultShokoFilter**](../../models/ListResultShokoFilter.md) |  | 


### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **filter_filter_id_group_get**
<a id="filter_filter_id_group_get"></a>
> ListResultShokoGroup filter_filter_id_group_get(filter_id)

Get a paginated list of all the top-level Shoko.Server.API.v3.Models.Shoko.Groups for the Shoko.Server.API.v3.Models.Shoko.Filter with the given filterID.

The Shoko.Server.API.v3.Models.Shoko.Filter must have Shoko.Server.API.v3.Models.Shoko.Filter.IsDirectory set to false to use  this endpoint.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import tree_api
from lib.shoko.v3.lib.shoko.v3.models.list_result_shoko_group import ListResultShokoGroup
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = lib.shoko.v3.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Enter a context with an instance of the API client
with lib.shoko.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tree_api.TreeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'filterID': 1,
    }
    query_params = {
    }
    try:
        # Get a paginated list of all the top-level Shoko.Server.API.v3.Models.Shoko.Groups for the Shoko.Server.API.v3.Models.Shoko.Filter with the given filterID.
        api_response = api_instance.filter_filter_id_group_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling TreeApi->filter_filter_id_group_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'filterID': 1,
    }
    query_params = {
        'pageSize': 50,
        'page': 1,
        'includeEmpty': False,
        'randomImages': False,
        'orderByName': False,
    }
    try:
        # Get a paginated list of all the top-level Shoko.Server.API.v3.Models.Shoko.Groups for the Shoko.Server.API.v3.Models.Shoko.Filter with the given filterID.
        api_response = api_instance.filter_filter_id_group_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling TreeApi->filter_filter_id_group_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pageSize | PageSizeSchema | | optional
page | PageSchema | | optional
includeEmpty | IncludeEmptySchema | | optional
randomImages | RandomImagesSchema | | optional
orderByName | OrderByNameSchema | | optional


# PageSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 50value must be a 32 bit integer

# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1value must be a 32 bit integer

# IncludeEmptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# RandomImagesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# OrderByNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
filterID | FilterIDSchema | | 

# FilterIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#filter_filter_id_group_get.ApiResponseFor200) | Success

#### filter_filter_id_group_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ListResultShokoGroup**](../../models/ListResultShokoGroup.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ListResultShokoGroup**](../../models/ListResultShokoGroup.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ListResultShokoGroup**](../../models/ListResultShokoGroup.md) |  | 


### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **filter_filter_id_group_group_id_group_get**
<a id="filter_filter_id_group_group_id_group_get"></a>
> [ShokoGroup] filter_filter_id_group_group_id_group_get(filter_idgroup_id)

Get a list of all the sub-Shoko.Server.API.v3.Models.Shoko.Groups belonging to the Shoko.Server.API.v3.Models.Shoko.Group with the given groupID and which are present within the Shoko.Server.API.v3.Models.Shoko.Filter with the given filterID.

The Shoko.Server.API.v3.Models.Shoko.Filter must have Shoko.Server.API.v3.Models.Shoko.Filter.IsDirectory set to false to use  this endpoint.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import tree_api
from lib.shoko.v3.lib.shoko.v3.models.shoko_group import ShokoGroup
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = lib.shoko.v3.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Enter a context with an instance of the API client
with lib.shoko.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tree_api.TreeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'filterID': 1,
        'groupID': 1,
    }
    query_params = {
    }
    try:
        # Get a list of all the sub-Shoko.Server.API.v3.Models.Shoko.Groups belonging to the Shoko.Server.API.v3.Models.Shoko.Group with the given groupID and which are present within the Shoko.Server.API.v3.Models.Shoko.Filter with the given filterID.
        api_response = api_instance.filter_filter_id_group_group_id_group_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling TreeApi->filter_filter_id_group_group_id_group_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'filterID': 1,
        'groupID': 1,
    }
    query_params = {
        'randomImages': False,
        'includeEmpty': False,
    }
    try:
        # Get a list of all the sub-Shoko.Server.API.v3.Models.Shoko.Groups belonging to the Shoko.Server.API.v3.Models.Shoko.Group with the given groupID and which are present within the Shoko.Server.API.v3.Models.Shoko.Filter with the given filterID.
        api_response = api_instance.filter_filter_id_group_group_id_group_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling TreeApi->filter_filter_id_group_group_id_group_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
randomImages | RandomImagesSchema | | optional
includeEmpty | IncludeEmptySchema | | optional


# RandomImagesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# IncludeEmptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
filterID | FilterIDSchema | | 
groupID | GroupIDSchema | | 

# FilterIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# GroupIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#filter_filter_id_group_group_id_group_get.ApiResponseFor200) | Success

#### filter_filter_id_group_group_id_group_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShokoGroup**]({{complexTypePrefix}}ShokoGroup.md) | [**ShokoGroup**]({{complexTypePrefix}}ShokoGroup.md) | [**ShokoGroup**]({{complexTypePrefix}}ShokoGroup.md) |  | 

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShokoGroup**]({{complexTypePrefix}}ShokoGroup.md) | [**ShokoGroup**]({{complexTypePrefix}}ShokoGroup.md) | [**ShokoGroup**]({{complexTypePrefix}}ShokoGroup.md) |  | 

# SchemaFor200ResponseBodyTextJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShokoGroup**]({{complexTypePrefix}}ShokoGroup.md) | [**ShokoGroup**]({{complexTypePrefix}}ShokoGroup.md) | [**ShokoGroup**]({{complexTypePrefix}}ShokoGroup.md) |  | 

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **filter_filter_id_group_group_id_series_get**
<a id="filter_filter_id_group_group_id_series_get"></a>
> [ShokoSeries] filter_filter_id_group_group_id_series_get(filter_idgroup_id)

Get a list of all the Shoko.Server.API.v3.Models.Shoko.Series for the Shoko.Server.API.v3.Models.Shoko.Group within the Shoko.Server.API.v3.Models.Shoko.Filter.

 Pass a filterID of ```0``` to disable filter.  <br />  The Shoko.Server.API.v3.Models.Shoko.Filter must have Shoko.Server.API.v3.Models.Shoko.Filter.IsDirectory set to false to use  this endpoint.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import tree_api
from lib.shoko.v3.lib.shoko.v3.models.shoko_series import ShokoSeries
from lib.shoko.v3.lib.shoko.v3.models.common_data_source import CommonDataSource
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = lib.shoko.v3.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Enter a context with an instance of the API client
with lib.shoko.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tree_api.TreeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'filterID': 1,
        'groupID': 1,
    }
    query_params = {
    }
    try:
        # Get a list of all the Shoko.Server.API.v3.Models.Shoko.Series for the Shoko.Server.API.v3.Models.Shoko.Group within the Shoko.Server.API.v3.Models.Shoko.Filter.
        api_response = api_instance.filter_filter_id_group_group_id_series_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling TreeApi->filter_filter_id_group_group_id_series_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'filterID': 1,
        'groupID': 1,
    }
    query_params = {
        'recursive': False,
        'includeMissing': False,
        'randomImages': False,
        'includeDataFrom': [
        CommonDataSource("None")
    ],
    }
    try:
        # Get a list of all the Shoko.Server.API.v3.Models.Shoko.Series for the Shoko.Server.API.v3.Models.Shoko.Group within the Shoko.Server.API.v3.Models.Shoko.Filter.
        api_response = api_instance.filter_filter_id_group_group_id_series_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling TreeApi->filter_filter_id_group_group_id_series_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
recursive | RecursiveSchema | | optional
includeMissing | IncludeMissingSchema | | optional
randomImages | RandomImagesSchema | | optional
includeDataFrom | IncludeDataFromSchema | | optional


# RecursiveSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# IncludeMissingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# RandomImagesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# IncludeDataFromSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CommonDataSource**]({{complexTypePrefix}}CommonDataSource.md) | [**CommonDataSource**]({{complexTypePrefix}}CommonDataSource.md) | [**CommonDataSource**]({{complexTypePrefix}}CommonDataSource.md) |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
filterID | FilterIDSchema | | 
groupID | GroupIDSchema | | 

# FilterIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# GroupIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#filter_filter_id_group_group_id_series_get.ApiResponseFor200) | Success

#### filter_filter_id_group_group_id_series_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShokoSeries**]({{complexTypePrefix}}ShokoSeries.md) | [**ShokoSeries**]({{complexTypePrefix}}ShokoSeries.md) | [**ShokoSeries**]({{complexTypePrefix}}ShokoSeries.md) |  | 

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShokoSeries**]({{complexTypePrefix}}ShokoSeries.md) | [**ShokoSeries**]({{complexTypePrefix}}ShokoSeries.md) | [**ShokoSeries**]({{complexTypePrefix}}ShokoSeries.md) |  | 

# SchemaFor200ResponseBodyTextJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShokoSeries**]({{complexTypePrefix}}ShokoSeries.md) | [**ShokoSeries**]({{complexTypePrefix}}ShokoSeries.md) | [**ShokoSeries**]({{complexTypePrefix}}ShokoSeries.md) |  | 

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **filter_filter_id_group_letters_get**
<a id="filter_filter_id_group_letters_get"></a>
> {str: (int,)} filter_filter_id_group_letters_get(filter_id)

Get a dictionary with the count for each starting character in each of  the top-level group's name with the filter for the given  filterID applied.

The Shoko.Server.API.v3.Models.Shoko.Filter must have Shoko.Server.API.v3.Models.Shoko.Filter.IsDirectory set to false to use  this endpoint.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import tree_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = lib.shoko.v3.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Enter a context with an instance of the API client
with lib.shoko.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tree_api.TreeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'filterID': 1,
    }
    query_params = {
    }
    try:
        # Get a dictionary with the count for each starting character in each of  the top-level group's name with the filter for the given  filterID applied.
        api_response = api_instance.filter_filter_id_group_letters_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling TreeApi->filter_filter_id_group_letters_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'filterID': 1,
    }
    query_params = {
        'includeEmpty': False,
    }
    try:
        # Get a dictionary with the count for each starting character in each of  the top-level group's name with the filter for the given  filterID applied.
        api_response = api_instance.filter_filter_id_group_letters_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling TreeApi->filter_filter_id_group_letters_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
includeEmpty | IncludeEmptySchema | | optional


# IncludeEmptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
filterID | FilterIDSchema | | 

# FilterIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#filter_filter_id_group_letters_get.ApiResponseFor200) | Success

#### filter_filter_id_group_letters_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | decimal.Decimal, int,  | decimal.Decimal,  | any string name can be used but the value must be the correct type | [optional] value must be a 32 bit integer

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | decimal.Decimal, int,  | decimal.Decimal,  | any string name can be used but the value must be the correct type | [optional] value must be a 32 bit integer

# SchemaFor200ResponseBodyTextJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | decimal.Decimal, int,  | decimal.Decimal,  | any string name can be used but the value must be the correct type | [optional] value must be a 32 bit integer

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **filter_filter_id_series_get**
<a id="filter_filter_id_series_get"></a>
> ListResultShokoSeries filter_filter_id_series_get(filter_id)

Get a paginated list of all the Shoko.Server.API.v3.Models.Shoko.Series within a Shoko.Server.API.v3.Models.Shoko.Filter.

 Pass a filterID of ```0``` to disable filter.  <br />  The Shoko.Server.API.v3.Models.Shoko.Filter must have Shoko.Server.API.v3.Models.Shoko.Filter.IsDirectory set to false to use  this endpoint.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import tree_api
from lib.shoko.v3.lib.shoko.v3.models.list_result_shoko_series import ListResultShokoSeries
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = lib.shoko.v3.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Enter a context with an instance of the API client
with lib.shoko.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tree_api.TreeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'filterID': 1,
    }
    query_params = {
    }
    try:
        # Get a paginated list of all the Shoko.Server.API.v3.Models.Shoko.Series within a Shoko.Server.API.v3.Models.Shoko.Filter.
        api_response = api_instance.filter_filter_id_series_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling TreeApi->filter_filter_id_series_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'filterID': 1,
    }
    query_params = {
        'pageSize': 50,
        'page': 1,
        'randomImages': False,
        'includeMissing': False,
    }
    try:
        # Get a paginated list of all the Shoko.Server.API.v3.Models.Shoko.Series within a Shoko.Server.API.v3.Models.Shoko.Filter.
        api_response = api_instance.filter_filter_id_series_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling TreeApi->filter_filter_id_series_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pageSize | PageSizeSchema | | optional
page | PageSchema | | optional
randomImages | RandomImagesSchema | | optional
includeMissing | IncludeMissingSchema | | optional


# PageSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 50value must be a 32 bit integer

# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1value must be a 32 bit integer

# RandomImagesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# IncludeMissingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
filterID | FilterIDSchema | | 

# FilterIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#filter_filter_id_series_get.ApiResponseFor200) | Success

#### filter_filter_id_series_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ListResultShokoSeries**](../../models/ListResultShokoSeries.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ListResultShokoSeries**](../../models/ListResultShokoSeries.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ListResultShokoSeries**](../../models/ListResultShokoSeries.md) |  | 


### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **group_group_id_group_get**
<a id="group_group_id_group_get"></a>
> [ShokoGroup] group_group_id_group_get(group_id)

Get a list of sub-Shoko.Server.API.v3.Models.Shoko.Groups a the Shoko.Server.API.v3.Models.Shoko.Group.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import tree_api
from lib.shoko.v3.lib.shoko.v3.models.shoko_group import ShokoGroup
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = lib.shoko.v3.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Enter a context with an instance of the API client
with lib.shoko.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tree_api.TreeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupID': 1,
    }
    query_params = {
    }
    try:
        # Get a list of sub-Shoko.Server.API.v3.Models.Shoko.Groups a the Shoko.Server.API.v3.Models.Shoko.Group.
        api_response = api_instance.group_group_id_group_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling TreeApi->group_group_id_group_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupID': 1,
    }
    query_params = {
        'randomImages': False,
        'includeEmpty': False,
    }
    try:
        # Get a list of sub-Shoko.Server.API.v3.Models.Shoko.Groups a the Shoko.Server.API.v3.Models.Shoko.Group.
        api_response = api_instance.group_group_id_group_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling TreeApi->group_group_id_group_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
randomImages | RandomImagesSchema | | optional
includeEmpty | IncludeEmptySchema | | optional


# RandomImagesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# IncludeEmptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
groupID | GroupIDSchema | | 

# GroupIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#group_group_id_group_get.ApiResponseFor200) | Success

#### group_group_id_group_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShokoGroup**]({{complexTypePrefix}}ShokoGroup.md) | [**ShokoGroup**]({{complexTypePrefix}}ShokoGroup.md) | [**ShokoGroup**]({{complexTypePrefix}}ShokoGroup.md) |  | 

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShokoGroup**]({{complexTypePrefix}}ShokoGroup.md) | [**ShokoGroup**]({{complexTypePrefix}}ShokoGroup.md) | [**ShokoGroup**]({{complexTypePrefix}}ShokoGroup.md) |  | 

# SchemaFor200ResponseBodyTextJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShokoGroup**]({{complexTypePrefix}}ShokoGroup.md) | [**ShokoGroup**]({{complexTypePrefix}}ShokoGroup.md) | [**ShokoGroup**]({{complexTypePrefix}}ShokoGroup.md) |  | 

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **group_group_id_main_series_get**
<a id="group_group_id_main_series_get"></a>
> ShokoSeries group_group_id_main_series_get(group_id)

Get the main Shoko.Server.API.v3.Models.Shoko.Series in a Shoko.Server.API.v3.Models.Shoko.Group.

It will return 1) the default series or 2) the earliest running  series if the group contains a series, or nothing if the group is  empty.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import tree_api
from lib.shoko.v3.lib.shoko.v3.models.shoko_series import ShokoSeries
from lib.shoko.v3.lib.shoko.v3.models.common_data_source import CommonDataSource
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = lib.shoko.v3.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Enter a context with an instance of the API client
with lib.shoko.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tree_api.TreeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupID': 1,
    }
    query_params = {
    }
    try:
        # Get the main Shoko.Server.API.v3.Models.Shoko.Series in a Shoko.Server.API.v3.Models.Shoko.Group.
        api_response = api_instance.group_group_id_main_series_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling TreeApi->group_group_id_main_series_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupID': 1,
    }
    query_params = {
        'randomImages': False,
        'includeDataFrom': [
        CommonDataSource("None")
    ],
    }
    try:
        # Get the main Shoko.Server.API.v3.Models.Shoko.Series in a Shoko.Server.API.v3.Models.Shoko.Group.
        api_response = api_instance.group_group_id_main_series_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling TreeApi->group_group_id_main_series_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
randomImages | RandomImagesSchema | | optional
includeDataFrom | IncludeDataFromSchema | | optional


# RandomImagesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# IncludeDataFromSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CommonDataSource**]({{complexTypePrefix}}CommonDataSource.md) | [**CommonDataSource**]({{complexTypePrefix}}CommonDataSource.md) | [**CommonDataSource**]({{complexTypePrefix}}CommonDataSource.md) |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
groupID | GroupIDSchema | | 

# GroupIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#group_group_id_main_series_get.ApiResponseFor200) | Success

#### group_group_id_main_series_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoSeries**](../../models/ShokoSeries.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoSeries**](../../models/ShokoSeries.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoSeries**](../../models/ShokoSeries.md) |  | 


### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **group_group_id_series_get**
<a id="group_group_id_series_get"></a>
> [ShokoSeries] group_group_id_series_get(group_id)

Get a list of Shoko.Server.API.v3.Models.Shoko.Series within a Shoko.Server.API.v3.Models.Shoko.Group.

It will return all the Shoko.Server.API.v3.Models.Shoko.Series within the group and all sub-groups if  recursive is set to ```true```.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import tree_api
from lib.shoko.v3.lib.shoko.v3.models.shoko_series import ShokoSeries
from lib.shoko.v3.lib.shoko.v3.models.common_data_source import CommonDataSource
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = lib.shoko.v3.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Enter a context with an instance of the API client
with lib.shoko.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tree_api.TreeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupID': 1,
    }
    query_params = {
    }
    try:
        # Get a list of Shoko.Server.API.v3.Models.Shoko.Series within a Shoko.Server.API.v3.Models.Shoko.Group.
        api_response = api_instance.group_group_id_series_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling TreeApi->group_group_id_series_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupID': 1,
    }
    query_params = {
        'recursive': False,
        'includeMissing': False,
        'randomImages': False,
        'includeDataFrom': [
        CommonDataSource("None")
    ],
    }
    try:
        # Get a list of Shoko.Server.API.v3.Models.Shoko.Series within a Shoko.Server.API.v3.Models.Shoko.Group.
        api_response = api_instance.group_group_id_series_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling TreeApi->group_group_id_series_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
recursive | RecursiveSchema | | optional
includeMissing | IncludeMissingSchema | | optional
randomImages | RandomImagesSchema | | optional
includeDataFrom | IncludeDataFromSchema | | optional


# RecursiveSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# IncludeMissingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# RandomImagesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# IncludeDataFromSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CommonDataSource**]({{complexTypePrefix}}CommonDataSource.md) | [**CommonDataSource**]({{complexTypePrefix}}CommonDataSource.md) | [**CommonDataSource**]({{complexTypePrefix}}CommonDataSource.md) |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
groupID | GroupIDSchema | | 

# GroupIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#group_group_id_series_get.ApiResponseFor200) | Success

#### group_group_id_series_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShokoSeries**]({{complexTypePrefix}}ShokoSeries.md) | [**ShokoSeries**]({{complexTypePrefix}}ShokoSeries.md) | [**ShokoSeries**]({{complexTypePrefix}}ShokoSeries.md) |  | 

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShokoSeries**]({{complexTypePrefix}}ShokoSeries.md) | [**ShokoSeries**]({{complexTypePrefix}}ShokoSeries.md) | [**ShokoSeries**]({{complexTypePrefix}}ShokoSeries.md) |  | 

# SchemaFor200ResponseBodyTextJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShokoSeries**]({{complexTypePrefix}}ShokoSeries.md) | [**ShokoSeries**]({{complexTypePrefix}}ShokoSeries.md) | [**ShokoSeries**]({{complexTypePrefix}}ShokoSeries.md) |  | 

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **import_folder_folder_id_file_get**
<a id="import_folder_folder_id_file_get"></a>
> ListResultShokoFile import_folder_folder_id_file_get(folder_id)

Get all Shoko.Server.API.v3.Models.Shoko.Files in the Shoko.Server.API.v3.Models.Shoko.ImportFolder with the given folderID.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import tree_api
from lib.shoko.v3.lib.shoko.v3.models.list_result_shoko_file import ListResultShokoFile
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = lib.shoko.v3.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Enter a context with an instance of the API client
with lib.shoko.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tree_api.TreeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'folderID': 1,
    }
    query_params = {
    }
    try:
        # Get all Shoko.Server.API.v3.Models.Shoko.Files in the Shoko.Server.API.v3.Models.Shoko.ImportFolder with the given folderID.
        api_response = api_instance.import_folder_folder_id_file_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling TreeApi->import_folder_folder_id_file_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'folderID': 1,
    }
    query_params = {
        'pageSize': 50,
        'page': 1,
        'includeXRefs': False,
    }
    try:
        # Get all Shoko.Server.API.v3.Models.Shoko.Files in the Shoko.Server.API.v3.Models.Shoko.ImportFolder with the given folderID.
        api_response = api_instance.import_folder_folder_id_file_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling TreeApi->import_folder_folder_id_file_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pageSize | PageSizeSchema | | optional
page | PageSchema | | optional
includeXRefs | IncludeXRefsSchema | | optional


# PageSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 50value must be a 32 bit integer

# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1value must be a 32 bit integer

# IncludeXRefsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
folderID | FolderIDSchema | | 

# FolderIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#import_folder_folder_id_file_get.ApiResponseFor200) | Success

#### import_folder_folder_id_file_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ListResultShokoFile**](../../models/ListResultShokoFile.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ListResultShokoFile**](../../models/ListResultShokoFile.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ListResultShokoFile**](../../models/ListResultShokoFile.md) |  | 


### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **series_series_id_episode_get**
<a id="series_series_id_episode_get"></a>
> ListResultShokoEpisode series_series_id_episode_get(series_id)

Get the Shoko.Server.API.v3.Models.Shoko.Episodes for the Shoko.Server.API.v3.Models.Shoko.Series with seriesID.

Shoko.Server.API.v3.Models.Shoko.Filter or Shoko.Server.API.v3.Models.Shoko.Group is irrelevant at this level.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import tree_api
from lib.shoko.v3.lib.shoko.v3.models.list_result_shoko_episode import ListResultShokoEpisode
from lib.shoko.v3.lib.shoko.v3.models.common_include_only_filter import CommonIncludeOnlyFilter
from lib.shoko.v3.lib.shoko.v3.models.common_data_source import CommonDataSource
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = lib.shoko.v3.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Enter a context with an instance of the API client
with lib.shoko.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tree_api.TreeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'seriesID': 1,
    }
    query_params = {
    }
    try:
        # Get the Shoko.Server.API.v3.Models.Shoko.Episodes for the Shoko.Server.API.v3.Models.Shoko.Series with seriesID.
        api_response = api_instance.series_series_id_episode_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling TreeApi->series_series_id_episode_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'seriesID': 1,
    }
    query_params = {
        'pageSize': 20,
        'page': 1,
        'includeMissing': CommonIncludeOnlyFilter("false"),
        'includeHidden': CommonIncludeOnlyFilter("false"),
        'includeDataFrom': [
        CommonDataSource("None")
    ],
        'includeWatched': CommonIncludeOnlyFilter("false"),
        'type': [
        "type_example"
    ],
        'search': "search_example",
        'fuzzy': True,
    }
    try:
        # Get the Shoko.Server.API.v3.Models.Shoko.Episodes for the Shoko.Server.API.v3.Models.Shoko.Series with seriesID.
        api_response = api_instance.series_series_id_episode_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling TreeApi->series_series_id_episode_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pageSize | PageSizeSchema | | optional
page | PageSchema | | optional
includeMissing | IncludeMissingSchema | | optional
includeHidden | IncludeHiddenSchema | | optional
includeDataFrom | IncludeDataFromSchema | | optional
includeWatched | IncludeWatchedSchema | | optional
type | TypeSchema | | optional
search | SearchSchema | | optional
fuzzy | FuzzySchema | | optional


# PageSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 20value must be a 32 bit integer

# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1value must be a 32 bit integer

# IncludeMissingSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**CommonIncludeOnlyFilter**](../../models/CommonIncludeOnlyFilter.md) |  | 


# IncludeHiddenSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**CommonIncludeOnlyFilter**](../../models/CommonIncludeOnlyFilter.md) |  | 


# IncludeDataFromSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CommonDataSource**]({{complexTypePrefix}}CommonDataSource.md) | [**CommonDataSource**]({{complexTypePrefix}}CommonDataSource.md) | [**CommonDataSource**]({{complexTypePrefix}}CommonDataSource.md) |  | 

# IncludeWatchedSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**CommonIncludeOnlyFilter**](../../models/CommonIncludeOnlyFilter.md) |  | 


# TypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# SearchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FuzzySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of True

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
seriesID | SeriesIDSchema | | 

# SeriesIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#series_series_id_episode_get.ApiResponseFor200) | Success

#### series_series_id_episode_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ListResultShokoEpisode**](../../models/ListResultShokoEpisode.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ListResultShokoEpisode**](../../models/ListResultShokoEpisode.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ListResultShokoEpisode**](../../models/ListResultShokoEpisode.md) |  | 


### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **series_series_id_file_get**
<a id="series_series_id_file_get"></a>
> [ShokoFile] series_series_id_file_get(series_id)

Get the Shoko.Server.API.v3.Models.Shoko.Files for the Shoko.Server.API.v3.Models.Shoko.Series with the given seriesID.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import tree_api
from lib.shoko.v3.lib.shoko.v3.models.shoko_file import ShokoFile
from lib.shoko.v3.lib.shoko.v3.models.common_data_source import CommonDataSource
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = lib.shoko.v3.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Enter a context with an instance of the API client
with lib.shoko.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tree_api.TreeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'seriesID': 1,
    }
    query_params = {
    }
    try:
        # Get the Shoko.Server.API.v3.Models.Shoko.Files for the Shoko.Server.API.v3.Models.Shoko.Series with the given seriesID.
        api_response = api_instance.series_series_id_file_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling TreeApi->series_series_id_file_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'seriesID': 1,
    }
    query_params = {
        'includeXRefs': False,
        'includeDataFrom': [
        CommonDataSource("None")
    ],
        'isManuallyLinked': True,
        'includeMediaInfo': False,
    }
    try:
        # Get the Shoko.Server.API.v3.Models.Shoko.Files for the Shoko.Server.API.v3.Models.Shoko.Series with the given seriesID.
        api_response = api_instance.series_series_id_file_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling TreeApi->series_series_id_file_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
includeXRefs | IncludeXRefsSchema | | optional
includeDataFrom | IncludeDataFromSchema | | optional
isManuallyLinked | IsManuallyLinkedSchema | | optional
includeMediaInfo | IncludeMediaInfoSchema | | optional


# IncludeXRefsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# IncludeDataFromSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CommonDataSource**]({{complexTypePrefix}}CommonDataSource.md) | [**CommonDataSource**]({{complexTypePrefix}}CommonDataSource.md) | [**CommonDataSource**]({{complexTypePrefix}}CommonDataSource.md) |  | 

# IsManuallyLinkedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# IncludeMediaInfoSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
seriesID | SeriesIDSchema | | 

# SeriesIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#series_series_id_file_get.ApiResponseFor200) | Success

#### series_series_id_file_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShokoFile**]({{complexTypePrefix}}ShokoFile.md) | [**ShokoFile**]({{complexTypePrefix}}ShokoFile.md) | [**ShokoFile**]({{complexTypePrefix}}ShokoFile.md) |  | 

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShokoFile**]({{complexTypePrefix}}ShokoFile.md) | [**ShokoFile**]({{complexTypePrefix}}ShokoFile.md) | [**ShokoFile**]({{complexTypePrefix}}ShokoFile.md) |  | 

# SchemaFor200ResponseBodyTextJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShokoFile**]({{complexTypePrefix}}ShokoFile.md) | [**ShokoFile**]({{complexTypePrefix}}ShokoFile.md) | [**ShokoFile**]({{complexTypePrefix}}ShokoFile.md) |  | 

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **series_series_id_next_up_episode_get**
<a id="series_series_id_next_up_episode_get"></a>
> ShokoEpisode series_series_id_next_up_episode_get(series_id)

Get the next Shoko.Server.API.v3.Models.Shoko.Episode for the Shoko.Server.API.v3.Models.Shoko.Series with seriesID.

Shoko.Server.API.v3.Models.Shoko.Filter or Shoko.Server.API.v3.Models.Shoko.Group is irrelevant at this level.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import tree_api
from lib.shoko.v3.lib.shoko.v3.models.shoko_episode import ShokoEpisode
from lib.shoko.v3.lib.shoko.v3.models.common_data_source import CommonDataSource
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = lib.shoko.v3.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Enter a context with an instance of the API client
with lib.shoko.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tree_api.TreeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'seriesID': 1,
    }
    query_params = {
    }
    try:
        # Get the next Shoko.Server.API.v3.Models.Shoko.Episode for the Shoko.Server.API.v3.Models.Shoko.Series with seriesID.
        api_response = api_instance.series_series_id_next_up_episode_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling TreeApi->series_series_id_next_up_episode_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'seriesID': 1,
    }
    query_params = {
        'onlyUnwatched': True,
        'includeSpecials': True,
        'includeMissing': True,
        'includeHidden': False,
        'includeRewatching': False,
        'includeDataFrom': [
        CommonDataSource("None")
    ],
    }
    try:
        # Get the next Shoko.Server.API.v3.Models.Shoko.Episode for the Shoko.Server.API.v3.Models.Shoko.Series with seriesID.
        api_response = api_instance.series_series_id_next_up_episode_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling TreeApi->series_series_id_next_up_episode_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
onlyUnwatched | OnlyUnwatchedSchema | | optional
includeSpecials | IncludeSpecialsSchema | | optional
includeMissing | IncludeMissingSchema | | optional
includeHidden | IncludeHiddenSchema | | optional
includeRewatching | IncludeRewatchingSchema | | optional
includeDataFrom | IncludeDataFromSchema | | optional


# OnlyUnwatchedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of True

# IncludeSpecialsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of True

# IncludeMissingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of True

# IncludeHiddenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# IncludeRewatchingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# IncludeDataFromSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CommonDataSource**]({{complexTypePrefix}}CommonDataSource.md) | [**CommonDataSource**]({{complexTypePrefix}}CommonDataSource.md) | [**CommonDataSource**]({{complexTypePrefix}}CommonDataSource.md) |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
seriesID | SeriesIDSchema | | 

# SeriesIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#series_series_id_next_up_episode_get.ApiResponseFor200) | Success

#### series_series_id_next_up_episode_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoEpisode**](../../models/ShokoEpisode.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoEpisode**](../../models/ShokoEpisode.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoEpisode**](../../models/ShokoEpisode.md) |  | 


### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

