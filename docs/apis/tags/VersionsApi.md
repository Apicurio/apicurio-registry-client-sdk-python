<a name="__pageTop"></a>
# apicurioregistryclient.apis.tags.versions_api.VersionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_artifact_version**](#create_artifact_version) | **post** /groups/{groupId}/artifacts/{artifactId}/versions | Create artifact version
[**delete_artifact_version**](#delete_artifact_version) | **delete** /groups/{groupId}/artifacts/{artifactId}/versions/{version} | Delete artifact version
[**get_artifact_version**](#get_artifact_version) | **get** /groups/{groupId}/artifacts/{artifactId}/versions/{version} | Get artifact version
[**get_artifact_version_references**](#get_artifact_version_references) | **get** /groups/{groupId}/artifacts/{artifactId}/versions/{version}/references | Get artifact version
[**list_artifact_versions**](#list_artifact_versions) | **get** /groups/{groupId}/artifacts/{artifactId}/versions | List artifact versions
[**update_artifact_version_state**](#update_artifact_version_state) | **put** /groups/{groupId}/artifacts/{artifactId}/versions/{version}/state | Update artifact version state

# **create_artifact_version**
<a name="create_artifact_version"></a>
> VersionMetaData create_artifact_version(group_idartifact_idbody)

Create artifact version

Creates a new version of the artifact by uploading new content.  The configured rules for the artifact are applied, and if they all pass, the new content is added as the most recent  version of the artifact.  If any of the rules fail, an error is returned.  The body of the request can be the raw content of the new artifact version, or the raw content  and a set of references pointing to other artifacts, and the type of that content should match the artifact's type (for example if the artifact type is `AVRO` then the content of the request should be an Apache Avro document).  This operation can fail for the following reasons:  * Provided content (request body) was empty (HTTP error `400`) * No artifact with this `artifactId` exists (HTTP error `404`) * The new content violates one of the rules configured for the artifact (HTTP error `409`) * A server error occurred (HTTP error `500`) 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import versions_api
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
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = versions_api.VersionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "\"my-group\"",
        'artifactId': "\"example-artifact\"",
    }
    header_params = {
    }
    body = "{\"openapi\":\"3.0.2\",\"info\":{\"title\":\"Empty API\",\"version\":\"1.0.7\",\"description\":\"An example API design using OpenAPI.\"},\"paths\":{\"/widgets\":{\"get\":{\"responses\":{\"200\":{\"content\":{\"application/json\":{\"schema\":{\"type\":\"array\",\"items\":{\"type\":\"string\"}}}},\"description\":\"All widgets\"}},\"summary\":\"Get widgets\"}}},\"components\":{\"schemas\":{\"Widget\":{\"title\":\"Root Type for Widget\",\"description\":\"A sample data type.\",\"type\":\"object\",\"properties\":{\"property-1\":{\"type\":\"string\"},\"property-2\":{\"type\":\"boolean\"}},\"example\":{\"property-1\":\"value1\",\"property-2\":true}}}}}"
    try:
        # Create artifact version
        api_response = api_instance.create_artifact_version(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling VersionsApi->create_artifact_version: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "\"my-group\"",
        'artifactId': "\"example-artifact\"",
    }
    header_params = {
        'X-Registry-Version': "\"3.1.6\"",
        'X-Registry-Name': "\"Artifact name\"",
        'X-Registry-Description': "\"Artifact description\"",
        'X-Registry-Description-Encoded': "\"QXJ0aWZhY3QgZGVzY3JpcHRpb24K\"",
        'X-Registry-Name-Encoded': "\"QXJ0aWZhY3QgbmFtZQo=\"",
    }
    body = "{\"openapi\":\"3.0.2\",\"info\":{\"title\":\"Empty API\",\"version\":\"1.0.7\",\"description\":\"An example API design using OpenAPI.\"},\"paths\":{\"/widgets\":{\"get\":{\"responses\":{\"200\":{\"content\":{\"application/json\":{\"schema\":{\"type\":\"array\",\"items\":{\"type\":\"string\"}}}},\"description\":\"All widgets\"}},\"summary\":\"Get widgets\"}}},\"components\":{\"schemas\":{\"Widget\":{\"title\":\"Root Type for Widget\",\"description\":\"A sample data type.\",\"type\":\"object\",\"properties\":{\"property-1\":{\"type\":\"string\"},\"property-2\":{\"type\":\"boolean\"}},\"example\":{\"property-1\":\"value1\",\"property-2\":true}}}}}"
    try:
        # Create artifact version
        api_response = api_instance.create_artifact_version(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling VersionsApi->create_artifact_version: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody, SchemaForRequestBodyApplicationCreateExtendedjson, SchemaForRequestBodyApplicationVndCreateExtendedjson] | required |
header_params | RequestHeaderParams | |
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

# SchemaForRequestBodyApplicationCreateExtendedjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ContentCreateRequest**](../../models/ContentCreateRequest.md) |  | 


# SchemaForRequestBodyApplicationVndCreateExtendedjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ContentCreateRequest**](../../models/ContentCreateRequest.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Registry-Version | XRegistryVersionSchema | | optional
X-Registry-Name | XRegistryNameSchema | | optional
X-Registry-Description | XRegistryDescriptionSchema | | optional
X-Registry-Description-Encoded | XRegistryDescriptionEncodedSchema | | optional
X-Registry-Name-Encoded | XRegistryNameEncodedSchema | | optional

# XRegistryVersionSchema

A single version of an artifact.  Can be provided by the client when creating a new version, or it can be server-generated.  The value can be any string unique to the artifact, but it is recommended to use a simple integer or a semver value.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | A single version of an artifact.  Can be provided by the client when creating a new version, or it can be server-generated.  The value can be any string unique to the artifact, but it is recommended to use a simple integer or a semver value. | 

# XRegistryNameSchema

Name of the artifact.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Name of the artifact. | 

# XRegistryDescriptionSchema

Description of the artifact.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Description of the artifact. | 

# XRegistryDescriptionEncodedSchema

Base64 encoded description of the artifact.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Base64 encoded description of the artifact. | 

# XRegistryNameEncodedSchema

Base64 encoded name of the artifact.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Base64 encoded name of the artifact. | 

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
200 | [ApiResponseFor200](#create_artifact_version.ApiResponseFor200) | The artifact version was successfully created.
404 | [ApiResponseFor404](#create_artifact_version.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
409 | [ApiResponseFor409](#create_artifact_version.ApiResponseFor409) | Common response used when an input conflicts with existing data.
500 | [ApiResponseFor500](#create_artifact_version.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### create_artifact_version.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**VersionMetaData**](../../models/VersionMetaData.md) |  | 


#### create_artifact_version.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### create_artifact_version.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RuleViolationError**](../../models/RuleViolationError.md) |  | 


#### create_artifact_version.ApiResponseFor500
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

# **delete_artifact_version**
<a name="delete_artifact_version"></a>
> delete_artifact_version(group_idartifact_idversion)

Delete artifact version

Deletes a single version of the artifact. Parameters `groupId`, `artifactId` and the unique `version` are needed. If this is the only version of the artifact, this operation is the same as  deleting the entire artifact.  This feature is disabled by default and it's discouraged for normal usage. To enable it, set the `registry.rest.artifact.deletion.enabled` property to true. This operation can fail for the following reasons:  * No artifact with this `artifactId` exists (HTTP error `404`) * No version with this `version` exists (HTTP error `404`)  * Feature is disabled (HTTP error `405`)  * A server error occurred (HTTP error `500`) 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import versions_api
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
    api_instance = versions_api.VersionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "\"my-group\"",
        'artifactId': "\"example-artifact\"",
        'version': "\"3.1.6\"",
    }
    try:
        # Delete artifact version
        api_response = api_instance.delete_artifact_version(
            path_params=path_params,
        )
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling VersionsApi->delete_artifact_version: %s\n" % e)
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
204 | [ApiResponseFor204](#delete_artifact_version.ApiResponseFor204) | The artifact version was successfully deleted.
404 | [ApiResponseFor404](#delete_artifact_version.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
405 | [ApiResponseFor405](#delete_artifact_version.ApiResponseFor405) | Common response for all operations that can fail due to method not allowed or disabled.
500 | [ApiResponseFor500](#delete_artifact_version.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### delete_artifact_version.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_artifact_version.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### delete_artifact_version.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor405ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor405ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### delete_artifact_version.ApiResponseFor500
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

# **get_artifact_version**
<a name="get_artifact_version"></a>
> file_type get_artifact_version(group_idartifact_idversion)

Get artifact version

Retrieves a single version of the artifact content.  Both the `artifactId` and the unique `version` number must be provided.  The `Content-Type` of the response depends  on the artifact type.  In most cases, this is `application/json`, but for some types  it may be different (for example, `PROTOBUF`).  This operation can fail for the following reasons:  * No artifact with this `artifactId` exists (HTTP error `404`) * No version with this `version` exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import versions_api
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
    api_instance = versions_api.VersionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "\"my-group\"",
        'artifactId': "\"example-artifact\"",
        'version': "\"3.1.6\"",
    }
    query_params = {
    }
    try:
        # Get artifact version
        api_response = api_instance.get_artifact_version(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling VersionsApi->get_artifact_version: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "\"my-group\"",
        'artifactId': "\"example-artifact\"",
        'version': "\"3.1.6\"",
    }
    query_params = {
        'dereference': True,
    }
    try:
        # Get artifact version
        api_response = api_instance.get_artifact_version(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling VersionsApi->get_artifact_version: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
dereference | DereferenceSchema | | optional


# DereferenceSchema

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
200 | [ApiResponseFor200](#get_artifact_version.ApiResponseFor200) | The content of one version of one artifact.
404 | [ApiResponseFor404](#get_artifact_version.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
500 | [ApiResponseFor500](#get_artifact_version.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### get_artifact_version.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBody

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 

#### get_artifact_version.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### get_artifact_version.ApiResponseFor500
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

# **get_artifact_version_references**
<a name="get_artifact_version_references"></a>
> [ArtifactReference] get_artifact_version_references(group_idartifact_idversion)

Get artifact version

Retrieves a single version of the artifact content.  Both the `artifactId` and the unique `version` number must be provided.  The `Content-Type` of the response depends  on the artifact type.  In most cases, this is `application/json`, but for some types  it may be different (for example, `PROTOBUF`).  This operation can fail for the following reasons:  * No artifact with this `artifactId` exists (HTTP error `404`) * No version with this `version` exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import versions_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.artifact_reference import ArtifactReference
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = versions_api.VersionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "\"my-group\"",
        'artifactId': "\"example-artifact\"",
        'version': "\"3.1.6\"",
    }
    try:
        # Get artifact version
        api_response = api_instance.get_artifact_version_references(
            path_params=path_params,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling VersionsApi->get_artifact_version_references: %s\n" % e)
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
200 | [ApiResponseFor200](#get_artifact_version_references.ApiResponseFor200) | List of all the artifact references for this artifact.
404 | [ApiResponseFor404](#get_artifact_version_references.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
500 | [ApiResponseFor500](#get_artifact_version_references.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### get_artifact_version_references.ApiResponseFor200
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
[**ArtifactReference**]({{complexTypePrefix}}ArtifactReference.md) | [**ArtifactReference**]({{complexTypePrefix}}ArtifactReference.md) | [**ArtifactReference**]({{complexTypePrefix}}ArtifactReference.md) |  | 

#### get_artifact_version_references.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### get_artifact_version_references.ApiResponseFor500
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

# **list_artifact_versions**
<a name="list_artifact_versions"></a>
> VersionSearchResults list_artifact_versions(group_idartifact_id)

List artifact versions

Returns a list of all versions of the artifact.  The result set is paged.  This operation can fail for the following reasons:  * No artifact with this `artifactId` exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import versions_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.version_search_results import VersionSearchResults
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = versions_api.VersionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "\"my-group\"",
        'artifactId': "\"example-artifact\"",
    }
    query_params = {
    }
    try:
        # List artifact versions
        api_response = api_instance.list_artifact_versions(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling VersionsApi->list_artifact_versions: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "\"my-group\"",
        'artifactId': "\"example-artifact\"",
    }
    query_params = {
        'offset': 1,
        'limit': 1,
    }
    try:
        # List artifact versions
        api_response = api_instance.list_artifact_versions(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling VersionsApi->list_artifact_versions: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
offset | OffsetSchema | | optional
limit | LimitSchema | | optional


# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

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
200 | [ApiResponseFor200](#list_artifact_versions.ApiResponseFor200) | List of all artifact versions.
404 | [ApiResponseFor404](#list_artifact_versions.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
500 | [ApiResponseFor500](#list_artifact_versions.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### list_artifact_versions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**VersionSearchResults**](../../models/VersionSearchResults.md) |  | 


#### list_artifact_versions.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### list_artifact_versions.ApiResponseFor500
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

# **update_artifact_version_state**
<a name="update_artifact_version_state"></a>
> update_artifact_version_state(group_idartifact_idversionupdate_state)

Update artifact version state

Updates the state of a specific version of an artifact.  For example, you can use  this operation to disable a specific version.  This operation can fail for the following reasons:  * No artifact with this `artifactId` exists (HTTP error `404`) * No version with this `version` exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import versions_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.update_state import UpdateState
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = versions_api.VersionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "\"my-group\"",
        'artifactId': "\"example-artifact\"",
        'version': "\"3.1.6\"",
    }
    body = UpdateState(
        state=ArtifactState("ENABLED"),
    )
    try:
        # Update artifact version state
        api_response = api_instance.update_artifact_version_state(
            path_params=path_params,
            body=body,
        )
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling VersionsApi->update_artifact_version_state: %s\n" % e)
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
[**UpdateState**](../../models/UpdateState.md) |  | 


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
204 | [ApiResponseFor204](#update_artifact_version_state.ApiResponseFor204) | Returned when the update was successful.
400 | [ApiResponseFor400](#update_artifact_version_state.ApiResponseFor400) | Common response for all operations that can return a &#x60;400&#x60; error.
404 | [ApiResponseFor404](#update_artifact_version_state.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
500 | [ApiResponseFor500](#update_artifact_version_state.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### update_artifact_version_state.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_artifact_version_state.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### update_artifact_version_state.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### update_artifact_version_state.ApiResponseFor500
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

