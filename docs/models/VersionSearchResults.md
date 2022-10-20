# apicurioregistryclient.model.version_search_results.VersionSearchResults

Describes the response received when searching for artifacts.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Describes the response received when searching for artifacts. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[versions](#versions)** | list, tuple,  | tuple,  | The collection of artifact versions returned in the result set. | 
**count** | decimal.Decimal, int,  | decimal.Decimal,  | The total number of versions that matched the query (may be more than the number of versions returned in the result set). | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# versions

The collection of artifact versions returned in the result set.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The collection of artifact versions returned in the result set. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SearchedVersion**](SearchedVersion.md) | [**SearchedVersion**](SearchedVersion.md) | [**SearchedVersion**](SearchedVersion.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

