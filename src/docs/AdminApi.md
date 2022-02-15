# registryclient.AdminApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_global_rule**](AdminApi.md#create_global_rule) | **POST** /admin/rules | Create global rule
[**create_role_mapping**](AdminApi.md#create_role_mapping) | **POST** /admin/roleMappings | Create a new role mapping
[**delete_all_global_rules**](AdminApi.md#delete_all_global_rules) | **DELETE** /admin/rules | Delete all global rules
[**delete_global_rule**](AdminApi.md#delete_global_rule) | **DELETE** /admin/rules/{rule} | Delete global rule
[**delete_role_mapping**](AdminApi.md#delete_role_mapping) | **DELETE** /admin/roleMappings/{principalId} | Delete a role mapping
[**export_data**](AdminApi.md#export_data) | **GET** /admin/export | Export registry data
[**get_global_rule_config**](AdminApi.md#get_global_rule_config) | **GET** /admin/rules/{rule} | Get global rule configuration
[**get_log_configuration**](AdminApi.md#get_log_configuration) | **GET** /admin/loggers/{logger} | Get a single logger configuration
[**get_role_mapping**](AdminApi.md#get_role_mapping) | **GET** /admin/roleMappings/{principalId} | Return a single role mapping
[**import_data**](AdminApi.md#import_data) | **POST** /admin/import | Import registry data
[**list_global_rules**](AdminApi.md#list_global_rules) | **GET** /admin/rules | List global rules
[**list_log_configurations**](AdminApi.md#list_log_configurations) | **GET** /admin/loggers | List logging configurations
[**list_role_mappings**](AdminApi.md#list_role_mappings) | **GET** /admin/roleMappings | List all role mappings
[**remove_log_configuration**](AdminApi.md#remove_log_configuration) | **DELETE** /admin/loggers/{logger} | Removes logger configuration
[**set_log_configuration**](AdminApi.md#set_log_configuration) | **PUT** /admin/loggers/{logger} | Set a logger&#39;s configuration
[**update_global_rule_config**](AdminApi.md#update_global_rule_config) | **PUT** /admin/rules/{rule} | Update global rule configuration
[**update_role_mapping**](AdminApi.md#update_role_mapping) | **PUT** /admin/roleMappings/{principalId} | Update a role mapping


# **create_global_rule**
> create_global_rule(rule)

Create global rule

Adds a rule to the list of globally configured rules.  This operation can fail for the following reasons:  * The rule type is unknown (HTTP error `400`) * The rule already exists (HTTP error `409`) * A server error occurred (HTTP error `500`) 

### Example


```python
import time
import registryclient
from registryclient.api import admin_api
from registryclient.model.error import Error
from registryclient.model.rule import Rule
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = registryclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with registryclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = admin_api.AdminApi(api_client)
    rule = Rule(
        config="config_example",
        type=RuleType("VALIDITY"),
    ) # Rule | 

    # example passing only required values which don't have defaults set
    try:
        # Create global rule
        api_instance.create_global_rule(rule)
    except registryclient.ApiException as e:
        print("Exception when calling AdminApi->create_global_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | [**Rule**](Rule.md)|  |

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
**204** | The global rule was added. |  -  |
**400** | Common response for all operations that can return a &#x60;400&#x60; error. |  -  |
**409** | Common response used when an input conflicts with existing data. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_role_mapping**
> create_role_mapping(role_mapping)

Create a new role mapping

Creates a new mapping between a user/principal and a role.  This operation can fail for the following reasons:  * A server error occurred (HTTP error `500`)  

### Example


```python
import time
import registryclient
from registryclient.api import admin_api
from registryclient.model.role_mapping import RoleMapping
from registryclient.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = registryclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with registryclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = admin_api.AdminApi(api_client)
    role_mapping = RoleMapping(
        principal_id="principal_id_example",
        role=RoleType("READ_ONLY"),
        principal_name="principal_name_example",
    ) # RoleMapping | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new role mapping
        api_instance.create_role_mapping(role_mapping)
    except registryclient.ApiException as e:
        print("Exception when calling AdminApi->create_role_mapping: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_mapping** | [**RoleMapping**](RoleMapping.md)|  |

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
**204** | Returned when the role mapping was successfully created. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_global_rules**
> delete_all_global_rules()

Delete all global rules

Deletes all globally configured rules.  This operation can fail for the following reasons:  * A server error occurred (HTTP error `500`) 

### Example


```python
import time
import registryclient
from registryclient.api import admin_api
from registryclient.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = registryclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with registryclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Delete all global rules
        api_instance.delete_all_global_rules()
    except registryclient.ApiException as e:
        print("Exception when calling AdminApi->delete_all_global_rules: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | All global rules have been removed successfully. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_global_rule**
> delete_global_rule(rule)

Delete global rule

Deletes a single global rule.  If this is the only rule configured, this is the same as deleting **all** rules.  This operation can fail for the following reasons:  * Invalid rule name/type (HTTP error `400`) * No rule with name/type `rule` exists (HTTP error `404`) * Rule cannot be deleted (HTTP error `409`) * A server error occurred (HTTP error `500`) 

### Example


```python
import time
import registryclient
from registryclient.api import admin_api
from registryclient.model.rule_type import RuleType
from registryclient.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = registryclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with registryclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = admin_api.AdminApi(api_client)
    rule = RuleType("VALIDITY") # RuleType | The unique name/type of a rule.

    # example passing only required values which don't have defaults set
    try:
        # Delete global rule
        api_instance.delete_global_rule(rule)
    except registryclient.ApiException as e:
        print("Exception when calling AdminApi->delete_global_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | **RuleType**| The unique name/type of a rule. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The global rule was successfully deleted. |  -  |
**404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role_mapping**
> delete_role_mapping(principal_id)

Delete a role mapping

Deletes a single role mapping, effectively denying access to a user/principal.  This operation can fail for the following reasons:  * No role mapping for the principalId exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example


```python
import time
import registryclient
from registryclient.api import admin_api
from registryclient.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = registryclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with registryclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = admin_api.AdminApi(api_client)
    principal_id = "principalId_example" # str | Unique id of a principal (typically either a user or service account).

    # example passing only required values which don't have defaults set
    try:
        # Delete a role mapping
        api_instance.delete_role_mapping(principal_id)
    except registryclient.ApiException as e:
        print("Exception when calling AdminApi->delete_role_mapping: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **principal_id** | **str**| Unique id of a principal (typically either a user or service account). |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response returned when the delete was successful. |  -  |
**404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_data**
> file_type export_data()

Export registry data

Exports registry data as a ZIP archive.

### Example


```python
import time
import registryclient
from registryclient.api import admin_api
from registryclient.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = registryclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with registryclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Export registry data
        api_response = api_instance.export_data()
        pprint(api_response)
    except registryclient.ApiException as e:
        print("Exception when calling AdminApi->export_data: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**file_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response when the export is successful. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_global_rule_config**
> Rule get_global_rule_config(rule)

Get global rule configuration

Returns information about the named globally configured rule.  This operation can fail for the following reasons:  * Invalid rule name/type (HTTP error `400`) * No rule with name/type `rule` exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example


```python
import time
import registryclient
from registryclient.api import admin_api
from registryclient.model.rule_type import RuleType
from registryclient.model.error import Error
from registryclient.model.rule import Rule
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = registryclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with registryclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = admin_api.AdminApi(api_client)
    rule = RuleType("VALIDITY") # RuleType | The unique name/type of a rule.

    # example passing only required values which don't have defaults set
    try:
        # Get global rule configuration
        api_response = api_instance.get_global_rule_config(rule)
        pprint(api_response)
    except registryclient.ApiException as e:
        print("Exception when calling AdminApi->get_global_rule_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | **RuleType**| The unique name/type of a rule. |

### Return type

[**Rule**](Rule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The global rule&#39;s configuration. |  -  |
**404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_log_configuration**
> NamedLogConfiguration get_log_configuration(logger)

Get a single logger configuration

Returns the configured logger configuration for the provided logger name, if no logger configuration is persisted it will return the current default log configuration in the system.

### Example


```python
import time
import registryclient
from registryclient.api import admin_api
from registryclient.model.named_log_configuration import NamedLogConfiguration
from registryclient.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = registryclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with registryclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = admin_api.AdminApi(api_client)
    logger = "logger_example" # str | The name of a single logger.

    # example passing only required values which don't have defaults set
    try:
        # Get a single logger configuration
        api_response = api_instance.get_log_configuration(logger)
        pprint(api_response)
    except registryclient.ApiException as e:
        print("Exception when calling AdminApi->get_log_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logger** | **str**| The name of a single logger. |

### Return type

[**NamedLogConfiguration**](NamedLogConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The logger configuration for the named logger. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_mapping**
> RoleMapping get_role_mapping(principal_id)

Return a single role mapping

Gets the details of a single role mapping (by principalId).  This operation can fail for the following reasons:  * No role mapping for the principalId exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example


```python
import time
import registryclient
from registryclient.api import admin_api
from registryclient.model.role_mapping import RoleMapping
from registryclient.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = registryclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with registryclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = admin_api.AdminApi(api_client)
    principal_id = "principalId_example" # str | Unique id of a principal (typically either a user or service account).

    # example passing only required values which don't have defaults set
    try:
        # Return a single role mapping
        api_response = api_instance.get_role_mapping(principal_id)
        pprint(api_response)
    except registryclient.ApiException as e:
        print("Exception when calling AdminApi->get_role_mapping: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **principal_id** | **str**| Unique id of a principal (typically either a user or service account). |

### Return type

[**RoleMapping**](RoleMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | When successful, returns the details of a role mapping. |  -  |
**404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_data**
> import_data(body)

Import registry data

Imports registry data that was previously exported using the `/admin/export` operation.

### Example


```python
import time
import registryclient
from registryclient.api import admin_api
from registryclient.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = registryclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with registryclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = admin_api.AdminApi(api_client)
    body = open('/path/to/file', 'rb') # file_type | The ZIP file representing the previously exported registry data.

    # example passing only required values which don't have defaults set
    try:
        # Import registry data
        api_instance.import_data(body)
    except registryclient.ApiException as e:
        print("Exception when calling AdminApi->import_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **file_type**| The ZIP file representing the previously exported registry data. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/zip
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Indicates that the import was successful. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_global_rules**
> [RuleType] list_global_rules()

List global rules

Gets a list of all the currently configured global rules (if any).  This operation can fail for the following reasons:  * A server error occurred (HTTP error `500`) 

### Example


```python
import time
import registryclient
from registryclient.api import admin_api
from registryclient.model.rule_type import RuleType
from registryclient.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = registryclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with registryclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List global rules
        api_response = api_instance.list_global_rules()
        pprint(api_response)
    except registryclient.ApiException as e:
        print("Exception when calling AdminApi->list_global_rules: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[RuleType]**](RuleType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of names of the globally configured rules. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_log_configurations**
> [NamedLogConfiguration] list_log_configurations()

List logging configurations

List all of the configured logging levels.  These override the default logging configuration.

### Example


```python
import time
import registryclient
from registryclient.api import admin_api
from registryclient.model.named_log_configuration import NamedLogConfiguration
from registryclient.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = registryclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with registryclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List logging configurations
        api_response = api_instance.list_log_configurations()
        pprint(api_response)
    except registryclient.ApiException as e:
        print("Exception when calling AdminApi->list_log_configurations: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[NamedLogConfiguration]**](NamedLogConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of logging configurations. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_role_mappings**
> [RoleMapping] list_role_mappings()

List all role mappings

Gets a list of all role mappings configured in the registry (if any).  This operation can fail for the following reasons:  * A server error occurred (HTTP error `500`) 

### Example


```python
import time
import registryclient
from registryclient.api import admin_api
from registryclient.model.role_mapping import RoleMapping
from registryclient.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = registryclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with registryclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List all role mappings
        api_response = api_instance.list_role_mappings()
        pprint(api_response)
    except registryclient.ApiException as e:
        print("Exception when calling AdminApi->list_role_mappings: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[RoleMapping]**](RoleMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response will return the list of role mappings. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_log_configuration**
> NamedLogConfiguration remove_log_configuration(logger)

Removes logger configuration

Removes the configured logger configuration (if any) for the given logger.

### Example


```python
import time
import registryclient
from registryclient.api import admin_api
from registryclient.model.named_log_configuration import NamedLogConfiguration
from registryclient.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = registryclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with registryclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = admin_api.AdminApi(api_client)
    logger = "logger_example" # str | The name of a single logger.

    # example passing only required values which don't have defaults set
    try:
        # Removes logger configuration
        api_response = api_instance.remove_log_configuration(logger)
        pprint(api_response)
    except registryclient.ApiException as e:
        print("Exception when calling AdminApi->remove_log_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logger** | **str**| The name of a single logger. |

### Return type

[**NamedLogConfiguration**](NamedLogConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The default logger configuration (now that the configuration for this logger has been removed, the  default configuration is applied). |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_log_configuration**
> NamedLogConfiguration set_log_configuration(logger, log_configuration)

Set a logger's configuration

Configures the logger referenced by the provided logger name with the given configuration.

### Example


```python
import time
import registryclient
from registryclient.api import admin_api
from registryclient.model.named_log_configuration import NamedLogConfiguration
from registryclient.model.log_configuration import LogConfiguration
from registryclient.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = registryclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with registryclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = admin_api.AdminApi(api_client)
    logger = "logger_example" # str | The name of a single logger.
    log_configuration = LogConfiguration(
        level=LogLevel("DEBUG"),
    ) # LogConfiguration | The new logger configuration.

    # example passing only required values which don't have defaults set
    try:
        # Set a logger's configuration
        api_response = api_instance.set_log_configuration(logger, log_configuration)
        pprint(api_response)
    except registryclient.ApiException as e:
        print("Exception when calling AdminApi->set_log_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logger** | **str**| The name of a single logger. |
 **log_configuration** | [**LogConfiguration**](LogConfiguration.md)| The new logger configuration. |

### Return type

[**NamedLogConfiguration**](NamedLogConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new configuration for the given logger. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_global_rule_config**
> Rule update_global_rule_config(rule, rule2)

Update global rule configuration

Updates the configuration for a globally configured rule.  This operation can fail for the following reasons:  * Invalid rule name/type (HTTP error `400`) * No rule with name/type `rule` exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example


```python
import time
import registryclient
from registryclient.api import admin_api
from registryclient.model.rule_type import RuleType
from registryclient.model.error import Error
from registryclient.model.rule import Rule
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = registryclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with registryclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = admin_api.AdminApi(api_client)
    rule = RuleType("VALIDITY") # RuleType | The unique name/type of a rule.
    rule2 = Rule(
        config="config_example",
        type=RuleType("VALIDITY"),
    ) # Rule | 

    # example passing only required values which don't have defaults set
    try:
        # Update global rule configuration
        api_response = api_instance.update_global_rule_config(rule, rule2)
        pprint(api_response)
    except registryclient.ApiException as e:
        print("Exception when calling AdminApi->update_global_rule_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | **RuleType**| The unique name/type of a rule. |
 **rule2** | [**Rule**](Rule.md)|  |

### Return type

[**Rule**](Rule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The global rule&#39;s configuration was successfully updated. |  -  |
**404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role_mapping**
> update_role_mapping(principal_id, update_role)

Update a role mapping

Updates a single role mapping for one user/principal.  This operation can fail for the following reasons:  * No role mapping for the principalId exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example


```python
import time
import registryclient
from registryclient.api import admin_api
from registryclient.model.update_role import UpdateRole
from registryclient.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = registryclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with registryclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = admin_api.AdminApi(api_client)
    principal_id = "principalId_example" # str | Unique id of a principal (typically either a user or service account).
    update_role = UpdateRole(
        role=RoleType("READ_ONLY"),
    ) # UpdateRole | 

    # example passing only required values which don't have defaults set
    try:
        # Update a role mapping
        api_instance.update_role_mapping(principal_id, update_role)
    except registryclient.ApiException as e:
        print("Exception when calling AdminApi->update_role_mapping: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **principal_id** | **str**| Unique id of a principal (typically either a user or service account). |
 **update_role** | [**UpdateRole**](UpdateRole.md)|  |

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
**204** | Response when the update is successful. |  -  |
**404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

