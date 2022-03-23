# apicurioregistryclient.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**references_by_content_hash**](DefaultApi.md#references_by_content_hash) | **GET** /ids/contentHashes/{contentHash}/references | Returns a list with all the references for the artifact with the given hash
[**references_by_content_id**](DefaultApi.md#references_by_content_id) | **GET** /ids/contentIds/{contentId}/references | Returns a list with all the references for the artifact with the given content id.
[**references_by_global_id**](DefaultApi.md#references_by_global_id) | **GET** /ids/globalIds/{globalId}/references | Returns a list with all the references for the artifact with the given global id.


# **references_by_content_hash**
> [ArtifactReference] references_by_content_hash(UNKNOWN_PARAMETER_NAME)

Returns a list with all the references for the artifact with the given hash

Returns a list containing all the artifact references using the artifact content hash.  This operation may fail for one of the following reasons:  * A server error occurred (HTTP error `500`) 

### Example


```python
import time
import apicurioregistryclient
from apicurioregistryclient.api import default_api
from apicurioregistryclient.model.artifact_reference import ArtifactReference
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    UNKNOWN_PARAMETER_NAME =  #  | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a list with all the references for the artifact with the given hash
        api_response = api_instance.references_by_content_hash(UNKNOWN_PARAMETER_NAME)
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling DefaultApi->references_by_content_hash: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **UNKNOWN_PARAMETER_NAME** | ****|  |

### Return type

[**[ArtifactReference]**](ArtifactReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list containing all the references for the artifact with the given content hash. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **references_by_content_id**
> [ArtifactReference] references_by_content_id(UNKNOWN_PARAMETER_NAME)

Returns a list with all the references for the artifact with the given content id.

Returns a list containing all the artifact references using the artifact contentId.  This operation may fail for one of the following reasons:  * A server error occurred (HTTP error `500`)

### Example


```python
import time
import apicurioregistryclient
from apicurioregistryclient.api import default_api
from apicurioregistryclient.model.artifact_reference import ArtifactReference
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    UNKNOWN_PARAMETER_NAME =  #  | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a list with all the references for the artifact with the given content id.
        api_response = api_instance.references_by_content_id(UNKNOWN_PARAMETER_NAME)
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling DefaultApi->references_by_content_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **UNKNOWN_PARAMETER_NAME** | ****|  |

### Return type

[**[ArtifactReference]**](ArtifactReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list containing all the references for the artifact with the given content id. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **references_by_global_id**
> [ArtifactReference] references_by_global_id(UNKNOWN_PARAMETER_NAME)

Returns a list with all the references for the artifact with the given global id.

Returns a list containing all the artifact references using the artifact global id.  This operation may fail for one of the following reasons:  * A server error occurred (HTTP error `500`)

### Example


```python
import time
import apicurioregistryclient
from apicurioregistryclient.api import default_api
from apicurioregistryclient.model.artifact_reference import ArtifactReference
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    UNKNOWN_PARAMETER_NAME =  #  | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a list with all the references for the artifact with the given global id.
        api_response = api_instance.references_by_global_id(UNKNOWN_PARAMETER_NAME)
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling DefaultApi->references_by_global_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **UNKNOWN_PARAMETER_NAME** | ****|  |

### Return type

[**[ArtifactReference]**](ArtifactReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list containing all the references for the artifact with the given global id. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

