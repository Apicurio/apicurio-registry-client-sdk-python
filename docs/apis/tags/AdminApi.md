<a name="__pageTop"></a>
# apicurioregistryclient.apis.tags.admin_api.AdminApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_global_rule**](#create_global_rule) | **post** /admin/rules | Create global rule
[**create_role_mapping**](#create_role_mapping) | **post** /admin/roleMappings | Create a new role mapping
[**delete_all_global_rules**](#delete_all_global_rules) | **delete** /admin/rules | Delete all global rules
[**delete_global_rule**](#delete_global_rule) | **delete** /admin/rules/{rule} | Delete global rule
[**delete_role_mapping**](#delete_role_mapping) | **delete** /admin/roleMappings/{principalId} | Delete a role mapping
[**export_data**](#export_data) | **get** /admin/export | Export registry data
[**get_config_property**](#get_config_property) | **get** /admin/config/properties/{propertyName} | Get configuration property value
[**get_global_rule_config**](#get_global_rule_config) | **get** /admin/rules/{rule} | Get global rule configuration
[**get_log_configuration**](#get_log_configuration) | **get** /admin/loggers/{logger} | Get a single logger configuration
[**get_role_mapping**](#get_role_mapping) | **get** /admin/roleMappings/{principalId} | Return a single role mapping
[**import_data**](#import_data) | **post** /admin/import | Import registry data
[**list_artifact_types**](#list_artifact_types) | **get** /admin/artifactTypes | List artifact types
[**list_config_properties**](#list_config_properties) | **get** /admin/config/properties | List all configuration properties
[**list_global_rules**](#list_global_rules) | **get** /admin/rules | List global rules
[**list_log_configurations**](#list_log_configurations) | **get** /admin/loggers | List logging configurations
[**list_role_mappings**](#list_role_mappings) | **get** /admin/roleMappings | List all role mappings
[**remove_log_configuration**](#remove_log_configuration) | **delete** /admin/loggers/{logger} | Removes logger configuration
[**reset_config_property**](#reset_config_property) | **delete** /admin/config/properties/{propertyName} | Reset a configuration property
[**set_log_configuration**](#set_log_configuration) | **put** /admin/loggers/{logger} | Set a logger&#x27;s configuration
[**update_config_property**](#update_config_property) | **put** /admin/config/properties/{propertyName} | Update a configuration property
[**update_global_rule_config**](#update_global_rule_config) | **put** /admin/rules/{rule} | Update global rule configuration
[**update_role_mapping**](#update_role_mapping) | **put** /admin/roleMappings/{principalId} | Update a role mapping

# **create_global_rule**
<a name="create_global_rule"></a>
> create_global_rule(rule)

Create global rule

Adds a rule to the list of globally configured rules.  This operation can fail for the following reasons:  * The rule type is unknown (HTTP error `400`) * The rule already exists (HTTP error `409`) * A server error occurred (HTTP error `500`) 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import admin_api
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
    api_instance = admin_api.AdminApi(api_client)

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
        print("Exception when calling AdminApi->create_global_rule: %s\n" % e)
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

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_role_mapping**
<a name="create_role_mapping"></a>
> create_role_mapping(role_mapping)

Create a new role mapping

Creates a new mapping between a user/principal and a role.  This operation can fail for the following reasons:  * A server error occurred (HTTP error `500`)  

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import admin_api
from apicurioregistryclient.model.role_mapping import RoleMapping
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    body = RoleMapping(
        principal_id="principal_id_example",
        role=RoleType("READ_ONLY"),
        principal_name="principal_name_example",
    )
    try:
        # Create a new role mapping
        api_response = api_instance.create_role_mapping(
            body=body,
        )
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling AdminApi->create_role_mapping: %s\n" % e)
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
[**RoleMapping**](../../models/RoleMapping.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#create_role_mapping.ApiResponseFor204) | Returned when the role mapping was successfully created.
500 | [ApiResponseFor500](#create_role_mapping.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### create_role_mapping.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_role_mapping.ApiResponseFor500
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

# **delete_all_global_rules**
<a name="delete_all_global_rules"></a>
> delete_all_global_rules()

Delete all global rules

Deletes all globally configured rules.  This operation can fail for the following reasons:  * A server error occurred (HTTP error `500`) 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import admin_api
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
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Delete all global rules
        api_response = api_instance.delete_all_global_rules()
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling AdminApi->delete_all_global_rules: %s\n" % e)
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

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_global_rule**
<a name="delete_global_rule"></a>
> delete_global_rule(rule)

Delete global rule

Deletes a single global rule.  If this is the only rule configured, this is the same as deleting **all** rules.  This operation can fail for the following reasons:  * Invalid rule name/type (HTTP error `400`) * No rule with name/type `rule` exists (HTTP error `404`) * Rule cannot be deleted (HTTP error `409`) * A server error occurred (HTTP error `500`) 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import admin_api
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
    api_instance = admin_api.AdminApi(api_client)

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
        print("Exception when calling AdminApi->delete_global_rule: %s\n" % e)
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

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_role_mapping**
<a name="delete_role_mapping"></a>
> delete_role_mapping(principal_id)

Delete a role mapping

Deletes a single role mapping, effectively denying access to a user/principal.  This operation can fail for the following reasons:  * No role mapping for the principalId exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import admin_api
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'principalId': "principalId_example",
    }
    try:
        # Delete a role mapping
        api_response = api_instance.delete_role_mapping(
            path_params=path_params,
        )
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling AdminApi->delete_role_mapping: %s\n" % e)
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
principalId | PrincipalIdSchema | | 

# PrincipalIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_role_mapping.ApiResponseFor204) | Response returned when the delete was successful.
404 | [ApiResponseFor404](#delete_role_mapping.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
500 | [ApiResponseFor500](#delete_role_mapping.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### delete_role_mapping.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_role_mapping.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### delete_role_mapping.ApiResponseFor500
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

# **export_data**
<a name="export_data"></a>
> file_type export_data()

Export registry data

Exports registry data as a ZIP archive.

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import admin_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.download_ref import DownloadRef
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = admin_api.AdminApi(api_client)

    # example passing only optional values
    query_params = {
        'forBrowser': True,
    }
    try:
        # Export registry data
        api_response = api_instance.export_data(
            query_params=query_params,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling AdminApi->export_data: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/zip', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
forBrowser | ForBrowserSchema | | optional


# ForBrowserSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#export_data.ApiResponseFor200) | Response when the export is successful.
500 | [ApiResponseFor500](#export_data.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### export_data.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationZip, SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationZip

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DownloadRef**](../../models/DownloadRef.md) |  | 


#### export_data.ApiResponseFor500
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

# **get_config_property**
<a name="get_config_property"></a>
> ConfigurationProperty get_config_property(property_name)

Get configuration property value

Returns the value of a single configuration property.  This operation may fail for one of the following reasons:  * Property not found or not configured (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import admin_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.configuration_property import ConfigurationProperty
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'propertyName': "propertyName_example",
    }
    try:
        # Get configuration property value
        api_response = api_instance.get_config_property(
            path_params=path_params,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling AdminApi->get_config_property: %s\n" % e)
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
propertyName | PropertyNameSchema | | 

# PropertyNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_config_property.ApiResponseFor200) | The configuration property value.
404 | [ApiResponseFor404](#get_config_property.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
500 | [ApiResponseFor500](#get_config_property.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### get_config_property.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConfigurationProperty**](../../models/ConfigurationProperty.md) |  | 


#### get_config_property.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### get_config_property.ApiResponseFor500
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

# **get_global_rule_config**
<a name="get_global_rule_config"></a>
> Rule get_global_rule_config(rule)

Get global rule configuration

Returns information about the named globally configured rule.  This operation can fail for the following reasons:  * Invalid rule name/type (HTTP error `400`) * No rule with name/type `rule` exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import admin_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.rule import Rule
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
    api_instance = admin_api.AdminApi(api_client)

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
        print("Exception when calling AdminApi->get_global_rule_config: %s\n" % e)
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

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_log_configuration**
<a name="get_log_configuration"></a>
> NamedLogConfiguration get_log_configuration(logger)

Get a single logger configuration

Returns the configured logger configuration for the provided logger name, if no logger configuration is persisted it will return the current default log configuration in the system.

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import admin_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.named_log_configuration import NamedLogConfiguration
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'logger': "logger_example",
    }
    try:
        # Get a single logger configuration
        api_response = api_instance.get_log_configuration(
            path_params=path_params,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling AdminApi->get_log_configuration: %s\n" % e)
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
logger | LoggerSchema | | 

# LoggerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_log_configuration.ApiResponseFor200) | The logger configuration for the named logger.
500 | [ApiResponseFor500](#get_log_configuration.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### get_log_configuration.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NamedLogConfiguration**](../../models/NamedLogConfiguration.md) |  | 


#### get_log_configuration.ApiResponseFor500
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

# **get_role_mapping**
<a name="get_role_mapping"></a>
> RoleMapping get_role_mapping(principal_id)

Return a single role mapping

Gets the details of a single role mapping (by `principalId`).  This operation can fail for the following reasons:  * No role mapping for the `principalId` exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import admin_api
from apicurioregistryclient.model.role_mapping import RoleMapping
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'principalId': "principalId_example",
    }
    try:
        # Return a single role mapping
        api_response = api_instance.get_role_mapping(
            path_params=path_params,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling AdminApi->get_role_mapping: %s\n" % e)
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
principalId | PrincipalIdSchema | | 

# PrincipalIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_role_mapping.ApiResponseFor200) | When successful, returns the details of a role mapping.
404 | [ApiResponseFor404](#get_role_mapping.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
500 | [ApiResponseFor500](#get_role_mapping.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### get_role_mapping.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RoleMapping**](../../models/RoleMapping.md) |  | 


#### get_role_mapping.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### get_role_mapping.ApiResponseFor500
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

# **import_data**
<a name="import_data"></a>
> import_data(body)

Import registry data

Imports registry data that was previously exported using the `/admin/export` operation.

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import admin_api
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = open('/path/to/file', 'rb')
    try:
        # Import registry data
        api_response = api_instance.import_data(
            header_params=header_params,
            body=body,
        )
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling AdminApi->import_data: %s\n" % e)

    # example passing only optional values
    header_params = {
        'X-Registry-Preserve-GlobalId': True,
        'X-Registry-Preserve-ContentId': True,
    }
    body = open('/path/to/file', 'rb')
    try:
        # Import registry data
        api_response = api_instance.import_data(
            header_params=header_params,
            body=body,
        )
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling AdminApi->import_data: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationZip] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/zip' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationZip

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Registry-Preserve-GlobalId | XRegistryPreserveGlobalIdSchema | | optional
X-Registry-Preserve-ContentId | XRegistryPreserveContentIdSchema | | optional

# XRegistryPreserveGlobalIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# XRegistryPreserveContentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#import_data.ApiResponseFor201) | Indicates that the import was successful.
500 | [ApiResponseFor500](#import_data.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### import_data.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### import_data.ApiResponseFor500
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

# **list_artifact_types**
<a name="list_artifact_types"></a>
> [ArtifactTypeInfo] list_artifact_types()

List artifact types

Gets a list of all the configured artifact types.  This operation can fail for the following reasons:  * A server error occurred (HTTP error `500`) 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import admin_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.artifact_type_info import ArtifactTypeInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List artifact types
        api_response = api_instance.list_artifact_types()
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling AdminApi->list_artifact_types: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_artifact_types.ApiResponseFor200) | The list of available artifact types.
500 | [ApiResponseFor500](#list_artifact_types.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### list_artifact_types.ApiResponseFor200
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
[**ArtifactTypeInfo**]({{complexTypePrefix}}ArtifactTypeInfo.md) | [**ArtifactTypeInfo**]({{complexTypePrefix}}ArtifactTypeInfo.md) | [**ArtifactTypeInfo**]({{complexTypePrefix}}ArtifactTypeInfo.md) |  | 

#### list_artifact_types.ApiResponseFor500
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

# **list_config_properties**
<a name="list_config_properties"></a>
> [ConfigurationProperty] list_config_properties()

List all configuration properties

Returns a list of all configuration properties that have been set.  The list is not paged.  This operation may fail for one of the following reasons:  * A server error occurred (HTTP error `500`) 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import admin_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.configuration_property import ConfigurationProperty
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List all configuration properties
        api_response = api_instance.list_config_properties()
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling AdminApi->list_config_properties: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_config_properties.ApiResponseFor200) | On a successful response, returns a list of configuration properties.
500 | [ApiResponseFor500](#list_config_properties.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### list_config_properties.ApiResponseFor200
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
[**ConfigurationProperty**]({{complexTypePrefix}}ConfigurationProperty.md) | [**ConfigurationProperty**]({{complexTypePrefix}}ConfigurationProperty.md) | [**ConfigurationProperty**]({{complexTypePrefix}}ConfigurationProperty.md) |  | 

#### list_config_properties.ApiResponseFor500
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

# **list_global_rules**
<a name="list_global_rules"></a>
> [RuleType] list_global_rules()

List global rules

Gets a list of all the currently configured global rules (if any).  This operation can fail for the following reasons:  * A server error occurred (HTTP error `500`) 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import admin_api
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
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List global rules
        api_response = api_instance.list_global_rules()
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling AdminApi->list_global_rules: %s\n" % e)
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

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_log_configurations**
<a name="list_log_configurations"></a>
> [NamedLogConfiguration] list_log_configurations()

List logging configurations

List all of the configured logging levels.  These override the default logging configuration.

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import admin_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.named_log_configuration import NamedLogConfiguration
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List logging configurations
        api_response = api_instance.list_log_configurations()
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling AdminApi->list_log_configurations: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_log_configurations.ApiResponseFor200) | The list of logging configurations.
500 | [ApiResponseFor500](#list_log_configurations.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### list_log_configurations.ApiResponseFor200
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
[**NamedLogConfiguration**]({{complexTypePrefix}}NamedLogConfiguration.md) | [**NamedLogConfiguration**]({{complexTypePrefix}}NamedLogConfiguration.md) | [**NamedLogConfiguration**]({{complexTypePrefix}}NamedLogConfiguration.md) |  | 

#### list_log_configurations.ApiResponseFor500
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

# **list_role_mappings**
<a name="list_role_mappings"></a>
> [RoleMapping] list_role_mappings()

List all role mappings

Gets a list of all role mappings configured in the registry (if any).  This operation can fail for the following reasons:  * A server error occurred (HTTP error `500`) 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import admin_api
from apicurioregistryclient.model.role_mapping import RoleMapping
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
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List all role mappings
        api_response = api_instance.list_role_mappings()
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling AdminApi->list_role_mappings: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_role_mappings.ApiResponseFor200) | A successful response will return the list of role mappings.
500 | [ApiResponseFor500](#list_role_mappings.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### list_role_mappings.ApiResponseFor200
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
[**RoleMapping**]({{complexTypePrefix}}RoleMapping.md) | [**RoleMapping**]({{complexTypePrefix}}RoleMapping.md) | [**RoleMapping**]({{complexTypePrefix}}RoleMapping.md) |  | 

#### list_role_mappings.ApiResponseFor500
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

# **remove_log_configuration**
<a name="remove_log_configuration"></a>
> NamedLogConfiguration remove_log_configuration(logger)

Removes logger configuration

Removes the configured logger configuration (if any) for the given logger.

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import admin_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.named_log_configuration import NamedLogConfiguration
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'logger': "logger_example",
    }
    try:
        # Removes logger configuration
        api_response = api_instance.remove_log_configuration(
            path_params=path_params,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling AdminApi->remove_log_configuration: %s\n" % e)
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
logger | LoggerSchema | | 

# LoggerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#remove_log_configuration.ApiResponseFor200) | The default logger configuration (now that the configuration for this logger has been removed, the  default configuration is applied).
500 | [ApiResponseFor500](#remove_log_configuration.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### remove_log_configuration.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NamedLogConfiguration**](../../models/NamedLogConfiguration.md) |  | 


#### remove_log_configuration.ApiResponseFor500
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

# **reset_config_property**
<a name="reset_config_property"></a>
> reset_config_property(property_name)

Reset a configuration property

Resets the value of a single configuration property.  This will return the property to its default value (see external documentation for supported properties and their default values).  This operation may fail for one of the following reasons:  * Property not found or not configured (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import admin_api
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'propertyName': "propertyName_example",
    }
    try:
        # Reset a configuration property
        api_response = api_instance.reset_config_property(
            path_params=path_params,
        )
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling AdminApi->reset_config_property: %s\n" % e)
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
propertyName | PropertyNameSchema | | 

# PropertyNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#reset_config_property.ApiResponseFor204) | The configuration property was deleted.
404 | [ApiResponseFor404](#reset_config_property.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
500 | [ApiResponseFor500](#reset_config_property.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### reset_config_property.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### reset_config_property.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### reset_config_property.ApiResponseFor500
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

# **set_log_configuration**
<a name="set_log_configuration"></a>
> NamedLogConfiguration set_log_configuration(loggerlog_configuration)

Set a logger's configuration

Configures the logger referenced by the provided logger name with the given configuration.

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import admin_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.log_configuration import LogConfiguration
from apicurioregistryclient.model.named_log_configuration import NamedLogConfiguration
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'logger': "logger_example",
    }
    body = LogConfiguration(
        level=LogLevel("DEBUG"),
    )
    try:
        # Set a logger's configuration
        api_response = api_instance.set_log_configuration(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling AdminApi->set_log_configuration: %s\n" % e)
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
[**LogConfiguration**](../../models/LogConfiguration.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
logger | LoggerSchema | | 

# LoggerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#set_log_configuration.ApiResponseFor200) | The new configuration for the given logger.
500 | [ApiResponseFor500](#set_log_configuration.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### set_log_configuration.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NamedLogConfiguration**](../../models/NamedLogConfiguration.md) |  | 


#### set_log_configuration.ApiResponseFor500
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

# **update_config_property**
<a name="update_config_property"></a>
> update_config_property(property_nameupdate_configuration_property)

Update a configuration property

Updates the value of a single configuration property.  This operation may fail for one of the following reasons:  * Property not found or not configured (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import admin_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.update_configuration_property import UpdateConfigurationProperty
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'propertyName': "propertyName_example",
    }
    body = UpdateConfigurationProperty(
        value="value_example",
    )
    try:
        # Update a configuration property
        api_response = api_instance.update_config_property(
            path_params=path_params,
            body=body,
        )
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling AdminApi->update_config_property: %s\n" % e)
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
[**UpdateConfigurationProperty**](../../models/UpdateConfigurationProperty.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
propertyName | PropertyNameSchema | | 

# PropertyNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#update_config_property.ApiResponseFor204) | The configuration property was updated.
404 | [ApiResponseFor404](#update_config_property.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
500 | [ApiResponseFor500](#update_config_property.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### update_config_property.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_config_property.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### update_config_property.ApiResponseFor500
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

# **update_global_rule_config**
<a name="update_global_rule_config"></a>
> Rule update_global_rule_config(rulerule2)

Update global rule configuration

Updates the configuration for a globally configured rule.  This operation can fail for the following reasons:  * Invalid rule name/type (HTTP error `400`) * No rule with name/type `rule` exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import admin_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.rule import Rule
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
    api_instance = admin_api.AdminApi(api_client)

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
        print("Exception when calling AdminApi->update_global_rule_config: %s\n" % e)
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

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_role_mapping**
<a name="update_role_mapping"></a>
> update_role_mapping(principal_idupdate_role)

Update a role mapping

Updates a single role mapping for one user/principal.  This operation can fail for the following reasons:  * No role mapping for the principalId exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example

```python
import apicurioregistryclient
from apicurioregistryclient.apis.tags import admin_api
from apicurioregistryclient.model.error import Error
from apicurioregistryclient.model.update_role import UpdateRole
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = apicurioregistryclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with apicurioregistryclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'principalId': "principalId_example",
    }
    body = UpdateRole(
        role=RoleType("READ_ONLY"),
    )
    try:
        # Update a role mapping
        api_response = api_instance.update_role_mapping(
            path_params=path_params,
            body=body,
        )
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling AdminApi->update_role_mapping: %s\n" % e)
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
[**UpdateRole**](../../models/UpdateRole.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
principalId | PrincipalIdSchema | | 

# PrincipalIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#update_role_mapping.ApiResponseFor204) | Response when the update is successful.
404 | [ApiResponseFor404](#update_role_mapping.ApiResponseFor404) | Common response for all operations that can return a &#x60;404&#x60; error.
500 | [ApiResponseFor500](#update_role_mapping.ApiResponseFor500) | Common response for all operations that can fail with an unexpected server error.

#### update_role_mapping.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_role_mapping.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### update_role_mapping.ApiResponseFor500
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

