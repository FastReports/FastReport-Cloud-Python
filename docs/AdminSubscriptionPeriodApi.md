# fastreport_cloud_sdk.AdminSubscriptionPeriodApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_subscription_period_renew_subscription**](AdminSubscriptionPeriodApi.md#admin_subscription_period_renew_subscription) | **POST** /api/admin/v1/Subscriptions/{id}/Renew | Create a new subscripiton period, move current period to old


# **admin_subscription_period_renew_subscription**
> SubscriptionVM admin_subscription_period_renew_subscription(id, view_model=view_model)

Create a new subscripiton period, move current period to old

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

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with fastreport_cloud_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fastreport_cloud_sdk.AdminSubscriptionPeriodApi(api_client)
    id = 'id_example' # str | 
view_model = fastreport_cloud_sdk.CreateSubscriptionPeriodVM() # CreateSubscriptionPeriodVM |  (optional)

    try:
        # Create a new subscripiton period, move current period to old
        api_response = api_instance.admin_subscription_period_renew_subscription(id, view_model=view_model)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminSubscriptionPeriodApi->admin_subscription_period_renew_subscription: %s\n" % e)
```

* Api Key Authentication (JWT):
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

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with fastreport_cloud_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fastreport_cloud_sdk.AdminSubscriptionPeriodApi(api_client)
    id = 'id_example' # str | 
view_model = fastreport_cloud_sdk.CreateSubscriptionPeriodVM() # CreateSubscriptionPeriodVM |  (optional)

    try:
        # Create a new subscripiton period, move current period to old
        api_response = api_instance.admin_subscription_period_renew_subscription(id, view_model=view_model)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminSubscriptionPeriodApi->admin_subscription_period_renew_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **view_model** | [**CreateSubscriptionPeriodVM**](CreateSubscriptionPeriodVM.md)|  | [optional] 

### Return type

[**SubscriptionVM**](SubscriptionVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succesfully created |  -  |
**400** | The reqeust is wrong |  -  |
**403** | You don&#39;t have rights for the operation |  -  |
**404** | Plan is not found |  -  |
**500** | Exception caught while renewing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

