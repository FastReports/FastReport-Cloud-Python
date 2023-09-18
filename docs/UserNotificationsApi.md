# fastreport_cloud_sdk.UserNotificationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_notifications_clear_notifications**](UserNotificationsApi.md#user_notifications_clear_notifications) | **DELETE** /api/manage/v1/notifications | Use this endpoint to \&quot;clear\&quot; your notifications
[**user_notifications_get_notifications**](UserNotificationsApi.md#user_notifications_get_notifications) | **GET** /api/manage/v1/notifications | Use this endpoint to recieve notifications


# **user_notifications_clear_notifications**
> user_notifications_clear_notifications(clear_notifications_vm=clear_notifications_vm)

Use this endpoint to \"clear\" your notifications

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
    api_instance = fastreport_cloud_sdk.UserNotificationsApi(api_client)
    clear_notifications_vm = fastreport_cloud_sdk.ClearNotificationsVM() # ClearNotificationsVM |  (optional)

    try:
        # Use this endpoint to \"clear\" your notifications
        api_instance.user_notifications_clear_notifications(clear_notifications_vm=clear_notifications_vm)
    except ApiException as e:
        print("Exception when calling UserNotificationsApi->user_notifications_clear_notifications: %s\n" % e)
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
    api_instance = fastreport_cloud_sdk.UserNotificationsApi(api_client)
    clear_notifications_vm = fastreport_cloud_sdk.ClearNotificationsVM() # ClearNotificationsVM |  (optional)

    try:
        # Use this endpoint to \"clear\" your notifications
        api_instance.user_notifications_clear_notifications(clear_notifications_vm=clear_notifications_vm)
    except ApiException as e:
        print("Exception when calling UserNotificationsApi->user_notifications_clear_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clear_notifications_vm** | [**ClearNotificationsVM**](ClearNotificationsVM.md)|  | [optional] 

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
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_notifications_get_notifications**
> AuditActionsVM user_notifications_get_notifications(skip=skip, take=take, subscription_id=subscription_id)

Use this endpoint to recieve notifications

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
    api_instance = fastreport_cloud_sdk.UserNotificationsApi(api_client)
    skip = 0 # int |  (optional) (default to 0)
take = 5 # int |  (optional) (default to 5)
subscription_id = '' # str |  (optional) (default to '')

    try:
        # Use this endpoint to recieve notifications
        api_response = api_instance.user_notifications_get_notifications(skip=skip, take=take, subscription_id=subscription_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserNotificationsApi->user_notifications_get_notifications: %s\n" % e)
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
    api_instance = fastreport_cloud_sdk.UserNotificationsApi(api_client)
    skip = 0 # int |  (optional) (default to 0)
take = 5 # int |  (optional) (default to 5)
subscription_id = '' # str |  (optional) (default to '')

    try:
        # Use this endpoint to recieve notifications
        api_response = api_instance.user_notifications_get_notifications(skip=skip, take=take, subscription_id=subscription_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserNotificationsApi->user_notifications_get_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**|  | [optional] [default to 0]
 **take** | **int**|  | [optional] [default to 5]
 **subscription_id** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**AuditActionsVM**](AuditActionsVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

