# fastreport_cloud_sdk.SubscriptionPlansApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscription_plans_get_subscription_plan**](SubscriptionPlansApi.md#subscription_plans_get_subscription_plan) | **GET** /api/manage/v1/SubscriptionPlans/{id} | Returns a subscription plan. Not all subscriptions can be issued for customer.
[**subscription_plans_get_subscription_plans**](SubscriptionPlansApi.md#subscription_plans_get_subscription_plans) | **GET** /api/manage/v1/SubscriptionPlans | Returns a list of active subscription plans that can be issued to the user.


# **subscription_plans_get_subscription_plan**
> SubscriptionPlanVM subscription_plans_get_subscription_plan(id)

Returns a subscription plan. Not all subscriptions can be issued for customer.

### Example

* Basic Authentication (ApiKey):
```python
from __future__ import print_function
import time
import fastreport_cloud_sdk
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): JWT
configuration = fastreport_cloud_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with fastreport_cloud_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fastreport_cloud_sdk.SubscriptionPlansApi(api_client)
    id = 'id_example' # str | Identifier of subsctiption plan

    try:
        # Returns a subscription plan. Not all subscriptions can be issued for customer.
        api_response = api_instance.subscription_plans_get_subscription_plan(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubscriptionPlansApi->subscription_plans_get_subscription_plan: %s\n" % e)
```

* Bearer (JWT) Authentication (JWT):
```python
from __future__ import print_function
import time
import fastreport_cloud_sdk
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): JWT
configuration = fastreport_cloud_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with fastreport_cloud_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fastreport_cloud_sdk.SubscriptionPlansApi(api_client)
    id = 'id_example' # str | Identifier of subsctiption plan

    try:
        # Returns a subscription plan. Not all subscriptions can be issued for customer.
        api_response = api_instance.subscription_plans_get_subscription_plan(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubscriptionPlansApi->subscription_plans_get_subscription_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of subsctiption plan | 

### Return type

[**SubscriptionPlanVM**](SubscriptionPlanVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succesfully returned |  -  |
**400** | The reqeust is wrong |  -  |
**404** | Subscription plan with this id is not found |  -  |
**500** | Exception thrown |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_plans_get_subscription_plans**
> SubscriptionPlansVM subscription_plans_get_subscription_plans(skip=skip, take=take)

Returns a list of active subscription plans that can be issued to the user.

If no active subscription plans, then the endpoint will return empty list

### Example

* Basic Authentication (ApiKey):
```python
from __future__ import print_function
import time
import fastreport_cloud_sdk
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): JWT
configuration = fastreport_cloud_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with fastreport_cloud_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fastreport_cloud_sdk.SubscriptionPlansApi(api_client)
    skip = 0 # int | Variable for pagination, defautl value is 0 (optional) (default to 0)
take = 10 # int | Variable for pagination, default value is 10 (optional) (default to 10)

    try:
        # Returns a list of active subscription plans that can be issued to the user.
        api_response = api_instance.subscription_plans_get_subscription_plans(skip=skip, take=take)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubscriptionPlansApi->subscription_plans_get_subscription_plans: %s\n" % e)
```

* Bearer (JWT) Authentication (JWT):
```python
from __future__ import print_function
import time
import fastreport_cloud_sdk
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): JWT
configuration = fastreport_cloud_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with fastreport_cloud_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fastreport_cloud_sdk.SubscriptionPlansApi(api_client)
    skip = 0 # int | Variable for pagination, defautl value is 0 (optional) (default to 0)
take = 10 # int | Variable for pagination, default value is 10 (optional) (default to 10)

    try:
        # Returns a list of active subscription plans that can be issued to the user.
        api_response = api_instance.subscription_plans_get_subscription_plans(skip=skip, take=take)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubscriptionPlansApi->subscription_plans_get_subscription_plans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Variable for pagination, defautl value is 0 | [optional] [default to 0]
 **take** | **int**| Variable for pagination, default value is 10 | [optional] [default to 10]

### Return type

[**SubscriptionPlansVM**](SubscriptionPlansVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succesfully returned |  -  |
**400** | The reqeust is wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

