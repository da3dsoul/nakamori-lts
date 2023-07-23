<a id="__pageTop"></a>
# lib.shoko.v3.lib.shoko.v3.api.tags.user_api.UserApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_current_change_password_post**](#user_current_change_password_post) | **post** /User/Current/ChangePassword | Change the password for the current user.
[**user_current_get**](#user_current_get) | **get** /User/Current | Get the current user.
[**user_current_patch**](#user_current_patch) | **patch** /User/Current | Edit the current user using a JSON patch document to do a partial  update.
[**user_current_put**](#user_current_put) | **put** /User/Current | Edit the current user using a raw object to do a partial update.
[**user_get**](#user_get) | **get** /User | List all available users.
[**user_post**](#user_post) | **post** /User | Add a new user.
[**user_user_id_change_password_post**](#user_user_id_change_password_post) | **post** /User/{userID}/ChangePassword | Change the password for a user.
[**user_user_id_delete**](#user_user_id_delete) | **delete** /User/{userID} | Delete a user by id. This updates group filters and wipes internal watched states, so be careful.
[**user_user_id_get**](#user_user_id_get) | **get** /User/{userID} | Get a user by id.
[**user_user_id_patch**](#user_user_id_patch) | **patch** /User/{userID} | Edit an user by id using a JSON patch document to do a partial update.
[**user_user_id_put**](#user_user_id_put) | **put** /User/{userID} | Edit an user by id using a raw object to do a partial update.

# **user_current_change_password_post**
<a id="user_current_change_password_post"></a>
> user_current_change_password_post()

Change the password for the current user.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import user_api
from lib.shoko.v3.lib.shoko.v3.models.input_change_password_body import InputChangePasswordBody
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
    api_instance = user_api.UserApi(api_client)

    # example passing only optional values
    body = InputChangePasswordBody(
        password="password_example",
        revoke_api_keys=True,
    )
    try:
        # Change the password for the current user.
        api_response = api_instance.user_current_change_password_post(
            body=body,
        )
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling UserApi->user_current_change_password_post: %s\n" % e)
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
[**InputChangePasswordBody**](../../models/InputChangePasswordBody.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InputChangePasswordBody**](../../models/InputChangePasswordBody.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InputChangePasswordBody**](../../models/InputChangePasswordBody.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InputChangePasswordBody**](../../models/InputChangePasswordBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_current_change_password_post.ApiResponseFor200) | Success

#### user_current_change_password_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_current_get**
<a id="user_current_get"></a>
> ShokoUser user_current_get()

Get the current user.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import user_api
from lib.shoko.v3.lib.shoko.v3.models.shoko_user import ShokoUser
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
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the current user.
        api_response = api_instance.user_current_get()
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling UserApi->user_current_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_current_get.ApiResponseFor200) | Success

#### user_current_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoUser**](../../models/ShokoUser.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoUser**](../../models/ShokoUser.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoUser**](../../models/ShokoUser.md) |  | 


### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_current_patch**
<a id="user_current_patch"></a>
> ShokoUser user_current_patch()

Edit the current user using a JSON patch document to do a partial  update.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import user_api
from lib.shoko.v3.lib.shoko.v3.models.operations_operation import OperationsOperation
from lib.shoko.v3.lib.shoko.v3.models.shoko_user import ShokoUser
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
    api_instance = user_api.UserApi(api_client)

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
        # Edit the current user using a JSON patch document to do a partial  update.
        api_response = api_instance.user_current_patch(
            body=body,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling UserApi->user_current_patch: %s\n" % e)
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
200 | [ApiResponseFor200](#user_current_patch.ApiResponseFor200) | Success

#### user_current_patch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoUser**](../../models/ShokoUser.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoUser**](../../models/ShokoUser.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoUser**](../../models/ShokoUser.md) |  | 


### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_current_put**
<a id="user_current_put"></a>
> ShokoUser user_current_put()

Edit the current user using a raw object to do a partial update.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import user_api
from lib.shoko.v3.lib.shoko.v3.models.shoko_user import ShokoUser
from lib.shoko.v3.lib.shoko.v3.models.input_create_or_update_user_body import InputCreateOrUpdateUserBody
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
    api_instance = user_api.UserApi(api_client)

    # example passing only optional values
    body = InputCreateOrUpdateUserBody(
        username="username_example",
        is_admin=True,
        community_sites=[
            EnumsCommunitySites(0)
        ],
        restricted_tags=[
            1
        ],
        avatar="avatar_example",
    )
    try:
        # Edit the current user using a raw object to do a partial update.
        api_response = api_instance.user_current_put(
            body=body,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling UserApi->user_current_put: %s\n" % e)
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
[**InputCreateOrUpdateUserBody**](../../models/InputCreateOrUpdateUserBody.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InputCreateOrUpdateUserBody**](../../models/InputCreateOrUpdateUserBody.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InputCreateOrUpdateUserBody**](../../models/InputCreateOrUpdateUserBody.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InputCreateOrUpdateUserBody**](../../models/InputCreateOrUpdateUserBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_current_put.ApiResponseFor200) | Success

#### user_current_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoUser**](../../models/ShokoUser.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoUser**](../../models/ShokoUser.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoUser**](../../models/ShokoUser.md) |  | 


### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_get**
<a id="user_get"></a>
> [ShokoUser] user_get()

List all available users.

Only for administrators.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import user_api
from lib.shoko.v3.lib.shoko.v3.models.shoko_user import ShokoUser
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
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List all available users.
        api_response = api_instance.user_get()
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling UserApi->user_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_get.ApiResponseFor200) | Success

#### user_get.ApiResponseFor200
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
[**ShokoUser**]({{complexTypePrefix}}ShokoUser.md) | [**ShokoUser**]({{complexTypePrefix}}ShokoUser.md) | [**ShokoUser**]({{complexTypePrefix}}ShokoUser.md) |  | 

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShokoUser**]({{complexTypePrefix}}ShokoUser.md) | [**ShokoUser**]({{complexTypePrefix}}ShokoUser.md) | [**ShokoUser**]({{complexTypePrefix}}ShokoUser.md) |  | 

# SchemaFor200ResponseBodyTextJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShokoUser**]({{complexTypePrefix}}ShokoUser.md) | [**ShokoUser**]({{complexTypePrefix}}ShokoUser.md) | [**ShokoUser**]({{complexTypePrefix}}ShokoUser.md) |  | 

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_post**
<a id="user_post"></a>
> ShokoUser user_post()

Add a new user.

Only for administrators.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import user_api
from lib.shoko.v3.lib.shoko.v3.models.input_create_user_body import InputCreateUserBody
from lib.shoko.v3.lib.shoko.v3.models.shoko_user import ShokoUser
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
    api_instance = user_api.UserApi(api_client)

    # example passing only optional values
    body = InputCreateUserBody(
        password="password_example",
        username="username_example",
        is_admin=True,
        community_sites=[
            EnumsCommunitySites(0)
        ],
        restricted_tags=[
            1
        ],
        avatar="avatar_example",
    )
    try:
        # Add a new user.
        api_response = api_instance.user_post(
            body=body,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling UserApi->user_post: %s\n" % e)
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
[**InputCreateUserBody**](../../models/InputCreateUserBody.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InputCreateUserBody**](../../models/InputCreateUserBody.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InputCreateUserBody**](../../models/InputCreateUserBody.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InputCreateUserBody**](../../models/InputCreateUserBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_post.ApiResponseFor200) | Success

#### user_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoUser**](../../models/ShokoUser.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoUser**](../../models/ShokoUser.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoUser**](../../models/ShokoUser.md) |  | 


### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_user_id_change_password_post**
<a id="user_user_id_change_password_post"></a>
> user_user_id_change_password_post(user_id)

Change the password for a user.

Can only be called by admins or the user the password belongs to.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import user_api
from lib.shoko.v3.lib.shoko.v3.models.input_change_password_body import InputChangePasswordBody
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
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userID': 1,
    }
    try:
        # Change the password for a user.
        api_response = api_instance.user_user_id_change_password_post(
            path_params=path_params,
        )
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling UserApi->user_user_id_change_password_post: %s\n" % e)

    # example passing only optional values
    path_params = {
        'userID': 1,
    }
    body = InputChangePasswordBody(
        password="password_example",
        revoke_api_keys=True,
    )
    try:
        # Change the password for a user.
        api_response = api_instance.user_user_id_change_password_post(
            path_params=path_params,
            body=body,
        )
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling UserApi->user_user_id_change_password_post: %s\n" % e)
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
[**InputChangePasswordBody**](../../models/InputChangePasswordBody.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InputChangePasswordBody**](../../models/InputChangePasswordBody.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InputChangePasswordBody**](../../models/InputChangePasswordBody.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InputChangePasswordBody**](../../models/InputChangePasswordBody.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
userID | UserIDSchema | | 

# UserIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_user_id_change_password_post.ApiResponseFor200) | Success

#### user_user_id_change_password_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_user_id_delete**
<a id="user_user_id_delete"></a>
> user_user_id_delete(user_id)

Delete a user by id. This updates group filters and wipes internal watched states, so be careful.

Only for administrators.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import user_api
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
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userID': 1,
    }
    try:
        # Delete a user by id. This updates group filters and wipes internal watched states, so be careful.
        api_response = api_instance.user_user_id_delete(
            path_params=path_params,
        )
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling UserApi->user_user_id_delete: %s\n" % e)
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
userID | UserIDSchema | | 

# UserIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_user_id_delete.ApiResponseFor200) | Success

#### user_user_id_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_user_id_get**
<a id="user_user_id_get"></a>
> ShokoUser user_user_id_get(user_id)

Get a user by id.

Only for administrators.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import user_api
from lib.shoko.v3.lib.shoko.v3.models.shoko_user import ShokoUser
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
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userID': 1,
    }
    try:
        # Get a user by id.
        api_response = api_instance.user_user_id_get(
            path_params=path_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling UserApi->user_user_id_get: %s\n" % e)
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
userID | UserIDSchema | | 

# UserIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_user_id_get.ApiResponseFor200) | Success

#### user_user_id_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoUser**](../../models/ShokoUser.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoUser**](../../models/ShokoUser.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoUser**](../../models/ShokoUser.md) |  | 


### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_user_id_patch**
<a id="user_user_id_patch"></a>
> ShokoUser user_user_id_patch(user_id)

Edit an user by id using a JSON patch document to do a partial update.

Only for administrators.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import user_api
from lib.shoko.v3.lib.shoko.v3.models.operations_operation import OperationsOperation
from lib.shoko.v3.lib.shoko.v3.models.shoko_user import ShokoUser
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
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userID': 1,
    }
    try:
        # Edit an user by id using a JSON patch document to do a partial update.
        api_response = api_instance.user_user_id_patch(
            path_params=path_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling UserApi->user_user_id_patch: %s\n" % e)

    # example passing only optional values
    path_params = {
        'userID': 1,
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
        # Edit an user by id using a JSON patch document to do a partial update.
        api_response = api_instance.user_user_id_patch(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling UserApi->user_user_id_patch: %s\n" % e)
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
userID | UserIDSchema | | 

# UserIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_user_id_patch.ApiResponseFor200) | Success

#### user_user_id_patch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoUser**](../../models/ShokoUser.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoUser**](../../models/ShokoUser.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoUser**](../../models/ShokoUser.md) |  | 


### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_user_id_put**
<a id="user_user_id_put"></a>
> ShokoUser user_user_id_put(user_id)

Edit an user by id using a raw object to do a partial update.

Only for administrators.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import user_api
from lib.shoko.v3.lib.shoko.v3.models.shoko_user import ShokoUser
from lib.shoko.v3.lib.shoko.v3.models.input_create_or_update_user_body import InputCreateOrUpdateUserBody
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
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userID': 1,
    }
    try:
        # Edit an user by id using a raw object to do a partial update.
        api_response = api_instance.user_user_id_put(
            path_params=path_params,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling UserApi->user_user_id_put: %s\n" % e)

    # example passing only optional values
    path_params = {
        'userID': 1,
    }
    body = InputCreateOrUpdateUserBody(
        username="username_example",
        is_admin=True,
        community_sites=[
            EnumsCommunitySites(0)
        ],
        restricted_tags=[
            1
        ],
        avatar="avatar_example",
    )
    try:
        # Edit an user by id using a raw object to do a partial update.
        api_response = api_instance.user_user_id_put(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling UserApi->user_user_id_put: %s\n" % e)
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
[**InputCreateOrUpdateUserBody**](../../models/InputCreateOrUpdateUserBody.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InputCreateOrUpdateUserBody**](../../models/InputCreateOrUpdateUserBody.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InputCreateOrUpdateUserBody**](../../models/InputCreateOrUpdateUserBody.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InputCreateOrUpdateUserBody**](../../models/InputCreateOrUpdateUserBody.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
userID | UserIDSchema | | 

# UserIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_user_id_put.ApiResponseFor200) | Success

#### user_user_id_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoUser**](../../models/ShokoUser.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoUser**](../../models/ShokoUser.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShokoUser**](../../models/ShokoUser.md) |  | 


### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

