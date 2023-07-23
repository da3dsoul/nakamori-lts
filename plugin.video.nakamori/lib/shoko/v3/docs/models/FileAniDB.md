# lib.shoko.v3.lib.shoko.v3.models.file_ani_db.FileAniDB

AniDB_File info

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | AniDB_File info | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ID** | decimal.Decimal, int,  | decimal.Decimal,  | The AniDB File ID | [optional] value must be a 32 bit integer
**Source** | [**ShokoFileSource**](ShokoFileSource.md) | [**ShokoFileSource**](ShokoFileSource.md) |  | [optional] 
**ReleaseGroup** | [**AniDBAniDBReleaseGroup**](AniDBAniDBReleaseGroup.md) | [**AniDBAniDBReleaseGroup**](AniDBAniDBReleaseGroup.md) |  | [optional] 
**ReleaseDate** | None, str, datetime,  | NoneClass, str,  | The file&#x27;s release date. This is probably not filled in | [optional] value must conform to RFC-3339 date-time
**Version** | decimal.Decimal, int,  | decimal.Decimal,  | The file&#x27;s version, Usually 1, sometimes more when there are edits released later | [optional] value must be a 32 bit integer
**IsDeprecated** | bool,  | BoolClass,  | Is the file marked as deprecated. Generally, yes if there&#x27;s a V2, and this isn&#x27;t it | [optional] 
**IsCensored** | None, bool,  | NoneClass, BoolClass,  | Mostly applicable to hentai, but on occasion a TV release is censored enough to earn this. | [optional] 
**OriginalFileName** | None, str,  | NoneClass, str,  | The original FileName. Useful for when you obtained from a shady source or when you renamed it without thinking. | [optional] 
**FileSize** | decimal.Decimal, int,  | decimal.Decimal,  | The reported FileSize. If you got this far and it doesn&#x27;t match, something very odd has occurred | [optional] value must be a 64 bit integer
**Duration** | str,  | str,  | The reported duration of the file | [optional] 
**Description** | None, str,  | NoneClass, str,  | Any comments that were added to the file, such as something wrong with it. | [optional] 
**[AudioLanguages](#AudioLanguages)** | list, tuple, None,  | tuple, NoneClass,  | The audio languages | [optional] 
**[SubLanguages](#SubLanguages)** | list, tuple, None,  | tuple, NoneClass,  | Sub languages | [optional] 
**Chaptered** | bool,  | BoolClass,  | Does the file have chapters. This may be wrong, since it was only added in AVDump2 (a more recent version at that) | [optional] 
**Updated** | str, datetime,  | str,  | When we last got data on this file | [optional] value must conform to RFC-3339 date-time

# AudioLanguages

The audio languages

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The audio languages | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# SubLanguages

Sub languages

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | Sub languages | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

