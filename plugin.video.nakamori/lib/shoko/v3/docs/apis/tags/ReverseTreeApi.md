<a id="__pageTop"></a>
# lib.shoko.v3.lib.shoko.v3.api.tags.reverse_tree_api.ReverseTreeApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**episode_episode_id_series_get**](#episode_episode_id_series_get) | **get** /Episode/{episodeID}/Series | Get the Shoko.Server.API.v3.Models.Shoko.Series for the Shoko.Server.API.v3.Models.Shoko.Episode with the given episodeID.
[**file_file_id_episode_get**](#file_file_id_episode_get) | **get** /File/{fileID}/Episode | Get the Shoko.Server.API.v3.Models.Shoko.Episodes for the Shoko.Server.API.v3.Models.Shoko.File with the given fileID.
[**filter_filter_id_parent_get**](#filter_filter_id_parent_get) | **get** /Filter/{filterID}/Parent | Get the parent Shoko.Server.API.v3.Models.Shoko.Filter for the Shoko.Server.API.v3.Models.Shoko.Filter with the given filterID.
[**group_group_id_parent_get**](#group_group_id_parent_get) | **get** /Group/{groupID}/Parent | Get the parent Shoko.Server.API.v3.Models.Shoko.Group for the Shoko.Server.API.v3.Models.Shoko.Group with the given groupID.
[**series_series_id_group_get**](#series_series_id_group_get) | **get** /Series/{seriesID}/Group | Get the Shoko.Server.API.v3.Models.Shoko.Group for the Shoko.Server.API.v3.Models.Shoko.Series with the given seriesID.

# **episode_episode_id_series_get**
<a id="episode_episode_id_series_get"></a>
> ShokoSeries episode_episode_id_series_get(episode_id)

Get the Shoko.Server.API.v3.Models.Shoko.Series for the Shoko.Server.API.v3.Models.Shoko.Episode with the given episodeID.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import reverse_tree_api
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
    api_instance = reverse_tree_api.ReverseTreeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'episodeID': 1,
    }
    query_params = {
    }
    try:
        # Get the Shoko.Server.API.v3.Models.Shoko.Series for the Shoko.Server.API.v3.Models.Shoko.Episode with the given episodeID.
        api_response = api_instance.episode_episode_id_series_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ReverseTreeApi->episode_episode_id_series_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'episodeID': 1,
    }
    query_params = {
        'randomImages': False,
        'includeDataFrom': [
        CommonDataSource("None")
    ],
    }
    try:
        # Get the Shoko.Server.API.v3.Models.Shoko.Series for the Shoko.Server.API.v3.Models.Shoko.Episode with the given episodeID.
        api_response = api_instance.episode_episode_id_series_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ReverseTreeApi->episode_episode_id_series_get: %s\n" % e)
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
200 | [ApiResponseFor200](#episode_episode_id_series_get.ApiResponseFor200) | Success

#### episode_episode_id_series_get.ApiResponseFor200
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

# **file_file_id_episode_get**
<a id="file_file_id_episode_get"></a>
> [ShokoEpisode] file_file_id_episode_get(file_id)

Get the Shoko.Server.API.v3.Models.Shoko.Episodes for the Shoko.Server.API.v3.Models.Shoko.File with the given fileID.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import reverse_tree_api
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
    api_instance = reverse_tree_api.ReverseTreeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'fileID': 1,
    }
    query_params = {
    }
    try:
        # Get the Shoko.Server.API.v3.Models.Shoko.Episodes for the Shoko.Server.API.v3.Models.Shoko.File with the given fileID.
        api_response = api_instance.file_file_id_episode_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ReverseTreeApi->file_file_id_episode_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'fileID': 1,
    }
    query_params = {
        'includeDataFrom': [
        CommonDataSource("None")
    ],
    }
    try:
        # Get the Shoko.Server.API.v3.Models.Shoko.Episodes for the Shoko.Server.API.v3.Models.Shoko.File with the given fileID.
        api_response = api_instance.file_file_id_episode_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ReverseTreeApi->file_file_id_episode_get: %s\n" % e)
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
includeDataFrom | IncludeDataFromSchema | | optional


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
fileID | FileIDSchema | | 

# FileIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#file_file_id_episode_get.ApiResponseFor200) | Success

#### file_file_id_episode_get.ApiResponseFor200
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
[**ShokoEpisode**]({{complexTypePrefix}}ShokoEpisode.md) | [**ShokoEpisode**]({{complexTypePrefix}}ShokoEpisode.md) | [**ShokoEpisode**]({{complexTypePrefix}}ShokoEpisode.md) |  | 

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShokoEpisode**]({{complexTypePrefix}}ShokoEpisode.md) | [**ShokoEpisode**]({{complexTypePrefix}}ShokoEpisode.md) | [**ShokoEpisode**]({{complexTypePrefix}}ShokoEpisode.md) |  | 

# SchemaFor200ResponseBodyTextJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShokoEpisode**]({{complexTypePrefix}}ShokoEpisode.md) | [**ShokoEpisode**]({{complexTypePrefix}}ShokoEpisode.md) | [**ShokoEpisode**]({{complexTypePrefix}}ShokoEpisode.md) |  | 

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **filter_filter_id_parent_get**
<a id="filter_filter_id_parent_get"></a>
> ShokoFilter filter_filter_id_parent_get(filter_id)

Get the parent Shoko.Server.API.v3.Models.Shoko.Filter for the Shoko.Server.API.v3.Models.Shoko.Filter with the given filterID.

