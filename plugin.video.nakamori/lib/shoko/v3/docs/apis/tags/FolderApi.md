<a id="__pageTop"></a>
# lib.shoko.v3.lib.shoko.v3.api.tags.folder_api.FolderApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**folder_drives_get**](#folder_drives_get) | **get** /Folder/Drives | 
[**folder_get**](#folder_get) | **get** /Folder | 

# **folder_drives_get**
<a id="folder_drives_get"></a>
> [ShokoDrive] folder_drives_get()



### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import folder_api
from lib.shoko.v3.lib.shoko.v3.models.shoko_drive import ShokoDrive
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
    api_instance = folder_api.FolderApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.folder_drives_get()
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling FolderApi->folder_drives_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#folder_drives_get.ApiResponseFor200) | Success

#### folder_drives_get.ApiResponseFor200
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
[**ShokoDrive**]({{complexTypePrefix}}ShokoDrive.md) | [**ShokoDrive**]({{complexTypePrefix}}ShokoDrive.md) | [**ShokoDrive**]({{complexTypePrefix}}ShokoDrive.md) |  | 

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShokoDrive**]({{complexTypePrefix}}ShokoDrive.md) | [**ShokoDrive**]({{complexTypePrefix}}ShokoDrive.md) | [**ShokoDrive**]({{complexTypePrefix}}ShokoDrive.md) |  | 

# SchemaFor200ResponseBodyTextJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShokoDrive**]({{complexTypePrefix}}ShokoDrive.md) | [**ShokoDrive**]({{complexTypePrefix}}ShokoDrive.md) | [**ShokoDrive**]({{complexTypePrefix}}ShokoDrive.md) |  | 

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **folder_get**
<a id="folder_get"></a>
> [ShokoFolder] folder_get()



### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import folder_api
from lib.shoko.v3.lib.shoko.v3.models.shoko_folder import ShokoFolder
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
    api_instance = folder_api.FolderApi(api_client)

    # example passing only optional values
    query_params = {
        'path': "path_example",
    }
    try:
        api_response = api_instance.folder_get(
            query_params=query_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling FolderApi->folder_get: %s\n" % e)
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
path | PathSchema | | optional


# PathSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#folder_get.ApiResponseFor200) | Success

#### folder_get.ApiResponseFor200
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
[**ShokoFolder**]({{complexTypePrefix}}ShokoFolder.md) | [**ShokoFolder**]({{complexTypePrefix}}ShokoFolder.md) | [**ShokoFolder**]({{complexTypePrefix}}ShokoFolder.md) |  | 

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShokoFolder**]({{complexTypePrefix}}ShokoFolder.md) | [**ShokoFolder**]({{complexTypePrefix}}ShokoFolder.md) | [**ShokoFolder**]({{complexTypePrefix}}ShokoFolder.md) |  | 

# SchemaFor200ResponseBodyTextJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShokoFolder**]({{complexTypePrefix}}ShokoFolder.md) | [**ShokoFolder**]({{complexTypePrefix}}ShokoFolder.md) | [**ShokoFolder**]({{complexTypePrefix}}ShokoFolder.md) |  | 

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

