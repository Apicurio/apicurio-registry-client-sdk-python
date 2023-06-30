<a id="__pageTop"></a>
# apicurioregistryclient.apis.tags.users_api.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_user_info**](#get_current_user_info) | **get** /users/me | Get current user

# **get_current_user_info**
<a id="get_current_user_info"></a>
> UserInfo get_current_user_info()

Get current user

Returns information about the currently authenticated user.

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import users_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.user_info import UserInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get current user
        api_response = api_instance.get_current_user_info()
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling UsersApi->get_current_user_info: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_current_user_info.ApiResponseFor200) | Response when the endpoint is successfully invoked.
500 | [ApiResponseFor500](#get_current_user_info.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### get_current_user_info.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserInfo**](../../models/UserInfo.md) |  | 


#### get_current_user_info.ApiResponseFor500
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

