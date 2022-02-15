# Error

All error responses, whether `4xx` or `5xx` will include one of these as the response body.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The short error message. | [optional] 
**error_code** | **int** | The server-side error code. | [optional] 
**detail** | **str** | Full details about the error.  This might contain a server stack trace, for example. | [optional] 
**name** | **str** | The error name - typically the classname of the exception thrown by the server. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


