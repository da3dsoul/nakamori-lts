# lib.shoko.v3.lib.shoko.v3.models.common_image.CommonImage

Image container

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Image container | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Type** | [**ImageImageType**](ImageImageType.md) | [**ImageImageType**](ImageImageType.md) |  | 
**ID** | str,  | str,  | The image&#x27;s ID, usually an int, but in the case of Static resources, it is the resource name. | 
**Source** | [**ImageImageSource**](ImageImageSource.md) | [**ImageImageSource**](ImageImageSource.md) |  | 
**RelativeFilepath** | None, str,  | NoneClass, str,  | The relative path from the base image directory. A client with access to the server&#x27;s filesystem can map  these for quick access and no need for caching | [optional] 
**Preferred** | bool,  | BoolClass,  | Is it marked as default. Only one default is possible for a given Shoko.Server.API.v3.Models.Common.Image.Type. | [optional] 
**Width** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Width of the image. | [optional] value must be a 32 bit integer
**Height** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Height of the image. | [optional] value must be a 32 bit integer
**Disabled** | bool,  | BoolClass,  | Is it marked as disabled. You must explicitly ask for these, for obvious reasons. | [optional] 
**Series** | [**ImageImageSeriesInfo**](ImageImageSeriesInfo.md) | [**ImageImageSeriesInfo**](ImageImageSeriesInfo.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

