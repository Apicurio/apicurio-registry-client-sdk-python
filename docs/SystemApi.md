# apicurioregistryclient.SystemApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_resource_limits**](SystemApi.md#get_resource_limits) | **GET** /system/limits | Get resource limits information
[**get_system_info**](SystemApi.md#get_system_info) | **GET** /system/info | Get system information


# **get_resource_limits**
> Limits get_resource_limits()

Get resource limits information

This operation retrieves the list of limitations on used resources, that are applied on the current instance of Registry.

### Example

* Basic Authentication (basicAuth):

```python
import time
import apicurioregistryclient
from apicurioregistryclient.api import system_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.limits import Limits
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = apicurioregistryclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
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

### Return type

[**Limits**](Limits.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | On success, returns resource limits |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_info**
> SystemInfo get_system_info()

Get system information

This operation retrieves information about the running registry system, such as the version of the software and when it was built.

### Example

* Basic Authentication (basicAuth):

```python
import time
import apicurioregistryclient
from apicurioregistryclient.api import system_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.system_info import SystemInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = apicurioregistryclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
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

### Return type

[**SystemInfo**](SystemInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | On success, returns the system information. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

