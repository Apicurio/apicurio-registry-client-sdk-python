<a name="__pageTop"></a>
# apicurioregistryclient.apis.tags.artifact_rules_api.ArtifactRulesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_artifact_rule**](#create_artifact_rule) | **post** /groups/{groupId}/artifacts/{artifactId}/rules | Create artifact rule
[**delete_artifact_rule**](#delete_artifact_rule) | **delete** /groups/{groupId}/artifacts/{artifactId}/rules/{rule} | Delete artifact rule
[**delete_artifact_rules**](#delete_artifact_rules) | **delete** /groups/{groupId}/artifacts/{artifactId}/rules | Delete artifact rules
[**get_artifact_rule_config**](#get_artifact_rule_config) | **get** /groups/{groupId}/artifacts/{artifactId}/rules/{rule} | Get artifact rule configuration
[**list_artifact_rules**](#list_artifact_rules) | **get** /groups/{groupId}/artifacts/{artifactId}/rules | List artifact rules
[**test_update_artifact**](#test_update_artifact) | **put** /groups/{groupId}/artifacts/{artifactId}/test | Test update artifact
[**update_artifact_rule_config**](#update_artifact_rule_config) | **put** /groups/{groupId}/artifacts/{artifactId}/rules/{rule} | Update artifact rule configuration

# **create_artifact_rule**
<a name="create_artifact_rule"></a>
> create_artifact_rule(group_idartifact_idrule)

Create artifact rule

Adds a rule to the list of rules that get applied to the artifact when adding new versions.  All configured rules must pass to successfully add a new artifact version.  This operation can fail for the following reasons:  * No artifact with this `artifactId` exists (HTTP error `404`) * Rule (named in the request body) is unknown (HTTP error `400`) * A server error occurred (HTTP error `500`)

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import artifact_rules_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.rule import Rule
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = artifact_rules_api.ArtifactRulesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "\"my-group\"",
        'artifactId': "\"example-artifact\"",
    }
    body = Rule(
        config="config_example",
        type=RuleType("VALIDITY"),
    )
    try:
        # Create artifact rule
        api_response = api_instance.create_artifact_rule(
            path_params=path_params,
            body=body,
        )
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling ArtifactRulesApi->create_artifact_rule: %s\n" % e)
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
[**Rule**](../../models/Rule.md) |  | 


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
204 | [ApiResponseFor204](#create_artifact_rule.ApiResponseFor204) | The rule was added.
400 | [ApiResponseFor400](#create_artifact_rule.ApiResponseFor400) | Common response for all operations that can return a &#x60;400&#x60; error.
404 | [ApiResponseFor404](#create_artifact_rule.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
500 | [ApiResponseFor500](#create_artifact_rule.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### create_artifact_rule.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_artifact_rule.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### create_artifact_rule.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### create_artifact_rule.ApiResponseFor500
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

# **delete_artifact_rule**
<a name="delete_artifact_rule"></a>
> delete_artifact_rule(group_idartifact_idrule)

Delete artifact rule

Deletes a rule from the artifact.  This results in the rule no longer applying for this artifact.  If this is the only rule configured for the artifact, this is the  same as deleting **all** rules, and the globally configured rules now apply to this artifact.  This operation can fail for the following reasons:  * No artifact with this `artifactId` exists (HTTP error `404`) * No rule with this name/type is configured for this artifact (HTTP error `404`) * Invalid rule type (HTTP error `400`) * A server error occurred (HTTP error `500`)

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import artifact_rules_api
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
    api_instance = artifact_rules_api.ArtifactRulesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "\"my-group\"",
        'artifactId': "\"example-artifact\"",
        'rule': "VALIDITY",
    }
    try:
        # Delete artifact rule
        api_response = api_instance.delete_artifact_rule(
            path_params=path_params,
        )
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling ArtifactRulesApi->delete_artifact_rule: %s\n" % e)
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
rule | RuleSchema | | 

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

# RuleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["VALIDITY", "COMPATIBILITY", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_artifact_rule.ApiResponseFor204) | The rule was successfully deleted.
404 | [ApiResponseFor404](#delete_artifact_rule.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
500 | [ApiResponseFor500](#delete_artifact_rule.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### delete_artifact_rule.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_artifact_rule.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### delete_artifact_rule.ApiResponseFor500
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

# **delete_artifact_rules**
<a name="delete_artifact_rules"></a>
> delete_artifact_rules(group_idartifact_id)

Delete artifact rules

Deletes all of the rules configured for the artifact.  After this is done, the global rules apply to the artifact again.  This operation can fail for the following reasons:  * No artifact with this `artifactId` exists (HTTP error `404`) * A server error occurred (HTTP error `500`)

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import artifact_rules_api
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
    api_instance = artifact_rules_api.ArtifactRulesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "\"my-group\"",
        'artifactId': "\"example-artifact\"",
    }
    try:
        # Delete artifact rules
        api_response = api_instance.delete_artifact_rules(
            path_params=path_params,
        )
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling ArtifactRulesApi->delete_artifact_rules: %s\n" % e)
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
204 | [ApiResponseFor204](#delete_artifact_rules.ApiResponseFor204) | The rules were successfully deleted.
404 | [ApiResponseFor404](#delete_artifact_rules.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
500 | [ApiResponseFor500](#delete_artifact_rules.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### delete_artifact_rules.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_artifact_rules.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### delete_artifact_rules.ApiResponseFor500
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

# **get_artifact_rule_config**
<a name="get_artifact_rule_config"></a>
> Rule get_artifact_rule_config(group_idartifact_idrule)

Get artifact rule configuration

Returns information about a single rule configured for an artifact.  This is useful when you want to know what the current configuration settings are for a specific rule.  This operation can fail for the following reasons:  * No artifact with this `artifactId` exists (HTTP error `404`) * No rule with this name/type is configured for this artifact (HTTP error `404`) * Invalid rule type (HTTP error `400`) * A server error occurred (HTTP error `500`)

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import artifact_rules_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.rule import Rule
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = artifact_rules_api.ArtifactRulesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "\"my-group\"",
        'artifactId': "\"example-artifact\"",
        'rule': "VALIDITY",
    }
    try:
        # Get artifact rule configuration
        api_response = api_instance.get_artifact_rule_config(
            path_params=path_params,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling ArtifactRulesApi->get_artifact_rule_config: %s\n" % e)
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
rule | RuleSchema | | 

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

# RuleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["VALIDITY", "COMPATIBILITY", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_artifact_rule_config.ApiResponseFor200) | Information about a rule.
404 | [ApiResponseFor404](#get_artifact_rule_config.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
500 | [ApiResponseFor500](#get_artifact_rule_config.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### get_artifact_rule_config.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Rule**](../../models/Rule.md) |  | 


#### get_artifact_rule_config.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### get_artifact_rule_config.ApiResponseFor500
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

# **list_artifact_rules**
<a name="list_artifact_rules"></a>
> [RuleType] list_artifact_rules(group_idartifact_id)

List artifact rules

Returns a list of all rules configured for the artifact.  The set of rules determines how the content of an artifact can evolve over time.  If no rules are configured for an artifact, the set of globally configured rules are used.  If no global rules  are defined, there are no restrictions on content evolution.  This operation can fail for the following reasons:  * No artifact with this `artifactId` exists (HTTP error `404`) * A server error occurred (HTTP error `500`)

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import artifact_rules_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.rule_type import RuleType
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = artifact_rules_api.ArtifactRulesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "\"my-group\"",
        'artifactId': "\"example-artifact\"",
    }
    try:
        # List artifact rules
        api_response = api_instance.list_artifact_rules(
            path_params=path_params,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling ArtifactRulesApi->list_artifact_rules: %s\n" % e)
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
200 | [ApiResponseFor200](#list_artifact_rules.ApiResponseFor200) | Returns the names of the rules configured for the artifact.
404 | [ApiResponseFor404](#list_artifact_rules.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
500 | [ApiResponseFor500](#list_artifact_rules.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### list_artifact_rules.ApiResponseFor200
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
[**RuleType**]({{complexTypePrefix}}RuleType.md) | [**RuleType**]({{complexTypePrefix}}RuleType.md) | [**RuleType**]({{complexTypePrefix}}RuleType.md) |  | 

#### list_artifact_rules.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### list_artifact_rules.ApiResponseFor500
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

# **test_update_artifact**
<a name="test_update_artifact"></a>
> test_update_artifact(group_idartifact_idbody)

Test update artifact

Tests whether an update to the artifact's content *would* succeed for the provided content. Ultimately, this applies any rules configured for the artifact against the given content to determine whether the rules would pass or fail, but without actually updating the artifact content.  The body of the request should be the raw content of the artifact.  This is typically in  JSON format for *most* of the supported types, but may be in another format for a few  (for example, `PROTOBUF`).  The update could fail for a number of reasons including:  * Provided content (request body) was empty (HTTP error `400`) * No artifact with the `artifactId` exists (HTTP error `404`) * The new content violates one of the rules configured for the artifact (HTTP error `409`) * The provided artifact type is not recognized (HTTP error `404`) * A server error occurred (HTTP error `500`)  When successful, this operation simply returns a *No Content* response.  This response indicates that the content is valid against the configured content rules for the  artifact (or the global rules if no artifact rules are enabled).

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import artifact_rules_api
from apicurioregistryclient.model.error import Error
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
    api_instance = artifact_rules_api.ArtifactRulesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "\"my-group\"",
        'artifactId': "\"example-artifact\"",
    }
    body = None
    try:
        # Test update artifact
        api_response = api_instance.test_update_artifact(
            path_params=path_params,
            body=body,
        )
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling ArtifactRulesApi->test_update_artifact: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody] | required |
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
204 | [ApiResponseFor204](#test_update_artifact.ApiResponseFor204) | When successful, returns \&quot;No Content\&quot; to indicate that the rules passed, and the content was not updated.
404 | [ApiResponseFor404](#test_update_artifact.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
409 | [ApiResponseFor409](#test_update_artifact.ApiResponseFor409) | Common response used when an input conflicts with existing data.
500 | [ApiResponseFor500](#test_update_artifact.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### test_update_artifact.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### test_update_artifact.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### test_update_artifact.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RuleViolationError**](../../models/RuleViolationError.md) |  | 


#### test_update_artifact.ApiResponseFor500
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

# **update_artifact_rule_config**
<a name="update_artifact_rule_config"></a>
> Rule update_artifact_rule_config(group_idartifact_idrulerule2)

Update artifact rule configuration

Updates the configuration of a single rule for the artifact.  The configuration data is specific to each rule type, so the configuration of the `COMPATIBILITY` rule  is in a different format from the configuration of the `VALIDITY` rule.  This operation can fail for the following reasons:  * No artifact with this `artifactId` exists (HTTP error `404`) * No rule with this name/type is configured for this artifact (HTTP error `404`) * Invalid rule type (HTTP error `400`) * A server error occurred (HTTP error `500`) 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import artifact_rules_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.rule import Rule
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = artifact_rules_api.ArtifactRulesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "\"my-group\"",
        'artifactId': "\"example-artifact\"",
        'rule': "VALIDITY",
    }
    body = Rule(
        config="config_example",
        type=RuleType("VALIDITY"),
    )
    try:
        # Update artifact rule configuration
        api_response = api_instance.update_artifact_rule_config(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling ArtifactRulesApi->update_artifact_rule_config: %s\n" % e)
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
[**Rule**](../../models/Rule.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
groupId | GroupIdSchema | | 
artifactId | ArtifactIdSchema | | 
rule | RuleSchema | | 

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

# RuleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["VALIDITY", "COMPATIBILITY", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_artifact_rule_config.ApiResponseFor200) | Rule configuration was updated.
404 | [ApiResponseFor404](#update_artifact_rule_config.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
500 | [ApiResponseFor500](#update_artifact_rule_config.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### update_artifact_rule_config.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Rule**](../../models/Rule.md) |  | 


#### update_artifact_rule_config.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### update_artifact_rule_config.ApiResponseFor500
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

