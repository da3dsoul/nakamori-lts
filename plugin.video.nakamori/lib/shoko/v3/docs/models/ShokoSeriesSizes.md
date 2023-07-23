# lib.shoko.v3.lib.shoko.v3.models.shoko_series_sizes.ShokoSeriesSizes

Downloaded, Watched, Total, etc

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Downloaded, Watched, Total, etc | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Total** | [**SeriesSizesEpisodeTypeCounts**](SeriesSizesEpisodeTypeCounts.md) | [**SeriesSizesEpisodeTypeCounts**](SeriesSizesEpisodeTypeCounts.md) |  | 
**Local** | [**SeriesSizesEpisodeTypeCounts**](SeriesSizesEpisodeTypeCounts.md) | [**SeriesSizesEpisodeTypeCounts**](SeriesSizesEpisodeTypeCounts.md) |  | 
**FileSources** | [**SeriesSizesFileSourceCounts**](SeriesSizesFileSourceCounts.md) | [**SeriesSizesFileSourceCounts**](SeriesSizesFileSourceCounts.md) |  | 
**Missing** | decimal.Decimal, int,  | decimal.Decimal,  | Count of missing episodes that are not hidden. | [optional] value must be a 32 bit integer
**Hidden** | decimal.Decimal, int,  | decimal.Decimal,  | Count of hidden episodes, be it available or missing. | [optional] value must be a 32 bit integer
**Watched** | [**SeriesSizesEpisodeTypeCounts**](SeriesSizesEpisodeTypeCounts.md) | [**SeriesSizesEpisodeTypeCounts**](SeriesSizesEpisodeTypeCounts.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

