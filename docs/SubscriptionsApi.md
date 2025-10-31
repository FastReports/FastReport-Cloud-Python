# fastreport_cloud_sdk.SubscriptionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscriptions_get_default_permissions**](SubscriptionsApi.md#subscriptions_get_default_permissions) | **GET** /api/manage/v1/Subscriptions/{subscriptionId}/defaultPermissions | Get subscription&#39;s default permissions for new entities
[**subscriptions_get_my_permissions**](SubscriptionsApi.md#subscriptions_get_my_permissions) | **GET** /api/manage/v1/Subscriptions/{subId}/mypermissions | Get user&#39;s permissions for a subscription by id
[**subscriptions_get_permissions**](SubscriptionsApi.md#subscriptions_get_permissions) | **GET** /api/manage/v1/Subscriptions/{id}/permissions | Get permissions for a subscription by id
[**subscriptions_get_subscription**](SubscriptionsApi.md#subscriptions_get_subscription) | **GET** /api/manage/v1/Subscriptions/{id} | Returns the subscription by id
[**subscriptions_get_subscriptions**](SubscriptionsApi.md#subscriptions_get_subscriptions) | **GET** /api/manage/v1/Subscriptions | Returns a list of all subscriptions of current user
[**subscriptions_rename_subscription**](SubscriptionsApi.md#subscriptions_rename_subscription) | **PUT** /api/manage/v1/Subscriptions/{subscriptionId}/rename | Rename subscription
[**subscriptions_update_default_permissions**](SubscriptionsApi.md#subscriptions_update_default_permissions) | **PUT** /api/manage/v1/Subscriptions/{subscriptionId}/defaultPermissions | Change subscription&#39;s default permissions for new entities
[**subscriptions_update_locale**](SubscriptionsApi.md#subscriptions_update_locale) | **PUT** /api/manage/v1/Subscriptions/{subscriptionId}/Locale | Update subscription&#39;s default locale
[**subscriptions_update_permissions**](SubscriptionsApi.md#subscriptions_update_permissions) | **POST** /api/manage/v1/Subscriptions/{id}/permissions | Update permissions
[**subscriptions_update_preview_type**](SubscriptionsApi.md#subscriptions_update_preview_type) | **PUT** /api/manage/v1/Subscriptions/{subscriptionId}/PreviewType | Update subscription&#39;s preview type
[**subscriptions_update_subscription_domains**](SubscriptionsApi.md#subscriptions_update_subscription_domains) | **PUT** /api/manage/v1/Subscriptions/{subscriptionId}/Domains | Update subscription&#39;s allowed domains


# **subscriptions_get_default_permissions**
> DefaultPermissionsVM subscriptions_get_default_permissions(subscription_id)

Get subscription's default permissions for new entities

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.default_permissions_vm import DefaultPermissionsVM
from fastreport_cloud_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fastreport_cloud_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: ApiKey
configuration = fastreport_cloud_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (JWT): JWT
configuration = fastreport_cloud_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fastreport_cloud_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fastreport_cloud_sdk.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | id

    try:
        # Get subscription's default permissions for new entities
        api_response = api_instance.subscriptions_get_default_permissions(subscription_id)
        print("The response of SubscriptionsApi->subscriptions_get_default_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscriptions_get_default_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| id | 

### Return type

[**DefaultPermissionsVM**](DefaultPermissionsVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned |  -  |
**400** | Request is wrong |  -  |
**402** | Subscription is outdated |  -  |
**403** | Not enough permissions |  -  |
**404** | There is no subscription with such id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_get_my_permissions**
> MyPermissionsVM subscriptions_get_my_permissions(sub_id)

Get user's permissions for a subscription by id

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.my_permissions_vm import MyPermissionsVM
from fastreport_cloud_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fastreport_cloud_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: ApiKey
configuration = fastreport_cloud_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (JWT): JWT
configuration = fastreport_cloud_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fastreport_cloud_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fastreport_cloud_sdk.SubscriptionsApi(api_client)
    sub_id = 'sub_id_example' # str | subscription id

    try:
        # Get user's permissions for a subscription by id
        api_response = api_instance.subscriptions_get_my_permissions(sub_id)
        print("The response of SubscriptionsApi->subscriptions_get_my_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscriptions_get_my_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_id** | **str**| subscription id | 

### Return type

[**MyPermissionsVM**](MyPermissionsVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succesfully returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_get_permissions**
> SubscriptionPermissionsVM subscriptions_get_permissions(id)

Get permissions for a subscription by id

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.subscription_permissions_vm import SubscriptionPermissionsVM
from fastreport_cloud_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fastreport_cloud_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: ApiKey
configuration = fastreport_cloud_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (JWT): JWT
configuration = fastreport_cloud_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fastreport_cloud_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fastreport_cloud_sdk.SubscriptionsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get permissions for a subscription by id
        api_response = api_instance.subscriptions_get_permissions(id)
        print("The response of SubscriptionsApi->subscriptions_get_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscriptions_get_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SubscriptionPermissionsVM**](SubscriptionPermissionsVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succesfully returned |  -  |
**400** | Request is wrong |  -  |
**402** | Subscription is outdated |  -  |
**403** | Not enough permissions |  -  |
**404** | There is no subscription with such id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_get_subscription**
> SubscriptionVM subscriptions_get_subscription(id)

Returns the subscription by id

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.subscription_vm import SubscriptionVM
from fastreport_cloud_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fastreport_cloud_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: ApiKey
configuration = fastreport_cloud_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (JWT): JWT
configuration = fastreport_cloud_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fastreport_cloud_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fastreport_cloud_sdk.SubscriptionsApi(api_client)
    id = 'id_example' # str | Identifier of subscription

    try:
        # Returns the subscription by id
        api_response = api_instance.subscriptions_get_subscription(id)
        print("The response of SubscriptionsApi->subscriptions_get_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscriptions_get_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of subscription | 

### Return type

[**SubscriptionVM**](SubscriptionVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succesfully returned |  -  |
**400** | The request is wrong |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Subscription is not found |  -  |
**500** | Try again, if error still here - text our support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_get_subscriptions**
> SubscriptionsVM subscriptions_get_subscriptions(skip=skip, take=take)

Returns a list of all subscriptions of current user

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.subscriptions_vm import SubscriptionsVM
from fastreport_cloud_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fastreport_cloud_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: ApiKey
configuration = fastreport_cloud_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (JWT): JWT
configuration = fastreport_cloud_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fastreport_cloud_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fastreport_cloud_sdk.SubscriptionsApi(api_client)
    skip = 0 # int | Variable for pagination, defautl value is 0 (optional) (default to 0)
    take = 10 # int | Variable for pagination, default value is 10 (optional) (default to 10)

    try:
        # Returns a list of all subscriptions of current user
        api_response = api_instance.subscriptions_get_subscriptions(skip=skip, take=take)
        print("The response of SubscriptionsApi->subscriptions_get_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscriptions_get_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Variable for pagination, defautl value is 0 | [optional] [default to 0]
 **take** | **int**| Variable for pagination, default value is 10 | [optional] [default to 10]

### Return type

[**SubscriptionsVM**](SubscriptionsVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succesfully returned |  -  |
**400** | unrealistic skip &#39;n take provided |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_rename_subscription**
> SubscriptionVM subscriptions_rename_subscription(subscription_id, rename_subscription_vm)

Rename subscription

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.rename_subscription_vm import RenameSubscriptionVM
from fastreport_cloud_sdk.models.subscription_vm import SubscriptionVM
from fastreport_cloud_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fastreport_cloud_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: ApiKey
configuration = fastreport_cloud_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (JWT): JWT
configuration = fastreport_cloud_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fastreport_cloud_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fastreport_cloud_sdk.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | id
    rename_subscription_vm = fastreport_cloud_sdk.RenameSubscriptionVM() # RenameSubscriptionVM | rename VM

    try:
        # Rename subscription
        api_response = api_instance.subscriptions_rename_subscription(subscription_id, rename_subscription_vm)
        print("The response of SubscriptionsApi->subscriptions_rename_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscriptions_rename_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| id | 
 **rename_subscription_vm** | [**RenameSubscriptionVM**](RenameSubscriptionVM.md)| rename VM | 

### Return type

[**SubscriptionVM**](SubscriptionVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully renamed |  -  |
**400** | Request is wrong |  -  |
**402** | Subscription is outdated |  -  |
**403** | Not enough permissions |  -  |
**404** | There is no subscription with such id (or user have no permission) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_update_default_permissions**
> DefaultPermissionsVM subscriptions_update_default_permissions(subscription_id, update_default_permissions_vm)

Change subscription's default permissions for new entities

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.default_permissions_vm import DefaultPermissionsVM
from fastreport_cloud_sdk.models.update_default_permissions_vm import UpdateDefaultPermissionsVM
from fastreport_cloud_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fastreport_cloud_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: ApiKey
configuration = fastreport_cloud_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (JWT): JWT
configuration = fastreport_cloud_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fastreport_cloud_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fastreport_cloud_sdk.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | id
    update_default_permissions_vm = fastreport_cloud_sdk.UpdateDefaultPermissionsVM() # UpdateDefaultPermissionsVM | update default permissions VM

    try:
        # Change subscription's default permissions for new entities
        api_response = api_instance.subscriptions_update_default_permissions(subscription_id, update_default_permissions_vm)
        print("The response of SubscriptionsApi->subscriptions_update_default_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscriptions_update_default_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| id | 
 **update_default_permissions_vm** | [**UpdateDefaultPermissionsVM**](UpdateDefaultPermissionsVM.md)| update default permissions VM | 

### Return type

[**DefaultPermissionsVM**](DefaultPermissionsVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully changed |  -  |
**400** | Request is wrong |  -  |
**402** | Subscription is outdated |  -  |
**403** | Not enough permissions |  -  |
**404** | There is no subscription with such id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_update_locale**
> SubscriptionVM subscriptions_update_locale(subscription_id, update_subscription_locale_vm)

Update subscription's default locale

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.subscription_vm import SubscriptionVM
from fastreport_cloud_sdk.models.update_subscription_locale_vm import UpdateSubscriptionLocaleVM
from fastreport_cloud_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fastreport_cloud_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: ApiKey
configuration = fastreport_cloud_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (JWT): JWT
configuration = fastreport_cloud_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fastreport_cloud_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fastreport_cloud_sdk.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | id
    update_subscription_locale_vm = fastreport_cloud_sdk.UpdateSubscriptionLocaleVM() # UpdateSubscriptionLocaleVM | update VM

    try:
        # Update subscription's default locale
        api_response = api_instance.subscriptions_update_locale(subscription_id, update_subscription_locale_vm)
        print("The response of SubscriptionsApi->subscriptions_update_locale:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscriptions_update_locale: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| id | 
 **update_subscription_locale_vm** | [**UpdateSubscriptionLocaleVM**](UpdateSubscriptionLocaleVM.md)| update VM | 

### Return type

[**SubscriptionVM**](SubscriptionVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully renamed |  -  |
**400** | Request is wrong |  -  |
**402** | Subscription is outdated |  -  |
**403** | Not enough permissions |  -  |
**404** | There is no subscription with such id (or user have no permission) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_update_permissions**
> subscriptions_update_permissions(id, update_subscription_permissions_vm=update_subscription_permissions_vm)

Update permissions

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.update_subscription_permissions_vm import UpdateSubscriptionPermissionsVM
from fastreport_cloud_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fastreport_cloud_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: ApiKey
configuration = fastreport_cloud_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (JWT): JWT
configuration = fastreport_cloud_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fastreport_cloud_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fastreport_cloud_sdk.SubscriptionsApi(api_client)
    id = 'id_example' # str | 
    update_subscription_permissions_vm = fastreport_cloud_sdk.UpdateSubscriptionPermissionsVM() # UpdateSubscriptionPermissionsVM |  (optional)

    try:
        # Update permissions
        api_instance.subscriptions_update_permissions(id, update_subscription_permissions_vm=update_subscription_permissions_vm)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscriptions_update_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_subscription_permissions_vm** | [**UpdateSubscriptionPermissionsVM**](UpdateSubscriptionPermissionsVM.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Succesfully updated |  -  |
**400** | Request is wrong |  -  |
**402** | Subscription is outdated |  -  |
**403** | Not enough permissions |  -  |
**404** | There is no subscription with such id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_update_preview_type**
> SubscriptionVM subscriptions_update_preview_type(subscription_id, update_subscription_preview_type_vm)

Update subscription's preview type

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.subscription_vm import SubscriptionVM
from fastreport_cloud_sdk.models.update_subscription_preview_type_vm import UpdateSubscriptionPreviewTypeVM
from fastreport_cloud_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fastreport_cloud_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: ApiKey
configuration = fastreport_cloud_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (JWT): JWT
configuration = fastreport_cloud_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fastreport_cloud_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fastreport_cloud_sdk.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | id
    update_subscription_preview_type_vm = fastreport_cloud_sdk.UpdateSubscriptionPreviewTypeVM() # UpdateSubscriptionPreviewTypeVM | update VM

    try:
        # Update subscription's preview type
        api_response = api_instance.subscriptions_update_preview_type(subscription_id, update_subscription_preview_type_vm)
        print("The response of SubscriptionsApi->subscriptions_update_preview_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscriptions_update_preview_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| id | 
 **update_subscription_preview_type_vm** | [**UpdateSubscriptionPreviewTypeVM**](UpdateSubscriptionPreviewTypeVM.md)| update VM | 

### Return type

[**SubscriptionVM**](SubscriptionVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated |  -  |
**400** | Request is wrong |  -  |
**402** | Subscription is outdated |  -  |
**403** | Not enough permissions |  -  |
**404** | There is no subscription with such id (or user have no permission) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_update_subscription_domains**
> SubscriptionVM subscriptions_update_subscription_domains(subscription_id, update_subscription_domains_vm)

Update subscription's allowed domains

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.subscription_vm import SubscriptionVM
from fastreport_cloud_sdk.models.update_subscription_domains_vm import UpdateSubscriptionDomainsVM
from fastreport_cloud_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fastreport_cloud_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: ApiKey
configuration = fastreport_cloud_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (JWT): JWT
configuration = fastreport_cloud_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fastreport_cloud_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fastreport_cloud_sdk.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | id
    update_subscription_domains_vm = fastreport_cloud_sdk.UpdateSubscriptionDomainsVM() # UpdateSubscriptionDomainsVM | update VM

    try:
        # Update subscription's allowed domains
        api_response = api_instance.subscriptions_update_subscription_domains(subscription_id, update_subscription_domains_vm)
        print("The response of SubscriptionsApi->subscriptions_update_subscription_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscriptions_update_subscription_domains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| id | 
 **update_subscription_domains_vm** | [**UpdateSubscriptionDomainsVM**](UpdateSubscriptionDomainsVM.md)| update VM | 

### Return type

[**SubscriptionVM**](SubscriptionVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully renamed |  -  |
**400** | Request is wrong |  -  |
**402** | Subscription is outdated |  -  |
**403** | Not enough permissions |  -  |
**404** | There is no subscription with such id (or user have no permission) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

