<a id="__pageTop"></a>
# apicurioregistryclient.apis.tags.artifact_type_api.ArtifactTypeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_artifact_types**](#list_artifact_types) | **get** /admin/artifactTypes | List artifact types

# **list_artifact_types**
<a id="list_artifact_types"></a>
> [ArtifactTypeInfo] list_artifact_types()

List artifact types

Gets a list of all the configured artifact types.  This operation can fail for the following reasons:  * A server error occurred (HTTP error `500`) 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import artifact_type_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.artifact_type_info import ArtifactTypeInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = artifact_type_api.ArtifactTypeApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List artifact types
        api_response = api_instance.list_artifact_types()
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling ArtifactTypeApi->list_artifact_types: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_artifact_types.ApiResponseFor200) | The list of available artifact types.
500 | [ApiResponseFor500](#list_artifact_types.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### list_artifact_types.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ArtifactTypeInfo**]({{complexTypePrefix}}ArtifactTypeInfo.md) | [**ArtifactTypeInfo**]({{complexTypePrefix}}ArtifactTypeInfo.md) | [**ArtifactTypeInfo**]({{complexTypePrefix}}ArtifactTypeInfo.md) |  | 

#### list_artifact_types.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

