# lib.shoko.v3.lib.shoko.v3.models.role_person.RolePerson

A generic person object with the name, altname, description, and image

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A generic person object with the name, altname, description, and image | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Name** | str,  | str,  | Main Name, romanized if needed  ex. Sawano Hiroyuki | 
**AlternateName** | None, str,  | NoneClass, str,  | Alternate Name, this can be any other name, whether kanji, an alias, etc  ex. 澤野弘之 | [optional] 
**Description** | None, str,  | NoneClass, str,  | A description, bio, etc  ex. Sawano Hiroyuki was born September 12, 1980 in Tokyo, Japan. He is a composer and arranger. | [optional] 
**Image** | [**CommonImage**](CommonImage.md) | [**CommonImage**](CommonImage.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

