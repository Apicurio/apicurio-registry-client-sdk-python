# apicurioregistryclient.model.searched_version.SearchedVersion

Models a single artifact from the result set returned when searching for artifacts.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Models a single artifact from the result set returned when searching for artifacts. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[references](#references)** | list, tuple,  | tuple,  |  | 
**createdBy** | str,  | str,  |  | 
**contentId** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**globalId** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**state** | [**ArtifactState**](ArtifactState.md) | [**ArtifactState**](ArtifactState.md) |  | 
**type** | [**ArtifactType**](ArtifactType.md) | [**ArtifactType**](ArtifactType.md) |  | 
**createdOn** | str,  | str,  |  | 
**version** | str,  | str,  |  | 
**name** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**[labels](#labels)** | list, tuple,  | tuple,  |  | [optional] 
**properties** | [**Properties**](Properties.md) | [**Properties**](Properties.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# references

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ArtifactReference**](ArtifactReference.md) | [**ArtifactReference**](ArtifactReference.md) | [**ArtifactReference**](ArtifactReference.md) |  | 

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

