# fastreport_cloud_sdk.TasksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tasks_create_task**](TasksApi.md#tasks_create_task) | **POST** /api/tasks | Create a new task
[**tasks_delete_task**](TasksApi.md#tasks_delete_task) | **DELETE** /api/tasks/{taskId} | Delete a task from a storage
[**tasks_get**](TasksApi.md#tasks_get) | **GET** /api/tasks/{taskId} | Get a task by a specified id
[**tasks_get_list**](TasksApi.md#tasks_get_list) | **GET** /api/tasks | Get tasks list
[**tasks_get_permissions**](TasksApi.md#tasks_get_permissions) | **GET** /api/tasks/{id}/permissions | Get all Task permissions
[**tasks_rename_task**](TasksApi.md#tasks_rename_task) | **PUT** /api/tasks/{taskId}/rename | Rename a task
[**tasks_run_task**](TasksApi.md#tasks_run_task) | **POST** /api/tasks/run | Run a task from request body
[**tasks_run_task_by_id**](TasksApi.md#tasks_run_task_by_id) | **POST** /api/tasks/{taskId}/run | Run a task by id
[**tasks_update_permissions**](TasksApi.md#tasks_update_permissions) | **POST** /api/tasks/{id}/permissions | Update permissions
[**tasks_update_task**](TasksApi.md#tasks_update_task) | **PUT** /api/tasks/{taskId} | Update a task


# **tasks_create_task**
> TaskBaseVM tasks_create_task(create_task_base_vm=create_task_base_vm)

Create a new task

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
    api_instance = fastreport_cloud_sdk.TasksApi(api_client)
    create_task_base_vm = fastreport_cloud_sdk.CreateTaskBaseVM() # CreateTaskBaseVM | task's view model. You have to specify task type (type: \"ExportTemplate\") (optional)

    try:
        # Create a new task
        api_response = api_instance.tasks_create_task(create_task_base_vm=create_task_base_vm)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->tasks_create_task: %s\n" % e)
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
    api_instance = fastreport_cloud_sdk.TasksApi(api_client)
    create_task_base_vm = fastreport_cloud_sdk.CreateTaskBaseVM() # CreateTaskBaseVM | task's view model. You have to specify task type (type: \"ExportTemplate\") (optional)

    try:
        # Create a new task
        api_response = api_instance.tasks_create_task(create_task_base_vm=create_task_base_vm)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->tasks_create_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_task_base_vm** | [**CreateTaskBaseVM**](CreateTaskBaseVM.md)| task&#39;s view model. You have to specify task type (type: \&quot;ExportTemplate\&quot;) | [optional] 

### Return type

[**TaskBaseVM**](TaskBaseVM.md)

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

# **tasks_delete_task**
> tasks_delete_task(task_id)

Delete a task from a storage

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
    api_instance = fastreport_cloud_sdk.TasksApi(api_client)
    task_id = 'task_id_example' # str | deleting task id

    try:
        # Delete a task from a storage
        api_instance.tasks_delete_task(task_id)
    except ApiException as e:
        print("Exception when calling TasksApi->tasks_delete_task: %s\n" % e)
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
    api_instance = fastreport_cloud_sdk.TasksApi(api_client)
    task_id = 'task_id_example' # str | deleting task id

    try:
        # Delete a task from a storage
        api_instance.tasks_delete_task(task_id)
    except ApiException as e:
        print("Exception when calling TasksApi->tasks_delete_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| deleting task id | 

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
**204** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**402** | Client Error |  -  |
**400** | Bad Request |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_get**
> TaskBaseVM tasks_get(task_id)

Get a task by a specified id

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
    api_instance = fastreport_cloud_sdk.TasksApi(api_client)
    task_id = 'task_id_example' # str | a task id

    try:
        # Get a task by a specified id
        api_response = api_instance.tasks_get(task_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->tasks_get: %s\n" % e)
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
    api_instance = fastreport_cloud_sdk.TasksApi(api_client)
    task_id = 'task_id_example' # str | a task id

    try:
        # Get a task by a specified id
        api_response = api_instance.tasks_get(task_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->tasks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| a task id | 

### Return type

[**TaskBaseVM**](TaskBaseVM.md)

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

# **tasks_get_list**
> TasksVM tasks_get_list(skip=skip, take=take, subscription_id=subscription_id)

Get tasks list

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
    api_instance = fastreport_cloud_sdk.TasksApi(api_client)
    skip = 0 # int | number of tasks, that have to be skipped (optional) (default to 0)
take = 10 # int | number of tasks, that have to be returned (optional) (default to 10)
subscription_id = 'subscription_id_example' # str | subscription id (optional)

    try:
        # Get tasks list
        api_response = api_instance.tasks_get_list(skip=skip, take=take, subscription_id=subscription_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->tasks_get_list: %s\n" % e)
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
    api_instance = fastreport_cloud_sdk.TasksApi(api_client)
    skip = 0 # int | number of tasks, that have to be skipped (optional) (default to 0)
take = 10 # int | number of tasks, that have to be returned (optional) (default to 10)
subscription_id = 'subscription_id_example' # str | subscription id (optional)

    try:
        # Get tasks list
        api_response = api_instance.tasks_get_list(skip=skip, take=take, subscription_id=subscription_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->tasks_get_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| number of tasks, that have to be skipped | [optional] [default to 0]
 **take** | **int**| number of tasks, that have to be returned | [optional] [default to 10]
 **subscription_id** | **str**| subscription id | [optional] 

### Return type

[**TasksVM**](TasksVM.md)

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

# **tasks_get_permissions**
> TaskPermissionsVM tasks_get_permissions(id)

Get all Task permissions

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
    api_instance = fastreport_cloud_sdk.TasksApi(api_client)
    id = 'id_example' # str | task id

    try:
        # Get all Task permissions
        api_response = api_instance.tasks_get_permissions(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->tasks_get_permissions: %s\n" % e)
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
    api_instance = fastreport_cloud_sdk.TasksApi(api_client)
    id = 'id_example' # str | task id

    try:
        # Get all Task permissions
        api_response = api_instance.tasks_get_permissions(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->tasks_get_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| task id | 

### Return type

[**TaskPermissionsVM**](TaskPermissionsVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **tasks_rename_task**
> TaskBaseVM tasks_rename_task(task_id, new_name=new_name)

Rename a task

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
    api_instance = fastreport_cloud_sdk.TasksApi(api_client)
    task_id = 'task_id_example' # str | renaming task id
new_name = 'new_name_example' # str | task's new Name (optional)

    try:
        # Rename a task
        api_response = api_instance.tasks_rename_task(task_id, new_name=new_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->tasks_rename_task: %s\n" % e)
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
    api_instance = fastreport_cloud_sdk.TasksApi(api_client)
    task_id = 'task_id_example' # str | renaming task id
new_name = 'new_name_example' # str | task's new Name (optional)

    try:
        # Rename a task
        api_response = api_instance.tasks_rename_task(task_id, new_name=new_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->tasks_rename_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| renaming task id | 
 **new_name** | **str**| task&#39;s new Name | [optional] 

### Return type

[**TaskBaseVM**](TaskBaseVM.md)

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

# **tasks_run_task**
> tasks_run_task(run_task_base_vm=run_task_base_vm)

Run a task from request body

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
    api_instance = fastreport_cloud_sdk.TasksApi(api_client)
    run_task_base_vm = fastreport_cloud_sdk.RunTaskBaseVM() # RunTaskBaseVM | task's view model (optional)

    try:
        # Run a task from request body
        api_instance.tasks_run_task(run_task_base_vm=run_task_base_vm)
    except ApiException as e:
        print("Exception when calling TasksApi->tasks_run_task: %s\n" % e)
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
    api_instance = fastreport_cloud_sdk.TasksApi(api_client)
    run_task_base_vm = fastreport_cloud_sdk.RunTaskBaseVM() # RunTaskBaseVM | task's view model (optional)

    try:
        # Run a task from request body
        api_instance.tasks_run_task(run_task_base_vm=run_task_base_vm)
    except ApiException as e:
        print("Exception when calling TasksApi->tasks_run_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_task_base_vm** | [**RunTaskBaseVM**](RunTaskBaseVM.md)| task&#39;s view model | [optional] 

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
**200** | Success |  -  |
**204** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**402** | Client Error |  -  |
**400** | Bad Request |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_run_task_by_id**
> tasks_run_task_by_id(task_id)

Run a task by id

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
    api_instance = fastreport_cloud_sdk.TasksApi(api_client)
    task_id = 'task_id_example' # str | task id

    try:
        # Run a task by id
        api_instance.tasks_run_task_by_id(task_id)
    except ApiException as e:
        print("Exception when calling TasksApi->tasks_run_task_by_id: %s\n" % e)
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
    api_instance = fastreport_cloud_sdk.TasksApi(api_client)
    task_id = 'task_id_example' # str | task id

    try:
        # Run a task by id
        api_instance.tasks_run_task_by_id(task_id)
    except ApiException as e:
        print("Exception when calling TasksApi->tasks_run_task_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| task id | 

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
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**402** | Client Error |  -  |
**400** | Bad Request |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_update_permissions**
> tasks_update_permissions(id, update_task_permissions_vm=update_task_permissions_vm)

Update permissions

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
    api_instance = fastreport_cloud_sdk.TasksApi(api_client)
    id = 'id_example' # str | task id
update_task_permissions_vm = fastreport_cloud_sdk.UpdateTaskPermissionsVM() # UpdateTaskPermissionsVM | new permissions (optional)

    try:
        # Update permissions
        api_instance.tasks_update_permissions(id, update_task_permissions_vm=update_task_permissions_vm)
    except ApiException as e:
        print("Exception when calling TasksApi->tasks_update_permissions: %s\n" % e)
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
    api_instance = fastreport_cloud_sdk.TasksApi(api_client)
    id = 'id_example' # str | task id
update_task_permissions_vm = fastreport_cloud_sdk.UpdateTaskPermissionsVM() # UpdateTaskPermissionsVM | new permissions (optional)

    try:
        # Update permissions
        api_instance.tasks_update_permissions(id, update_task_permissions_vm=update_task_permissions_vm)
    except ApiException as e:
        print("Exception when calling TasksApi->tasks_update_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| task id | 
 **update_task_permissions_vm** | [**UpdateTaskPermissionsVM**](UpdateTaskPermissionsVM.md)| new permissions | [optional] 

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
**200** | Success |  -  |
**400** | Bad Request |  -  |
**402** | Client Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_update_task**
> TaskBaseVM tasks_update_task(task_id, update_task_base_vm=update_task_base_vm)

Update a task

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
    api_instance = fastreport_cloud_sdk.TasksApi(api_client)
    task_id = 'task_id_example' # str | updating task id
update_task_base_vm = fastreport_cloud_sdk.UpdateTaskBaseVM() # UpdateTaskBaseVM | task's view model. You have to specify task type (type: \"ExportTemplate\") (optional)

    try:
        # Update a task
        api_response = api_instance.tasks_update_task(task_id, update_task_base_vm=update_task_base_vm)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->tasks_update_task: %s\n" % e)
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
    api_instance = fastreport_cloud_sdk.TasksApi(api_client)
    task_id = 'task_id_example' # str | updating task id
update_task_base_vm = fastreport_cloud_sdk.UpdateTaskBaseVM() # UpdateTaskBaseVM | task's view model. You have to specify task type (type: \"ExportTemplate\") (optional)

    try:
        # Update a task
        api_response = api_instance.tasks_update_task(task_id, update_task_base_vm=update_task_base_vm)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->tasks_update_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| updating task id | 
 **update_task_base_vm** | [**UpdateTaskBaseVM**](UpdateTaskBaseVM.md)| task&#39;s view model. You have to specify task type (type: \&quot;ExportTemplate\&quot;) | [optional] 

### Return type

[**TaskBaseVM**](TaskBaseVM.md)

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

