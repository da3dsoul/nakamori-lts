# lib.shoko.v3.lib.shoko.v3.models.shoko_file.ShokoFile

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ID** | decimal.Decimal, int,  | decimal.Decimal,  | The ID of the File. You&#x27;ll need this to play it. | [optional] value must be a 32 bit integer
**[SeriesIDs](#SeriesIDs)** | list, tuple, None,  | tuple, NoneClass,  | The Cross Reference Models for every episode this file belongs to, created in a reverse tree and  transformed back into a tree. Series -&gt; Episode such that only episodes that this file is linked to are  shown. In many cases, this will have arrays of 1 item | [optional] 
**Size** | decimal.Decimal, int,  | decimal.Decimal,  | The Filesize in bytes | [optional] value must be a 64 bit integer
**IsVariation** | bool,  | BoolClass,  | If this file is marked as a file variation. | [optional] 
**Hashes** | [**ServerHashes**](ServerHashes.md) | [**ServerHashes**](ServerHashes.md) |  | [optional] 
**[Locations](#Locations)** | list, tuple, None,  | tuple, NoneClass,  | All of the Locations that this file exists in | [optional] 
**Resolution** | None, str,  | NoneClass, str,  | Try to fit this file&#x27;s resolution to something like 1080p, 480p, etc | [optional] 
**Duration** | str,  | str,  | The duration of the file. | [optional] 
**ResumePosition** | None, str,  | NoneClass, str,  | Where to resume the next playback. | [optional] 
**Viewed** | None, str, datetime,  | NoneClass, str,  | The last time the current user viewed the file. Will be null if the user  have not viewed the file yet. | [optional] value must conform to RFC-3339 date-time
**Watched** | None, str, datetime,  | NoneClass, str,  | The last time the current user watched the file until completion, or  otherwise marked the file was watched. Will be null if the user have not  watched the file yet. | [optional] value must conform to RFC-3339 date-time
**Imported** | None, str, datetime,  | NoneClass, str,  | When the file was last imported. Usually is a file only imported once,  but there may be exceptions. | [optional] value must conform to RFC-3339 date-time
**Created** | str, datetime,  | str,  | The file creation date of this file | [optional] value must conform to RFC-3339 date-time
**Updated** | str, datetime,  | str,  | When the file was last updated (e.g. the hashes were added/updated). | [optional] value must conform to RFC-3339 date-time
**AniDB** | [**FileAniDB**](FileAniDB.md) | [**FileAniDB**](FileAniDB.md) |  | [optional] 
**MediaInfo** | [**ShokoMediaInfo**](ShokoMediaInfo.md) | [**ShokoMediaInfo**](ShokoMediaInfo.md) |  | [optional] 

# SeriesIDs

The Cross Reference Models for every episode this file belongs to, created in a reverse tree and  transformed back into a tree. Series -> Episode such that only episodes that this file is linked to are  shown. In many cases, this will have arrays of 1 item

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The Cross Reference Models for every episode this file belongs to, created in a reverse tree and  transformed back into a tree. Series -&gt; Episode such that only episodes that this file is linked to are  shown. In many cases, this will have arrays of 1 item | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FileSeriesCrossReference**](FileSeriesCrossReference.md) | [**FileSeriesCrossReference**](FileSeriesCrossReference.md) | [**FileSeriesCrossReference**](FileSeriesCrossReference.md) |  | 

# Locations

All of the Locations that this file exists in

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | All of the Locations that this file exists in | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FileLocation**](FileLocation.md) | [**FileLocation**](FileLocation.md) | [**FileLocation**](FileLocation.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

