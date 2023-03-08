# apicurioregistryclient.model.version_meta_data.VersionMetaData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**createdBy** | str,  | str,  |  | 
**contentId** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**globalId** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**id** | str,  | str,  | The ID of a single artifact. | 
**type** | str,  | str,  |  | 
**createdOn** | str,  | str,  |  | 
**version** | str,  | str,  |  | 
**name** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**state** | [**ArtifactState**](ArtifactState.md) | [**ArtifactState**](ArtifactState.md) |  | [optional] 
**[labels](#labels)** | list, tuple,  | tuple,  |  | [optional] 
**properties** | [**Properties**](Properties.md) | [**Properties**](Properties.md) |  | [optional] 
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

