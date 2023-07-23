# lib.shoko.v3.lib.shoko.v3.models.episode_tv_db.EpisodeTvDB

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ID** | decimal.Decimal, int,  | decimal.Decimal,  | TvDB Episode ID | [optional] value must be a 32 bit integer
**Season** | decimal.Decimal, int,  | decimal.Decimal,  | Season Number, 0 is Specials. TvDB&#x27;s Season system doesn&#x27;t always make sense for anime, so don&#x27;t count on it | [optional] value must be a 32 bit integer
**Number** | decimal.Decimal, int,  | decimal.Decimal,  | Episode Number in the Season. This is not Absolute Number | [optional] value must be a 32 bit integer
**AbsoluteNumber** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Absolute Episode Number. Keep in mind that due to reordering, this may not be accurate. | [optional] value must be a 32 bit integer
**Title** | None, str,  | NoneClass, str,  | Episode Title, in the language selected for TvDB. TvDB doesn&#x27;t allow pulling more than one language at a time, so this isn&#x27;t a list. | [optional] 
**Description** | None, str,  | NoneClass, str,  | Episode Description, in the language selected for TvDB. See Title for more info on Language. | [optional] 
**AirDate** | None, str, datetime,  | NoneClass, str,  | Air Date. Unfortunately, the TvDB air date doesn&#x27;t necessarily conform to a specific timezone, so it can be a day off. If you see one that&#x27;s wrong, please fix it on TvDB. You have the ID here in this model for easy lookup. | [optional] value must conform to RFC-3339 date-time
**AirsAfterSeason** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Mostly for specials. It shows when in the timeline the episode aired. I wouldn&#x27;t count on it, as it&#x27;s often blank. | [optional] value must be a 32 bit integer
**AirsBeforeSeason** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Mostly for specials. It shows when in the timeline the episode aired. I wouldn&#x27;t count on it, as it&#x27;s often blank. | [optional] value must be a 32 bit integer
**AirsBeforeEpisode** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Like AirsAfterSeason, it is for determining where in the timeline an episode airs. Also often blank. | [optional] value must be a 32 bit integer
**Rating** | [**CommonRating**](CommonRating.md) | [**CommonRating**](CommonRating.md) |  | [optional] 
**Thumbnail** | [**CommonImage**](CommonImage.md) | [**CommonImage**](CommonImage.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

