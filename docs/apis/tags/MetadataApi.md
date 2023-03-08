<a name="__pageTop"></a>
# apicurioregistryclient.apis.tags.metadata_api.MetadataApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_artifact_version_meta_data**](#delete_artifact_version_meta_data) | **delete** /groups/{groupId}/artifacts/{artifactId}/versions/{version}/meta | Delete artifact version metadata
[**get_artifact_meta_data**](#get_artifact_meta_data) | **get** /groups/{groupId}/artifacts/{artifactId}/meta | Get artifact metadata
[**get_artifact_owner**](#get_artifact_owner) | **get** /groups/{groupId}/artifacts/{artifactId}/owner | Get artifact owner
[**get_artifact_version_meta_data**](#get_artifact_version_meta_data) | **get** /groups/{groupId}/artifacts/{artifactId}/versions/{version}/meta | Get artifact version metadata
[**get_artifact_version_meta_data_by_content**](#get_artifact_version_meta_data_by_content) | **post** /groups/{groupId}/artifacts/{artifactId}/meta | Get artifact version metadata by content
[**update_artifact_meta_data**](#update_artifact_meta_data) | **put** /groups/{groupId}/artifacts/{artifactId}/meta | Update artifact metadata
[**update_artifact_owner**](#update_artifact_owner) | **put** /groups/{groupId}/artifacts/{artifactId}/owner | Update artifact owner
[**update_artifact_version_meta_data**](#update_artifact_version_meta_data) | **put** /groups/{groupId}/artifacts/{artifactId}/versions/{version}/meta | Update artifact version metadata

# **delete_artifact_version_meta_data**
<a name="delete_artifact_version_meta_data"></a>
> delete_artifact_version_meta_data(group_idartifact_idversion)

Delete artifact version metadata

Deletes the user-editable metadata properties of the artifact version.  Any properties that are not user-editable are preserved.  This operation can fail for the following reasons:  * No artifact with this `artifactId` exists (HTTP error `404`) * No version with this `version` exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import metadata_api
from apicurioregistryclient.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "\"my-group\"",
        'artifactId': "\"example-artifact\"",
        'version': "\"3.1.6\"",
    }
    try:
        # Delete artifact version metadata
        api_response = api_instance.delete_artifact_version_meta_data(
            path_params=path_params,
        )
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling MetadataApi->delete_artifact_version_meta_data: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
groupId | GroupIdSchema | | 
artifactId | ArtifactIdSchema | | 
version | VersionSchema | | 

# GroupIdSchema

An ID of a single artifact group.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | An ID of a single artifact group. | 

# ArtifactIdSchema

The ID of a single artifact.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The ID of a single artifact. | 

# VersionSchema

A single version of an artifact.  Can be provided by the client when creating a new version, or it can be server-generated.  The value can be any string unique to the artifact, but it is recommended to use a simple integer or a semver value.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | A single version of an artifact.  Can be provided by the client when creating a new version, or it can be server-generated.  The value can be any string unique to the artifact, but it is recommended to use a simple integer or a semver value. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_artifact_version_meta_data.ApiResponseFor204) | The artifact version&#x27;s user-editable metadata was successfully deleted.
404 | [ApiResponseFor404](#delete_artifact_version_meta_data.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
500 | [ApiResponseFor500](#delete_artifact_version_meta_data.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### delete_artifact_version_meta_data.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_artifact_version_meta_data.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### delete_artifact_version_meta_data.ApiResponseFor500
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

# **get_artifact_meta_data**
<a name="get_artifact_meta_data"></a>
> ArtifactMetaData get_artifact_meta_data(group_idartifact_id)

Get artifact metadata

Gets the metadata for an artifact in the registry.  The returned metadata includes both generated (read-only) and editable metadata (such as name and description).  This operation can fail for the following reasons:  * No artifact with this `artifactId` exists (HTTP error `404`) * A server error occurred (HTTP error `500`)

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import metadata_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.artifact_meta_data import ArtifactMetaData
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "\"my-group\"",
        'artifactId': "\"example-artifact\"",
    }
    try:
        # Get artifact metadata
        api_response = api_instance.get_artifact_meta_data(
            path_params=path_params,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling MetadataApi->get_artifact_meta_data: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
groupId | GroupIdSchema | | 
artifactId | ArtifactIdSchema | | 

# GroupIdSchema

An ID of a single artifact group.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | An ID of a single artifact group. | 

# ArtifactIdSchema

The ID of a single artifact.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The ID of a single artifact. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_artifact_meta_data.ApiResponseFor200) | The artifact&#x27;s metadata.
404 | [ApiResponseFor404](#get_artifact_meta_data.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
500 | [ApiResponseFor500](#get_artifact_meta_data.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### get_artifact_meta_data.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArtifactMetaData**](../../models/ArtifactMetaData.md) |  | 


#### get_artifact_meta_data.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### get_artifact_meta_data.ApiResponseFor500
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

# **get_artifact_owner**
<a name="get_artifact_owner"></a>
> ArtifactOwner get_artifact_owner(group_idartifact_id)

Get artifact owner

Gets the owner of an artifact in the registry.  This operation can fail for the following reasons:  * No artifact with this `artifactId` exists (HTTP error `404`) * A server error occurred (HTTP error `500`)

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import metadata_api
from apicurioregistryclient.model.artifact_owner import ArtifactOwner
from apicurioregistryclient.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "\"my-group\"",
        'artifactId': "\"example-artifact\"",
    }
    try:
        # Get artifact owner
        api_response = api_instance.get_artifact_owner(
            path_params=path_params,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling MetadataApi->get_artifact_owner: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
groupId | GroupIdSchema | | 
artifactId | ArtifactIdSchema | | 

# GroupIdSchema

An ID of a single artifact group.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | An ID of a single artifact group. | 

# ArtifactIdSchema

The ID of a single artifact.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The ID of a single artifact. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_artifact_owner.ApiResponseFor200) | The artifact&#x27;s owner.
404 | [ApiResponseFor404](#get_artifact_owner.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
500 | [ApiResponseFor500](#get_artifact_owner.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### get_artifact_owner.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArtifactOwner**](../../models/ArtifactOwner.md) |  | 


#### get_artifact_owner.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### get_artifact_owner.ApiResponseFor500
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

# **get_artifact_version_meta_data**
<a name="get_artifact_version_meta_data"></a>
> VersionMetaData get_artifact_version_meta_data(group_idartifact_idversion)

Get artifact version metadata

Retrieves the metadata for a single version of the artifact.  The version metadata is  a subset of the artifact metadata and only includes the metadata that is specific to the version (for example, this doesn't include `modifiedOn`).  This operation can fail for the following reasons:  * No artifact with this `artifactId` exists (HTTP error `404`) * No version with this `version` exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import metadata_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.version_meta_data import VersionMetaData
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "\"my-group\"",
        'artifactId': "\"example-artifact\"",
        'version': "\"3.1.6\"",
    }
    try:
        # Get artifact version metadata
        api_response = api_instance.get_artifact_version_meta_data(
            path_params=path_params,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling MetadataApi->get_artifact_version_meta_data: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
groupId | GroupIdSchema | | 
artifactId | ArtifactIdSchema | | 
version | VersionSchema | | 

# GroupIdSchema

An ID of a single artifact group.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | An ID of a single artifact group. | 

# ArtifactIdSchema

The ID of a single artifact.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The ID of a single artifact. | 

# VersionSchema

A single version of an artifact.  Can be provided by the client when creating a new version, or it can be server-generated.  The value can be any string unique to the artifact, but it is recommended to use a simple integer or a semver value.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | A single version of an artifact.  Can be provided by the client when creating a new version, or it can be server-generated.  The value can be any string unique to the artifact, but it is recommended to use a simple integer or a semver value. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_artifact_version_meta_data.ApiResponseFor200) | The artifact version&#x27;s metadata.
404 | [ApiResponseFor404](#get_artifact_version_meta_data.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
500 | [ApiResponseFor500](#get_artifact_version_meta_data.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### get_artifact_version_meta_data.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**VersionMetaData**](../../models/VersionMetaData.md) |  | 


#### get_artifact_version_meta_data.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### get_artifact_version_meta_data.ApiResponseFor500
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

# **get_artifact_version_meta_data_by_content**
<a name="get_artifact_version_meta_data_by_content"></a>
> VersionMetaData get_artifact_version_meta_data_by_content(group_idartifact_idbody)

Get artifact version metadata by content

Gets the metadata for an artifact that matches the raw content.  Searches the registry for a version of the given artifact matching the content provided in the body of the POST.  This operation can fail for the following reasons:  * Provided content (request body) was empty (HTTP error `400`) * No artifact with the `artifactId` exists (HTTP error `404`) * No artifact version matching the provided content exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import metadata_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.version_meta_data import VersionMetaData
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "\"my-group\"",
        'artifactId': "\"example-artifact\"",
    }
    query_params = {
    }
    body = "{\"openapi\":\"3.0.2\",\"info\":{\"title\":\"Empty API\",\"version\":\"1.0.7\",\"description\":\"An example API design using OpenAPI.\"},\"paths\":{\"/widgets\":{\"get\":{\"responses\":{\"200\":{\"content\":{\"application/json\":{\"schema\":{\"type\":\"array\",\"items\":{\"type\":\"string\"}}}},\"description\":\"All widgets\"}},\"summary\":\"Get widgets\"}}},\"components\":{\"schemas\":{\"Widget\":{\"title\":\"Root Type for Widget\",\"description\":\"A sample data type.\",\"type\":\"object\",\"properties\":{\"property-1\":{\"type\":\"string\"},\"property-2\":{\"type\":\"boolean\"}},\"example\":{\"property-1\":\"value1\",\"property-2\":true}}}}}"
    try:
        # Get artifact version metadata by content
        api_response = api_instance.get_artifact_version_meta_data_by_content(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling MetadataApi->get_artifact_version_meta_data_by_content: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "\"my-group\"",
        'artifactId': "\"example-artifact\"",
    }
    query_params = {
        'canonical': True,
    }
    body = "{\"openapi\":\"3.0.2\",\"info\":{\"title\":\"Empty API\",\"version\":\"1.0.7\",\"description\":\"An example API design using OpenAPI.\"},\"paths\":{\"/widgets\":{\"get\":{\"responses\":{\"200\":{\"content\":{\"application/json\":{\"schema\":{\"type\":\"array\",\"items\":{\"type\":\"string\"}}}},\"description\":\"All widgets\"}},\"summary\":\"Get widgets\"}}},\"components\":{\"schemas\":{\"Widget\":{\"title\":\"Root Type for Widget\",\"description\":\"A sample data type.\",\"type\":\"object\",\"properties\":{\"property-1\":{\"type\":\"string\"},\"property-2\":{\"type\":\"boolean\"}},\"example\":{\"property-1\":\"value1\",\"property-2\":true}}}}}"
    try:
        # Get artifact version metadata by content
        api_response = api_instance.get_artifact_version_meta_data_by_content(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling MetadataApi->get_artifact_version_meta_data_by_content: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
canonical | CanonicalSchema | | optional


# CanonicalSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
groupId | GroupIdSchema | | 
artifactId | ArtifactIdSchema | | 

# GroupIdSchema

An ID of a single artifact group.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | An ID of a single artifact group. | 

# ArtifactIdSchema

The ID of a single artifact.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The ID of a single artifact. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_artifact_version_meta_data_by_content.ApiResponseFor200) | The metadata of the artifact version matching the provided content.
404 | [ApiResponseFor404](#get_artifact_version_meta_data_by_content.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
500 | [ApiResponseFor500](#get_artifact_version_meta_data_by_content.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### get_artifact_version_meta_data_by_content.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**VersionMetaData**](../../models/VersionMetaData.md) |  | 


#### get_artifact_version_meta_data_by_content.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### get_artifact_version_meta_data_by_content.ApiResponseFor500
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

# **update_artifact_meta_data**
<a name="update_artifact_meta_data"></a>
> update_artifact_meta_data(group_idartifact_ideditable_meta_data)

Update artifact metadata

Updates the editable parts of the artifact's metadata.  Not all metadata fields can be updated.  For example, `createdOn` and `createdBy` are both read-only properties.  This operation can fail for the following reasons:  * No artifact with the `artifactId` exists (HTTP error `404`) * A server error occurred (HTTP error `500`)

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import metadata_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.editable_meta_data import EditableMetaData
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "\"my-group\"",
        'artifactId': "\"example-artifact\"",
    }
    body = EditableMetaData(
        name="name_example",
        description="description_example",
        labels=[
            "labels_example"
        ],
        properties=Properties(
            key="key_example",
        ),
    )
    try:
        # Update artifact metadata
        api_response = api_instance.update_artifact_meta_data(
            path_params=path_params,
            body=body,
        )
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling MetadataApi->update_artifact_meta_data: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EditableMetaData**](../../models/EditableMetaData.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
groupId | GroupIdSchema | | 
artifactId | ArtifactIdSchema | | 

# GroupIdSchema

An ID of a single artifact group.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | An ID of a single artifact group. | 

# ArtifactIdSchema

The ID of a single artifact.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The ID of a single artifact. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#update_artifact_meta_data.ApiResponseFor204) | The artifact&#x27;s metadata was updated.
404 | [ApiResponseFor404](#update_artifact_meta_data.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
500 | [ApiResponseFor500](#update_artifact_meta_data.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### update_artifact_meta_data.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_artifact_meta_data.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### update_artifact_meta_data.ApiResponseFor500
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

# **update_artifact_owner**
<a name="update_artifact_owner"></a>
> update_artifact_owner(group_idartifact_idartifact_owner)

Update artifact owner

Changes the ownership of an artifact.  This operation can fail for the following reasons:  * No artifact with this `artifactId` exists (HTTP error `404`) * A server error occurred (HTTP error `500`)

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import metadata_api
from apicurioregistryclient.model.artifact_owner import ArtifactOwner
from apicurioregistryclient.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "\"my-group\"",
        'artifactId': "\"example-artifact\"",
    }
    body = ArtifactOwner(
        owner="owner_example",
    )
    try:
        # Update artifact owner
        api_response = api_instance.update_artifact_owner(
            path_params=path_params,
            body=body,
        )
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling MetadataApi->update_artifact_owner: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArtifactOwner**](../../models/ArtifactOwner.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
groupId | GroupIdSchema | | 
artifactId | ArtifactIdSchema | | 

# GroupIdSchema

An ID of a single artifact group.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | An ID of a single artifact group. | 

# ArtifactIdSchema

The ID of a single artifact.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The ID of a single artifact. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#update_artifact_owner.ApiResponseFor204) | The owner was successfully changed.
404 | [ApiResponseFor404](#update_artifact_owner.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
500 | [ApiResponseFor500](#update_artifact_owner.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### update_artifact_owner.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_artifact_owner.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### update_artifact_owner.ApiResponseFor500
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

# **update_artifact_version_meta_data**
<a name="update_artifact_version_meta_data"></a>
> update_artifact_version_meta_data(group_idartifact_idversioneditable_meta_data)

Update artifact version metadata

Updates the user-editable portion of the artifact version's metadata.  Only some of  the metadata fields are editable by the user.  For example, `description` is editable,  but `createdOn` is not.  This operation can fail for the following reasons:  * No artifact with this `artifactId` exists (HTTP error `404`) * No version with this `version` exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import metadata_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.editable_meta_data import EditableMetaData
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "\"my-group\"",
        'artifactId': "\"example-artifact\"",
        'version': "\"3.1.6\"",
    }
    body = EditableMetaData(
        name="name_example",
        description="description_example",
        labels=[
            "labels_example"
        ],
        properties=Properties(
            key="key_example",
        ),
    )
    try:
        # Update artifact version metadata
        api_response = api_instance.update_artifact_version_meta_data(
            path_params=path_params,
            body=body,
        )
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling MetadataApi->update_artifact_version_meta_data: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EditableMetaData**](../../models/EditableMetaData.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
groupId | GroupIdSchema | | 
artifactId | ArtifactIdSchema | | 
version | VersionSchema | | 

# GroupIdSchema

An ID of a single artifact group.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | An ID of a single artifact group. | 

# ArtifactIdSchema

The ID of a single artifact.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The ID of a single artifact. | 

# VersionSchema

A single version of an artifact.  Can be provided by the client when creating a new version, or it can be server-generated.  The value can be any string unique to the artifact, but it is recommended to use a simple integer or a semver value.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | A single version of an artifact.  Can be provided by the client when creating a new version, or it can be server-generated.  The value can be any string unique to the artifact, but it is recommended to use a simple integer or a semver value. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#update_artifact_version_meta_data.ApiResponseFor204) | The artifact version&#x27;s metadata was successfully updated.
404 | [ApiResponseFor404](#update_artifact_version_meta_data.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
500 | [ApiResponseFor500](#update_artifact_version_meta_data.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### update_artifact_version_meta_data.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_artifact_version_meta_data.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### update_artifact_version_meta_data.ApiResponseFor500
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

