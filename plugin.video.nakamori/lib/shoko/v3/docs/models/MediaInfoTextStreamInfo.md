# lib.shoko.v3.lib.shoko.v3.models.media_info_text_stream_info.MediaInfoTextStreamInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**SubTitle** | None, str,  | NoneClass, str,  | Sub-title of the text stream. | [optional] 
**IsExternal** | bool,  | BoolClass,  | Not From MediaInfo. Is this an external sub file | [optional] 
**ExternalFilename** | None, str,  | NoneClass, str,  | The name of the external subtitle file if this is stream is from an  external source. This field is only sent if Shoko.Server.API.v3.Models.Shoko.MediaInfo.TextStreamInfo.IsExternal  is set to &#x60;&#x60;&#x60;true&#x60;&#x60;&#x60;. | [optional] 
**ID** | decimal.Decimal, int,  | decimal.Decimal,  | Local id for the stream. | [optional] value must be a 32 bit integer
**UID** | None, str,  | NoneClass, str,  | Unique id for the stream. | [optional] 
**Title** | None, str,  | NoneClass, str,  | Stream title, if available. | [optional] 
**Order** | decimal.Decimal, int,  | decimal.Decimal,  | Stream order. | [optional] value must be a 32 bit integer
**IsDefault** | bool,  | BoolClass,  | True if this is the default stream of the given type. | [optional] 
**IsForced** | bool,  | BoolClass,  | True if the stream is forced to be used. | [optional] 
**Language** | [**DataModelsTitleLanguage**](DataModelsTitleLanguage.md) | [**DataModelsTitleLanguage**](DataModelsTitleLanguage.md) |  | [optional] 
**LanguageCode** | None, str,  | NoneClass, str,  | 3 character language code of the language of the stream. | [optional] 
**Codec** | [**MediaInfoStreamCodecInfo**](MediaInfoStreamCodecInfo.md) | [**MediaInfoStreamCodecInfo**](MediaInfoStreamCodecInfo.md) |  | [optional] 
**Format** | [**MediaInfoStreamFormatInfo**](MediaInfoStreamFormatInfo.md) | [**MediaInfoStreamFormatInfo**](MediaInfoStreamFormatInfo.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

