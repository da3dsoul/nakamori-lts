<a id="__pageTop"></a>
# lib.shoko.v3.lib.shoko.v3.api.tags.episode_api.EpisodeApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**episode_ani_db_anidb_episode_id_episode_get**](#episode_ani_db_anidb_episode_id_episode_get) | **get** /Episode/AniDB/{anidbEpisodeID}/Episode | Get the Shoko.Server.API.v3.Models.Shoko.Episode entry for the given anidbEpisodeID, if any.
[**episode_ani_db_anidb_episode_id_get**](#episode_ani_db_anidb_episode_id_get) | **get** /Episode/AniDB/{anidbEpisodeID} | Get the Shoko.Server.API.v3.Models.Shoko.Episode.AniDB entry for the given anidbEpisodeID.
[**episode_ani_db_get**](#episode_ani_db_get) | **get** /Episode/AniDB | Get all Shoko.Server.API.v3.Models.Shoko.Episode.AniDBs. Admins only.
[**episode_episode_id_ani_db_get**](#episode_episode_id_ani_db_get) | **get** /Episode/{episodeID}/AniDB | Get the Shoko.Server.API.v3.Models.Shoko.Episode.AniDB entry for the given episodeID.
[**episode_episode_id_get**](#episode_episode_id_get) | **get** /Episode/{episodeID} | Get the Shoko.Server.API.v3.Models.Shoko.Episode entry for the given episodeID.
[**episode_episode_id_set_hidden_post**](#episode_episode_id_set_hidden_post) | **post** /Episode/{episodeID}/SetHidden | Set or unset the episode hidden status by the given episodeID.
[**episode_episode_id_vote_post**](#episode_episode_id_vote_post) | **post** /Episode/{episodeID}/Vote | Add a permanent user-submitted rating for the episode.
[**episode_episode_id_watched_watched_post**](#episode_episode_id_watched_watched_post) | **post** /Episode/{episodeID}/Watched/{watched} | Set the watched status on an episode
[**episode_episode_idtv_db_get**](#episode_episode_idtv_db_get) | **get** /Episode/{episodeID}/TvDB | Get the TvDB details for episode with Shoko ID
[**episode_get**](#episode_get) | **get** /Episode | Get all Shoko.Server.API.v3.Models.Shoko.Episodes for the given filter.
[**episode_tv_db_get**](#episode_tv_db_get) | **get** /Episode/TvDB | Get all Shoko.Server.API.v3.Models.Shoko.Episode.TvDBs. Admins only.
[**episode_with_multiple_files_get**](#episode_with_multiple_files_get) | **get** /Episode/WithMultipleFiles | Get episodes with multiple files attached.
[**episode_with_no_files_get**](#episode_with_no_files_get) | **get** /Episode/WithNoFiles | Get all episodes with no files.

# **episode_ani_db_anidb_episode_id_episode_get**
<a id="episode_ani_db_anidb_episode_id_episode_get"></a>
> ShokoEpisode episode_ani_db_anidb_episode_id_episode_get(anidb_episode_id)

Get the Shoko.Server.API.v3.Models.Shoko.Episode entry for the given anidbEpisodeID, if any.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import episode_api
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
    api_instance = episode_api.EpisodeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'anidbEpisodeID': 1,
    }
    query_params = {
    }
    try:
        # Get the Shoko.Server.API.v3.Models.Shoko.Episode entry for the given anidbEpisodeID, if any.
        api_response = api_instance.episode_ani_db_anidb_episode_id_episode_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling EpisodeApi->episode_ani_db_anidb_episode_id_episode_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'anidbEpisodeID': 1,
    }
    query_params = {
        'includeDataFrom': [
        CommonDataSource("None")
    ],
    }
    try:
        # Get the Shoko.Server.API.v3.Models.Shoko.Episode entry for the given anidbEpisodeID, if any.
        api_response = api_instance.episode_ani_db_anidb_episode_id_episode_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling EpisodeApi->episode_ani_db_anidb_episode_id_episode_get: %s\n" % e)
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
anidbEpisodeID | AnidbEpisodeIDSchema | | 

# AnidbEpisodeIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#episode_ani_db_anidb_episode_id_episode_get.ApiResponseFor200) | Success

#### episode_ani_db_anidb_episode_id_episode_get.ApiResponseFor200
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

# **episode_ani_db_anidb_episode_id_get**
<a id="episode_ani_db_anidb_episode_id_get"></a>
> EpisodeAniDB episode_ani_db_anidb_episode_id_get(anidb_episode_id)

Get the Shoko.Server.API.v3.Models.Shoko.Episode.AniDB entry for the given anidbEpisodeID.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import episode_api
from lib.shoko.v3.lib.shoko.v3.models.episode_ani_db import EpisodeAniDB
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
    api_instance = episode_api.EpisodeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'anidbEpisodeID': 1,
    }
    try:
        # Get the Shoko.Server.API.v3.Models.Shoko.Episode.AniDB entry for the given anidbEpisodeID.
        api_response = api_instance.episode_ani_db_anidb_episode_id_get(
            path_params=path_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling EpisodeApi->episode_ani_db_anidb_episode_id_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
anidbEpisodeID | AnidbEpisodeIDSchema | | 

# AnidbEpisodeIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#episode_ani_db_anidb_episode_id_get.ApiResponseFor200) | Success

#### episode_ani_db_anidb_episode_id_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**EpisodeAniDB**](../../models/EpisodeAniDB.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EpisodeAniDB**](../../models/EpisodeAniDB.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EpisodeAniDB**](../../models/EpisodeAniDB.md) |  | 


### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **episode_ani_db_get**
<a id="episode_ani_db_get"></a>
> ListResultEpisodeAniDB episode_ani_db_get()

Get all Shoko.Server.API.v3.Models.Shoko.Episode.AniDBs. Admins only.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import episode_api
from lib.shoko.v3.lib.shoko.v3.models.list_result_episode_ani_db import ListResultEpisodeAniDB
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
    api_instance = episode_api.EpisodeApi(api_client)

    # example passing only optional values
    query_params = {
        'pageSize': 20,
        'page': 1,
        'type': [
        "type_example"
    ],
    }
    try:
        # Get all Shoko.Server.API.v3.Models.Shoko.Episode.AniDBs. Admins only.
        api_response = api_instance.episode_ani_db_get(
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling EpisodeApi->episode_ani_db_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
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
type | TypeSchema | | optional


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

# TypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#episode_ani_db_get.ApiResponseFor200) | Success

#### episode_ani_db_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ListResultEpisodeAniDB**](../../models/ListResultEpisodeAniDB.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ListResultEpisodeAniDB**](../../models/ListResultEpisodeAniDB.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ListResultEpisodeAniDB**](../../models/ListResultEpisodeAniDB.md) |  | 


### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **episode_episode_id_ani_db_get**
<a id="episode_episode_id_ani_db_get"></a>
> EpisodeAniDB episode_episode_id_ani_db_get(episode_id)

Get the Shoko.Server.API.v3.Models.Shoko.Episode.AniDB entry for the given episodeID.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import episode_api
from lib.shoko.v3.lib.shoko.v3.models.episode_ani_db import EpisodeAniDB
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
    api_instance = episode_api.EpisodeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'episodeID': 1,
    }
    try:
        # Get the Shoko.Server.API.v3.Models.Shoko.Episode.AniDB entry for the given episodeID.
        api_response = api_instance.episode_episode_id_ani_db_get(
            path_params=path_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling EpisodeApi->episode_episode_id_ani_db_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

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
200 | [ApiResponseFor200](#episode_episode_id_ani_db_get.ApiResponseFor200) | Success

#### episode_episode_id_ani_db_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**EpisodeAniDB**](../../models/EpisodeAniDB.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EpisodeAniDB**](../../models/EpisodeAniDB.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EpisodeAniDB**](../../models/EpisodeAniDB.md) |  | 


### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **episode_episode_id_get**
<a id="episode_episode_id_get"></a>
> ShokoEpisode episode_episode_id_get(episode_id)

Get the Shoko.Server.API.v3.Models.Shoko.Episode entry for the given episodeID.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import episode_api
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
    api_instance = episode_api.EpisodeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'episodeID': 1,
    }
    query_params = {
    }
    try:
        # Get the Shoko.Server.API.v3.Models.Shoko.Episode entry for the given episodeID.
        api_response = api_instance.episode_episode_id_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling EpisodeApi->episode_episode_id_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'episodeID': 1,
    }
    query_params = {
        'includeDataFrom': [
        CommonDataSource("None")
    ],
    }
    try:
        # Get the Shoko.Server.API.v3.Models.Shoko.Episode entry for the given episodeID.
        api_response = api_instance.episode_episode_id_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling EpisodeApi->episode_episode_id_get: %s\n" % e)
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
200 | [ApiResponseFor200](#episode_episode_id_get.ApiResponseFor200) | Success

#### episode_episode_id_get.ApiResponseFor200
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

# **episode_episode_id_set_hidden_post**
<a id="episode_episode_id_set_hidden_post"></a>
> episode_episode_id_set_hidden_post(episode_id)

Set or unset the episode hidden status by the given episodeID.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import episode_api
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
    api_instance = episode_api.EpisodeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'episodeID': 1,
    }
    query_params = {
    }
    try:
        # Set or unset the episode hidden status by the given episodeID.
        api_response = api_instance.episode_episode_id_set_hidden_post(
            path_params=path_params,
            query_params=query_params,
        )
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling EpisodeApi->episode_episode_id_set_hidden_post: %s\n" % e)

    # example passing only optional values
    path_params = {
        'episodeID': 1,
    }
    query_params = {
        'value': True,
        'updateStats': True,
    }
    try:
        # Set or unset the episode hidden status by the given episodeID.
        api_response = api_instance.episode_episode_id_set_hidden_post(
            path_params=path_params,
            query_params=query_params,
        )
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling EpisodeApi->episode_episode_id_set_hidden_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
value | ValueSchema | | optional
updateStats | UpdateStatsSchema | | optional


# ValueSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of True

# UpdateStatsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of True

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
200 | [ApiResponseFor200](#episode_episode_id_set_hidden_post.ApiResponseFor200) | Success

#### episode_episode_id_set_hidden_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **episode_episode_id_vote_post**
<a id="episode_episode_id_vote_post"></a>
> episode_episode_id_vote_post(episode_id)

Add a permanent user-submitted rating for the episode.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import episode_api
from lib.shoko.v3.lib.shoko.v3.models.common_vote import CommonVote
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
    api_instance = episode_api.EpisodeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'episodeID': 1,
    }
    try:
        # Add a permanent user-submitted rating for the episode.
        api_response = api_instance.episode_episode_id_vote_post(
            path_params=path_params,
        )
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling EpisodeApi->episode_episode_id_vote_post: %s\n" % e)

    # example passing only optional values
    path_params = {
        'episodeID': 1,
    }
    body = CommonVote(
        value=0,
        max_value=10,
        type="type_example",
    )
    try:
        # Add a permanent user-submitted rating for the episode.
        api_response = api_instance.episode_episode_id_vote_post(
            path_params=path_params,
            body=body,
        )
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling EpisodeApi->episode_episode_id_vote_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json-patch+json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJsonPatchjson
Type | Description  | Notes
------------- | ------------- | -------------
[**CommonVote**](../../models/CommonVote.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CommonVote**](../../models/CommonVote.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CommonVote**](../../models/CommonVote.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CommonVote**](../../models/CommonVote.md) |  | 


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
200 | [ApiResponseFor200](#episode_episode_id_vote_post.ApiResponseFor200) | Success

#### episode_episode_id_vote_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **episode_episode_id_watched_watched_post**
<a id="episode_episode_id_watched_watched_post"></a>
> episode_episode_id_watched_watched_post(episode_idwatched)

Set the watched status on an episode

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import episode_api
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
    api_instance = episode_api.EpisodeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'episodeID': 1,
        'watched': True,
    }
    try:
        # Set the watched status on an episode
        api_response = api_instance.episode_episode_id_watched_watched_post(
            path_params=path_params,
        )
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling EpisodeApi->episode_episode_id_watched_watched_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
episodeID | EpisodeIDSchema | | 
watched | WatchedSchema | | 

# EpisodeIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# WatchedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#episode_episode_id_watched_watched_post.ApiResponseFor200) | Success

#### episode_episode_id_watched_watched_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **episode_episode_idtv_db_get**
<a id="episode_episode_idtv_db_get"></a>
> [EpisodeTvDB] episode_episode_idtv_db_get(episode_id)

Get the TvDB details for episode with Shoko ID

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import episode_api
from lib.shoko.v3.lib.shoko.v3.models.episode_tv_db import EpisodeTvDB
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
    api_instance = episode_api.EpisodeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'episodeID': 1,
    }
    try:
        # Get the TvDB details for episode with Shoko ID
        api_response = api_instance.episode_episode_idtv_db_get(
            path_params=path_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling EpisodeApi->episode_episode_idtv_db_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

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
200 | [ApiResponseFor200](#episode_episode_idtv_db_get.ApiResponseFor200) | Success

#### episode_episode_idtv_db_get.ApiResponseFor200
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
[**EpisodeTvDB**]({{complexTypePrefix}}EpisodeTvDB.md) | [**EpisodeTvDB**]({{complexTypePrefix}}EpisodeTvDB.md) | [**EpisodeTvDB**]({{complexTypePrefix}}EpisodeTvDB.md) |  | 

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EpisodeTvDB**]({{complexTypePrefix}}EpisodeTvDB.md) | [**EpisodeTvDB**]({{complexTypePrefix}}EpisodeTvDB.md) | [**EpisodeTvDB**]({{complexTypePrefix}}EpisodeTvDB.md) |  | 

# SchemaFor200ResponseBodyTextJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EpisodeTvDB**]({{complexTypePrefix}}EpisodeTvDB.md) | [**EpisodeTvDB**]({{complexTypePrefix}}EpisodeTvDB.md) | [**EpisodeTvDB**]({{complexTypePrefix}}EpisodeTvDB.md) |  | 

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **episode_get**
<a id="episode_get"></a>
> ListResultShokoEpisode episode_get()

Get all Shoko.Server.API.v3.Models.Shoko.Episodes for the given filter.

Shoko.Server.API.v3.Models.Shoko.Filter or Shoko.Server.API.v3.Models.Shoko.Group is irrelevant at this level.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import episode_api
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
    api_instance = episode_api.EpisodeApi(api_client)

    # example passing only optional values
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
        # Get all Shoko.Server.API.v3.Models.Shoko.Episodes for the given filter.
        api_response = api_instance.episode_get(
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling EpisodeApi->episode_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#episode_get.ApiResponseFor200) | Success

#### episode_get.ApiResponseFor200
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

# **episode_tv_db_get**
<a id="episode_tv_db_get"></a>
> ListResultEpisodeTvDB episode_tv_db_get()

Get all Shoko.Server.API.v3.Models.Shoko.Episode.TvDBs. Admins only.

It's admins only since i don't want to add the logic to

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import episode_api
from lib.shoko.v3.lib.shoko.v3.models.list_result_episode_tv_db import ListResultEpisodeTvDB
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
    api_instance = episode_api.EpisodeApi(api_client)

    # example passing only optional values
    query_params = {
        'pageSize': 20,
        'page': 1,
    }
    try:
        # Get all Shoko.Server.API.v3.Models.Shoko.Episode.TvDBs. Admins only.
        api_response = api_instance.episode_tv_db_get(
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling EpisodeApi->episode_tv_db_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#episode_tv_db_get.ApiResponseFor200) | Success

#### episode_tv_db_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ListResultEpisodeTvDB**](../../models/ListResultEpisodeTvDB.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ListResultEpisodeTvDB**](../../models/ListResultEpisodeTvDB.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ListResultEpisodeTvDB**](../../models/ListResultEpisodeTvDB.md) |  | 


### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **episode_with_multiple_files_get**
<a id="episode_with_multiple_files_get"></a>
> ListResultShokoEpisode episode_with_multiple_files_get()

Get episodes with multiple files attached.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import episode_api
from lib.shoko.v3.lib.shoko.v3.models.list_result_shoko_episode import ListResultShokoEpisode
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
    api_instance = episode_api.EpisodeApi(api_client)

    # example passing only optional values
    query_params = {
        'ignoreVariations': True,
        'onlyFinishedSeries': False,
        'pageSize': 100,
        'page': 1,
    }
    try:
        # Get episodes with multiple files attached.
        api_response = api_instance.episode_with_multiple_files_get(
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling EpisodeApi->episode_with_multiple_files_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ignoreVariations | IgnoreVariationsSchema | | optional
onlyFinishedSeries | OnlyFinishedSeriesSchema | | optional
pageSize | PageSizeSchema | | optional
page | PageSchema | | optional


# IgnoreVariationsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of True

# OnlyFinishedSeriesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# PageSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 100value must be a 32 bit integer

# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#episode_with_multiple_files_get.ApiResponseFor200) | Success

#### episode_with_multiple_files_get.ApiResponseFor200
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

# **episode_with_no_files_get**
<a id="episode_with_no_files_get"></a>
> ListResultShokoEpisode episode_with_no_files_get()

Get all episodes with no files.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import episode_api
from lib.shoko.v3.lib.shoko.v3.models.list_result_shoko_episode import ListResultShokoEpisode
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
    api_instance = episode_api.EpisodeApi(api_client)

    # example passing only optional values
    query_params = {
        'includeSpecials': False,
        'onlyFinishedSeries': False,
        'pageSize': 100,
        'page': 1,
    }
    try:
        # Get all episodes with no files.
        api_response = api_instance.episode_with_no_files_get(
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling EpisodeApi->episode_with_no_files_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
includeSpecials | IncludeSpecialsSchema | | optional
onlyFinishedSeries | OnlyFinishedSeriesSchema | | optional
pageSize | PageSizeSchema | | optional
page | PageSchema | | optional


# IncludeSpecialsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# OnlyFinishedSeriesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# PageSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 100value must be a 32 bit integer

# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#episode_with_no_files_get.ApiResponseFor200) | Success

#### episode_with_no_files_get.ApiResponseFor200
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

