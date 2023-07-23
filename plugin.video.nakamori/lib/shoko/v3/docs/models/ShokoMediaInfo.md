# lib.shoko.v3.lib.shoko.v3.models.shoko_media_info.ShokoMediaInfo

Parsed information from a Shoko.Server.API.v3.Models.Shoko.MediaInfo.MediaContainer.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Parsed information from a Shoko.Server.API.v3.Models.Shoko.MediaInfo.MediaContainer. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Title** | None, str,  | NoneClass, str,  | General title for the media. | [optional] 
**Duration** | str,  | str,  | Overall duration of the media. | [optional] 
**BitRate** | decimal.Decimal, int,  | decimal.Decimal,  | Overall bit-rate across all streams in the media container. | [optional] value must be a 32 bit integer
**FrameRate** | decimal.Decimal, int, float,  | decimal.Decimal,  | Average frame-rate across all the streams in the media container. | [optional] value must be a 64 bit float
**Encoded** | None, str, datetime,  | NoneClass, str,  | Date when encoding took place, if known. | [optional] value must conform to RFC-3339 date-time
**IsStreamable** | bool,  | BoolClass,  | True if the media is streaming-friendly. | [optional] 
**FileExtension** | None, str,  | NoneClass, str,  | Common file extension for the media container format. | [optional] 
**MediaContainer** | None, str,  | NoneClass, str,  | The media container format. | [optional] 
**MediaContainerVersion** | decimal.Decimal, int,  | decimal.Decimal,  | The media container format version. | [optional] value must be a 32 bit integer
**[Video](#Video)** | list, tuple, None,  | tuple, NoneClass,  | Video streams in the media container. | [optional] 
**[Audio](#Audio)** | list, tuple, None,  | tuple, NoneClass,  | Audio streams in the media container. | [optional] 
**[Subtitles](#Subtitles)** | list, tuple, None,  | tuple, NoneClass,  | Sub-title (text) streams in the media container. | [optional] 
**[Chapters](#Chapters)** | list, tuple, None,  | tuple, NoneClass,  | Chapter information present in the media container. | [optional] 

# Video

Video streams in the media container.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | Video streams in the media container. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**MediaInfoVideoStreamInfo**](MediaInfoVideoStreamInfo.md) | [**MediaInfoVideoStreamInfo**](MediaInfoVideoStreamInfo.md) | [**MediaInfoVideoStreamInfo**](MediaInfoVideoStreamInfo.md) |  | 

# Audio

Audio streams in the media container.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | Audio streams in the media container. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**MediaInfoAudioStreamInfo**](MediaInfoAudioStreamInfo.md) | [**MediaInfoAudioStreamInfo**](MediaInfoAudioStreamInfo.md) | [**MediaInfoAudioStreamInfo**](MediaInfoAudioStreamInfo.md) |  | 

# Subtitles

Sub-title (text) streams in the media container.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | Sub-title (text) streams in the media container. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**MediaInfoTextStreamInfo**](MediaInfoTextStreamInfo.md) | [**MediaInfoTextStreamInfo**](MediaInfoTextStreamInfo.md) | [**MediaInfoTextStreamInfo**](MediaInfoTextStreamInfo.md) |  | 

# Chapters

Chapter information present in the media container.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | Chapter information present in the media container. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**MediaInfoChapterInfo**](MediaInfoChapterInfo.md) | [**MediaInfoChapterInfo**](MediaInfoChapterInfo.md) | [**MediaInfoChapterInfo**](MediaInfoChapterInfo.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

