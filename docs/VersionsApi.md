# apicurioregistryclient.VersionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_artifact_version**](VersionsApi.md#create_artifact_version) | **POST** /groups/{groupId}/artifacts/{artifactId}/versions | Create artifact version
[**get_artifact_version**](VersionsApi.md#get_artifact_version) | **GET** /groups/{groupId}/artifacts/{artifactId}/versions/{version} | Get artifact version
[**get_artifact_version_references**](VersionsApi.md#get_artifact_version_references) | **GET** /groups/{groupId}/artifacts/{artifactId}/versions/{version}/references | Get artifact version
[**list_artifact_versions**](VersionsApi.md#list_artifact_versions) | **GET** /groups/{groupId}/artifacts/{artifactId}/versions | List artifact versions
[**update_artifact_version_state**](VersionsApi.md#update_artifact_version_state) | **PUT** /groups/{groupId}/artifacts/{artifactId}/versions/{version}/state | Update artifact version state


# **create_artifact_version**
> VersionMetaData create_artifact_version(group_id, artifact_id, body)

Create artifact version

Creates a new version of the artifact by uploading new content.  The configured rules for the artifact are applied, and if they all pass, the new content is added as the most recent  version of the artifact.  If any of the rules fail, an error is returned.  The body of the request can be the raw content of the new artifact version, or the raw content  and a set of references pointing to other artifacts, and the type of that content should match the artifact's type (for example if the artifact type is `AVRO` then the content of the request should be an Apache Avro document).  This operation can fail for the following reasons:  * Provided content (request body) was empty (HTTP error `400`) * No artifact with this `artifactId` exists (HTTP error `404`) * The new content violates one of the rules configured for the artifact (HTTP error `409`) * A server error occurred (HTTP error `500`) 

### Example


```python
import time
import apicurioregistryclient
from apicurioregistryclient.api import versions_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.version_meta_data import VersionMetaData
from apicurioregistryclient.model.content_create_request import ContentCreateRequest
from apicurioregistryclient.model.rule_violation_error import RuleViolationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = versions_api.VersionsApi(api_client)
    group_id = "my-group" # str | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    artifact_id = "example-artifact" # str | The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    body = open('{"openapi":"3.0.2","info":{"title":"Empty API","version":"1.0.7","description":"An example API design using OpenAPI."},"paths":{"/widgets":{"get":{"responses":{"200":{"content":{"application/json":{"schema":{"type":"array","items":{"type":"string"}}}},"description":"All widgets"}},"summary":"Get widgets"}}},"components":{"schemas":{"Widget":{"title":"Root Type for Widget","description":"A sample data type.","type":"object","properties":{"property-1":{"type":"string"},"property-2":{"type":"boolean"}},"example":{"property-1":"value1","property-2":true}}}}}', 'rb') # file_type | The content of the artifact version being created or the content and a set of references to other artifacts. This is often, but not always, JSON data representing one of the supported artifact types:  * Avro (`AVRO`) * Protobuf (`PROTOBUF`) * JSON Schema (`JSON`) * Kafka Connect (`KCONNECT`) * OpenAPI (`OPENAPI`) * AsyncAPI (`ASYNCAPI`) * GraphQL (`GRAPHQL`) * Web Services Description Language (`WSDL`) * XML Schema (`XSD`) 
    x_registry_version = "3.1.6" # str | Specifies the version number of this new version of the artifact content.  This would typically be a simple integer or a SemVer value.  It must be unique within the artifact.  If this is not provided, the server will generate a new, unique version number for this new updated content. (optional)
    x_registry_name = "Artifact name" # str | Specifies the artifact name of this new version of the artifact content. Name must be ASCII-only string. If this is not provided, the server will extract the name from the artifact content. (optional)
    x_registry_description = "Artifact description" # str | Specifies the artifact description of this new version of the artifact content. Description must be ASCII-only string. If this is not provided, the server will extract the description from the artifact content. (optional)
    x_registry_description_encoded = "QXJ0aWZhY3QgZGVzY3JpcHRpb24K" # str | Specifies the artifact description of this new version of the artifact content. Value of this must be Base64 encoded string. If this is not provided, the server will extract the description from the artifact content. (optional)
    x_registry_name_encoded = "QXJ0aWZhY3QgbmFtZQo=" # str | Specifies the artifact name of this new version of the artifact content. Value of this must be Base64 encoded string. If this is not provided, the server will extract the name from the artifact content. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create artifact version
        api_response = api_instance.create_artifact_version(group_id, artifact_id, body)
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling VersionsApi->create_artifact_version: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create artifact version
        api_response = api_instance.create_artifact_version(group_id, artifact_id, body, x_registry_version=x_registry_version, x_registry_name=x_registry_name, x_registry_description=x_registry_description, x_registry_description_encoded=x_registry_description_encoded, x_registry_name_encoded=x_registry_name_encoded)
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling VersionsApi->create_artifact_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts. |
 **artifact_id** | **str**| The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier. |
 **body** | **file_type**| The content of the artifact version being created or the content and a set of references to other artifacts. This is often, but not always, JSON data representing one of the supported artifact types:  * Avro (&#x60;AVRO&#x60;) * Protobuf (&#x60;PROTOBUF&#x60;) * JSON Schema (&#x60;JSON&#x60;) * Kafka Connect (&#x60;KCONNECT&#x60;) * OpenAPI (&#x60;OPENAPI&#x60;) * AsyncAPI (&#x60;ASYNCAPI&#x60;) * GraphQL (&#x60;GRAPHQL&#x60;) * Web Services Description Language (&#x60;WSDL&#x60;) * XML Schema (&#x60;XSD&#x60;)  |
 **x_registry_version** | **str**| Specifies the version number of this new version of the artifact content.  This would typically be a simple integer or a SemVer value.  It must be unique within the artifact.  If this is not provided, the server will generate a new, unique version number for this new updated content. | [optional]
 **x_registry_name** | **str**| Specifies the artifact name of this new version of the artifact content. Name must be ASCII-only string. If this is not provided, the server will extract the name from the artifact content. | [optional]
 **x_registry_description** | **str**| Specifies the artifact description of this new version of the artifact content. Description must be ASCII-only string. If this is not provided, the server will extract the description from the artifact content. | [optional]
 **x_registry_description_encoded** | **str**| Specifies the artifact description of this new version of the artifact content. Value of this must be Base64 encoded string. If this is not provided, the server will extract the description from the artifact content. | [optional]
 **x_registry_name_encoded** | **str**| Specifies the artifact name of this new version of the artifact content. Value of this must be Base64 encoded string. If this is not provided, the server will extract the name from the artifact content. | [optional]

### Return type

[**VersionMetaData**](VersionMetaData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/create.extended+json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The artifact version was successfully created. |  -  |
**404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
**409** | Common response used when an input conflicts with existing data. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact_version**
> file_type get_artifact_version(group_id, artifact_id, version)

Get artifact version

Retrieves a single version of the artifact content.  Both the `artifactId` and the unique `version` number must be provided.  The `Content-Type` of the response depends  on the artifact type.  In most cases, this is `application/json`, but for some types  it may be different (for example, `PROTOBUF`).  This operation can fail for the following reasons:  * No artifact with this `artifactId` exists (HTTP error `404`) * No version with this `version` exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example


```python
import time
import apicurioregistryclient
from apicurioregistryclient.api import versions_api
from apicurioregistryclient.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = versions_api.VersionsApi(api_client)
    group_id = "my-group" # str | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    artifact_id = "example-artifact" # str | The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    version = "3.1.6" # str | The unique identifier of a specific version of the artifact content.
    dereference = True # bool | Allows the user to specify if the content should be dereferenced when being returned (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get artifact version
        api_response = api_instance.get_artifact_version(group_id, artifact_id, version)
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling VersionsApi->get_artifact_version: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get artifact version
        api_response = api_instance.get_artifact_version(group_id, artifact_id, version, dereference=dereference)
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling VersionsApi->get_artifact_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts. |
 **artifact_id** | **str**| The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier. |
 **version** | **str**| The unique identifier of a specific version of the artifact content. |
 **dereference** | **bool**| Allows the user to specify if the content should be dereferenced when being returned | [optional]

### Return type

**file_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |
**200** | The content of one version of one artifact. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact_version_references**
> [ArtifactReference] get_artifact_version_references(group_id, artifact_id, version)

Get artifact version

Retrieves a single version of the artifact content.  Both the `artifactId` and the unique `version` number must be provided.  The `Content-Type` of the response depends  on the artifact type.  In most cases, this is `application/json`, but for some types  it may be different (for example, `PROTOBUF`).  This operation can fail for the following reasons:  * No artifact with this `artifactId` exists (HTTP error `404`) * No version with this `version` exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example


```python
import time
import apicurioregistryclient
from apicurioregistryclient.api import versions_api
from apicurioregistryclient.model.error import Error
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
    api_instance = versions_api.VersionsApi(api_client)
    group_id = "my-group" # str | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    artifact_id = "example-artifact" # str | The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    version = "3.1.6" # str | The unique identifier of a specific version of the artifact content.

    # example passing only required values which don't have defaults set
    try:
        # Get artifact version
        api_response = api_instance.get_artifact_version_references(group_id, artifact_id, version)
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling VersionsApi->get_artifact_version_references: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts. |
 **artifact_id** | **str**| The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier. |
 **version** | **str**| The unique identifier of a specific version of the artifact content. |

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
**404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |
**200** | List of all the artifact references for this artifact. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_artifact_versions**
> VersionSearchResults list_artifact_versions(group_id, artifact_id)

List artifact versions

Returns a list of all versions of the artifact.  The result set is paged.  This operation can fail for the following reasons:  * No artifact with this `artifactId` exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example


```python
import time
import apicurioregistryclient
from apicurioregistryclient.api import versions_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.version_search_results import VersionSearchResults
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = versions_api.VersionsApi(api_client)
    group_id = "my-group" # str | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    artifact_id = "example-artifact" # str | The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    offset = 1 # int | The number of versions to skip before starting to collect the result set.  Defaults to 0. (optional)
    limit = 1 # int | The number of versions to return.  Defaults to 20. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List artifact versions
        api_response = api_instance.list_artifact_versions(group_id, artifact_id)
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling VersionsApi->list_artifact_versions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List artifact versions
        api_response = api_instance.list_artifact_versions(group_id, artifact_id, offset=offset, limit=limit)
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling VersionsApi->list_artifact_versions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts. |
 **artifact_id** | **str**| The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier. |
 **offset** | **int**| The number of versions to skip before starting to collect the result set.  Defaults to 0. | [optional]
 **limit** | **int**| The number of versions to return.  Defaults to 20. | [optional]

### Return type

[**VersionSearchResults**](VersionSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all artifact versions. |  -  |
**404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_artifact_version_state**
> update_artifact_version_state(group_id, artifact_id, version, update_state)

Update artifact version state

Updates the state of a specific version of an artifact.  For example, you can use  this operation to disable a specific version.  This operation can fail for the following reasons:  * No artifact with this `artifactId` exists (HTTP error `404`) * No version with this `version` exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example


```python
import time
import apicurioregistryclient
from apicurioregistryclient.api import versions_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.update_state import UpdateState
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = versions_api.VersionsApi(api_client)
    group_id = "my-group" # str | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    artifact_id = "example-artifact" # str | The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    version = "3.1.6" # str | The unique identifier of a specific version of the artifact content.
    update_state = UpdateState(
        state=ArtifactState("ENABLED"),
    ) # UpdateState | 

    # example passing only required values which don't have defaults set
    try:
        # Update artifact version state
        api_instance.update_artifact_version_state(group_id, artifact_id, version, update_state)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling VersionsApi->update_artifact_version_state: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts. |
 **artifact_id** | **str**| The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier. |
 **version** | **str**| The unique identifier of a specific version of the artifact content. |
 **update_state** | [**UpdateState**](UpdateState.md)|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Returned when the update was successful. |  -  |
**400** | Common response for all operations that can return a &#x60;400&#x60; error. |  -  |
**404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

