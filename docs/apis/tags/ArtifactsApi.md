<a name="__pageTop"></a>
# apicurioregistryclient.apis.tags.artifacts_api.ArtifactsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_artifact**](#create_artifact) | **post** /groups/{groupId}/artifacts | Create artifact
[**delete_artifact**](#delete_artifact) | **delete** /groups/{groupId}/artifacts/{artifactId} | Delete artifact
[**delete_artifacts_in_group**](#delete_artifacts_in_group) | **delete** /groups/{groupId}/artifacts | Delete artifacts in group
[**get_content_by_global_id**](#get_content_by_global_id) | **get** /ids/globalIds/{globalId} | Get artifact by global ID
[**get_content_by_hash**](#get_content_by_hash) | **get** /ids/contentHashes/{contentHash}/ | Get artifact content by SHA-256 hash
[**get_content_by_id**](#get_content_by_id) | **get** /ids/contentIds/{contentId}/ | Get artifact content by ID
[**get_latest_artifact**](#get_latest_artifact) | **get** /groups/{groupId}/artifacts/{artifactId} | Get latest artifact
[**list_artifacts_in_group**](#list_artifacts_in_group) | **get** /groups/{groupId}/artifacts | List artifacts in group
[**references_by_content_hash**](#references_by_content_hash) | **get** /ids/contentHashes/{contentHash}/references | List artifact references by hash
[**references_by_content_id**](#references_by_content_id) | **get** /ids/contentIds/{contentId}/references | List artifact references by content ID
[**references_by_global_id**](#references_by_global_id) | **get** /ids/globalIds/{globalId}/references | List artifact references by global ID
[**search_artifacts**](#search_artifacts) | **get** /search/artifacts | Search for artifacts
[**search_artifacts_by_content**](#search_artifacts_by_content) | **post** /search/artifacts | Search for artifacts by content
[**update_artifact**](#update_artifact) | **put** /groups/{groupId}/artifacts/{artifactId} | Update artifact
[**update_artifact_state**](#update_artifact_state) | **put** /groups/{groupId}/artifacts/{artifactId}/state | Update artifact state

# **create_artifact**
<a name="create_artifact"></a>
> ArtifactMetaData create_artifact(group_idbody)

Create artifact

Creates a new artifact by posting the artifact content.  The body of the request should be the raw content of the artifact.  This is typically in JSON format for *most* of the  supported types, but may be in another format for a few (for example, `PROTOBUF`).  The registry attempts to figure out what kind of artifact is being added from the following supported list:  * Avro (`AVRO`) * Protobuf (`PROTOBUF`) * JSON Schema (`JSON`) * Kafka Connect (`KCONNECT`) * OpenAPI (`OPENAPI`) * AsyncAPI (`ASYNCAPI`) * GraphQL (`GRAPHQL`) * Web Services Description Language (`WSDL`) * XML Schema (`XSD`)  Alternatively, you can specify the artifact type using the `X-Registry-ArtifactType`  HTTP request header, or include a hint in the request's `Content-Type`.  For example:  ``` Content-Type: application/json; artifactType=AVRO ```  An artifact is created using the content provided in the body of the request.  This content is created under a unique artifact ID that can be provided in the request using the `X-Registry-ArtifactId` request header.  If not provided in the request, the server generates a unique ID for the artifact.  It is typically recommended that callers provide the ID, because this is typically a meaningful identifier,  and for most use cases should be supplied by the caller.  If an artifact with the provided artifact ID already exists, the default behavior is for the server to reject the content with a 409 error.  However, the caller can supply the `ifExists` query parameter to alter this default behavior. The `ifExists` query parameter can have one of the following values:  * `FAIL` (*default*) - server rejects the content with a 409 error * `UPDATE` - server updates the existing artifact and returns the new metadata * `RETURN` - server does not create or add content to the server, but instead  returns the metadata for the existing artifact * `RETURN_OR_UPDATE` - server returns an existing **version** that matches the  provided content if such a version exists, otherwise a new version is created  This operation may fail for one of the following reasons:  * An invalid `ArtifactType` was indicated (HTTP error `400`) * No `ArtifactType` was indicated and the server could not determine one from the content (HTTP error `400`) * Provided content (request body) was empty (HTTP error `400`) * An artifact with the provided ID already exists (HTTP error `409`) * The content violates one of the configured global rules (HTTP error `409`) * A server error occurred (HTTP error `500`) 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import artifacts_api
from apicurioregistryclient.model.if_exists import IfExists
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.content_create_request import ContentCreateRequest
from apicurioregistryclient.model.artifact_type import ArtifactType
from apicurioregistryclient.model.rule_violation_error import RuleViolationError
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
    api_instance = artifacts_api.ArtifactsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "\"my-group\"",
    }
    query_params = {
    }
    header_params = {
    }
    body = None
    try:
        # Create artifact
        api_response = api_instance.create_artifact(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling ArtifactsApi->create_artifact: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "\"my-group\"",
    }
    query_params = {
        'ifExists': IfExists("FAIL"),
        'canonical': True,
    }
    header_params = {
        'X-Registry-ArtifactType': ArtifactType("AVRO"),
        'X-Registry-ArtifactId': "X-Registry-ArtifactId_example",
        'X-Registry-Version': "\"3.1.6\"",
        'X-Registry-Description': "\"Artifact description\"",
        'X-Registry-Description-Encoded': "\"QXJ0aWZhY3QgZGVzY3JpcHRpb24K\"",
        'X-Registry-Name': "\"Artifact name\"",
        'X-Registry-Name-Encoded': "\"QXJ0aWZhY3QgbmFtZQo=\"",
        'X-Registry-Content-Hash': "X-Registry-Content-Hash_example",
        'X-Registry-Hash-Algorithm': "SHA256",
    }
    body = None
    try:
        # Create artifact
        api_response = api_instance.create_artifact(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling ArtifactsApi->create_artifact: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody, SchemaForRequestBodyApplicationCreateExtendedjson] | required |
query_params | RequestQueryParams | |
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
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# SchemaForRequestBodyApplicationCreateExtendedjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ContentCreateRequest**](../../models/ContentCreateRequest.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ifExists | IfExistsSchema | | optional
canonical | CanonicalSchema | | optional


# IfExistsSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**IfExists**](../../models/IfExists.md) |  | 


# CanonicalSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Registry-ArtifactType | XRegistryArtifactTypeSchema | | optional
X-Registry-ArtifactId | XRegistryArtifactIdSchema | | optional
X-Registry-Version | XRegistryVersionSchema | | optional
X-Registry-Description | XRegistryDescriptionSchema | | optional
X-Registry-Description-Encoded | XRegistryDescriptionEncodedSchema | | optional
X-Registry-Name | XRegistryNameSchema | | optional
X-Registry-Name-Encoded | XRegistryNameEncodedSchema | | optional
X-Registry-Content-Hash | XRegistryContentHashSchema | | optional
X-Registry-Hash-Algorithm | XRegistryHashAlgorithmSchema | | optional

# XRegistryArtifactTypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**ArtifactType**](../../models/ArtifactType.md) |  | 


# XRegistryArtifactIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XRegistryVersionSchema

A single version of an artifact.  Can be provided by the client when creating a new version, or it can be server-generated.  The value can be any string unique to the artifact, but it is recommended to use a simple integer or a semver value.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | A single version of an artifact.  Can be provided by the client when creating a new version, or it can be server-generated.  The value can be any string unique to the artifact, but it is recommended to use a simple integer or a semver value. | 

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

# XRegistryNameSchema

Name of the artifact.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Name of the artifact. | 

# XRegistryNameEncodedSchema

Base64 encoded name of the artifact.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Base64 encoded name of the artifact. | 

# XRegistryContentHashSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XRegistryHashAlgorithmSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["SHA256", "MD5", ] 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
groupId | GroupIdSchema | | 

# GroupIdSchema

An ID of a single artifact group.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | An ID of a single artifact group. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_artifact.ApiResponseFor200) | Artifact was successfully created.
400 | [ApiResponseFor400](#create_artifact.ApiResponseFor400) | Common response for all operations that can return a &#x60;400&#x60; error.
409 | [ApiResponseFor409](#create_artifact.ApiResponseFor409) | Common response used when an input conflicts with existing data.
500 | [ApiResponseFor500](#create_artifact.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### create_artifact.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArtifactMetaData**](../../models/ArtifactMetaData.md) |  | 


#### create_artifact.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### create_artifact.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RuleViolationError**](../../models/RuleViolationError.md) |  | 


#### create_artifact.ApiResponseFor500
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

# **delete_artifact**
<a name="delete_artifact"></a>
> delete_artifact(group_idartifact_id)

Delete artifact

Deletes an artifact completely, resulting in all versions of the artifact also being deleted.  This may fail for one of the following reasons:  * No artifact with the `artifactId` exists (HTTP error `404`) * A server error occurred (HTTP error `500`)

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import artifacts_api
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
    api_instance = artifacts_api.ArtifactsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "\"my-group\"",
        'artifactId': "\"example-artifact\"",
    }
    try:
        # Delete artifact
        api_response = api_instance.delete_artifact(
            path_params=path_params,
        )
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling ArtifactsApi->delete_artifact: %s\n" % e)
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
204 | [ApiResponseFor204](#delete_artifact.ApiResponseFor204) | Returned when the artifact was successfully deleted.
404 | [ApiResponseFor404](#delete_artifact.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
500 | [ApiResponseFor500](#delete_artifact.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### delete_artifact.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_artifact.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### delete_artifact.ApiResponseFor500
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

# **delete_artifacts_in_group**
<a name="delete_artifacts_in_group"></a>
> delete_artifacts_in_group(group_id)

Delete artifacts in group

Deletes all of the artifacts that exist in a given group.

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import artifacts_api
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
    api_instance = artifacts_api.ArtifactsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "\"my-group\"",
    }
    try:
        # Delete artifacts in group
        api_response = api_instance.delete_artifacts_in_group(
            path_params=path_params,
        )
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling ArtifactsApi->delete_artifacts_in_group: %s\n" % e)
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

# GroupIdSchema

An ID of a single artifact group.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | An ID of a single artifact group. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_artifacts_in_group.ApiResponseFor204) | When the delete operation is successful, a simple 204 is returned.
500 | [ApiResponseFor500](#delete_artifacts_in_group.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### delete_artifacts_in_group.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_artifacts_in_group.ApiResponseFor500
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

# **get_content_by_global_id**
<a name="get_content_by_global_id"></a>
> file_type get_content_by_global_id(global_id)

Get artifact by global ID

Gets the content for an artifact version in the registry using its globally unique identifier.  This operation may fail for one of the following reasons:  * No artifact version with this `globalId` exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import artifacts_api
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
    api_instance = artifacts_api.ArtifactsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'globalId': 1,
    }
    query_params = {
    }
    try:
        # Get artifact by global ID
        api_response = api_instance.get_content_by_global_id(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling ArtifactsApi->get_content_by_global_id: %s\n" % e)

    # example passing only optional values
    path_params = {
        'globalId': 1,
    }
    query_params = {
        'dereference': True,
    }
    try:
        # Get artifact by global ID
        api_response = api_instance.get_content_by_global_id(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling ArtifactsApi->get_content_by_global_id: %s\n" % e)
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
globalId | GlobalIdSchema | | 

# GlobalIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_content_by_global_id.ApiResponseFor200) | The content of one version of one artifact.
404 | [ApiResponseFor404](#get_content_by_global_id.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
500 | [ApiResponseFor500](#get_content_by_global_id.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### get_content_by_global_id.ApiResponseFor200
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

#### get_content_by_global_id.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### get_content_by_global_id.ApiResponseFor500
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

# **get_content_by_hash**
<a name="get_content_by_hash"></a>
> file_type get_content_by_hash(content_hash)

Get artifact content by SHA-256 hash

Gets the content for an artifact version in the registry using the  SHA-256 hash of the content.  This content hash may be shared by multiple artifact versions in the case where the artifact versions have identical content.  This operation may fail for one of the following reasons:  * No content with this `contentHash` exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import artifacts_api
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
    api_instance = artifacts_api.ArtifactsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'contentHash': "contentHash_example",
    }
    try:
        # Get artifact content by SHA-256 hash
        api_response = api_instance.get_content_by_hash(
            path_params=path_params,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling ArtifactsApi->get_content_by_hash: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
contentHash | ContentHashSchema | | 

# ContentHashSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_content_by_hash.ApiResponseFor200) | The content of one version of one artifact.
404 | [ApiResponseFor404](#get_content_by_hash.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
500 | [ApiResponseFor500](#get_content_by_hash.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### get_content_by_hash.ApiResponseFor200
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

#### get_content_by_hash.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### get_content_by_hash.ApiResponseFor500
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

# **get_content_by_id**
<a name="get_content_by_id"></a>
> file_type get_content_by_id(content_id)

Get artifact content by ID

Gets the content for an artifact version in the registry using the unique content identifier for that content.  This content ID may be shared by multiple artifact versions in the case where the artifact versions are identical.  This operation may fail for one of the following reasons:  * No content with this `contentId` exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import artifacts_api
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
    api_instance = artifacts_api.ArtifactsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'contentId': 1,
    }
    try:
        # Get artifact content by ID
        api_response = api_instance.get_content_by_id(
            path_params=path_params,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling ArtifactsApi->get_content_by_id: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
contentId | ContentIdSchema | | 

# ContentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_content_by_id.ApiResponseFor200) | The content of one version of one artifact.
404 | [ApiResponseFor404](#get_content_by_id.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
500 | [ApiResponseFor500](#get_content_by_id.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### get_content_by_id.ApiResponseFor200
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

#### get_content_by_id.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### get_content_by_id.ApiResponseFor500
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

# **get_latest_artifact**
<a name="get_latest_artifact"></a>
> file_type get_latest_artifact(group_idartifact_id)

Get latest artifact

Returns the latest version of the artifact in its raw form.  The `Content-Type` of the response depends on the artifact type.  In most cases, this is `application/json`, but  for some types it may be different (for example, `PROTOBUF`).  This operation may fail for one of the following reasons:  * No artifact with this `artifactId` exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import artifacts_api
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
    api_instance = artifacts_api.ArtifactsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "\"my-group\"",
        'artifactId': "\"example-artifact\"",
    }
    query_params = {
    }
    try:
        # Get latest artifact
        api_response = api_instance.get_latest_artifact(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling ArtifactsApi->get_latest_artifact: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "\"my-group\"",
        'artifactId': "\"example-artifact\"",
    }
    query_params = {
        'dereference': True,
    }
    try:
        # Get latest artifact
        api_response = api_instance.get_latest_artifact(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling ArtifactsApi->get_latest_artifact: %s\n" % e)
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
200 | [ApiResponseFor200](#get_latest_artifact.ApiResponseFor200) | The content of one version of one artifact.
404 | [ApiResponseFor404](#get_latest_artifact.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
500 | [ApiResponseFor500](#get_latest_artifact.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### get_latest_artifact.ApiResponseFor200
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

#### get_latest_artifact.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### get_latest_artifact.ApiResponseFor500
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

# **list_artifacts_in_group**
<a name="list_artifacts_in_group"></a>
> ArtifactSearchResults list_artifacts_in_group(group_id)

List artifacts in group

Returns a list of all artifacts in the group.  This list is paged.

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import artifacts_api
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

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = artifacts_api.ArtifactsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "\"my-group\"",
    }
    query_params = {
    }
    try:
        # List artifacts in group
        api_response = api_instance.list_artifacts_in_group(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling ArtifactsApi->list_artifacts_in_group: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "\"my-group\"",
    }
    query_params = {
        'limit': 1,
        'offset': 1,
        'order': SortOrder("asc"),
        'orderby': SortBy("name"),
    }
    try:
        # List artifacts in group
        api_response = api_instance.list_artifacts_in_group(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling ArtifactsApi->list_artifacts_in_group: %s\n" % e)
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
limit | LimitSchema | | optional
offset | OffsetSchema | | optional
order | OrderSchema | | optional
orderby | OrderbySchema | | optional


# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OrderSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**SortOrder**](../../models/SortOrder.md) |  | 


# OrderbySchema
Type | Description  | Notes
------------- | ------------- | -------------
[**SortBy**](../../models/SortBy.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
groupId | GroupIdSchema | | 

# GroupIdSchema

An ID of a single artifact group.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | An ID of a single artifact group. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_artifacts_in_group.ApiResponseFor200) | On a successful response, returns a bounded set of artifacts.
500 | [ApiResponseFor500](#list_artifacts_in_group.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### list_artifacts_in_group.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArtifactSearchResults**](../../models/ArtifactSearchResults.md) |  | 


#### list_artifacts_in_group.ApiResponseFor500
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

# **references_by_content_hash**
<a name="references_by_content_hash"></a>
> [ArtifactReference] references_by_content_hash(content_hash)

List artifact references by hash

Returns a list containing all the artifact references for the artifact identified by the content hash.  This operation may fail for one of the following reasons:  * A server error occurred (HTTP error `500`) 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import artifacts_api
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
    api_instance = artifacts_api.ArtifactsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'contentHash': "contentHash_example",
    }
    try:
        # List artifact references by hash
        api_response = api_instance.references_by_content_hash(
            path_params=path_params,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling ArtifactsApi->references_by_content_hash: %s\n" % e)
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
contentHash | ContentHashSchema | | 

# ContentHashSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#references_by_content_hash.ApiResponseFor200) | A list containing all the references for the artifact identified by the content hash.

#### references_by_content_hash.ApiResponseFor200
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

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **references_by_content_id**
<a name="references_by_content_id"></a>
> [ArtifactReference] references_by_content_id(content_id)

List artifact references by content ID

Returns a list containing all the artifact references identified by content id.  This operation may fail for one of the following reasons:  * A server error occurred (HTTP error `500`)

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import artifacts_api
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
    api_instance = artifacts_api.ArtifactsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'contentId': 1,
    }
    try:
        # List artifact references by content ID
        api_response = api_instance.references_by_content_id(
            path_params=path_params,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling ArtifactsApi->references_by_content_id: %s\n" % e)
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
contentId | ContentIdSchema | | 

# ContentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#references_by_content_id.ApiResponseFor200) | A list containing all the references for the artifact identified by content id.

#### references_by_content_id.ApiResponseFor200
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

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **references_by_global_id**
<a name="references_by_global_id"></a>
> [ArtifactReference] references_by_global_id(global_id)

List artifact references by global ID

Returns a list containing all the artifact references for the artifact identified by global id..  This operation may fail for one of the following reasons:  * A server error occurred (HTTP error `500`)

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import artifacts_api
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
    api_instance = artifacts_api.ArtifactsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'globalId': 1,
    }
    try:
        # List artifact references by global ID
        api_response = api_instance.references_by_global_id(
            path_params=path_params,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling ArtifactsApi->references_by_global_id: %s\n" % e)
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
globalId | GlobalIdSchema | | 

# GlobalIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#references_by_global_id.ApiResponseFor200) | A list containing all the references for the artifact identified by global id.

#### references_by_global_id.ApiResponseFor200
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

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **search_artifacts**
<a name="search_artifacts"></a>
> ArtifactSearchResults search_artifacts()

Search for artifacts

Returns a paginated list of all artifacts that match the provided filter criteria. 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import artifacts_api
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

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = artifacts_api.ArtifactsApi(api_client)

    # example passing only optional values
    query_params = {
        'name': "name_example",
        'offset': 0,
        'limit': 20,
        'order': SortOrder("asc"),
        'orderby': SortBy("name"),
        'labels': [
        "labels_example"
    ],
        'properties': [
        "properties_example"
    ],
        'description': "description_example",
        'group': "group_example",
        'globalId': 1,
        'contentId': 1,
    }
    try:
        # Search for artifacts
        api_response = api_instance.search_artifacts(
            query_params=query_params,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling ArtifactsApi->search_artifacts: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | optional
offset | OffsetSchema | | optional
limit | LimitSchema | | optional
order | OrderSchema | | optional
orderby | OrderbySchema | | optional
labels | LabelsSchema | | optional
properties | PropertiesSchema | | optional
description | DescriptionSchema | | optional
group | GroupSchema | | optional
globalId | GlobalIdSchema | | optional
contentId | ContentIdSchema | | optional


# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 20

# OrderSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**SortOrder**](../../models/SortOrder.md) |  | 


# OrderbySchema
Type | Description  | Notes
------------- | ------------- | -------------
[**SortBy**](../../models/SortBy.md) |  | 


# LabelsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# PropertiesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# DescriptionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GroupSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GlobalIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# ContentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_artifacts.ApiResponseFor200) | On a successful response, returns a result set of artifacts - one for each artifact in the registry that matches the criteria.
500 | [ApiResponseFor500](#search_artifacts.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### search_artifacts.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArtifactSearchResults**](../../models/ArtifactSearchResults.md) |  | 


#### search_artifacts.ApiResponseFor500
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

# **search_artifacts_by_content**
<a name="search_artifacts_by_content"></a>
> ArtifactSearchResults search_artifacts_by_content(body)

Search for artifacts by content

Returns a paginated list of all artifacts with at least one version that matches the posted content. 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import artifacts_api
from apicurioregistryclient.model.artifact_search_results import ArtifactSearchResults
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.artifact_type import ArtifactType
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = artifacts_api.ArtifactsApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = open('/path/to/file', 'rb')
    try:
        # Search for artifacts by content
        api_response = api_instance.search_artifacts_by_content(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling ArtifactsApi->search_artifacts_by_content: %s\n" % e)

    # example passing only optional values
    query_params = {
        'canonical': True,
        'artifactType': ArtifactType("AVRO"),
        'offset': 0,
        'limit': 20,
        'order': "asc",
        'orderby': "name",
    }
    body = open('/path/to/file', 'rb')
    try:
        # Search for artifacts by content
        api_response = api_instance.search_artifacts_by_content(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling ArtifactsApi->search_artifacts_by_content: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody] | required |
query_params | RequestQueryParams | |
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
artifactType | ArtifactTypeSchema | | optional
offset | OffsetSchema | | optional
limit | LimitSchema | | optional
order | OrderSchema | | optional
orderby | OrderbySchema | | optional


# CanonicalSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# ArtifactTypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**ArtifactType**](../../models/ArtifactType.md) |  | 


# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 20

# OrderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["asc", "desc", ] 

# OrderbySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["name", "createdOn", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_artifacts_by_content.ApiResponseFor200) | On a successful response, returns a result set of artifacts - one for each artifact in the registry that matches the criteria.
500 | [ApiResponseFor500](#search_artifacts_by_content.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### search_artifacts_by_content.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArtifactSearchResults**](../../models/ArtifactSearchResults.md) |  | 


#### search_artifacts_by_content.ApiResponseFor500
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

# **update_artifact**
<a name="update_artifact"></a>
> ArtifactMetaData update_artifact(group_idartifact_idbody)

Update artifact

Updates an artifact by uploading new content.  The body of the request can be the raw content of the artifact or a JSON object containing both the raw content and a set of references to other artifacts..  This is typically in JSON format for *most* of the supported types, but may be in another format for a few (for example, `PROTOBUF`). The type of the content should be compatible with the artifact's type (it would be an error to update an `AVRO` artifact with new `OPENAPI` content, for example).  The update could fail for a number of reasons including:  * Provided content (request body) was empty (HTTP error `400`) * No artifact with the `artifactId` exists (HTTP error `404`) * The new content violates one of the rules configured for the artifact (HTTP error `409`) * A server error occurred (HTTP error `500`)  When successful, this creates a new version of the artifact, making it the most recent (and therefore official) version of the artifact.

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import artifacts_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.content_create_request import ContentCreateRequest
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
    api_instance = artifacts_api.ArtifactsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "\"my-group\"",
        'artifactId': "\"example-artifact\"",
    }
    header_params = {
    }
    body = None
    try:
        # Update artifact
        api_response = api_instance.update_artifact(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling ArtifactsApi->update_artifact: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "\"my-group\"",
        'artifactId': "\"example-artifact\"",
    }
    header_params = {
        'X-Registry-Version': "\"3.1.6\"",
        'X-Registry-Name': "\"Artifact name\"",
        'X-Registry-Name-Encoded': "\"QXJ0aWZhY3QgbmFtZQo=\"",
        'X-Registry-Description': "\"Artifact description\"",
        'X-Registry-Description-Encoded': "\"QXJ0aWZhY3QgZGVzY3JpcHRpb24K\"",
    }
    body = None
    try:
        # Update artifact
        api_response = api_instance.update_artifact(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling ArtifactsApi->update_artifact: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody, SchemaForRequestBodyApplicationCreateExtendedjson] | required |
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
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# SchemaForRequestBodyApplicationCreateExtendedjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ContentCreateRequest**](../../models/ContentCreateRequest.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Registry-Version | XRegistryVersionSchema | | optional
X-Registry-Name | XRegistryNameSchema | | optional
X-Registry-Name-Encoded | XRegistryNameEncodedSchema | | optional
X-Registry-Description | XRegistryDescriptionSchema | | optional
X-Registry-Description-Encoded | XRegistryDescriptionEncodedSchema | | optional

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

# XRegistryNameEncodedSchema

Base64 encoded name of the artifact.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Base64 encoded name of the artifact. | 

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
200 | [ApiResponseFor200](#update_artifact.ApiResponseFor200) | When successful, returns the updated artifact metadata.
404 | [ApiResponseFor404](#update_artifact.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
409 | [ApiResponseFor409](#update_artifact.ApiResponseFor409) | Common response used when an input conflicts with existing data.
500 | [ApiResponseFor500](#update_artifact.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### update_artifact.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArtifactMetaData**](../../models/ArtifactMetaData.md) |  | 


#### update_artifact.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### update_artifact.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### update_artifact.ApiResponseFor500
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

# **update_artifact_state**
<a name="update_artifact_state"></a>
> update_artifact_state(group_idartifact_idupdate_state)

Update artifact state

Updates the state of the artifact.  For example, you can use this to mark the latest version of an artifact as `DEPRECATED`.  The operation changes the state of the latest  version of the artifact.  If multiple versions exist, only the most recent is changed.  This operation can fail for the following reasons:  * No artifact with this `artifactId` exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import artifacts_api
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
    api_instance = artifacts_api.ArtifactsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "\"my-group\"",
        'artifactId': "\"example-artifact\"",
    }
    body = UpdateState(
        state=ArtifactState("ENABLED"),
    )
    try:
        # Update artifact state
        api_response = api_instance.update_artifact_state(
            path_params=path_params,
            body=body,
        )
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling ArtifactsApi->update_artifact_state: %s\n" % e)
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
204 | [ApiResponseFor204](#update_artifact_state.ApiResponseFor204) | Returned when the operation was successful.
400 | [ApiResponseFor400](#update_artifact_state.ApiResponseFor400) | Common response for all operations that can return a &#x60;400&#x60; error.
404 | [ApiResponseFor404](#update_artifact_state.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
500 | [ApiResponseFor500](#update_artifact_state.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### update_artifact_state.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_artifact_state.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### update_artifact_state.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### update_artifact_state.ApiResponseFor500
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

