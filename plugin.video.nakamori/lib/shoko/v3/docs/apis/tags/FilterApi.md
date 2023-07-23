<a id="__pageTop"></a>
# lib.shoko.v3.lib.shoko.v3.api.tags.filter_api.FilterApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_filter_id_delete**](#filter_filter_id_delete) | **delete** /Filter/{filterID} | Removes an existing filter. Requires admin.
[**filter_filter_id_get**](#filter_filter_id_get) | **get** /Filter/{filterID} | Get the Shoko.Server.API.v3.Models.Shoko.Filter for the given filterID.
[**filter_filter_id_patch**](#filter_filter_id_patch) | **patch** /Filter/{filterID} | Edit an existing filter using a JSON patch document to do a partial  update. Requires admin.
[**filter_filter_id_put**](#filter_filter_id_put) | **put** /Filter/{filterID} | Edit an existing filter using a raw object. Requires admin.
[**filter_get**](#filter_get) | **get** /Filter | Get all Shoko.Server.API.v3.Models.Shoko.Filters except the live filter.
[**filter_post**](#filter_post) | **post** /Filter | Add a new group filter. Requires admin.
[**filter_preview_delete**](#filter_preview_delete) | **delete** /Filter/Preview | Resets the live filter for the current user.
[**filter_preview_get**](#filter_preview_get) | **get** /Filter/Preview | Get the live filter for the current user.
[**filter_preview_group_get**](#filter_preview_group_get) | **get** /Filter/Preview/Group | Get a paginated list of all the top-level Shoko.Server.API.v3.Models.Shoko.Groups for the live filter.
[**filter_preview_group_group_id_group_get**](#filter_preview_group_group_id_group_get) | **get** /Filter/Preview/Group/{groupID}/Group | Get a list of all the sub-Shoko.Server.API.v3.Models.Shoko.Groups belonging to the Shoko.Server.API.v3.Models.Shoko.Group with the given groupID and which are present within the live filter.
[**filter_preview_group_group_id_series_get**](#filter_preview_group_group_id_series_get) | **get** /Filter/Preview/Group/{groupID}/Series | Get a list of all the Shoko.Server.API.v3.Models.Shoko.Series for the Shoko.Server.API.v3.Models.Shoko.Group within the live filter.
[**filter_preview_group_letters_get**](#filter_preview_group_letters_get) | **get** /Filter/Preview/Group/Letters | Get a dictionary with the count for each starting character in each of  the top-level group&#x27;s name with the live filter applied.
[**filter_preview_patch**](#filter_preview_patch) | **patch** /Filter/Preview | Edit the live filter for the current user using a JSON patch document to  do a partial update.
[**filter_preview_put**](#filter_preview_put) | **put** /Filter/Preview | Edit the live filter for the current user using a raw object.
[**filter_preview_series_get**](#filter_preview_series_get) | **get** /Filter/Preview/Series | Get a paginated list of all the Shoko.Server.API.v3.Models.Shoko.Series within the live filter.

# **filter_filter_id_delete**
<a id="filter_filter_id_delete"></a>
> filter_filter_id_delete(filter_id)

Removes an existing filter. Requires admin.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import filter_api
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
    api_instance = filter_api.FilterApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'filterID': 1,
    }
    try:
        # Removes an existing filter. Requires admin.
        api_response = api_instance.filter_filter_id_delete(
            path_params=path_params,
        )
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling FilterApi->filter_filter_id_delete: %s\n" % e)
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
200 | [ApiResponseFor200](#filter_filter_id_delete.ApiResponseFor200) | Success

#### filter_filter_id_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **filter_filter_id_get**
<a id="filter_filter_id_get"></a>
> ShokoFilter filter_filter_id_get(filter_id)

Get the Shoko.Server.API.v3.Models.Shoko.Filter for the given filterID.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import filter_api
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
    api_instance = filter_api.FilterApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'filterID': 1,
    }
    query_params = {
    }
    try:
        # Get the Shoko.Server.API.v3.Models.Shoko.Filter for the given filterID.
        api_response = api_instance.filter_filter_id_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling FilterApi->filter_filter_id_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'filterID': 1,
    }
    query_params = {
        'withConditions': False,
    }
    try:
        # Get the Shoko.Server.API.v3.Models.Shoko.Filter for the given filterID.
        api_response = api_instance.filter_filter_id_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling FilterApi->filter_filter_id_get: %s\n" % e)
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
withConditions | WithConditionsSchema | | optional


# WithConditionsSchema

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
200 | [ApiResponseFor200](#filter_filter_id_get.ApiResponseFor200) | Success

#### filter_filter_id_get.ApiResponseFor200
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

# **filter_filter_id_patch**
<a id="filter_filter_id_patch"></a>
> ShokoFilter filter_filter_id_patch(filter_id)

Edit an existing filter using a JSON patch document to do a partial  update. Requires admin.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import filter_api
from lib.shoko.v3.lib.shoko.v3.models.operations_operation import OperationsOperation
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
    api_instance = filter_api.FilterApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'filterID': 1,
    }
    try:
        # Edit an existing filter using a JSON patch document to do a partial  update. Requires admin.
        api_response = api_instance.filter_filter_id_patch(
            path_params=path_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling FilterApi->filter_filter_id_patch: %s\n" % e)

    # example passing only optional values
    path_params = {
        'filterID': 1,
    }
    body = [
        OperationsOperation(
            value=None,
            path="path_example",
            op="op_example",
            _from="_from_example",
        )
    ]
    try:
        # Edit an existing filter using a JSON patch document to do a partial  update. Requires admin.
        api_response = api_instance.filter_filter_id_patch(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling FilterApi->filter_filter_id_patch: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json-patch+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJsonPatchjson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OperationsOperation**]({{complexTypePrefix}}OperationsOperation.md) | [**OperationsOperation**]({{complexTypePrefix}}OperationsOperation.md) | [**OperationsOperation**]({{complexTypePrefix}}OperationsOperation.md) |  | 

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OperationsOperation**]({{complexTypePrefix}}OperationsOperation.md) | [**OperationsOperation**]({{complexTypePrefix}}OperationsOperation.md) | [**OperationsOperation**]({{complexTypePrefix}}OperationsOperation.md) |  | 

# SchemaForRequestBodyTextJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OperationsOperation**]({{complexTypePrefix}}OperationsOperation.md) | [**OperationsOperation**]({{complexTypePrefix}}OperationsOperation.md) | [**OperationsOperation**]({{complexTypePrefix}}OperationsOperation.md) |  | 

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OperationsOperation**]({{complexTypePrefix}}OperationsOperation.md) | [**OperationsOperation**]({{complexTypePrefix}}OperationsOperation.md) | [**OperationsOperation**]({{complexTypePrefix}}OperationsOperation.md) |  | 

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
200 | [ApiResponseFor200](#filter_filter_id_patch.ApiResponseFor200) | Success

#### filter_filter_id_patch.ApiResponseFor200
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

# **filter_filter_id_put**
<a id="filter_filter_id_put"></a>
> ShokoFilter filter_filter_id_put(filter_id)

Edit an existing filter using a raw object. Requires admin.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import filter_api
from lib.shoko.v3.lib.shoko.v3.models.shoko_filter import ShokoFilter
from lib.shoko.v3.lib.shoko.v3.models.input_create_or_update_filter_body import InputCreateOrUpdateFilterBody
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
    api_instance = filter_api.FilterApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'filterID': 1,
    }
    try:
        # Edit an existing filter using a raw object. Requires admin.
        api_response = api_instance.filter_filter_id_put(
            path_params=path_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling FilterApi->filter_filter_id_put: %s\n" % e)

    # example passing only optional values
    path_params = {
        'filterID': 1,
    }
    body = InputCreateOrUpdateFilterBody(
        name="name_example",
        parent_id=1,
        is_directory=True,
        is_inverted=True,
        is_hidden=True,
        apply_at_series_level=True,
        conditions=[
            FilterFilterCondition(
                type=EnumsGroupFilterConditionType(1),
                operator=EnumsGroupFilterOperator(1),
                parameter="parameter_example",
            )
        ],
        sorting=[
            FilterSortingCriteria(
                type=EnumsGroupFilterSorting(1),
                is_inverted=True,
            )
        ],
    )
    try:
        # Edit an existing filter using a raw object. Requires admin.
        api_response = api_instance.filter_filter_id_put(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling FilterApi->filter_filter_id_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json-patch+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJsonPatchjson
Type | Description  | Notes
------------- | ------------- | -------------
[**InputCreateOrUpdateFilterBody**](../../models/InputCreateOrUpdateFilterBody.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InputCreateOrUpdateFilterBody**](../../models/InputCreateOrUpdateFilterBody.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InputCreateOrUpdateFilterBody**](../../models/InputCreateOrUpdateFilterBody.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InputCreateOrUpdateFilterBody**](../../models/InputCreateOrUpdateFilterBody.md) |  | 


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
200 | [ApiResponseFor200](#filter_filter_id_put.ApiResponseFor200) | Success

#### filter_filter_id_put.ApiResponseFor200
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

# **filter_get**
<a id="filter_get"></a>
> ListResultShokoFilter filter_get()

Get all Shoko.Server.API.v3.Models.Shoko.Filters except the live filter.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import filter_api
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
    api_instance = filter_api.FilterApi(api_client)

    # example passing only optional values
    query_params = {
        'includeEmpty': False,
        'showHidden': False,
        'pageSize': 10,
        'page': 1,
        'withConditions': False,
    }
    try:
        # Get all Shoko.Server.API.v3.Models.Shoko.Filters except the live filter.
        api_response = api_instance.filter_get(
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling FilterApi->filter_get: %s\n" % e)
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
includeEmpty | IncludeEmptySchema | | optional
showHidden | ShowHiddenSchema | | optional
pageSize | PageSizeSchema | | optional
page | PageSchema | | optional
withConditions | WithConditionsSchema | | optional


# IncludeEmptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# ShowHiddenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# PageSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 10value must be a 32 bit integer

# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1value must be a 32 bit integer

# WithConditionsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#filter_get.ApiResponseFor200) | Success

#### filter_get.ApiResponseFor200
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

# **filter_post**
<a id="filter_post"></a>
> ShokoFilter filter_post()

Add a new group filter. Requires admin.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import filter_api
from lib.shoko.v3.lib.shoko.v3.models.shoko_filter import ShokoFilter
from lib.shoko.v3.lib.shoko.v3.models.input_create_or_update_filter_body import InputCreateOrUpdateFilterBody
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
    api_instance = filter_api.FilterApi(api_client)

    # example passing only optional values
    body = InputCreateOrUpdateFilterBody(
        name="name_example",
        parent_id=1,
        is_directory=True,
        is_inverted=True,
        is_hidden=True,
        apply_at_series_level=True,
        conditions=[
            FilterFilterCondition(
                type=EnumsGroupFilterConditionType(1),
                operator=EnumsGroupFilterOperator(1),
                parameter="parameter_example",
            )
        ],
        sorting=[
            FilterSortingCriteria(
                type=EnumsGroupFilterSorting(1),
                is_inverted=True,
            )
        ],
    )
    try:
        # Add a new group filter. Requires admin.
        api_response = api_instance.filter_post(
            body=body,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling FilterApi->filter_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json-patch+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJsonPatchjson
Type | Description  | Notes
------------- | ------------- | -------------
[**InputCreateOrUpdateFilterBody**](../../models/InputCreateOrUpdateFilterBody.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InputCreateOrUpdateFilterBody**](../../models/InputCreateOrUpdateFilterBody.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InputCreateOrUpdateFilterBody**](../../models/InputCreateOrUpdateFilterBody.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InputCreateOrUpdateFilterBody**](../../models/InputCreateOrUpdateFilterBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#filter_post.ApiResponseFor200) | Success

#### filter_post.ApiResponseFor200
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

# **filter_preview_delete**
<a id="filter_preview_delete"></a>
> filter_preview_delete()

Resets the live filter for the current user.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import filter_api
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
    api_instance = filter_api.FilterApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Resets the live filter for the current user.
        api_response = api_instance.filter_preview_delete()
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling FilterApi->filter_preview_delete: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#filter_preview_delete.ApiResponseFor200) | Success

#### filter_preview_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **filter_preview_get**
<a id="filter_preview_get"></a>
> InputCreateOrUpdateFilterBody filter_preview_get()

Get the live filter for the current user.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import filter_api
from lib.shoko.v3.lib.shoko.v3.models.input_create_or_update_filter_body import InputCreateOrUpdateFilterBody
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
    api_instance = filter_api.FilterApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the live filter for the current user.
        api_response = api_instance.filter_preview_get()
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling FilterApi->filter_preview_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#filter_preview_get.ApiResponseFor200) | Success

#### filter_preview_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**InputCreateOrUpdateFilterBody**](../../models/InputCreateOrUpdateFilterBody.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InputCreateOrUpdateFilterBody**](../../models/InputCreateOrUpdateFilterBody.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InputCreateOrUpdateFilterBody**](../../models/InputCreateOrUpdateFilterBody.md) |  | 


### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **filter_preview_group_get**
<a id="filter_preview_group_get"></a>
> ListResultShokoGroup filter_preview_group_get()

Get a paginated list of all the top-level Shoko.Server.API.v3.Models.Shoko.Groups for the live filter.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import filter_api
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
    api_instance = filter_api.FilterApi(api_client)

    # example passing only optional values
    query_params = {
        'pageSize': 50,
        'page': 1,
        'includeEmpty': False,
        'randomImages': False,
        'orderByName': False,
    }
    try:
        # Get a paginated list of all the top-level Shoko.Server.API.v3.Models.Shoko.Groups for the live filter.
        api_response = api_instance.filter_preview_group_get(
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling FilterApi->filter_preview_group_get: %s\n" % e)
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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#filter_preview_group_get.ApiResponseFor200) | Success

#### filter_preview_group_get.ApiResponseFor200
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

# **filter_preview_group_group_id_group_get**
<a id="filter_preview_group_group_id_group_get"></a>
> [ShokoGroup] filter_preview_group_group_id_group_get(group_id)

Get a list of all the sub-Shoko.Server.API.v3.Models.Shoko.Groups belonging to the Shoko.Server.API.v3.Models.Shoko.Group with the given groupID and which are present within the live filter.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import filter_api
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
    api_instance = filter_api.FilterApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupID': 1,
    }
    query_params = {
    }
    try:
        # Get a list of all the sub-Shoko.Server.API.v3.Models.Shoko.Groups belonging to the Shoko.Server.API.v3.Models.Shoko.Group with the given groupID and which are present within the live filter.
        api_response = api_instance.filter_preview_group_group_id_group_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling FilterApi->filter_preview_group_group_id_group_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupID': 1,
    }
    query_params = {
        'randomImages': False,
        'includeEmpty': False,
    }
    try:
        # Get a list of all the sub-Shoko.Server.API.v3.Models.Shoko.Groups belonging to the Shoko.Server.API.v3.Models.Shoko.Group with the given groupID and which are present within the live filter.
        api_response = api_instance.filter_preview_group_group_id_group_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling FilterApi->filter_preview_group_group_id_group_get: %s\n" % e)
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
200 | [ApiResponseFor200](#filter_preview_group_group_id_group_get.ApiResponseFor200) | Success

#### filter_preview_group_group_id_group_get.ApiResponseFor200
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

# **filter_preview_group_group_id_series_get**
<a id="filter_preview_group_group_id_series_get"></a>
> [ShokoSeries] filter_preview_group_group_id_series_get(group_id)

Get a list of all the Shoko.Server.API.v3.Models.Shoko.Series for the Shoko.Server.API.v3.Models.Shoko.Group within the live filter.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import filter_api
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
    api_instance = filter_api.FilterApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupID': 1,
    }
    query_params = {
    }
    try:
        # Get a list of all the Shoko.Server.API.v3.Models.Shoko.Series for the Shoko.Server.API.v3.Models.Shoko.Group within the live filter.
        api_response = api_instance.filter_preview_group_group_id_series_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling FilterApi->filter_preview_group_group_id_series_get: %s\n" % e)

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
        # Get a list of all the Shoko.Server.API.v3.Models.Shoko.Series for the Shoko.Server.API.v3.Models.Shoko.Group within the live filter.
        api_response = api_instance.filter_preview_group_group_id_series_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling FilterApi->filter_preview_group_group_id_series_get: %s\n" % e)
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
200 | [ApiResponseFor200](#filter_preview_group_group_id_series_get.ApiResponseFor200) | Success

#### filter_preview_group_group_id_series_get.ApiResponseFor200
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

# **filter_preview_group_letters_get**
<a id="filter_preview_group_letters_get"></a>
> {str: (int,)} filter_preview_group_letters_get()

Get a dictionary with the count for each starting character in each of  the top-level group's name with the live filter applied.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import filter_api
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
    api_instance = filter_api.FilterApi(api_client)

    # example passing only optional values
    query_params = {
        'includeEmpty': False,
    }
    try:
        # Get a dictionary with the count for each starting character in each of  the top-level group's name with the live filter applied.
        api_response = api_instance.filter_preview_group_letters_get(
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling FilterApi->filter_preview_group_letters_get: %s\n" % e)
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
includeEmpty | IncludeEmptySchema | | optional


# IncludeEmptySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#filter_preview_group_letters_get.ApiResponseFor200) | Success

#### filter_preview_group_letters_get.ApiResponseFor200
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

# **filter_preview_patch**
<a id="filter_preview_patch"></a>
> InputCreateOrUpdateFilterBody filter_preview_patch()

Edit the live filter for the current user using a JSON patch document to  do a partial update.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import filter_api
from lib.shoko.v3.lib.shoko.v3.models.operations_operation import OperationsOperation
from lib.shoko.v3.lib.shoko.v3.models.input_create_or_update_filter_body import InputCreateOrUpdateFilterBody
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
    api_instance = filter_api.FilterApi(api_client)

    # example passing only optional values
    body = [
        OperationsOperation(
            value=None,
            path="path_example",
            op="op_example",
            _from="_from_example",
        )
    ]
    try:
        # Edit the live filter for the current user using a JSON patch document to  do a partial update.
        api_response = api_instance.filter_preview_patch(
            body=body,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling FilterApi->filter_preview_patch: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json-patch+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJsonPatchjson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OperationsOperation**]({{complexTypePrefix}}OperationsOperation.md) | [**OperationsOperation**]({{complexTypePrefix}}OperationsOperation.md) | [**OperationsOperation**]({{complexTypePrefix}}OperationsOperation.md) |  | 

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OperationsOperation**]({{complexTypePrefix}}OperationsOperation.md) | [**OperationsOperation**]({{complexTypePrefix}}OperationsOperation.md) | [**OperationsOperation**]({{complexTypePrefix}}OperationsOperation.md) |  | 

# SchemaForRequestBodyTextJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OperationsOperation**]({{complexTypePrefix}}OperationsOperation.md) | [**OperationsOperation**]({{complexTypePrefix}}OperationsOperation.md) | [**OperationsOperation**]({{complexTypePrefix}}OperationsOperation.md) |  | 

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OperationsOperation**]({{complexTypePrefix}}OperationsOperation.md) | [**OperationsOperation**]({{complexTypePrefix}}OperationsOperation.md) | [**OperationsOperation**]({{complexTypePrefix}}OperationsOperation.md) |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#filter_preview_patch.ApiResponseFor200) | Success

#### filter_preview_patch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**InputCreateOrUpdateFilterBody**](../../models/InputCreateOrUpdateFilterBody.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InputCreateOrUpdateFilterBody**](../../models/InputCreateOrUpdateFilterBody.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InputCreateOrUpdateFilterBody**](../../models/InputCreateOrUpdateFilterBody.md) |  | 


### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **filter_preview_put**
<a id="filter_preview_put"></a>
> InputCreateOrUpdateFilterBody filter_preview_put()

Edit the live filter for the current user using a raw object.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import filter_api
from lib.shoko.v3.lib.shoko.v3.models.input_create_or_update_filter_body import InputCreateOrUpdateFilterBody
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
    api_instance = filter_api.FilterApi(api_client)

    # example passing only optional values
    body = InputCreateOrUpdateFilterBody(
        name="name_example",
        parent_id=1,
        is_directory=True,
        is_inverted=True,
        is_hidden=True,
        apply_at_series_level=True,
        conditions=[
            FilterFilterCondition(
                type=EnumsGroupFilterConditionType(1),
                operator=EnumsGroupFilterOperator(1),
                parameter="parameter_example",
            )
        ],
        sorting=[
            FilterSortingCriteria(
                type=EnumsGroupFilterSorting(1),
                is_inverted=True,
            )
        ],
    )
    try:
        # Edit the live filter for the current user using a raw object.
        api_response = api_instance.filter_preview_put(
            body=body,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling FilterApi->filter_preview_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json-patch+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJsonPatchjson
Type | Description  | Notes
------------- | ------------- | -------------
[**InputCreateOrUpdateFilterBody**](../../models/InputCreateOrUpdateFilterBody.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InputCreateOrUpdateFilterBody**](../../models/InputCreateOrUpdateFilterBody.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InputCreateOrUpdateFilterBody**](../../models/InputCreateOrUpdateFilterBody.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InputCreateOrUpdateFilterBody**](../../models/InputCreateOrUpdateFilterBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#filter_preview_put.ApiResponseFor200) | Success

#### filter_preview_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**InputCreateOrUpdateFilterBody**](../../models/InputCreateOrUpdateFilterBody.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InputCreateOrUpdateFilterBody**](../../models/InputCreateOrUpdateFilterBody.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InputCreateOrUpdateFilterBody**](../../models/InputCreateOrUpdateFilterBody.md) |  | 


### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **filter_preview_series_get**
<a id="filter_preview_series_get"></a>
> ListResultShokoSeries filter_preview_series_get()

Get a paginated list of all the Shoko.Server.API.v3.Models.Shoko.Series within the live filter.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import filter_api
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
    api_instance = filter_api.FilterApi(api_client)

    # example passing only optional values
    query_params = {
        'pageSize': 50,
        'page': 1,
        'randomImages': False,
        'includeMissing': False,
    }
    try:
        # Get a paginated list of all the Shoko.Server.API.v3.Models.Shoko.Series within the live filter.
        api_response = api_instance.filter_preview_series_get(
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling FilterApi->filter_preview_series_get: %s\n" % e)
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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#filter_preview_series_get.ApiResponseFor200) | Success

#### filter_preview_series_get.ApiResponseFor200
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

