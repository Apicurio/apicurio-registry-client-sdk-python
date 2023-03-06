# apicurioregistryclient.model.artifact_search_results.ArtifactSearchResults

Describes the response received when searching for artifacts.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Describes the response received when searching for artifacts. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**count** | decimal.Decimal, int,  | decimal.Decimal,  | The total number of artifacts that matched the query that produced the result set (may be  more than the number of artifacts in the result set). | 
**[artifacts](#artifacts)** | list, tuple,  | tuple,  | The artifacts returned in the result set. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# artifacts

The artifacts returned in the result set.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The artifacts returned in the result set. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SearchedArtifact**](SearchedArtifact.md) | [**SearchedArtifact**](SearchedArtifact.md) | [**SearchedArtifact**](SearchedArtifact.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