This endpoint can be used to get the direct Shoko.Server.API.v3.Models.Shoko.Filter parent to a Shoko.Server.API.v3.Models.Shoko.Filter (in case  it's within a sub-Filter) or to always get the top-level  Shoko.Server.API.v3.Models.Shoko.Filter regardless if  topLevel is set to ```true```.    Trying to get the parent of a top-level Shoko.Server.API.v3.Models.Shoko.Filter is an user error and will throw a complaint.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import reverse_tree_api
from lib.shoko.v3.lib.shoko.v3.models.shoko_filter import ShokoFilter
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
    api_instance = reverse_tree_api.ReverseTreeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'filterID': 1,
    }
    query_params = {
    }
    try:
        # Get the parent Shoko.Server.API.v3.Models.Shoko.Filter for the Shoko.Server.API.v3.Models.Shoko.Filter with the given filterID.
        api_response = api_instance.filter_filter_id_parent_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ReverseTreeApi->filter_filter_id_parent_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'filterID': 1,
    }
    query_params = {
        'topLevel': False,
    }
    try:
        # Get the parent Shoko.Server.API.v3.Models.Shoko.Filter for the Shoko.Server.API.v3.Models.Shoko.Filter with the given filterID.
        api_response = api_instance.filter_filter_id_parent_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ReverseTreeApi->filter_filter_id_parent_get: %s\n" % e)
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
topLevel | TopLevelSchema | | optional


# TopLevelSchema

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
200 | [ApiResponseFor200](#filter_filter_id_parent_get.ApiResponseFor200) | Success

#### filter_filter_id_parent_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoFilter**](../../models/ShokoFilter.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoFilter**](../../models/ShokoFilter.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoFilter**](../../models/ShokoFilter.md) |  | 


### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **group_group_id_parent_get**
<a id="group_group_id_parent_get"></a>
> ShokoGroup group_group_id_parent_get(group_id)

Get the parent Shoko.Server.API.v3.Models.Shoko.Group for the Shoko.Server.API.v3.Models.Shoko.Group with the given groupID.

This endpoint can be used to get the direct Shoko.Server.API.v3.Models.Shoko.Group parent to a Shoko.Server.API.v3.Models.Shoko.Group (in case  it's within a sub-group) or to always get the top-level  Shoko.Server.API.v3.Models.Shoko.Group regardless if  topLevel is set to ```true```.    Trying to get the parent of a top-level Shoko.Server.API.v3.Models.Shoko.Group is an user error and will throw a complaint.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import reverse_tree_api
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
    api_instance = reverse_tree_api.ReverseTreeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupID': 1,
    }
    query_params = {
    }
    try:
        # Get the parent Shoko.Server.API.v3.Models.Shoko.Group for the Shoko.Server.API.v3.Models.Shoko.Group with the given groupID.
        api_response = api_instance.group_group_id_parent_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ReverseTreeApi->group_group_id_parent_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupID': 1,
    }
    query_params = {
        'topLevel': False,
    }
    try:
        # Get the parent Shoko.Server.API.v3.Models.Shoko.Group for the Shoko.Server.API.v3.Models.Shoko.Group with the given groupID.
        api_response = api_instance.group_group_id_parent_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ReverseTreeApi->group_group_id_parent_get: %s\n" % e)
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
topLevel | TopLevelSchema | | optional


# TopLevelSchema

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
200 | [ApiResponseFor200](#group_group_id_parent_get.ApiResponseFor200) | Success

#### group_group_id_parent_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoGroup**](../../models/ShokoGroup.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoGroup**](../../models/ShokoGroup.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoGroup**](../../models/ShokoGroup.md) |  | 


### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **series_series_id_group_get**
<a id="series_series_id_group_get"></a>
> ShokoGroup series_series_id_group_get(series_id)

Get the Shoko.Server.API.v3.Models.Shoko.Group for the Shoko.Server.API.v3.Models.Shoko.Series with the given seriesID.

This endpoint can be used to get the direct Shoko.Server.API.v3.Models.Shoko.Group parent to a Shoko.Server.API.v3.Models.Shoko.Series (in case  it's within a sub-group) or to always get the top-level  Shoko.Server.API.v3.Models.Shoko.Group regardless if  topLevel is set to ```true```.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import reverse_tree_api
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
    api_instance = reverse_tree_api.ReverseTreeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'seriesID': 1,
    }
    query_params = {
    }
    try:
        # Get the Shoko.Server.API.v3.Models.Shoko.Group for the Shoko.Server.API.v3.Models.Shoko.Series with the given seriesID.
        api_response = api_instance.series_series_id_group_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ReverseTreeApi->series_series_id_group_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'seriesID': 1,
    }
    query_params = {
        'topLevel': False,
    }
    try:
        # Get the Shoko.Server.API.v3.Models.Shoko.Group for the Shoko.Server.API.v3.Models.Shoko.Series with the given seriesID.
        api_response = api_instance.series_series_id_group_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ReverseTreeApi->series_series_id_group_get: %s\n" % e)
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
topLevel | TopLevelSchema | | optional


# TopLevelSchema

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
200 | [ApiResponseFor200](#series_series_id_group_get.ApiResponseFor200) | Success

#### series_series_id_group_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoGroup**](../../models/ShokoGroup.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoGroup**](../../models/ShokoGroup.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoGroup**](../../models/ShokoGroup.md) |  | 


### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

