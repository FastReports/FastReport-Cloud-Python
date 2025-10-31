# fastreport_cloud_sdk.TasksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tasks_create_task**](TasksApi.md#tasks_create_task) | **POST** /api/tasks/v1/Tasks | Create a new task
[**tasks_delete_task**](TasksApi.md#tasks_delete_task) | **DELETE** /api/tasks/v1/Tasks/{taskId} | Delete a task from a storage
[**tasks_get**](TasksApi.md#tasks_get) | **GET** /api/tasks/v1/Tasks/{taskId} | Get a task by a specified id
[**tasks_get_list**](TasksApi.md#tasks_get_list) | **GET** /api/tasks/v1/Tasks | Get tasks list
[**tasks_get_my_permissions**](TasksApi.md#tasks_get_my_permissions) | **GET** /api/tasks/v1/Tasks/{id}/mypermissions | Get current user&#39;s permissions to Task
[**tasks_get_permissions**](TasksApi.md#tasks_get_permissions) | **GET** /api/tasks/v1/Tasks/{id}/permissions | Get all Task permissions
[**tasks_rename_task**](TasksApi.md#tasks_rename_task) | **PUT** /api/tasks/v1/Tasks/{taskId}/rename | Rename a task
[**tasks_run_task**](TasksApi.md#tasks_run_task) | **POST** /api/tasks/v1/Tasks/run | Run a task from request body
[**tasks_run_task_by_id**](TasksApi.md#tasks_run_task_by_id) | **POST** /api/tasks/v1/Tasks/{taskId}/run | Run a task by id
[**tasks_update_permissions**](TasksApi.md#tasks_update_permissions) | **POST** /api/tasks/v1/Tasks/{id}/permissions | Update permissions
[**tasks_update_task**](TasksApi.md#tasks_update_task) | **PUT** /api/tasks/v1/Tasks/{taskId} | Update a task


# **tasks_create_task**
> TaskBaseVM tasks_create_task(create_task_base_vm=create_task_base_vm)

Create a new task

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.create_task_base_vm import CreateTaskBaseVM
from fastreport_cloud_sdk.models.task_base_vm import TaskBaseVM
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
    api_instance = fastreport_cloud_sdk.TasksApi(api_client)
    create_task_base_vm = fastreport_cloud_sdk.CreateTaskBaseVM() # CreateTaskBaseVM | task's view model. You have to specify task type by placing parameter \"$t\": \"Vm name\",              this parameters always must be on the first place (optional)

    try:
        # Create a new task
        api_response = api_instance.tasks_create_task(create_task_base_vm=create_task_base_vm)
        print("The response of TasksApi->tasks_create_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->tasks_create_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_task_base_vm** | [**CreateTaskBaseVM**](CreateTaskBaseVM.md)| task&#39;s view model. You have to specify task type by placing parameter \&quot;$t\&quot;: \&quot;Vm name\&quot;,              this parameters always must be on the first place | [optional] 

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
**200** | Task was created |  -  |
**400** | Bad VM provided |  -  |
**402** | Subscription is outdated |  -  |
**403** | Not enough permissions for the operation |  -  |
**404** | Subscription was not found |  -  |
**500** | Try again, if error still here - text our support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_delete_task**
> tasks_delete_task(task_id)

Delete a task from a storage

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
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
    api_instance = fastreport_cloud_sdk.TasksApi(api_client)
    task_id = 'task_id_example' # str | deleting task id

    try:
        # Delete a task from a storage
        api_instance.tasks_delete_task(task_id)
    except Exception as e:
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
**204** | Task was deleted |  -  |
**400** | Bad id provided |  -  |
**402** | Subscription is outdated |  -  |
**403** | Not enough permissions for the operation |  -  |
**404** | Subscription or task was not found |  -  |
**500** | Try again, if error still here - text our support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_get**
> TaskBaseVM tasks_get(task_id)

Get a task by a specified id

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.task_base_vm import TaskBaseVM
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
    api_instance = fastreport_cloud_sdk.TasksApi(api_client)
    task_id = 'task_id_example' # str | a task id

    try:
        # Get a task by a specified id
        api_response = api_instance.tasks_get(task_id)
        print("The response of TasksApi->tasks_get:\n")
        pprint(api_response)
    except Exception as e:
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
**200** | Task was found |  -  |
**400** | Bad id provided |  -  |
**402** | Subscription is outdated |  -  |
**403** | Not enough permissions for the operation |  -  |
**404** | Subscription or task was not found |  -  |
**500** | Try again, if error still here - text our support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_get_list**
> TasksVM tasks_get_list(skip=skip, take=take, use_projection=use_projection, subscription_id=subscription_id, search_pattern=search_pattern, task_type=task_type)

Get tasks list

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.task_type import TaskType
from fastreport_cloud_sdk.models.tasks_vm import TasksVM
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
    api_instance = fastreport_cloud_sdk.TasksApi(api_client)
    skip = 0 # int | number of tasks, that have to be skipped (optional) (default to 0)
    take = 10 # int | number of tasks, that have to be returned (optional) (default to 10)
    use_projection = False # bool | use projection with only id and name (optional) (default to False)
    subscription_id = 'subscription_id_example' # str | subscription id (optional)
    search_pattern = '' # str |  (optional) (default to '')
    task_type = fastreport_cloud_sdk.TaskType() # TaskType | bit flag for types (optional)

    try:
        # Get tasks list
        api_response = api_instance.tasks_get_list(skip=skip, take=take, use_projection=use_projection, subscription_id=subscription_id, search_pattern=search_pattern, task_type=task_type)
        print("The response of TasksApi->tasks_get_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->tasks_get_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| number of tasks, that have to be skipped | [optional] [default to 0]
 **take** | **int**| number of tasks, that have to be returned | [optional] [default to 10]
 **use_projection** | **bool**| use projection with only id and name | [optional] [default to False]
 **subscription_id** | **str**| subscription id | [optional] 
 **search_pattern** | **str**|  | [optional] [default to &#39;&#39;]
 **task_type** | [**TaskType**](.md)| bit flag for types | [optional] 

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
**200** | Tasks were found |  -  |
**400** | Bad id provided |  -  |
**402** | Subscription is outdated |  -  |
**403** | Not enough permissions for the operation |  -  |
**404** | Subscription or tasks were not found |  -  |
**500** | Try again, if error still here - text our support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_get_my_permissions**
> TaskPermissionCRUDVM tasks_get_my_permissions(id)

Get current user's permissions to Task

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.task_permission_crudvm import TaskPermissionCRUDVM
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
    api_instance = fastreport_cloud_sdk.TasksApi(api_client)
    id = 'id_example' # str | task id

    try:
        # Get current user's permissions to Task
        api_response = api_instance.tasks_get_my_permissions(id)
        print("The response of TasksApi->tasks_get_my_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->tasks_get_my_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| task id | 

### Return type

[**TaskPermissionCRUDVM**](TaskPermissionCRUDVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | got permissions successfully |  -  |
**400** | The request is wrong |  -  |
**404** | Subscription or task was not found |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_get_permissions**
> TaskPermissionsVM tasks_get_permissions(id)

Get all Task permissions

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.task_permissions_vm import TaskPermissionsVM
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
    api_instance = fastreport_cloud_sdk.TasksApi(api_client)
    id = 'id_example' # str | task id

    try:
        # Get all Task permissions
        api_response = api_instance.tasks_get_permissions(id)
        print("The response of TasksApi->tasks_get_permissions:\n")
        pprint(api_response)
    except Exception as e:
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
**200** | Task was found |  -  |
**400** | Bad id provided |  -  |
**402** | Subscription is outdated |  -  |
**403** | Not enough permissions for the operation |  -  |
**404** | Subscription or task was not found |  -  |
**500** | Try again, if error still here - text our support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_rename_task**
> TaskBaseVM tasks_rename_task(task_id, new_name=new_name)

Rename a task

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.task_base_vm import TaskBaseVM
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
    api_instance = fastreport_cloud_sdk.TasksApi(api_client)
    task_id = 'task_id_example' # str | renaming task id
    new_name = 'new_name_example' # str | task's new Name (optional)

    try:
        # Rename a task
        api_response = api_instance.tasks_rename_task(task_id, new_name=new_name)
        print("The response of TasksApi->tasks_rename_task:\n")
        pprint(api_response)
    except Exception as e:
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
**200** | Task was found |  -  |
**400** | Bad id or name provided |  -  |
**402** | Subscription is outdated |  -  |
**403** | Not enough permissions for the operation |  -  |
**404** | Subscription or task was not found |  -  |
**500** | Try again, if error still here - text our support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_run_task**
> TaskMessageIdVM tasks_run_task(run_task_base_vm=run_task_base_vm)

Run a task from request body

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.run_task_base_vm import RunTaskBaseVM
from fastreport_cloud_sdk.models.task_message_id_vm import TaskMessageIdVM
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
    api_instance = fastreport_cloud_sdk.TasksApi(api_client)
    run_task_base_vm = fastreport_cloud_sdk.RunTaskBaseVM() # RunTaskBaseVM | task's view model. You have to specify task type by placing parameter \"$t\": \"Vm name\",              this parameters always must be on the first place (optional)

    try:
        # Run a task from request body
        api_response = api_instance.tasks_run_task(run_task_base_vm=run_task_base_vm)
        print("The response of TasksApi->tasks_run_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->tasks_run_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_task_base_vm** | [**RunTaskBaseVM**](RunTaskBaseVM.md)| task&#39;s view model. You have to specify task type by placing parameter \&quot;$t\&quot;: \&quot;Vm name\&quot;,              this parameters always must be on the first place | [optional] 

### Return type

[**TaskMessageIdVM**](TaskMessageIdVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task was executed |  -  |
**403** | Not enough permissions for the operation |  -  |
**404** | Subscription was not found |  -  |
**402** | Subscription is outdated |  -  |
**400** | Bad VM provided |  -  |
**500** | Try again, if error still here - text our support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_run_task_by_id**
> TaskMessageIdVM tasks_run_task_by_id(task_id)

Run a task by id

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.task_message_id_vm import TaskMessageIdVM
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
    api_instance = fastreport_cloud_sdk.TasksApi(api_client)
    task_id = 'task_id_example' # str | task id

    try:
        # Run a task by id
        api_response = api_instance.tasks_run_task_by_id(task_id)
        print("The response of TasksApi->tasks_run_task_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->tasks_run_task_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| task id | 

### Return type

[**TaskMessageIdVM**](TaskMessageIdVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task was executed |  -  |
**400** | Bad id provided |  -  |
**402** | Subscription is outdated |  -  |
**403** | Not enough permissions for the operation |  -  |
**404** | Subscription or task was not found |  -  |
**500** | Try again, if error still here - text our support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_update_permissions**
> tasks_update_permissions(id, update_task_permissions_vm=update_task_permissions_vm)

Update permissions

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.update_task_permissions_vm import UpdateTaskPermissionsVM
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
    api_instance = fastreport_cloud_sdk.TasksApi(api_client)
    id = 'id_example' # str | task id
    update_task_permissions_vm = fastreport_cloud_sdk.UpdateTaskPermissionsVM() # UpdateTaskPermissionsVM | new permissions. You have to specify VM type by placing parameter \"$t\": \"Vm name\",              this parameters always must be on first place (optional)

    try:
        # Update permissions
        api_instance.tasks_update_permissions(id, update_task_permissions_vm=update_task_permissions_vm)
    except Exception as e:
        print("Exception when calling TasksApi->tasks_update_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| task id | 
 **update_task_permissions_vm** | [**UpdateTaskPermissionsVM**](UpdateTaskPermissionsVM.md)| new permissions. You have to specify VM type by placing parameter \&quot;$t\&quot;: \&quot;Vm name\&quot;,              this parameters always must be on first place | [optional] 

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
**204** | Task was updated |  -  |
**400** | Bad id or VM provided |  -  |
**402** | Subscription is outdated |  -  |
**403** | Not enough permissions for the operation |  -  |
**404** | Subscription or task was not found |  -  |
**500** | Try again, if error still here - text our support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_update_task**
> TaskBaseVM tasks_update_task(task_id, update_task_base_vm=update_task_base_vm)

Update a task

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.task_base_vm import TaskBaseVM
from fastreport_cloud_sdk.models.update_task_base_vm import UpdateTaskBaseVM
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
    api_instance = fastreport_cloud_sdk.TasksApi(api_client)
    task_id = 'task_id_example' # str | updating task id
    update_task_base_vm = fastreport_cloud_sdk.UpdateTaskBaseVM() # UpdateTaskBaseVM | task's view model. You have to specify task type by placing parameter \"$t\": \"Vm name\",              this parameters always must be on first place (optional)

    try:
        # Update a task
        api_response = api_instance.tasks_update_task(task_id, update_task_base_vm=update_task_base_vm)
        print("The response of TasksApi->tasks_update_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->tasks_update_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| updating task id | 
 **update_task_base_vm** | [**UpdateTaskBaseVM**](UpdateTaskBaseVM.md)| task&#39;s view model. You have to specify task type by placing parameter \&quot;$t\&quot;: \&quot;Vm name\&quot;,              this parameters always must be on first place | [optional] 

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
**400** | Bad id or VM provided |  -  |
**402** | Subscription is outdated |  -  |
**403** | Not enough permissions for the operation |  -  |
**404** | Subscription or task was not found |  -  |
**500** | Try again, if error still here - text our support |  -  |
**204** | Task was updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

