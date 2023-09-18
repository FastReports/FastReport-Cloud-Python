# fastreport_cloud_sdk.ContactGroupsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contact_groups_create**](ContactGroupsApi.md#contact_groups_create) | **POST** /api/v1/ContactGroups/group | Creates contact group
[**contact_groups_delete**](ContactGroupsApi.md#contact_groups_delete) | **DELETE** /api/v1/ContactGroups/{id} | Removes contact by id
[**contact_groups_get**](ContactGroupsApi.md#contact_groups_get) | **GET** /api/v1/ContactGroups/{id} | Returns contact group by id
[**contact_groups_get_list**](ContactGroupsApi.md#contact_groups_get_list) | **GET** /api/v1/ContactGroups/subscription/{subscriptionId}/groups | Returns contact groups by subscriptionId
[**contact_groups_update**](ContactGroupsApi.md#contact_groups_update) | **PUT** /api/v1/ContactGroups/{id} | Updates contact group by id


# **contact_groups_create**
> ContactGroupVM contact_groups_create(create_contact_group_vm=create_contact_group_vm)

Creates contact group

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
    api_instance = fastreport_cloud_sdk.ContactGroupsApi(api_client)
    create_contact_group_vm = fastreport_cloud_sdk.CreateContactGroupVM() # CreateContactGroupVM |  (optional)

    try:
        # Creates contact group
        api_response = api_instance.contact_groups_create(create_contact_group_vm=create_contact_group_vm)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactGroupsApi->contact_groups_create: %s\n" % e)
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
    api_instance = fastreport_cloud_sdk.ContactGroupsApi(api_client)
    create_contact_group_vm = fastreport_cloud_sdk.CreateContactGroupVM() # CreateContactGroupVM |  (optional)

    try:
        # Creates contact group
        api_response = api_instance.contact_groups_create(create_contact_group_vm=create_contact_group_vm)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactGroupsApi->contact_groups_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_contact_group_vm** | [**CreateContactGroupVM**](CreateContactGroupVM.md)|  | [optional] 

### Return type

[**ContactGroupVM**](ContactGroupVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**402** | Client Error |  -  |
**400** | Bad Request |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contact_groups_delete**
> contact_groups_delete(id)

Removes contact by id

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
    api_instance = fastreport_cloud_sdk.ContactGroupsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Removes contact by id
        api_instance.contact_groups_delete(id)
    except ApiException as e:
        print("Exception when calling ContactGroupsApi->contact_groups_delete: %s\n" % e)
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
    api_instance = fastreport_cloud_sdk.ContactGroupsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Removes contact by id
        api_instance.contact_groups_delete(id)
    except ApiException as e:
        print("Exception when calling ContactGroupsApi->contact_groups_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**402** | Client Error |  -  |
**400** | Bad Request |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contact_groups_get**
> ContactGroupVM contact_groups_get(id)

Returns contact group by id

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
    api_instance = fastreport_cloud_sdk.ContactGroupsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Returns contact group by id
        api_response = api_instance.contact_groups_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactGroupsApi->contact_groups_get: %s\n" % e)
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
    api_instance = fastreport_cloud_sdk.ContactGroupsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Returns contact group by id
        api_response = api_instance.contact_groups_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactGroupsApi->contact_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ContactGroupVM**](ContactGroupVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**402** | Client Error |  -  |
**400** | Bad Request |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contact_groups_get_list**
> ContactGroupsVM contact_groups_get_list(subscription_id, skip=skip, take=take)

Returns contact groups by subscriptionId

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
    api_instance = fastreport_cloud_sdk.ContactGroupsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
skip = 0 # int |  (optional) (default to 0)
take = 10 # int |  (optional) (default to 10)

    try:
        # Returns contact groups by subscriptionId
        api_response = api_instance.contact_groups_get_list(subscription_id, skip=skip, take=take)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactGroupsApi->contact_groups_get_list: %s\n" % e)
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
    api_instance = fastreport_cloud_sdk.ContactGroupsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
skip = 0 # int |  (optional) (default to 0)
take = 10 # int |  (optional) (default to 10)

    try:
        # Returns contact groups by subscriptionId
        api_response = api_instance.contact_groups_get_list(subscription_id, skip=skip, take=take)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactGroupsApi->contact_groups_get_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **skip** | **int**|  | [optional] [default to 0]
 **take** | **int**|  | [optional] [default to 10]

### Return type

[**ContactGroupsVM**](ContactGroupsVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**402** | Client Error |  -  |
**400** | Bad Request |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contact_groups_update**
> ContactGroupVM contact_groups_update(id, update_contact_group_vm=update_contact_group_vm)

Updates contact group by id

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
    api_instance = fastreport_cloud_sdk.ContactGroupsApi(api_client)
    id = 'id_example' # str | 
update_contact_group_vm = fastreport_cloud_sdk.UpdateContactGroupVM() # UpdateContactGroupVM |  (optional)

    try:
        # Updates contact group by id
        api_response = api_instance.contact_groups_update(id, update_contact_group_vm=update_contact_group_vm)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactGroupsApi->contact_groups_update: %s\n" % e)
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
    api_instance = fastreport_cloud_sdk.ContactGroupsApi(api_client)
    id = 'id_example' # str | 
update_contact_group_vm = fastreport_cloud_sdk.UpdateContactGroupVM() # UpdateContactGroupVM |  (optional)

    try:
        # Updates contact group by id
        api_response = api_instance.contact_groups_update(id, update_contact_group_vm=update_contact_group_vm)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactGroupsApi->contact_groups_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_contact_group_vm** | [**UpdateContactGroupVM**](UpdateContactGroupVM.md)|  | [optional] 

### Return type

[**ContactGroupVM**](ContactGroupVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**402** | Client Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

