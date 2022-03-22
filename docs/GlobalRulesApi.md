# apicurioregistryclient.GlobalRulesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_global_rule**](GlobalRulesApi.md#create_global_rule) | **POST** /admin/rules | Create global rule
[**delete_all_global_rules**](GlobalRulesApi.md#delete_all_global_rules) | **DELETE** /admin/rules | Delete all global rules
[**delete_global_rule**](GlobalRulesApi.md#delete_global_rule) | **DELETE** /admin/rules/{rule} | Delete global rule
[**get_global_rule_config**](GlobalRulesApi.md#get_global_rule_config) | **GET** /admin/rules/{rule} | Get global rule configuration
[**list_global_rules**](GlobalRulesApi.md#list_global_rules) | **GET** /admin/rules | List global rules
[**update_global_rule_config**](GlobalRulesApi.md#update_global_rule_config) | **PUT** /admin/rules/{rule} | Update global rule configuration


# **create_global_rule**
> create_global_rule(rule)

Create global rule

Adds a rule to the list of globally configured rules.  This operation can fail for the following reasons:  * The rule type is unknown (HTTP error `400`) * The rule already exists (HTTP error `409`) * A server error occurred (HTTP error `500`) 

### Example

* Basic Authentication (basicAuth):

```python
import time
import apicurioregistryclient
from apicurioregistryclient.api import global_rules_api
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
    rule = Rule(
        config="config_example",
        type=RuleType("VALIDITY"),
    ) # Rule | 

    # example passing only required values which don't have defaults set
    try:
        # Create global rule
        api_instance.create_global_rule(rule)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling GlobalRulesApi->create_global_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | [**Rule**](Rule.md)|  |

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
**204** | The global rule was added. |  -  |
**400** | Common response for all operations that can return a &#x60;400&#x60; error. |  -  |
**409** | Common response used when an input conflicts with existing data. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_global_rules**
> delete_all_global_rules()

Delete all global rules

Deletes all globally configured rules.  This operation can fail for the following reasons:  * A server error occurred (HTTP error `500`) 

### Example

* Basic Authentication (basicAuth):

```python
import time
import apicurioregistryclient
from apicurioregistryclient.api import global_rules_api
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
        api_instance.delete_all_global_rules()
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling GlobalRulesApi->delete_all_global_rules: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**204** | All global rules have been removed successfully. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_global_rule**
> delete_global_rule(rule)

Delete global rule

Deletes a single global rule.  If this is the only rule configured, this is the same as deleting **all** rules.  This operation can fail for the following reasons:  * Invalid rule name/type (HTTP error `400`) * No rule with name/type `rule` exists (HTTP error `404`) * Rule cannot be deleted (HTTP error `409`) * A server error occurred (HTTP error `500`) 

### Example

* Basic Authentication (basicAuth):

```python
import time
import apicurioregistryclient
from apicurioregistryclient.api import global_rules_api
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
    rule = RuleType("VALIDITY") # RuleType | The unique name/type of a rule.

    # example passing only required values which don't have defaults set
    try:
        # Delete global rule
        api_instance.delete_global_rule(rule)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling GlobalRulesApi->delete_global_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | **RuleType**| The unique name/type of a rule. |

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
**204** | The global rule was successfully deleted. |  -  |
**404** | Common response for all operations that can return a &#x60;404&#x60; error. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_global_rule_config**
> Rule get_global_rule_config(rule)

Get global rule configuration

Returns information about the named globally configured rule.  This operation can fail for the following reasons:  * Invalid rule name/type (HTTP error `400`) * No rule with name/type `rule` exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example

* Basic Authentication (basicAuth):

```python
import time
import apicurioregistryclient
from apicurioregistryclient.api import global_rules_api
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
    rule = RuleType("VALIDITY") # RuleType | The unique name/type of a rule.

    # example passing only required values which don't have defaults set
    try:
        # Get global rule configuration
        api_response = api_instance.get_global_rule_config(rule)
        pprint(api_response)
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling GlobalRulesApi->get_global_rule_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | **RuleType**| The unique name/type of a rule. |

### Return type

[**Rule**](Rule.md)

### Authorization

[basicAuth](../README.md#basicAuth)

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

# **list_global_rules**
> [RuleType] list_global_rules()

List global rules

Gets a list of all the currently configured global rules (if any).  This operation can fail for the following reasons:  * A server error occurred (HTTP error `500`) 

### Example

* Basic Authentication (basicAuth):

```python
import time
import apicurioregistryclient
from apicurioregistryclient.api import global_rules_api
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

### Return type

[**[RuleType]**](RuleType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of names of the globally configured rules. |  -  |
**500** | Common response for all operations that can fail with an unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_global_rule_config**
> Rule update_global_rule_config(rule, rule2)

Update global rule configuration

Updates the configuration for a globally configured rule.  This operation can fail for the following reasons:  * Invalid rule name/type (HTTP error `400`) * No rule with name/type `rule` exists (HTTP error `404`) * A server error occurred (HTTP error `500`) 

### Example

* Basic Authentication (basicAuth):

```python
import time
import apicurioregistryclient
from apicurioregistryclient.api import global_rules_api
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
    except apicurioregistryclient.ApiException as e:
        print("Exception when calling GlobalRulesApi->update_global_rule_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | **RuleType**| The unique name/type of a rule. |
 **rule2** | [**Rule**](Rule.md)|  |

### Return type

[**Rule**](Rule.md)

### Authorization

[basicAuth](../README.md#basicAuth)

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

