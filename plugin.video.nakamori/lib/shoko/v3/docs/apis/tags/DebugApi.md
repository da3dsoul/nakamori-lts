<a id="__pageTop"></a>
# lib.shoko.v3.lib.shoko.v3.api.tags.debug_api.DebugApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**debug_ani_dbudp_call_post**](#debug_ani_dbudp_call_post) | **post** /Debug/AniDB/UDP/Call | Call the AniDB UDP API using the

# **debug_ani_dbudp_call_post**
<a id="debug_ani_dbudp_call_post"></a>
> DebugControllerAnidbUdpResponse debug_ani_dbudp_call_post()

Call the AniDB UDP API using the

Most of the code here is just copy-pasted from the UDPRequest class, and  afterwards modified to fit the new request/response models.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import debug_api
from lib.shoko.v3.lib.shoko.v3.models.debug_controller_anidb_udp_request import DebugControllerAnidbUdpRequest
from lib.shoko.v3.lib.shoko.v3.models.debug_controller_anidb_udp_response import DebugControllerAnidbUdpResponse
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
    api_instance = debug_api.DebugApi(api_client)

    # example passing only optional values
    body = DebugControllerAnidbUdpRequest(
        action="action_example",
        unsafe=True,
        payload=dict(
            "key": None,
        ),
    )
    try:
        # Call the AniDB UDP API using the
        api_response = api_instance.debug_ani_dbudp_call_post(
            body=body,
        )
        pprint(api_response)
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling DebugApi->debug_ani_dbudp_call_post: %s\n" % e)
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
[**DebugControllerAnidbUdpRequest**](../../models/DebugControllerAnidbUdpRequest.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DebugControllerAnidbUdpRequest**](../../models/DebugControllerAnidbUdpRequest.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DebugControllerAnidbUdpRequest**](../../models/DebugControllerAnidbUdpRequest.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DebugControllerAnidbUdpRequest**](../../models/DebugControllerAnidbUdpRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#debug_ani_dbudp_call_post.ApiResponseFor200) | Success

#### debug_ani_dbudp_call_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**DebugControllerAnidbUdpResponse**](../../models/DebugControllerAnidbUdpResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DebugControllerAnidbUdpResponse**](../../models/DebugControllerAnidbUdpResponse.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DebugControllerAnidbUdpResponse**](../../models/DebugControllerAnidbUdpResponse.md) |  | 


### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

