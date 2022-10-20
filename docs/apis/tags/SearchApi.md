<a name="__pageTop"></a>
# apicurioregistryclient.apis.tags.search_api.SearchApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_artifacts**](#search_artifacts) | **get** /search/artifacts | Search for artifacts
[**search_artifacts_by_content**](#search_artifacts_by_content) | **post** /search/artifacts | Search for artifacts by content

# **search_artifacts**
<a name="search_artifacts"></a>
> ArtifactSearchResults search_artifacts()

Search for artifacts

Returns a paginated list of all artifacts that match the provided filter criteria. 

### Example

* Basic Authentication (basicAuth):
```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import search_api
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
        print("Exception when calling SearchApi->search_artifacts: %s\n" % e)
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

[basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **search_artifacts_by_content**
<a name="search_artifacts_by_content"></a>
> ArtifactSearchResults search_artifacts_by_content(body)

Search for artifacts by content

Returns a paginated list of all artifacts with at least one version that matches the posted content. 

### Example

* Basic Authentication (basicAuth):
```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import search_api
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
        print("Exception when calling SearchApi->search_artifacts_by_content: %s\n" % e)

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
        print("Exception when calling SearchApi->search_artifacts_by_content: %s\n" % e)
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

[basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

