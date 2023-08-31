<a id="__pageTop"></a>
# apicurioregistryclient.apis.tags.system_api.SystemApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_resource_limits**](#get_resource_limits) | **get** /system/limits | Get resource limits information
[**get_system_info**](#get_system_info) | **get** /system/info | Get system information

# **get_resource_limits**
<a id="get_resource_limits"></a>
> Limits get_resource_limits()

Get resource limits information

This operation retrieves the list of limitations on used resources, that are applied on the current instance of Registry.

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import system_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.limits import Limits
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_api.SystemApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get resource limits information
        api_response = api_instance.get_resource_limits()
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling SystemApi->get_resource_limits: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_resource_limits.ApiResponseFor200) | On success, returns resource limits
500 | [ApiResponseFor500](#get_resource_limits.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### get_resource_limits.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Limits**](../../models/Limits.md) |  | 


#### get_resource_limits.ApiResponseFor500
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

# **get_system_info**
<a id="get_system_info"></a>
> SystemInfo get_system_info()

Get system information

This operation retrieves information about the running registry system, such as the version of the software and when it was built.

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import system_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.system_info import SystemInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = system_api.SystemApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get system information
        api_response = api_instance.get_system_info()
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling SystemApi->get_system_info: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_system_info.ApiResponseFor200) | On success, returns the system information.
500 | [ApiResponseFor500](#get_system_info.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### get_system_info.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SystemInfo**](../../models/SystemInfo.md) |  | 


#### get_system_info.ApiResponseFor500
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

