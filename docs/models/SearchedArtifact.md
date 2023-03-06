# apicurioregistryclient.model.searched_artifact.SearchedArtifact

Models a single artifact from the result set returned when searching for artifacts.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Models a single artifact from the result set returned when searching for artifacts. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**createdBy** | str,  | str,  |  | 
**id** | str,  | str,  | The ID of a single artifact. | 
**state** | [**ArtifactState**](ArtifactState.md) | [**ArtifactState**](ArtifactState.md) |  | 
**type** | str,  | str,  |  | 
**createdOn** | str,  | str,  |  | 
**group** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**name** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**[labels](#labels)** | list, tuple,  | tuple,  |  | [optional] 
**modifiedOn** | str,  | str,  |  | [optional] 
**modifiedBy** | str,  | str,  |  | [optional] 
**groupId** | str,  | str,  | An ID of a single artifact group. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# labels

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

