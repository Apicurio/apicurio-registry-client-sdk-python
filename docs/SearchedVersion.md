# SearchedVersion

Models a single artifact from the result set returned when searching for artifacts.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_on** | **str** |  | 
**created_by** | **str** |  | 
**type** | [**ArtifactType**](ArtifactType.md) |  | 
**state** | [**ArtifactState**](ArtifactState.md) |  | 
**global_id** | **int** |  | 
**version** | **str** |  | 
**content_id** | **int** |  | 
**references** | [**[ArtifactReference]**](ArtifactReference.md) |  | 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**labels** | **[str]** |  | [optional] 
**properties** | [**Properties**](Properties.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


