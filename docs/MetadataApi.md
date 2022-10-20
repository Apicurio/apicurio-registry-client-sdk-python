# apicurioregistryclient.MetadataApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_artifact_version_meta_data**](MetadataApi.md#delete_artifact_version_meta_data) | **DELETE** /groups/{groupId}/artifacts/{artifactId}/versions/{version}/meta | Delete artifact version metadata
[**get_artifact_meta_data**](MetadataApi.md#get_artifact_meta_data) | **GET** /groups/{groupId}/artifacts/{artifactId}/meta | Get artifact metadata
[**get_artifact_owner**](MetadataApi.md#get_artifact_owner) | **GET** /groups/{groupId}/artifacts/{artifactId}/owner | Get artifact owner
[**get_artifact_version_meta_data**](MetadataApi.md#get_artifact_version_meta_data) | **GET** /groups/{groupId}/artifacts/{artifactId}/versions/{version}/meta | Get artifact version metadata
[**get_artifact_version_meta_data_by_content**](MetadataApi.md#get_artifact_version_meta_data_by_content) | **POST** /groups/{groupId}/artifacts/{artifactId}/meta | Get artifact version metadata by content
[**update_artifact_meta_data**](MetadataApi.md#update_artifact_meta_data) | **PUT** /groups/{groupId}/artifacts/{artifactId}/meta | Update artifact metadata
[**update_artifact_owner**](MetadataApi.md#update_artifact_owner) | **PUT** /groups/{groupId}/artifacts/{artifactId}/owner | Update artifact owner
[**update_artifact_version_meta_data**](MetadataApi.md#update_artifact_version_meta_data) | **PUT** /groups/{groupId}/artifacts/{artifactId}/versions/{version}/meta | Update artifact version metadata


# **delete_artifact_version_meta_data**
> delete_artifact_version_meta_data(group_id, artifact_id, version)

Delete artifact version metadata

Deletes the user-editable metadata properties of the artifact version.  Any properties that are not user-editable are preserved.  This operation can fail for the following reasons:  * No artifact with this `artifactId` exists (HTTP error `404`) * No version with this `version` exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example

* Basic Authentication (basicAuth):

```python
import time
import apicurioregistryclient
from apicurioregistryclient.api import metadata_api
from apicurioregistryclient.model.error import Error
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
    api_instance = metadata_api.MetadataApi(api_client)
    group_id = "my-group" # str | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    artifact_id = "example-artifact" # str | The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    version = "3.1.6" # str | The unique identifier of a specific version of the artifact content.

    # example passing only required values which don't have defaults set
    try:
        # Delete artifact version metadata
        api_instance.delete_artifact_version_meta_data(group_id, artifact_id, version)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling MetadataApi->delete_artifact_version_meta_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts. |
 **artifact_id** | **str**| The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier. |
 **version** | **str**| The unique identifier of a specific version of the artifact content. |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The artifact version&#39;s user-editable metadata was successfully deleted. |  -  |
**404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact_meta_data**
> ArtifactMetaData get_artifact_meta_data(group_id, artifact_id)

Get artifact metadata

Gets the metadata for an artifact in the registry.  The returned metadata includes both generated (read-only) and editable metadata (such as name and description).  This operation can fail for the following reasons:  * No artifact with this `artifactId` exists (HTTP error `404`) * A server error occurred (HTTP error `500`)

### Example

* Basic Authentication (basicAuth):

```python
import time
import apicurioregistryclient
from apicurioregistryclient.api import metadata_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.artifact_meta_data import ArtifactMetaData
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
    api_instance = metadata_api.MetadataApi(api_client)
    group_id = "my-group" # str | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    artifact_id = "example-artifact" # str | The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

    # example passing only required values which don't have defaults set
    try:
        # Get artifact metadata
        api_response = api_instance.get_artifact_meta_data(group_id, artifact_id)
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling MetadataApi->get_artifact_meta_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts. |
 **artifact_id** | **str**| The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier. |

### Return type

[**ArtifactMetaData**](ArtifactMetaData.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The artifact&#39;s metadata. |  -  |
**404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact_owner**
> ArtifactOwner get_artifact_owner(group_id, artifact_id)

Get artifact owner

Gets the owner of an artifact in the registry.  This operation can fail for the following reasons:  * No artifact with this `artifactId` exists (HTTP error `404`) * A server error occurred (HTTP error `500`)

### Example

* Basic Authentication (basicAuth):

```python
import time
import apicurioregistryclient
from apicurioregistryclient.api import metadata_api
from apicurioregistryclient.model.artifact_owner import ArtifactOwner
from apicurioregistryclient.model.error import Error
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
    api_instance = metadata_api.MetadataApi(api_client)
    group_id = "my-group" # str | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    artifact_id = "example-artifact" # str | The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

    # example passing only required values which don't have defaults set
    try:
        # Get artifact owner
        api_response = api_instance.get_artifact_owner(group_id, artifact_id)
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling MetadataApi->get_artifact_owner: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts. |
 **artifact_id** | **str**| The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier. |

### Return type

[**ArtifactOwner**](ArtifactOwner.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The artifact&#39;s owner. |  -  |
**404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact_version_meta_data**
> VersionMetaData get_artifact_version_meta_data(group_id, artifact_id, version)

Get artifact version metadata

Retrieves the metadata for a single version of the artifact.  The version metadata is  a subset of the artifact metadata and only includes the metadata that is specific to the version (for example, this doesn't include `modifiedOn`).  This operation can fail for the following reasons:  * No artifact with this `artifactId` exists (HTTP error `404`) * No version with this `version` exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example

* Basic Authentication (basicAuth):

```python
import time
import apicurioregistryclient
from apicurioregistryclient.api import metadata_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.version_meta_data import VersionMetaData
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
    api_instance = metadata_api.MetadataApi(api_client)
    group_id = "my-group" # str | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    artifact_id = "example-artifact" # str | The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    version = "3.1.6" # str | The unique identifier of a specific version of the artifact content.

    # example passing only required values which don't have defaults set
    try:
        # Get artifact version metadata
        api_response = api_instance.get_artifact_version_meta_data(group_id, artifact_id, version)
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling MetadataApi->get_artifact_version_meta_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts. |
 **artifact_id** | **str**| The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier. |
 **version** | **str**| The unique identifier of a specific version of the artifact content. |

### Return type

[**VersionMetaData**](VersionMetaData.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The artifact version&#39;s metadata. |  -  |
**404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact_version_meta_data_by_content**
> VersionMetaData get_artifact_version_meta_data_by_content(group_id, artifact_id, body)

Get artifact version metadata by content

Gets the metadata for an artifact that matches the raw content.  Searches the registry for a version of the given artifact matching the content provided in the body of the POST.  This operation can fail for the following reasons:  * Provided content (request body) was empty (HTTP error `400`) * No artifact with the `artifactId` exists (HTTP error `404`) * No artifact version matching the provided content exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example

* Basic Authentication (basicAuth):

```python
import time
import apicurioregistryclient
from apicurioregistryclient.api import metadata_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.version_meta_data import VersionMetaData
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
    api_instance = metadata_api.MetadataApi(api_client)
    group_id = "my-group" # str | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    artifact_id = "example-artifact" # str | The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | The content of an artifact version.
    canonical = True # bool | Parameter that can be set to `true` to indicate that the server should \"canonicalize\" the content when searching for a matching version.  Canonicalization is unique to each artifact type, but typically involves removing any extra whitespace and formatting the content in a consistent manner. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get artifact version metadata by content
        api_response = api_instance.get_artifact_version_meta_data_by_content(group_id, artifact_id, body)
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling MetadataApi->get_artifact_version_meta_data_by_content: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get artifact version metadata by content
        api_response = api_instance.get_artifact_version_meta_data_by_content(group_id, artifact_id, body, canonical=canonical)
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling MetadataApi->get_artifact_version_meta_data_by_content: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts. |
 **artifact_id** | **str**| The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier. |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| The content of an artifact version. |
 **canonical** | **bool**| Parameter that can be set to &#x60;true&#x60; to indicate that the server should \&quot;canonicalize\&quot; the content when searching for a matching version.  Canonicalization is unique to each artifact type, but typically involves removing any extra whitespace and formatting the content in a consistent manner. | [optional]

### Return type

[**VersionMetaData**](VersionMetaData.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The metadata of the artifact version matching the provided content. |  -  |
**404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_artifact_meta_data**
> update_artifact_meta_data(group_id, artifact_id, editable_meta_data)

Update artifact metadata

Updates the editable parts of the artifact's metadata.  Not all metadata fields can be updated.  For example, `createdOn` and `createdBy` are both read-only properties.  This operation can fail for the following reasons:  * No artifact with the `artifactId` exists (HTTP error `404`) * A server error occurred (HTTP error `500`)

### Example

* Basic Authentication (basicAuth):

```python
import time
import apicurioregistryclient
from apicurioregistryclient.api import metadata_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.editable_meta_data import EditableMetaData
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
    api_instance = metadata_api.MetadataApi(api_client)
    group_id = "my-group" # str | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    artifact_id = "example-artifact" # str | The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    editable_meta_data = EditableMetaData(
        name="name_example",
        description="description_example",
        labels=[
            "labels_example",
        ],
        properties=Properties(
            key="key_example",
        ),
    ) # EditableMetaData | Updated artifact metadata.

    # example passing only required values which don't have defaults set
    try:
        # Update artifact metadata
        api_instance.update_artifact_meta_data(group_id, artifact_id, editable_meta_data)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling MetadataApi->update_artifact_meta_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts. |
 **artifact_id** | **str**| The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier. |
 **editable_meta_data** | [**EditableMetaData**](EditableMetaData.md)| Updated artifact metadata. |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The artifact&#39;s metadata was updated. |  -  |
**404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_artifact_owner**
> update_artifact_owner(group_id, artifact_id, artifact_owner)

Update artifact owner

Changes the ownership of an artifact.  This operation can fail for the following reasons:  * No artifact with this `artifactId` exists (HTTP error `404`) * A server error occurred (HTTP error `500`)

### Example

* Basic Authentication (basicAuth):

```python
import time
import apicurioregistryclient
from apicurioregistryclient.api import metadata_api
from apicurioregistryclient.model.artifact_owner import ArtifactOwner
from apicurioregistryclient.model.error import Error
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
    api_instance = metadata_api.MetadataApi(api_client)
    group_id = "my-group" # str | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    artifact_id = "example-artifact" # str | The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    artifact_owner = ArtifactOwner(
        owner="owner_example",
    ) # ArtifactOwner | 

    # example passing only required values which don't have defaults set
    try:
        # Update artifact owner
        api_instance.update_artifact_owner(group_id, artifact_id, artifact_owner)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling MetadataApi->update_artifact_owner: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts. |
 **artifact_id** | **str**| The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier. |
 **artifact_owner** | [**ArtifactOwner**](ArtifactOwner.md)|  |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The owner was successfully changed. |  -  |
**404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_artifact_version_meta_data**
> update_artifact_version_meta_data(group_id, artifact_id, version, editable_meta_data)

Update artifact version metadata

Updates the user-editable portion of the artifact version's metadata.  Only some of  the metadata fields are editable by the user.  For example, `description` is editable,  but `createdOn` is not.  This operation can fail for the following reasons:  * No artifact with this `artifactId` exists (HTTP error `404`) * No version with this `version` exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example

* Basic Authentication (basicAuth):

```python
import time
import apicurioregistryclient
from apicurioregistryclient.api import metadata_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.editable_meta_data import EditableMetaData
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
    api_instance = metadata_api.MetadataApi(api_client)
    group_id = "my-group" # str | The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    artifact_id = "example-artifact" # str | The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    version = "3.1.6" # str | The unique identifier of a specific version of the artifact content.
    editable_meta_data = EditableMetaData(
        name="name_example",
        description="description_example",
        labels=[
            "labels_example",
        ],
        properties=Properties(
            key="key_example",
        ),
    ) # EditableMetaData | 

    # example passing only required values which don't have defaults set
    try:
        # Update artifact version metadata
        api_instance.update_artifact_version_meta_data(group_id, artifact_id, version, editable_meta_data)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling MetadataApi->update_artifact_version_meta_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts. |
 **artifact_id** | **str**| The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier. |
 **version** | **str**| The unique identifier of a specific version of the artifact content. |
 **editable_meta_data** | [**EditableMetaData**](EditableMetaData.md)|  |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The artifact version&#39;s metadata was successfully updated. |  -  |
**404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

