<a name="__pageTop"></a>
# apicurioregistryclient.apis.tags.global_rules_api.GlobalRulesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_global_rule**](#create_global_rule) | **post** /admin/rules | Create global rule
[**delete_all_global_rules**](#delete_all_global_rules) | **delete** /admin/rules | Delete all global rules
[**delete_global_rule**](#delete_global_rule) | **delete** /admin/rules/{rule} | Delete global rule
[**get_global_rule_config**](#get_global_rule_config) | **get** /admin/rules/{rule} | Get global rule configuration
[**list_global_rules**](#list_global_rules) | **get** /admin/rules | List global rules
[**update_global_rule_config**](#update_global_rule_config) | **put** /admin/rules/{rule} | Update global rule configuration

# **create_global_rule**
<a name="create_global_rule"></a>
> create_global_rule(rule)

Create global rule

Adds a rule to the list of globally configured rules.  This operation can fail for the following reasons:  * The rule type is unknown (HTTP error `400`) * The rule already exists (HTTP error `409`) * A server error occurred (HTTP error `500`) 

### Example

* Basic Authentication (basicAuth):
```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import global_rules_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.rule import Rule
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
    api_instance = global_rules_api.GlobalRulesApi(api_client)

    # example passing only required values which don't have defaults set
    body = Rule(
        config="config_example",
        type=RuleType("VALIDITY"),
    )
    try:
        # Create global rule
        api_response = api_instance.create_global_rule(
            body=body,
        )
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling GlobalRulesApi->create_global_rule: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
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


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#create_global_rule.ApiResponseFor204) | The global rule was added.
400 | [ApiResponseFor400](#create_global_rule.ApiResponseFor400) | Common response for all operations that can return a &#x60;400&#x60; error.
409 | [ApiResponseFor409](#create_global_rule.ApiResponseFor409) | Common response used when an input conflicts with existing data.
500 | [ApiResponseFor500](#create_global_rule.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### create_global_rule.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_global_rule.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### create_global_rule.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### create_global_rule.ApiResponseFor500
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

# **delete_all_global_rules**
<a name="delete_all_global_rules"></a>
> delete_all_global_rules()

Delete all global rules

Deletes all globally configured rules.  This operation can fail for the following reasons:  * A server error occurred (HTTP error `500`) 

### Example

* Basic Authentication (basicAuth):
```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import global_rules_api
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
    api_instance = global_rules_api.GlobalRulesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Delete all global rules
        api_response = api_instance.delete_all_global_rules()
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling GlobalRulesApi->delete_all_global_rules: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_all_global_rules.ApiResponseFor204) | All global rules have been removed successfully.
500 | [ApiResponseFor500](#delete_all_global_rules.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### delete_all_global_rules.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_all_global_rules.ApiResponseFor500
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

# **delete_global_rule**
<a name="delete_global_rule"></a>
> delete_global_rule(rule)

Delete global rule

Deletes a single global rule.  If this is the only rule configured, this is the same as deleting **all** rules.  This operation can fail for the following reasons:  * Invalid rule name/type (HTTP error `400`) * No rule with name/type `rule` exists (HTTP error `404`) * Rule cannot be deleted (HTTP error `409`) * A server error occurred (HTTP error `500`) 

### Example

* Basic Authentication (basicAuth):
```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import global_rules_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.rule_type import RuleType
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
    api_instance = global_rules_api.GlobalRulesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'rule': RuleType("VALIDITY"),
    }
    try:
        # Delete global rule
        api_response = api_instance.delete_global_rule(
            path_params=path_params,
        )
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling GlobalRulesApi->delete_global_rule: %s\n" % e)
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
rule | RuleSchema | | 

# RuleSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**RuleType**](../../models/RuleType.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_global_rule.ApiResponseFor204) | The global rule was successfully deleted.
404 | [ApiResponseFor404](#delete_global_rule.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
500 | [ApiResponseFor500](#delete_global_rule.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### delete_global_rule.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_global_rule.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### delete_global_rule.ApiResponseFor500
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

# **get_global_rule_config**
<a name="get_global_rule_config"></a>
> Rule get_global_rule_config(rule)

Get global rule configuration

Returns information about the named globally configured rule.  This operation can fail for the following reasons:  * Invalid rule name/type (HTTP error `400`) * No rule with name/type `rule` exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example

* Basic Authentication (basicAuth):
```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import global_rules_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.rule import Rule
from apicurioregistryclient.model.rule_type import RuleType
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
    api_instance = global_rules_api.GlobalRulesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'rule': RuleType("VALIDITY"),
    }
    try:
        # Get global rule configuration
        api_response = api_instance.get_global_rule_config(
            path_params=path_params,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling GlobalRulesApi->get_global_rule_config: %s\n" % e)
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
rule | RuleSchema | | 

# RuleSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**RuleType**](../../models/RuleType.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_global_rule_config.ApiResponseFor200) | The global rule&#x27;s configuration.
404 | [ApiResponseFor404](#get_global_rule_config.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
500 | [ApiResponseFor500](#get_global_rule_config.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### get_global_rule_config.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Rule**](../../models/Rule.md) |  | 


#### get_global_rule_config.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### get_global_rule_config.ApiResponseFor500
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

# **list_global_rules**
<a name="list_global_rules"></a>
> [RuleType] list_global_rules()

List global rules

Gets a list of all the currently configured global rules (if any).  This operation can fail for the following reasons:  * A server error occurred (HTTP error `500`) 

### Example

* Basic Authentication (basicAuth):
```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import global_rules_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.rule_type import RuleType
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
    api_instance = global_rules_api.GlobalRulesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List global rules
        api_response = api_instance.list_global_rules()
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling GlobalRulesApi->list_global_rules: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_global_rules.ApiResponseFor200) | The list of names of the globally configured rules.
500 | [ApiResponseFor500](#list_global_rules.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### list_global_rules.ApiResponseFor200
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

#### list_global_rules.ApiResponseFor500
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

# **update_global_rule_config**
<a name="update_global_rule_config"></a>
> Rule update_global_rule_config(rulerule2)

Update global rule configuration

Updates the configuration for a globally configured rule.  This operation can fail for the following reasons:  * Invalid rule name/type (HTTP error `400`) * No rule with name/type `rule` exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example

* Basic Authentication (basicAuth):
```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import global_rules_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.rule import Rule
from apicurioregistryclient.model.rule_type import RuleType
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
    api_instance = global_rules_api.GlobalRulesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'rule': RuleType("VALIDITY"),
    }
    body = Rule(
        config="config_example",
        type=RuleType("VALIDITY"),
    )
    try:
        # Update global rule configuration
        api_response = api_instance.update_global_rule_config(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling GlobalRulesApi->update_global_rule_config: %s\n" % e)
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
rule | RuleSchema | | 

# RuleSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**RuleType**](../../models/RuleType.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_global_rule_config.ApiResponseFor200) | The global rule&#x27;s configuration was successfully updated.
404 | [ApiResponseFor404](#update_global_rule_config.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
500 | [ApiResponseFor500](#update_global_rule_config.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### update_global_rule_config.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Rule**](../../models/Rule.md) |  | 


#### update_global_rule_config.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### update_global_rule_config.ApiResponseFor500
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

