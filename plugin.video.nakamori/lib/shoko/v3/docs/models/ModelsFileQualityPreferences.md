# lib.shoko.v3.lib.shoko.v3.models.models_file_quality_preferences.ModelsFileQualityPreferences

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Require10BitVideo** | bool,  | BoolClass,  |  | [optional] 
**MaxNumberOfFilesToKeep** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**[PreferredTypes](#PreferredTypes)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 
**[PreferredAudioCodecs](#PreferredAudioCodecs)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 
**[PreferredResolutions](#PreferredResolutions)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 
**[PreferredSubGroups](#PreferredSubGroups)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 
**[PreferredVideoCodecs](#PreferredVideoCodecs)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 
**Prefer8BitVideo** | bool,  | BoolClass,  |  | [optional] 
**AllowDeletionOfImportedFiles** | bool,  | BoolClass,  |  | [optional] 
**[RequiredTypes](#RequiredTypes)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 
**RequiredAudioCodecs** | [**FileQualityTypeListPairListSystemString**](FileQualityTypeListPairListSystemString.md) | [**FileQualityTypeListPairListSystemString**](FileQualityTypeListPairListSystemString.md) |  | [optional] 
**RequiredAudioStreamCount** | [**FileQualityTypeListPairSystemInt32**](FileQualityTypeListPairSystemInt32.md) | [**FileQualityTypeListPairSystemInt32**](FileQualityTypeListPairSystemInt32.md) |  | [optional] 
**RequiredResolutions** | [**FileQualityTypeListPairListSystemString**](FileQualityTypeListPairListSystemString.md) | [**FileQualityTypeListPairListSystemString**](FileQualityTypeListPairListSystemString.md) |  | [optional] 
**RequiredSources** | [**FileQualityTypeListPairListSystemString**](FileQualityTypeListPairListSystemString.md) | [**FileQualityTypeListPairListSystemString**](FileQualityTypeListPairListSystemString.md) |  | [optional] 
**RequiredSubGroups** | [**FileQualityTypeListPairListSystemString**](FileQualityTypeListPairListSystemString.md) | [**FileQualityTypeListPairListSystemString**](FileQualityTypeListPairListSystemString.md) |  | [optional] 
**RequiredSubStreamCount** | [**FileQualityTypeListPairSystemInt32**](FileQualityTypeListPairSystemInt32.md) | [**FileQualityTypeListPairSystemInt32**](FileQualityTypeListPairSystemInt32.md) |  | [optional] 
**RequiredVideoCodecs** | [**FileQualityTypeListPairListSystemString**](FileQualityTypeListPairListSystemString.md) | [**FileQualityTypeListPairListSystemString**](FileQualityTypeListPairListSystemString.md) |  | [optional] 
**[PreferredSources](#PreferredSources)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 
**AllowDeletingFilesWithMissingInfo** | bool,  | BoolClass,  |  | [optional] 

# PreferredTypes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EnumsFileQualityFilterType**](EnumsFileQualityFilterType.md) | [**EnumsFileQualityFilterType**](EnumsFileQualityFilterType.md) | [**EnumsFileQualityFilterType**](EnumsFileQualityFilterType.md) |  | 

# PreferredAudioCodecs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# PreferredResolutions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# PreferredSubGroups

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# PreferredVideoCodecs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# RequiredTypes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EnumsFileQualityFilterType**](EnumsFileQualityFilterType.md) | [**EnumsFileQualityFilterType**](EnumsFileQualityFilterType.md) | [**EnumsFileQualityFilterType**](EnumsFileQualityFilterType.md) |  | 

# PreferredSources

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

