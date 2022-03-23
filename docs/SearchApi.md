# apicurioregistryclient.SearchApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_artifacts**](SearchApi.md#search_artifacts) | **GET** /search/artifacts | Search for artifacts
[**search_artifacts_by_content**](SearchApi.md#search_artifacts_by_content) | **POST** /search/artifacts | Search for artifacts by content


# **search_artifacts**
> ArtifactSearchResults search_artifacts()

Search for artifacts

Returns a paginated list of all artifacts that match the provided filter criteria. 

### Example

* Basic Authentication (basicAuth):

```python
import time
import apicurioregistryclient
from apicurioregistryclient.api import search_api
from apicurioregistryclient.model.artifact_search_results import ArtifactSearchResults
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.sort_by import SortBy
from apicurioregistryclient.model.sort_order import SortOrder
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
    api_instance = search_api.SearchApi(api_client)
    name = "name_example" # str | Filter by artifact name. (optional)
    offset = 0 # int | The number of artifacts to skip before starting to collect the result set.  Defaults to 0. (optional) if omitted the server will use the default value of 0
    limit = 20 # int | The number of artifacts to return.  Defaults to 20. (optional) if omitted the server will use the default value of 20
    order = SortOrder("asc") # SortOrder | Sort order, ascending (`asc`) or descending (`desc`). (optional)
    orderby = SortBy("name") # SortBy | The field to sort by.  Can be one of:  * `name` * `createdOn`  (optional)
    labels = [
        "labels_example",
    ] # [str] | Filter by label.  Include one or more label to only return artifacts containing all of the specified labels. (optional)
    properties = [
        "properties_example",
    ] # [str] | Filter by one or more name/value property.  Separate each name/value pair using a colon.  For example `properties=foo:bar` will return only artifacts with a custom property named `foo` and value `bar`. (optional)
    description = "description_example" # str | Filter by description. (optional)
    group = "group_example" # str | Filter by artifact group. (optional)
    global_id = 1 # int | Filter by globalId. (optional)
    content_id = 1 # int | Filter by contentId. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for artifacts
        api_response = api_instance.search_artifacts(name=name, offset=offset, limit=limit, order=order, orderby=orderby, labels=labels, properties=properties, description=description, group=group, global_id=global_id, content_id=content_id)
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling SearchApi->search_artifacts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter by artifact name. | [optional]
 **offset** | **int**| The number of artifacts to skip before starting to collect the result set.  Defaults to 0. | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The number of artifacts to return.  Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **order** | **SortOrder**| Sort order, ascending (&#x60;asc&#x60;) or descending (&#x60;desc&#x60;). | [optional]
 **orderby** | **SortBy**| The field to sort by.  Can be one of:  * &#x60;name&#x60; * &#x60;createdOn&#x60;  | [optional]
 **labels** | **[str]**| Filter by label.  Include one or more label to only return artifacts containing all of the specified labels. | [optional]
 **properties** | **[str]**| Filter by one or more name/value property.  Separate each name/value pair using a colon.  For example &#x60;properties&#x3D;foo:bar&#x60; will return only artifacts with a custom property named &#x60;foo&#x60; and value &#x60;bar&#x60;. | [optional]
 **description** | **str**| Filter by description. | [optional]
 **group** | **str**| Filter by artifact group. | [optional]
 **global_id** | **int**| Filter by globalId. | [optional]
 **content_id** | **int**| Filter by contentId. | [optional]

### Return type

[**ArtifactSearchResults**](ArtifactSearchResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | On a successful response, returns a result set of artifacts - one for each artifact in the registry that matches the criteria. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_artifacts_by_content**
> ArtifactSearchResults search_artifacts_by_content(body)

Search for artifacts by content

Returns a paginated list of all artifacts with at least one version that matches the posted content. 

### Example

* Basic Authentication (basicAuth):

```python
import time
import apicurioregistryclient
from apicurioregistryclient.api import search_api
from apicurioregistryclient.model.artifact_search_results import ArtifactSearchResults
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.artifact_type import ArtifactType
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
    api_instance = search_api.SearchApi(api_client)
    body = open('/path/to/file', 'rb') # file_type | The content to search for.
    canonical = True # bool | Parameter that can be set to `true` to indicate that the server should \"canonicalize\" the content when searching for matching artifacts.  Canonicalization is unique to each artifact type, but typically involves removing any extra whitespace and formatting the content in a consistent manner.  Must be used along with the `artifactType` query parameter. (optional)
    artifact_type = ArtifactType("AVRO") # ArtifactType | Indicates the type of artifact represented by the content being used for the search.  This is only needed when using the `canonical` query parameter, so that the server knows how to canonicalize the content prior to searching for matching artifacts. (optional)
    offset = 0 # int | The number of artifacts to skip before starting to collect the result set.  Defaults to 0. (optional) if omitted the server will use the default value of 0
    limit = 20 # int | The number of artifacts to return.  Defaults to 20. (optional) if omitted the server will use the default value of 20
    order = "asc" # str | Sort order, ascending (`asc`) or descending (`desc`). (optional)
    orderby = "name" # str | The field to sort by.  Can be one of:  * `name` * `createdOn`  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search for artifacts by content
        api_response = api_instance.search_artifacts_by_content(body)
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling SearchApi->search_artifacts_by_content: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for artifacts by content
        api_response = api_instance.search_artifacts_by_content(body, canonical=canonical, artifact_type=artifact_type, offset=offset, limit=limit, order=order, orderby=orderby)
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling SearchApi->search_artifacts_by_content: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **file_type**| The content to search for. |
 **canonical** | **bool**| Parameter that can be set to &#x60;true&#x60; to indicate that the server should \&quot;canonicalize\&quot; the content when searching for matching artifacts.  Canonicalization is unique to each artifact type, but typically involves removing any extra whitespace and formatting the content in a consistent manner.  Must be used along with the &#x60;artifactType&#x60; query parameter. | [optional]
 **artifact_type** | **ArtifactType**| Indicates the type of artifact represented by the content being used for the search.  This is only needed when using the &#x60;canonical&#x60; query parameter, so that the server knows how to canonicalize the content prior to searching for matching artifacts. | [optional]
 **offset** | **int**| The number of artifacts to skip before starting to collect the result set.  Defaults to 0. | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The number of artifacts to return.  Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **order** | **str**| Sort order, ascending (&#x60;asc&#x60;) or descending (&#x60;desc&#x60;). | [optional]
 **orderby** | **str**| The field to sort by.  Can be one of:  * &#x60;name&#x60; * &#x60;createdOn&#x60;  | [optional]

### Return type

[**ArtifactSearchResults**](ArtifactSearchResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | On a successful response, returns a result set of artifacts - one for each artifact in the registry that matches the criteria. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

