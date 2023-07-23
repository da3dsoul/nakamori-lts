# lib.shoko.v3.lib.shoko.v3.models.media_info_audio_stream_info.MediaInfoAudioStreamInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Channels** | decimal.Decimal, int,  | decimal.Decimal,  | Number of total channels in the audio stream. | [optional] value must be a 32 bit integer
**ChannelLayout** | None, str,  | NoneClass, str,  | A text representation of the layout of the channels available in the  audio stream. | [optional] 
**SamplesPerFrame** | decimal.Decimal, int,  | decimal.Decimal,  | Samples per frame. | [optional] value must be a 32 bit integer
**SamplingRate** | decimal.Decimal, int,  | decimal.Decimal,  | Sampling rate of the audio. | [optional] value must be a 32 bit integer
**CompressionMode** | None, str,  | NoneClass, str,  | Compression mode used. | [optional] 
**BitRate** | decimal.Decimal, int,  | decimal.Decimal,  | Bit-rate of the audio-stream. | [optional] value must be a 32 bit integer
**BitRateMode** | None, str,  | NoneClass, str,  | Bit-rate mode of the audio stream. | [optional] 
**BitDepth** | decimal.Decimal, int,  | decimal.Decimal,  | Bit-depth of the audio stream. | [optional] value must be a 32 bit integer
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

