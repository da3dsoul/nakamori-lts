<a id="__pageTop"></a>
# lib.shoko.v3.lib.shoko.v3.api.tags.action_api.ActionApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**action_add_all_manual_links_to_my_list_get**](#action_add_all_manual_links_to_my_list_get) | **get** /Action/AddAllManualLinksToMyList | Forcibly runs AddToMyList commands for all manual links
[**action_av_dump_mismatched_files_get**](#action_av_dump_mismatched_files_get) | **get** /Action/AVDumpMismatchedFiles | Gets files whose data does not match AniDB
[**action_download_missing_ani_db_anime_data_get**](#action_download_missing_ani_db_anime_data_get) | **get** /Action/DownloadMissingAniDBAnimeData | This Downloads XML data from AniDB where there is none. This should only happen:  A. If someone deleted or corrupted them.  B. If the server closed unexpectedly at the wrong time (it&#x27;ll only be one).  C. If there was a catastrophic error.
[**action_import_new_files_get**](#action_import_new_files_get) | **get** /Action/ImportNewFiles | Queues a task to import only new files found in the import folder
[**action_plex_sync_all_get**](#action_plex_sync_all_get) | **get** /Action/PlexSyncAll | Sync watch states with plex.
[**action_recreate_all_groups_get**](#action_recreate_all_groups_get) | **get** /Action/RecreateAllGroups | Recreate all Shoko.Server.API.v3.Models.Shoko.Groups. This will delete any and all existing groups.
[**action_regenerate_all_tv_db_episode_matchings_get**](#action_regenerate_all_tv_db_episode_matchings_get) | **get** /Action/RegenerateAllTvDBEpisodeMatchings | Regenerate All Episode Matchings for TvDB. Generally, don&#x27;t do this unless there was an error that was fixed.  In those cases, you&#x27;d be told to.
[**action_remove_missing_files_remove_from_my_list_get**](#action_remove_missing_files_remove_from_my_list_get) | **get** /Action/RemoveMissingFiles/{removeFromMyList} | Remove Entries in the Shoko Database for Files that are no longer accessible
[**action_rename_all_groups_get**](#action_rename_all_groups_get) | **get** /Action/RenameAllGroups | Rename al Shoko.Server.API.v3.Models.Shoko.Groups. This won&#x27;t recreate the whole library,  only rename any groups without a custom name set based on the current  language preference.
[**action_run_import_get**](#action_run_import_get) | **get** /Action/RunImport | Run Import. This checks for new files, hashes them etc, scans Drop Folders, checks and scans for community site links (tvdb, trakt, moviedb, etc), and downloads missing images.
[**action_sync_hashes_get**](#action_sync_hashes_get) | **get** /Action/SyncHashes | This was for web cache hash syncing, and will be for perceptual hashing maybe eventually.
[**action_sync_my_list_get**](#action_sync_my_list_get) | **get** /Action/SyncMyList | BEWARE this is a dangerous command!  It syncs all of the states in Shoko&#x27;s library to AniDB.  ONE WAY. THIS CAN ERASE ANIDB DATA IRREVERSIBLY
[**action_sync_trakt_get**](#action_sync_trakt_get) | **get** /Action/SyncTrakt | Sync Trakt states. Requires Trakt to be set up, obviously
[**action_sync_votes_get**](#action_sync_votes_get) | **get** /Action/SyncVotes | Sync the votes from Shoko to AniDB.
[**action_update_all_ani_db_info_get**](#action_update_all_ani_db_info_get) | **get** /Action/UpdateAllAniDBInfo | Update All AniDB Series Info
[**action_update_all_images_get**](#action_update_all_images_get) | **get** /Action/UpdateAllImages | Updates and Downloads Missing Images
[**action_update_all_media_info_get**](#action_update_all_media_info_get) | **get** /Action/UpdateAllMediaInfo | Queues a task to Update all media info
[**action_update_all_movie_db_info_get**](#action_update_all_movie_db_info_get) | **get** /Action/UpdateAllMovieDBInfo | Updates All MovieDB Info
[**action_update_all_trakt_info_get**](#action_update_all_trakt_info_get) | **get** /Action/UpdateAllTraktInfo | Update all Trakt info. Right now, that&#x27;s not much.
[**action_update_all_tv_db_info_get**](#action_update_all_tv_db_info_get) | **get** /Action/UpdateAllTvDBInfo | Update All TvDB Series Info
[**action_update_ani_db_calendar_get**](#action_update_ani_db_calendar_get) | **get** /Action/UpdateAniDBCalendar | Update the AniDB Calendar data for use on the dashboard.
[**action_update_missing_ani_db_file_info_get**](#action_update_missing_ani_db_file_info_get) | **get** /Action/UpdateMissingAniDBFileInfo | Update AniDB Files with missing file info, including with missing release  groups and/or with out-of-date internal data versions.
[**action_update_series_stats_get**](#action_update_series_stats_get) | **get** /Action/UpdateSeriesStats | Queues commands to Update All Series Stats and Force a Recalculation of All Group Filters
[**action_validate_all_images_get**](#action_validate_all_images_get) | **get** /Action/ValidateAllImages | Validates invalid images and redownloads them

# **action_add_all_manual_links_to_my_list_get**
<a id="action_add_all_manual_links_to_my_list_get"></a>
> action_add_all_manual_links_to_my_list_get()

Forcibly runs AddToMyList commands for all manual links

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import action_api
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
    api_instance = action_api.ActionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Forcibly runs AddToMyList commands for all manual links
        api_response = api_instance.action_add_all_manual_links_to_my_list_get()
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ActionApi->action_add_all_manual_links_to_my_list_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#action_add_all_manual_links_to_my_list_get.ApiResponseFor200) | Success

#### action_add_all_manual_links_to_my_list_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **action_av_dump_mismatched_files_get**
<a id="action_av_dump_mismatched_files_get"></a>
> action_av_dump_mismatched_files_get()

Gets files whose data does not match AniDB

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import action_api
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
    api_instance = action_api.ActionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Gets files whose data does not match AniDB
        api_response = api_instance.action_av_dump_mismatched_files_get()
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ActionApi->action_av_dump_mismatched_files_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#action_av_dump_mismatched_files_get.ApiResponseFor200) | Success

#### action_av_dump_mismatched_files_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **action_download_missing_ani_db_anime_data_get**
<a id="action_download_missing_ani_db_anime_data_get"></a>
> action_download_missing_ani_db_anime_data_get()

This Downloads XML data from AniDB where there is none. This should only happen:  A. If someone deleted or corrupted them.  B. If the server closed unexpectedly at the wrong time (it'll only be one).  C. If there was a catastrophic error.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import action_api
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
    api_instance = action_api.ActionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # This Downloads XML data from AniDB where there is none. This should only happen:  A. If someone deleted or corrupted them.  B. If the server closed unexpectedly at the wrong time (it'll only be one).  C. If there was a catastrophic error.
        api_response = api_instance.action_download_missing_ani_db_anime_data_get()
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ActionApi->action_download_missing_ani_db_anime_data_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#action_download_missing_ani_db_anime_data_get.ApiResponseFor200) | Success

#### action_download_missing_ani_db_anime_data_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **action_import_new_files_get**
<a id="action_import_new_files_get"></a>
> action_import_new_files_get()

Queues a task to import only new files found in the import folder

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import action_api
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
    api_instance = action_api.ActionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Queues a task to import only new files found in the import folder
        api_response = api_instance.action_import_new_files_get()
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ActionApi->action_import_new_files_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#action_import_new_files_get.ApiResponseFor200) | Success

#### action_import_new_files_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **action_plex_sync_all_get**
<a id="action_plex_sync_all_get"></a>
> action_plex_sync_all_get()

Sync watch states with plex.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import action_api
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
    api_instance = action_api.ActionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Sync watch states with plex.
        api_response = api_instance.action_plex_sync_all_get()
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ActionApi->action_plex_sync_all_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#action_plex_sync_all_get.ApiResponseFor200) | Success

#### action_plex_sync_all_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **action_recreate_all_groups_get**
<a id="action_recreate_all_groups_get"></a>
> action_recreate_all_groups_get()

Recreate all Shoko.Server.API.v3.Models.Shoko.Groups. This will delete any and all existing groups.

This action requires an admin account because it's a destructive action.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import action_api
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
    api_instance = action_api.ActionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Recreate all Shoko.Server.API.v3.Models.Shoko.Groups. This will delete any and all existing groups.
        api_response = api_instance.action_recreate_all_groups_get()
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ActionApi->action_recreate_all_groups_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#action_recreate_all_groups_get.ApiResponseFor200) | Success

#### action_recreate_all_groups_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **action_regenerate_all_tv_db_episode_matchings_get**
<a id="action_regenerate_all_tv_db_episode_matchings_get"></a>
> action_regenerate_all_tv_db_episode_matchings_get()

Regenerate All Episode Matchings for TvDB. Generally, don't do this unless there was an error that was fixed.  In those cases, you'd be told to.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import action_api
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
    api_instance = action_api.ActionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Regenerate All Episode Matchings for TvDB. Generally, don't do this unless there was an error that was fixed.  In those cases, you'd be told to.
        api_response = api_instance.action_regenerate_all_tv_db_episode_matchings_get()
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ActionApi->action_regenerate_all_tv_db_episode_matchings_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#action_regenerate_all_tv_db_episode_matchings_get.ApiResponseFor200) | Success

#### action_regenerate_all_tv_db_episode_matchings_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **action_remove_missing_files_remove_from_my_list_get**
<a id="action_remove_missing_files_remove_from_my_list_get"></a>
> action_remove_missing_files_remove_from_my_list_get()

Remove Entries in the Shoko Database for Files that are no longer accessible

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import action_api
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
    api_instance = action_api.ActionApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'removeFromMyList': True,
    }
    try:
        # Remove Entries in the Shoko Database for Files that are no longer accessible
        api_response = api_instance.action_remove_missing_files_remove_from_my_list_get(
            path_params=path_params,
        )
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ActionApi->action_remove_missing_files_remove_from_my_list_get: %s\n" % e)
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
removeFromMyList | RemoveFromMyListSchema | | 

# RemoveFromMyListSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of True

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#action_remove_missing_files_remove_from_my_list_get.ApiResponseFor200) | Success

#### action_remove_missing_files_remove_from_my_list_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **action_rename_all_groups_get**
<a id="action_rename_all_groups_get"></a>
> action_rename_all_groups_get()

Rename al Shoko.Server.API.v3.Models.Shoko.Groups. This won't recreate the whole library,  only rename any groups without a custom name set based on the current  language preference.

This action requires an admin account because it affects all groups.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import action_api
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
    api_instance = action_api.ActionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Rename al Shoko.Server.API.v3.Models.Shoko.Groups. This won't recreate the whole library,  only rename any groups without a custom name set based on the current  language preference.
        api_response = api_instance.action_rename_all_groups_get()
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ActionApi->action_rename_all_groups_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#action_rename_all_groups_get.ApiResponseFor200) | Success

#### action_rename_all_groups_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **action_run_import_get**
<a id="action_run_import_get"></a>
> action_run_import_get()

Run Import. This checks for new files, hashes them etc, scans Drop Folders, checks and scans for community site links (tvdb, trakt, moviedb, etc), and downloads missing images.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import action_api
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
    api_instance = action_api.ActionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Run Import. This checks for new files, hashes them etc, scans Drop Folders, checks and scans for community site links (tvdb, trakt, moviedb, etc), and downloads missing images.
        api_response = api_instance.action_run_import_get()
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ActionApi->action_run_import_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#action_run_import_get.ApiResponseFor200) | Success

#### action_run_import_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **action_sync_hashes_get**
<a id="action_sync_hashes_get"></a>
> action_sync_hashes_get()

This was for web cache hash syncing, and will be for perceptual hashing maybe eventually.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import action_api
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
    api_instance = action_api.ActionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # This was for web cache hash syncing, and will be for perceptual hashing maybe eventually.
        api_response = api_instance.action_sync_hashes_get()
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ActionApi->action_sync_hashes_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#action_sync_hashes_get.ApiResponseFor200) | Success

#### action_sync_hashes_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **action_sync_my_list_get**
<a id="action_sync_my_list_get"></a>
> action_sync_my_list_get()

BEWARE this is a dangerous command!  It syncs all of the states in Shoko's library to AniDB.  ONE WAY. THIS CAN ERASE ANIDB DATA IRREVERSIBLY

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import action_api
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
    api_instance = action_api.ActionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # BEWARE this is a dangerous command!  It syncs all of the states in Shoko's library to AniDB.  ONE WAY. THIS CAN ERASE ANIDB DATA IRREVERSIBLY
        api_response = api_instance.action_sync_my_list_get()
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ActionApi->action_sync_my_list_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#action_sync_my_list_get.ApiResponseFor200) | Success

#### action_sync_my_list_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **action_sync_trakt_get**
<a id="action_sync_trakt_get"></a>
> action_sync_trakt_get()

Sync Trakt states. Requires Trakt to be set up, obviously

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import action_api
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
    api_instance = action_api.ActionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Sync Trakt states. Requires Trakt to be set up, obviously
        api_response = api_instance.action_sync_trakt_get()
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ActionApi->action_sync_trakt_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#action_sync_trakt_get.ApiResponseFor200) | Success

#### action_sync_trakt_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **action_sync_votes_get**
<a id="action_sync_votes_get"></a>
> action_sync_votes_get()

Sync the votes from Shoko to AniDB.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import action_api
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
    api_instance = action_api.ActionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Sync the votes from Shoko to AniDB.
        api_response = api_instance.action_sync_votes_get()
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ActionApi->action_sync_votes_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#action_sync_votes_get.ApiResponseFor200) | Success

#### action_sync_votes_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **action_update_all_ani_db_info_get**
<a id="action_update_all_ani_db_info_get"></a>
> action_update_all_ani_db_info_get()

Update All AniDB Series Info

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import action_api
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
    api_instance = action_api.ActionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Update All AniDB Series Info
        api_response = api_instance.action_update_all_ani_db_info_get()
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ActionApi->action_update_all_ani_db_info_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#action_update_all_ani_db_info_get.ApiResponseFor200) | Success

#### action_update_all_ani_db_info_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **action_update_all_images_get**
<a id="action_update_all_images_get"></a>
> action_update_all_images_get()

Updates and Downloads Missing Images

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import action_api
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
    api_instance = action_api.ActionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Updates and Downloads Missing Images
        api_response = api_instance.action_update_all_images_get()
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ActionApi->action_update_all_images_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#action_update_all_images_get.ApiResponseFor200) | Success

#### action_update_all_images_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **action_update_all_media_info_get**
<a id="action_update_all_media_info_get"></a>
> action_update_all_media_info_get()

Queues a task to Update all media info

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import action_api
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
    api_instance = action_api.ActionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Queues a task to Update all media info
        api_response = api_instance.action_update_all_media_info_get()
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ActionApi->action_update_all_media_info_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#action_update_all_media_info_get.ApiResponseFor200) | Success

#### action_update_all_media_info_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **action_update_all_movie_db_info_get**
<a id="action_update_all_movie_db_info_get"></a>
> action_update_all_movie_db_info_get()

Updates All MovieDB Info

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import action_api
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
    api_instance = action_api.ActionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Updates All MovieDB Info
        api_response = api_instance.action_update_all_movie_db_info_get()
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ActionApi->action_update_all_movie_db_info_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#action_update_all_movie_db_info_get.ApiResponseFor200) | Success

#### action_update_all_movie_db_info_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **action_update_all_trakt_info_get**
<a id="action_update_all_trakt_info_get"></a>
> action_update_all_trakt_info_get()

Update all Trakt info. Right now, that's not much.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import action_api
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
    api_instance = action_api.ActionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Update all Trakt info. Right now, that's not much.
        api_response = api_instance.action_update_all_trakt_info_get()
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ActionApi->action_update_all_trakt_info_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#action_update_all_trakt_info_get.ApiResponseFor200) | Success

#### action_update_all_trakt_info_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **action_update_all_tv_db_info_get**
<a id="action_update_all_tv_db_info_get"></a>
> action_update_all_tv_db_info_get()

Update All TvDB Series Info

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import action_api
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
    api_instance = action_api.ActionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Update All TvDB Series Info
        api_response = api_instance.action_update_all_tv_db_info_get()
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ActionApi->action_update_all_tv_db_info_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#action_update_all_tv_db_info_get.ApiResponseFor200) | Success

#### action_update_all_tv_db_info_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **action_update_ani_db_calendar_get**
<a id="action_update_ani_db_calendar_get"></a>
> action_update_ani_db_calendar_get()

Update the AniDB Calendar data for use on the dashboard.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import action_api
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
    api_instance = action_api.ActionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Update the AniDB Calendar data for use on the dashboard.
        api_response = api_instance.action_update_ani_db_calendar_get()
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ActionApi->action_update_ani_db_calendar_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#action_update_ani_db_calendar_get.ApiResponseFor200) | Success

#### action_update_ani_db_calendar_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **action_update_missing_ani_db_file_info_get**
<a id="action_update_missing_ani_db_file_info_get"></a>
> action_update_missing_ani_db_file_info_get()

Update AniDB Files with missing file info, including with missing release  groups and/or with out-of-date internal data versions.

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import action_api
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
    api_instance = action_api.ActionApi(api_client)

    # example passing only optional values
    query_params = {
        'missingInfo': True,
        'outOfDate': False,
    }
    try:
        # Update AniDB Files with missing file info, including with missing release  groups and/or with out-of-date internal data versions.
        api_response = api_instance.action_update_missing_ani_db_file_info_get(
            query_params=query_params,
        )
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ActionApi->action_update_missing_ani_db_file_info_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
missingInfo | MissingInfoSchema | | optional
outOfDate | OutOfDateSchema | | optional


# MissingInfoSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of True

# OutOfDateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#action_update_missing_ani_db_file_info_get.ApiResponseFor200) | Success

#### action_update_missing_ani_db_file_info_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **action_update_series_stats_get**
<a id="action_update_series_stats_get"></a>
> action_update_series_stats_get()

Queues commands to Update All Series Stats and Force a Recalculation of All Group Filters

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import action_api
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
    api_instance = action_api.ActionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Queues commands to Update All Series Stats and Force a Recalculation of All Group Filters
        api_response = api_instance.action_update_series_stats_get()
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ActionApi->action_update_series_stats_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#action_update_series_stats_get.ApiResponseFor200) | Success

#### action_update_series_stats_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **action_validate_all_images_get**
<a id="action_validate_all_images_get"></a>
> action_validate_all_images_get()

Validates invalid images and redownloads them

### Example

* Api Key Authentication (ApiKey):
```python
import lib.shoko.v3
from lib.shoko.v3.lib.shoko.v3.api.tags import action_api
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
    api_instance = action_api.ActionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Validates invalid images and redownloads them
        api_response = api_instance.action_validate_all_images_get()
    except lib.shoko.v3.ApiException as e:
        print("Exception when calling ActionApi->action_validate_all_images_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#action_validate_all_images_get.ApiResponseFor200) | Success

#### action_validate_all_images_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

