# fastreport_cloud_sdk.AdminSubscriptionAnalyticsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_subscription_analytics_check_anon_permissions**](AdminSubscriptionAnalyticsApi.md#admin_subscription_analytics_check_anon_permissions) | **GET** /api/admin/v1/Analytics/Subscriptions/{subscriptionId}/AnonCheck | This will check if there are any files, related to subscription that available for anonymous users
[**admin_subscription_analytics_check_other_permissions**](AdminSubscriptionAnalyticsApi.md#admin_subscription_analytics_check_other_permissions) | **GET** /api/admin/v1/Analytics/Subscriptions/{subscriptionId}/OtherCheck | This will check if there are any files, related to subscription that not available for subscription users
[**admin_subscription_analytics_get_dead_subs_in_users**](AdminSubscriptionAnalyticsApi.md#admin_subscription_analytics_get_dead_subs_in_users) | **GET** /api/admin/v1/Analytics/Subscriptions/DeadSubsInUsers | This will check if there are any deleted subscriptions in users sub lists
[**admin_subscription_analytics_get_empty_subs**](AdminSubscriptionAnalyticsApi.md#admin_subscription_analytics_get_empty_subs) | **GET** /api/admin/v1/Analytics/Subscriptions/EmptySubs | This will check if there are any subscriptions without users
[**admin_subscription_analytics_get_lost_file_chunks**](AdminSubscriptionAnalyticsApi.md#admin_subscription_analytics_get_lost_file_chunks) | **GET** /api/admin/v1/Analytics/Subscriptions/LostFileChunks | This will check if there are any files in gridFS, which not related to any file model
[**admin_subscription_analytics_get_unrelated_documents**](AdminSubscriptionAnalyticsApi.md#admin_subscription_analytics_get_unrelated_documents) | **GET** /api/admin/v1/Analytics/Subscriptions/UnrelatedDocuments | This will check if there are any files, that not related to any existing subscription


# **admin_subscription_analytics_check_anon_permissions**
> AnalysisResultsVM admin_subscription_analytics_check_anon_permissions(subscription_id)

This will check if there are any files, related to subscription that available for anonymous users

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
    api_instance = fastreport_cloud_sdk.AdminSubscriptionAnalyticsApi(api_client)
    subscription_id = 'subscription_id_example' # str | subscription id

    try:
        # This will check if there are any files, related to subscription that available for anonymous users
        api_response = api_instance.admin_subscription_analytics_check_anon_permissions(subscription_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminSubscriptionAnalyticsApi->admin_subscription_analytics_check_anon_permissions: %s\n" % e)
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
    api_instance = fastreport_cloud_sdk.AdminSubscriptionAnalyticsApi(api_client)
    subscription_id = 'subscription_id_example' # str | subscription id

    try:
        # This will check if there are any files, related to subscription that available for anonymous users
        api_response = api_instance.admin_subscription_analytics_check_anon_permissions(subscription_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminSubscriptionAnalyticsApi->admin_subscription_analytics_check_anon_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| subscription id | 

### Return type

[**AnalysisResultsVM**](AnalysisResultsVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_subscription_analytics_check_other_permissions**
> AnalysisResultsVM admin_subscription_analytics_check_other_permissions(subscription_id)

This will check if there are any files, related to subscription that not available for subscription users

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
    api_instance = fastreport_cloud_sdk.AdminSubscriptionAnalyticsApi(api_client)
    subscription_id = 'subscription_id_example' # str | subscription id

    try:
        # This will check if there are any files, related to subscription that not available for subscription users
        api_response = api_instance.admin_subscription_analytics_check_other_permissions(subscription_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminSubscriptionAnalyticsApi->admin_subscription_analytics_check_other_permissions: %s\n" % e)
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
    api_instance = fastreport_cloud_sdk.AdminSubscriptionAnalyticsApi(api_client)
    subscription_id = 'subscription_id_example' # str | subscription id

    try:
        # This will check if there are any files, related to subscription that not available for subscription users
        api_response = api_instance.admin_subscription_analytics_check_other_permissions(subscription_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminSubscriptionAnalyticsApi->admin_subscription_analytics_check_other_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| subscription id | 

### Return type

[**AnalysisResultsVM**](AnalysisResultsVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_subscription_analytics_get_dead_subs_in_users**
> AnalysisResultsVM admin_subscription_analytics_get_dead_subs_in_users()

This will check if there are any deleted subscriptions in users sub lists

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
    api_instance = fastreport_cloud_sdk.AdminSubscriptionAnalyticsApi(api_client)
    
    try:
        # This will check if there are any deleted subscriptions in users sub lists
        api_response = api_instance.admin_subscription_analytics_get_dead_subs_in_users()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminSubscriptionAnalyticsApi->admin_subscription_analytics_get_dead_subs_in_users: %s\n" % e)
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
    api_instance = fastreport_cloud_sdk.AdminSubscriptionAnalyticsApi(api_client)
    
    try:
        # This will check if there are any deleted subscriptions in users sub lists
        api_response = api_instance.admin_subscription_analytics_get_dead_subs_in_users()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminSubscriptionAnalyticsApi->admin_subscription_analytics_get_dead_subs_in_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AnalysisResultsVM**](AnalysisResultsVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_subscription_analytics_get_empty_subs**
> AnalysisResultsVM admin_subscription_analytics_get_empty_subs()

This will check if there are any subscriptions without users

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
    api_instance = fastreport_cloud_sdk.AdminSubscriptionAnalyticsApi(api_client)
    
    try:
        # This will check if there are any subscriptions without users
        api_response = api_instance.admin_subscription_analytics_get_empty_subs()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminSubscriptionAnalyticsApi->admin_subscription_analytics_get_empty_subs: %s\n" % e)
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
    api_instance = fastreport_cloud_sdk.AdminSubscriptionAnalyticsApi(api_client)
    
    try:
        # This will check if there are any subscriptions without users
        api_response = api_instance.admin_subscription_analytics_get_empty_subs()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminSubscriptionAnalyticsApi->admin_subscription_analytics_get_empty_subs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AnalysisResultsVM**](AnalysisResultsVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_subscription_analytics_get_lost_file_chunks**
> AnalysisResultsVM admin_subscription_analytics_get_lost_file_chunks()

This will check if there are any files in gridFS, which not related to any file model

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
    api_instance = fastreport_cloud_sdk.AdminSubscriptionAnalyticsApi(api_client)
    
    try:
        # This will check if there are any files in gridFS, which not related to any file model
        api_response = api_instance.admin_subscription_analytics_get_lost_file_chunks()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminSubscriptionAnalyticsApi->admin_subscription_analytics_get_lost_file_chunks: %s\n" % e)
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
    api_instance = fastreport_cloud_sdk.AdminSubscriptionAnalyticsApi(api_client)
    
    try:
        # This will check if there are any files in gridFS, which not related to any file model
        api_response = api_instance.admin_subscription_analytics_get_lost_file_chunks()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminSubscriptionAnalyticsApi->admin_subscription_analytics_get_lost_file_chunks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AnalysisResultsVM**](AnalysisResultsVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_subscription_analytics_get_unrelated_documents**
> AnalysisResultsVM admin_subscription_analytics_get_unrelated_documents()

This will check if there are any files, that not related to any existing subscription

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
    api_instance = fastreport_cloud_sdk.AdminSubscriptionAnalyticsApi(api_client)
    
    try:
        # This will check if there are any files, that not related to any existing subscription
        api_response = api_instance.admin_subscription_analytics_get_unrelated_documents()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminSubscriptionAnalyticsApi->admin_subscription_analytics_get_unrelated_documents: %s\n" % e)
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
    api_instance = fastreport_cloud_sdk.AdminSubscriptionAnalyticsApi(api_client)
    
    try:
        # This will check if there are any files, that not related to any existing subscription
        api_response = api_instance.admin_subscription_analytics_get_unrelated_documents()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminSubscriptionAnalyticsApi->admin_subscription_analytics_get_unrelated_documents: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AnalysisResultsVM**](AnalysisResultsVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

