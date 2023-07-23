<a id="__pageTop"></a>
# lib.shoko.v3.lib.shoko.v3.api.tags.import_folder_api.ImportFolderApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_folder_folder_id_delete**](#import_folder_folder_id_delete) | **delete** /ImportFolder/{folderID} | Delete an Import Folder
[**import_folder_folder_id_get**](#import_folder_folder_id_get) | **get** /ImportFolder/{folderID} | Get the Shoko.Server.API.v3.Models.Shoko.ImportFolder by the given folderID.
[**import_folder_folder_id_patch**](#import_folder_folder_id_patch) | **patch** /ImportFolder/{folderID} | Patch the Shoko.Server.API.v3.Models.Shoko.ImportFolder by the given folderID using JSON Patch.
[**import_folder_folder_id_scan_get**](#import_folder_folder_id_scan_get) | **get** /ImportFolder/{folderID}/Scan | Scan a Specific Import Folder. This checks ALL files, not just new ones. Good for cleaning up files in strange states and making drop folders retry moves
[**import_folder_get**](#import_folder_get) | **get** /ImportFolder | List all Import Folders
[**import_folder_post**](#import_folder_post) | **post** /ImportFolder | Add an Import Folder. Does not run import on the folder, so you must scan it yourself.
[**import_folder_put**](#import_folder_put) | **put** /ImportFolder | Edit Import Folder. This replaces all values.

# **import_folder_folder_id_delete**
<a id="import_folder_folder_id_delete"></a>
> import_folder_folder_id_delete(folder_id)

Delete an Import Folder

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import import_folder_api
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
    api_instance = import_folder_api.ImportFolderApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'folderID': 1,
    }
    query_params = {
    }
    try:
        # Delete an Import Folder
        api_response = api_instance.import_folder_folder_id_delete(
            path_params=path_params,
            query_params=query_params,
        )
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ImportFolderApi->import_folder_folder_id_delete: %s\n" % e)

    # example passing only optional values
    path_params = {
        'folderID': 1,
    }
    query_params = {
        'removeRecords': True,
        'updateMyList': True,
    }
    try:
        # Delete an Import Folder
        api_response = api_instance.import_folder_folder_id_delete(
            path_params=path_params,
            query_params=query_params,
        )
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ImportFolderApi->import_folder_folder_id_delete: %s\n" % e)
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
removeRecords | RemoveRecordsSchema | | optional
updateMyList | UpdateMyListSchema | | optional


# RemoveRecordsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of True

# UpdateMyListSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of True

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
200 | [ApiResponseFor200](#import_folder_folder_id_delete.ApiResponseFor200) | Success

#### import_folder_folder_id_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **import_folder_folder_id_get**
<a id="import_folder_folder_id_get"></a>
> ShokoImportFolder import_folder_folder_id_get(folder_id)

Get the Shoko.Server.API.v3.Models.Shoko.ImportFolder by the given folderID.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import import_folder_api
from lib.shoko.v3.lib.shoko.v3.models.shoko_import_folder import ShokoImportFolder
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
    api_instance = import_folder_api.ImportFolderApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'folderID': 1,
    }
    try:
        # Get the Shoko.Server.API.v3.Models.Shoko.ImportFolder by the given folderID.
        api_response = api_instance.import_folder_folder_id_get(
            path_params=path_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ImportFolderApi->import_folder_folder_id_get: %s\n" % e)
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
200 | [ApiResponseFor200](#import_folder_folder_id_get.ApiResponseFor200) | Success

#### import_folder_folder_id_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoImportFolder**](../../models/ShokoImportFolder.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoImportFolder**](../../models/ShokoImportFolder.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoImportFolder**](../../models/ShokoImportFolder.md) |  | 


### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **import_folder_folder_id_patch**
<a id="import_folder_folder_id_patch"></a>
> import_folder_folder_id_patch(folder_id)

Patch the Shoko.Server.API.v3.Models.Shoko.ImportFolder by the given folderID using JSON Patch.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import import_folder_api
from lib.shoko.v3.lib.shoko.v3.models.operations_operation import OperationsOperation
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
    api_instance = import_folder_api.ImportFolderApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'folderID': 1,
    }
    try:
        # Patch the Shoko.Server.API.v3.Models.Shoko.ImportFolder by the given folderID using JSON Patch.
        api_response = api_instance.import_folder_folder_id_patch(
            path_params=path_params,
        )
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ImportFolderApi->import_folder_folder_id_patch: %s\n" % e)

    # example passing only optional values
    path_params = {
        'folderID': 1,
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
        # Patch the Shoko.Server.API.v3.Models.Shoko.ImportFolder by the given folderID using JSON Patch.
        api_response = api_instance.import_folder_folder_id_patch(
            path_params=path_params,
            body=body,
        )
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ImportFolderApi->import_folder_folder_id_patch: %s\n" % e)
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
200 | [ApiResponseFor200](#import_folder_folder_id_patch.ApiResponseFor200) | Success

#### import_folder_folder_id_patch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **import_folder_folder_id_scan_get**
<a id="import_folder_folder_id_scan_get"></a>
> import_folder_folder_id_scan_get(folder_id)

Scan a Specific Import Folder. This checks ALL files, not just new ones. Good for cleaning up files in strange states and making drop folders retry moves

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import import_folder_api
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
    api_instance = import_folder_api.ImportFolderApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'folderID': 1,
    }
    try:
        # Scan a Specific Import Folder. This checks ALL files, not just new ones. Good for cleaning up files in strange states and making drop folders retry moves
        api_response = api_instance.import_folder_folder_id_scan_get(
            path_params=path_params,
        )
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ImportFolderApi->import_folder_folder_id_scan_get: %s\n" % e)
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
200 | [ApiResponseFor200](#import_folder_folder_id_scan_get.ApiResponseFor200) | Success

#### import_folder_folder_id_scan_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **import_folder_get**
<a id="import_folder_get"></a>
> [ShokoImportFolder] import_folder_get()

List all Import Folders

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import import_folder_api
from lib.shoko.v3.lib.shoko.v3.models.shoko_import_folder import ShokoImportFolder
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
    api_instance = import_folder_api.ImportFolderApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List all Import Folders
        api_response = api_instance.import_folder_get()
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ImportFolderApi->import_folder_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#import_folder_get.ApiResponseFor200) | Success

#### import_folder_get.ApiResponseFor200
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
[**ShokoImportFolder**]({{complexTypePrefix}}ShokoImportFolder.md) | [**ShokoImportFolder**]({{complexTypePrefix}}ShokoImportFolder.md) | [**ShokoImportFolder**]({{complexTypePrefix}}ShokoImportFolder.md) |  | 

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShokoImportFolder**]({{complexTypePrefix}}ShokoImportFolder.md) | [**ShokoImportFolder**]({{complexTypePrefix}}ShokoImportFolder.md) | [**ShokoImportFolder**]({{complexTypePrefix}}ShokoImportFolder.md) |  | 

# SchemaFor200ResponseBodyTextJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShokoImportFolder**]({{complexTypePrefix}}ShokoImportFolder.md) | [**ShokoImportFolder**]({{complexTypePrefix}}ShokoImportFolder.md) | [**ShokoImportFolder**]({{complexTypePrefix}}ShokoImportFolder.md) |  | 

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **import_folder_post**
<a id="import_folder_post"></a>
> ShokoImportFolder import_folder_post()

Add an Import Folder. Does not run import on the folder, so you must scan it yourself.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import import_folder_api
from lib.shoko.v3.lib.shoko.v3.models.shoko_import_folder import ShokoImportFolder
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
    api_instance = import_folder_api.ImportFolderApi(api_client)

    # example passing only optional values
    body = ShokoImportFolder(
        id=1,
        watch_for_new_files=True,
        drop_folder_type=ShokoDropFolderType(0),
        path="path_example",
        file_size=1,
        name="name_example",
        size=1,
    )
    try:
        # Add an Import Folder. Does not run import on the folder, so you must scan it yourself.
        api_response = api_instance.import_folder_post(
            body=body,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ImportFolderApi->import_folder_post: %s\n" % e)
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
[**ShokoImportFolder**](../../models/ShokoImportFolder.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoImportFolder**](../../models/ShokoImportFolder.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoImportFolder**](../../models/ShokoImportFolder.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoImportFolder**](../../models/ShokoImportFolder.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#import_folder_post.ApiResponseFor200) | Success

#### import_folder_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoImportFolder**](../../models/ShokoImportFolder.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoImportFolder**](../../models/ShokoImportFolder.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoImportFolder**](../../models/ShokoImportFolder.md) |  | 


### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **import_folder_put**
<a id="import_folder_put"></a>
> import_folder_put()

Edit Import Folder. This replaces all values.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import import_folder_api
from lib.shoko.v3.lib.shoko.v3.models.shoko_import_folder import ShokoImportFolder
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
    api_instance = import_folder_api.ImportFolderApi(api_client)

    # example passing only optional values
    body = ShokoImportFolder(
        id=1,
        watch_for_new_files=True,
        drop_folder_type=ShokoDropFolderType(0),
        path="path_example",
        file_size=1,
        name="name_example",
        size=1,
    )
    try:
        # Edit Import Folder. This replaces all values.
        api_response = api_instance.import_folder_put(
            body=body,
        )
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ImportFolderApi->import_folder_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json-patch+json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJsonPatchjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoImportFolder**](../../models/ShokoImportFolder.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoImportFolder**](../../models/ShokoImportFolder.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoImportFolder**](../../models/ShokoImportFolder.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoImportFolder**](../../models/ShokoImportFolder.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#import_folder_put.ApiResponseFor200) | Success

#### import_folder_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

