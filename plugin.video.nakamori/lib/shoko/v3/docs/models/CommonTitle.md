# lib.shoko.v3.lib.shoko.v3.models.common_title.CommonTitle

Title object, stores the title, type, language, and source  if using a TvDB title, assume \"eng:official\". If using AniList, assume \"x-jat:main\"  AniDB's MainTitle is \"x-jat:main\"

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Title object, stores the title, type, language, and source  if using a TvDB title, assume \&quot;eng:official\&quot;. If using AniList, assume \&quot;x-jat:main\&quot;  AniDB&#x27;s MainTitle is \&quot;x-jat:main\&quot; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Language** | str,  | str,  | convert to AniDB style (x-jat is the special one, but most are standard 3-digit short names) | 
**Source** | str,  | str,  | AniDB, TvDB, AniList, etc | 
**Name** | str,  | str,  | the title | 
**Type** | [**DataModelsTitleType**](DataModelsTitleType.md) | [**DataModelsTitleType**](DataModelsTitleType.md) |  | [optional] 
**Default** | bool,  | BoolClass,  | If this is the default title | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

