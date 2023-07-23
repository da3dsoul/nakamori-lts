# lib.shoko.v3.lib.shoko.v3.models.dashboard_series_summary.DashboardSeriesSummary

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Series** | decimal.Decimal, int,  | decimal.Decimal,  | The number of normal Series | [optional] value must be a 32 bit integer
**OVA** | decimal.Decimal, int,  | decimal.Decimal,  | The Number of OVAs | [optional] value must be a 32 bit integer
**Movie** | decimal.Decimal, int,  | decimal.Decimal,  | The Number of Movies | [optional] value must be a 32 bit integer
**Special** | decimal.Decimal, int,  | decimal.Decimal,  | The Number of TV Specials | [optional] value must be a 32 bit integer
**Web** | decimal.Decimal, int,  | decimal.Decimal,  | ONAs and the like, it&#x27;s more of a new concept | [optional] value must be a 32 bit integer
**Other** | decimal.Decimal, int,  | decimal.Decimal,  | Things marked on AniDB as Other, different from None | [optional] value must be a 32 bit integer
**None** | decimal.Decimal, int,  | decimal.Decimal,  | Series that don&#x27;t have AniDB Records. This is very bad, and usually means there was an error in the import process. It can also happen if the API is hit at just the right time. | [optional] value must be a 32 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

