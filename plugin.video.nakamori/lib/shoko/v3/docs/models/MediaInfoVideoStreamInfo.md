# lib.shoko.v3.lib.shoko.v3.models.media_info_video_stream_info.MediaInfoVideoStreamInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Width** | decimal.Decimal, int,  | decimal.Decimal,  | Width of the video stream. | [optional] value must be a 32 bit integer
**Height** | decimal.Decimal, int,  | decimal.Decimal,  | Height of the video stream. | [optional] value must be a 32 bit integer
**Resolution** | None, str,  | NoneClass, str,  | Standarized resolution. | [optional] 
**PixelAspectRatio** | decimal.Decimal, int, float,  | decimal.Decimal,  | Pixel aspect-ratio. | [optional] value must be a 64 bit float
**FrameRate** | decimal.Decimal, int, float,  | decimal.Decimal,  | Frame-rate. | [optional] value must be a 64 bit float
**FrameRateMode** | None, str,  | NoneClass, str,  | Frame-rate mode. | [optional] 
**FrameCount** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of frames in the video stream. | [optional] value must be a 32 bit integer
**ScanType** | None, str,  | NoneClass, str,  | Scan-type. Interlaced or progressive. | [optional] 
**ColorSpace** | None, str,  | NoneClass, str,  | Color-space. | [optional] 
**ChromaSubsampling** | None, str,  | NoneClass, str,  | Chroma sub-sampling. | [optional] 
**MatrixCoefficients** | None, str,  | NoneClass, str,  | Matrix co-efficients. | [optional] 
**BitRate** | decimal.Decimal, int,  | decimal.Decimal,  | Bit-rate of the video stream. | [optional] value must be a 32 bit integer
**BitDepth** | decimal.Decimal, int,  | decimal.Decimal,  | Bit-depth of the video stream. | [optional] value must be a 32 bit integer
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

