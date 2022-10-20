# apicurioregistryclient.model.error.Error

All error responses, whether `4xx` or `5xx` will include one of these as the response body.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | All error responses, whether &#x60;4xx&#x60; or &#x60;5xx&#x60; will include one of these as the response body. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**message** | str,  | str,  | The short error message. | [optional] 
**error_code** | decimal.Decimal, int,  | decimal.Decimal,  | The server-side error code. | [optional] value must be a 32 bit integer
**detail** | str,  | str,  | Full details about the error.  This might contain a server stack trace, for example. | [optional] 
**name** | str,  | str,  | The error name - typically the classname of the exception thrown by the server. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

