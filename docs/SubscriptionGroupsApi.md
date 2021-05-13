# fastreport_cloud_sdk.SubscriptionGroupsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscription_groups_get_groups_list**](SubscriptionGroupsApi.md#subscription_groups_get_groups_list) | **GET** /api/manage/v1/Subscriptions/{subscriptionId}/groups | returns groups of the subscription or subscription user


# **subscription_groups_get_groups_list**
> GroupsVM subscription_groups_get_groups_list(subscription_id, user_id=user_id)

returns groups of the subscription or subscription user

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
    api_instance = fastreport_cloud_sdk.SubscriptionGroupsApi(api_client)
    subscription_id = 'subscription_id_example' # str | subscripiton id
user_id = 'user_id_example' # str | user Id (optional) (optional)

    try:
        # returns groups of the subscription or subscription user
        api_response = api_instance.subscription_groups_get_groups_list(subscription_id, user_id=user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubscriptionGroupsApi->subscription_groups_get_groups_list: %s\n" % e)
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
    api_instance = fastreport_cloud_sdk.SubscriptionGroupsApi(api_client)
    subscription_id = 'subscription_id_example' # str | subscripiton id
user_id = 'user_id_example' # str | user Id (optional) (optional)

    try:
        # returns groups of the subscription or subscription user
        api_response = api_instance.subscription_groups_get_groups_list(subscription_id, user_id=user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubscriptionGroupsApi->subscription_groups_get_groups_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| subscripiton id | 
 **user_id** | **str**| user Id (optional) | [optional] 

### Return type

[**GroupsVM**](GroupsVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Everything is all right (list of groups may be empty) |  -  |
**400** | id is not hex24 |  -  |
**403** | You don&#39;t have permisison to get groups from this subscription (or in your default (1st) subscription) |  -  |
**404** | there is no subscription with provided id found, or user don&#39;t even have a subscription |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

