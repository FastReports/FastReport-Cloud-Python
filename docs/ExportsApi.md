# fastreport_cloud_sdk.ExportsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_folder_and_file_clear_recycle_bin**](ExportsApi.md#export_folder_and_file_clear_recycle_bin) | **DELETE** /api/rp/v1/Exports/{subscriptionId}/ClearRecycleBin | Delete all folders and files from recycle bin
[**export_folder_and_file_copy_files**](ExportsApi.md#export_folder_and_file_copy_files) | **POST** /api/rp/v1/Exports/{subscriptionId}/CopyFiles | Copy folders and files to a specified folder
[**export_folder_and_file_count_recycle_bin_folders_and_files**](ExportsApi.md#export_folder_and_file_count_recycle_bin_folders_and_files) | **GET** /api/rp/v1/Exports/{subscriptionId}/CountRecycleBinFolderAndFiles | Count all folders and files from recycle bin
[**export_folder_and_file_delete_files**](ExportsApi.md#export_folder_and_file_delete_files) | **POST** /api/rp/v1/Exports/{subscriptionId}/DeleteFiles | Delete folders and files from a folder or the recycle bin
[**export_folder_and_file_get_count**](ExportsApi.md#export_folder_and_file_get_count) | **GET** /api/rp/v1/Exports/Folder/{id}/CountFolderAndFiles | Count folders and files in a folder
[**export_folder_and_file_get_folders_and_files**](ExportsApi.md#export_folder_and_file_get_folders_and_files) | **GET** /api/rp/v1/Exports/Folder/{id}/ListFolderAndFiles | Get all folders and files from specified folder
[**export_folder_and_file_get_recycle_bin_folders_and_files**](ExportsApi.md#export_folder_and_file_get_recycle_bin_folders_and_files) | **GET** /api/rp/v1/Exports/{subscriptionId}/ListRecycleBinFolderAndFiles | Get all folders and files from recycle bin
[**export_folder_and_file_move_files**](ExportsApi.md#export_folder_and_file_move_files) | **POST** /api/rp/v1/Exports/{subscriptionId}/MoveFiles | Move folders and files to a specified folder
[**export_folder_and_file_move_files_to_bin**](ExportsApi.md#export_folder_and_file_move_files_to_bin) | **POST** /api/rp/v1/Exports/{subscriptionId}/ToBin | Move folders and files to the recycle bin
[**export_folder_and_file_recover_all_from_recycle_bin**](ExportsApi.md#export_folder_and_file_recover_all_from_recycle_bin) | **POST** /api/rp/v1/Exports/{subscriptionId}/RecoverRecycleBin | Recover all folders and files from recycle bin
[**export_folder_and_file_recover_files**](ExportsApi.md#export_folder_and_file_recover_files) | **POST** /api/rp/v1/Exports/{subscriptionId}/RecoverFiles | Recover folders and files from the recycle bin
[**export_folders_calculate_folder_size**](ExportsApi.md#export_folders_calculate_folder_size) | **GET** /api/rp/v1/Exports/Folder/{id}/size | Get specified folder, calculate it&#39;s size
[**export_folders_copy_folder**](ExportsApi.md#export_folders_copy_folder) | **POST** /api/rp/v1/Exports/Folder/{id}/Copy/{folderId} | Move folder to a specified folder
[**export_folders_delete_folder**](ExportsApi.md#export_folders_delete_folder) | **DELETE** /api/rp/v1/Exports/Folder/{id} | Delete specified folder
[**export_folders_get_breadcrumbs**](ExportsApi.md#export_folders_get_breadcrumbs) | **GET** /api/rp/v1/Exports/Folder/{id}/Breadcrumbs | Get specified folder breadcrumbs
[**export_folders_get_folder**](ExportsApi.md#export_folders_get_folder) | **GET** /api/rp/v1/Exports/Folder/{id} | Get specified folder
[**export_folders_get_folders**](ExportsApi.md#export_folders_get_folders) | **GET** /api/rp/v1/Exports/Folder/{id}/ListFolders | Get all folders from specified folder
[**export_folders_get_folders_count**](ExportsApi.md#export_folders_get_folders_count) | **GET** /api/rp/v1/Exports/Folder/{id}/CountFolders | Get count of folders what contains in a specified folder
[**export_folders_get_my_permissions**](ExportsApi.md#export_folders_get_my_permissions) | **GET** /api/rp/v1/Exports/Folder/{folderId}/mypermissions | Get user&#39;s permissions for a folder by id
[**export_folders_get_or_create**](ExportsApi.md#export_folders_get_or_create) | **GET** /api/rp/v1/Exports/Folder/getOrCreate | Get specified folder
[**export_folders_get_permissions**](ExportsApi.md#export_folders_get_permissions) | **GET** /api/rp/v1/Exports/Folder/{id}/permissions | Get all folder permissions
[**export_folders_get_root_folder**](ExportsApi.md#export_folders_get_root_folder) | **GET** /api/rp/v1/Exports/Root | Get workspace&#39;s root folder
[**export_folders_move_folder**](ExportsApi.md#export_folders_move_folder) | **POST** /api/rp/v1/Exports/Folder/{id}/Move/{folderId} | Move folder into a specified folder
[**export_folders_move_folder_to_bin**](ExportsApi.md#export_folders_move_folder_to_bin) | **DELETE** /api/rp/v1/Exports/Folder/{id}/ToBin | Move specified folder to recycle bin
[**export_folders_post_folder**](ExportsApi.md#export_folders_post_folder) | **POST** /api/rp/v1/Exports/Folder/{id}/Folder | Create folder
[**export_folders_recover_folder**](ExportsApi.md#export_folders_recover_folder) | **POST** /api/rp/v1/Exports/Folder/{id}/Recover | Recover specified folder
[**export_folders_rename_folder**](ExportsApi.md#export_folders_rename_folder) | **PUT** /api/rp/v1/Exports/Folder/{id}/Rename | Rename a folder
[**export_folders_update_icon**](ExportsApi.md#export_folders_update_icon) | **PUT** /api/rp/v1/Exports/Folder/{id}/Icon | Update a folder&#39;s icon
[**export_folders_update_permissions**](ExportsApi.md#export_folders_update_permissions) | **POST** /api/rp/v1/Exports/{id}/permissions | Update permissions
[**export_folders_update_tags**](ExportsApi.md#export_folders_update_tags) | **PUT** /api/rp/v1/Exports/Folder/{id}/UpdateTags | Update tags
[**exports_copy_file**](ExportsApi.md#exports_copy_file) | **POST** /api/rp/v1/Exports/File/{id}/Copy/{folderId} | Copy a file into a specified folder
[**exports_create_sharing_key**](ExportsApi.md#exports_create_sharing_key) | **POST** /api/rp/v1/Exports/File/{id}/sharingKey | Create a new key, that can be used to share access to a file &lt;br /&gt;  (You need Administrate.Anon permission to create a new key)
[**exports_delete_file**](ExportsApi.md#exports_delete_file) | **DELETE** /api/rp/v1/Exports/File/{id} | Delete specified file
[**exports_delete_sharing_key**](ExportsApi.md#exports_delete_sharing_key) | **DELETE** /api/rp/v1/Exports/File/{id}/sharingKey | Deletes a sharing key, making links, that utilizing it no longer work
[**exports_get_by_task_id**](ExportsApi.md#exports_get_by_task_id) | **GET** /api/rp/v1/Exports/File/Task/{taskId} | Get exports by specified task id
[**exports_get_by_task_message_id**](ExportsApi.md#exports_get_by_task_message_id) | **GET** /api/rp/v1/Exports/File/TaskMessage/{taskMessageId} | Get export by specified task message id
[**exports_get_file**](ExportsApi.md#exports_get_file) | **GET** /api/rp/v1/Exports/File/{id} | Get export by specified id
[**exports_get_file_history**](ExportsApi.md#exports_get_file_history) | **GET** /api/rp/v1/Exports/File/{id}/History | Returns list of actions, performed on this file
[**exports_get_files_count**](ExportsApi.md#exports_get_files_count) | **GET** /api/rp/v1/Exports/Folder/{id}/CountFiles | Get count of files what contains in a specified folder
[**exports_get_files_list**](ExportsApi.md#exports_get_files_list) | **GET** /api/rp/v1/Exports/Folder/{id}/ListFiles | Get files from the specified folder
[**exports_get_my_permissions**](ExportsApi.md#exports_get_my_permissions) | **GET** /api/rp/v1/Exports/File/{id}/mypermissions | Get current user&#39;s permissions to a file
[**exports_get_permissions**](ExportsApi.md#exports_get_permissions) | **GET** /api/rp/v1/Exports/File/{id}/permissions | Get all permissions from a file. &lt;br /&gt;
[**exports_get_sharing_keys**](ExportsApi.md#exports_get_sharing_keys) | **GET** /api/rp/v1/Exports/File/{id}/sharingKeys | Returns all sharing keys, associated with the file
[**exports_move_file**](ExportsApi.md#exports_move_file) | **POST** /api/rp/v1/Exports/File/{id}/Move/{folderId} | Move file to a specified folder
[**exports_move_file_to_bin**](ExportsApi.md#exports_move_file_to_bin) | **DELETE** /api/rp/v1/Exports/File/{id}/ToBin | Move specified file to recycle bin
[**exports_recover_file**](ExportsApi.md#exports_recover_file) | **POST** /api/rp/v1/Exports/File/{id}/Recover | Recover specified file from bin
[**exports_rename_file**](ExportsApi.md#exports_rename_file) | **PUT** /api/rp/v1/Exports/File/{id}/Rename | Rename a file
[**exports_update_icon**](ExportsApi.md#exports_update_icon) | **PUT** /api/rp/v1/Exports/File/{id}/Icon | Update a files&#39;s icon
[**exports_update_permissions**](ExportsApi.md#exports_update_permissions) | **POST** /api/rp/v1/Exports/File/{id}/permissions | Update permissions
[**exports_update_tags**](ExportsApi.md#exports_update_tags) | **PUT** /api/rp/v1/Exports/File/{id}/UpdateTags | Update tags


# **export_folder_and_file_clear_recycle_bin**
> export_folder_and_file_clear_recycle_bin(subscription_id)

Delete all folders and files from recycle bin

User with a Delete RecycleBin permission can access this method.

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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    subscription_id = 'subscription_id_example' # str | subscription id

    try:
        # Delete all folders and files from recycle bin
        api_instance.export_folder_and_file_clear_recycle_bin(subscription_id)
    except Exception as e:
        print("Exception when calling ExportsApi->export_folder_and_file_clear_recycle_bin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| subscription id | 

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
**400** | Provided parameters did not pass the validation |  -  |
**402** | Subscription is outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Subscription not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_folder_and_file_copy_files**
> export_folder_and_file_copy_files(subscription_id, selected_files_vm=selected_files_vm)

Copy folders and files to a specified folder

User with a Get permission for a files and Create permission for a destination folder can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.selected_files_vm import SelectedFilesVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    subscription_id = 'subscription_id_example' # str | id of current subscription
    selected_files_vm = fastreport_cloud_sdk.SelectedFilesVM() # SelectedFilesVM | File selection VM (optional)

    try:
        # Copy folders and files to a specified folder
        api_instance.export_folder_and_file_copy_files(subscription_id, selected_files_vm=selected_files_vm)
    except Exception as e:
        print("Exception when calling ExportsApi->export_folder_and_file_copy_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| id of current subscription | 
 **selected_files_vm** | [**SelectedFilesVM**](SelectedFilesVM.md)| File selection VM | [optional] 

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
**204** | Success |  -  |
**400** | Parameters did not pass the validation |  -  |
**402** | Subscription is outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Folder or subscription not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_folder_and_file_count_recycle_bin_folders_and_files**
> CountVM export_folder_and_file_count_recycle_bin_folders_and_files(subscription_id, search_pattern=search_pattern, use_regex=use_regex)

Count all folders and files from recycle bin

User with a Get DeletedFiles permission can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.count_vm import CountVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    subscription_id = 'subscription_id_example' # str | subscription id
    search_pattern = '' # str | search pattern used to only include matching files in the recycle bin count<br />              (leave unspecified to count all files and folders) (optional) (default to '')
    use_regex = False # bool | set this to true if you want to use regular expression to search (optional) (default to False)

    try:
        # Count all folders and files from recycle bin
        api_response = api_instance.export_folder_and_file_count_recycle_bin_folders_and_files(subscription_id, search_pattern=search_pattern, use_regex=use_regex)
        print("The response of ExportsApi->export_folder_and_file_count_recycle_bin_folders_and_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->export_folder_and_file_count_recycle_bin_folders_and_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| subscription id | 
 **search_pattern** | **str**| search pattern used to only include matching files in the recycle bin count&lt;br /&gt;              (leave unspecified to count all files and folders) | [optional] [default to &#39;&#39;]
 **use_regex** | **bool**| set this to true if you want to use regular expression to search | [optional] [default to False]

### Return type

[**CountVM**](CountVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Provided parameters did not pass the validation |  -  |
**402** | Subscription is blocked |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Subscription not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_folder_and_file_delete_files**
> export_folder_and_file_delete_files(subscription_id, selected_files_vm=selected_files_vm)

Delete folders and files from a folder or the recycle bin

User with a Delete permission can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.selected_files_vm import SelectedFilesVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    subscription_id = 'subscription_id_example' # str | id of the subscription
    selected_files_vm = fastreport_cloud_sdk.SelectedFilesVM() # SelectedFilesVM | File selection VM (optional)

    try:
        # Delete folders and files from a folder or the recycle bin
        api_instance.export_folder_and_file_delete_files(subscription_id, selected_files_vm=selected_files_vm)
    except Exception as e:
        print("Exception when calling ExportsApi->export_folder_and_file_delete_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| id of the subscription | 
 **selected_files_vm** | [**SelectedFilesVM**](SelectedFilesVM.md)| File selection VM | [optional] 

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
**204** | Success |  -  |
**400** | Parameters did not pass the validation |  -  |
**402** | Subscription is outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Folder or subscription not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_folder_and_file_get_count**
> CountVM export_folder_and_file_get_count(id, search_pattern=search_pattern, use_regex=use_regex)

Count folders and files in a folder

User with a Get Count permission can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.count_vm import CountVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | folder id
    search_pattern = 'search_pattern_example' # str | search pattern used to only include matching files in the count<br />              (leave unspecified to count all files and folders) (optional)
    use_regex = False # bool | set this to true if you want to use regular expression to search (optional) (default to False)

    try:
        # Count folders and files in a folder
        api_response = api_instance.export_folder_and_file_get_count(id, search_pattern=search_pattern, use_regex=use_regex)
        print("The response of ExportsApi->export_folder_and_file_get_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->export_folder_and_file_get_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| folder id | 
 **search_pattern** | **str**| search pattern used to only include matching files in the count&lt;br /&gt;              (leave unspecified to count all files and folders) | [optional] 
 **use_regex** | **bool**| set this to true if you want to use regular expression to search | [optional] [default to False]

### Return type

[**CountVM**](CountVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Parameters did not pass the validation |  -  |
**402** | Subscription is blocked |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Folder or subscription not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_folder_and_file_get_folders_and_files**
> FilesVM export_folder_and_file_get_folders_and_files(id, skip=skip, take=take, order_by=order_by, desc=desc, search_pattern=search_pattern, use_regex=use_regex)

Get all folders and files from specified folder

User with a Get Entity permission can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.file_sorting import FileSorting
from fastreport_cloud_sdk.models.files_vm import FilesVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | folder id
    skip = 0 # int | number of folder and files to skip (optional) (default to 0)
    take = 10 # int | number of folder and files to take (optional) (default to 10)
    order_by = fastreport_cloud_sdk.FileSorting() # FileSorting | a field to sort by (optional)
    desc = False # bool | if true - sorting will be done in the descending order, otherwise - ascending (optional) (default to False)
    search_pattern = '' # str | search pattern used to only include matching files in the result<br />              (leave unspecified to list all files and folders) (optional) (default to '')
    use_regex = False # bool | set this to true if you want to use regular expression to search (optional) (default to False)

    try:
        # Get all folders and files from specified folder
        api_response = api_instance.export_folder_and_file_get_folders_and_files(id, skip=skip, take=take, order_by=order_by, desc=desc, search_pattern=search_pattern, use_regex=use_regex)
        print("The response of ExportsApi->export_folder_and_file_get_folders_and_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->export_folder_and_file_get_folders_and_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| folder id | 
 **skip** | **int**| number of folder and files to skip | [optional] [default to 0]
 **take** | **int**| number of folder and files to take | [optional] [default to 10]
 **order_by** | [**FileSorting**](.md)| a field to sort by | [optional] 
 **desc** | **bool**| if true - sorting will be done in the descending order, otherwise - ascending | [optional] [default to False]
 **search_pattern** | **str**| search pattern used to only include matching files in the result&lt;br /&gt;              (leave unspecified to list all files and folders) | [optional] [default to &#39;&#39;]
 **use_regex** | **bool**| set this to true if you want to use regular expression to search | [optional] [default to False]

### Return type

[**FilesVM**](FilesVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Provided parameters did not pass the validation |  -  |
**402** | Subscription is blocked |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Subscription or folder not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_folder_and_file_get_recycle_bin_folders_and_files**
> FilesVM export_folder_and_file_get_recycle_bin_folders_and_files(subscription_id, skip=skip, take=take, order_by=order_by, desc=desc, search_pattern=search_pattern, use_regex=use_regex)

Get all folders and files from recycle bin

User with a Get DeletedFiles permission can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.file_sorting import FileSorting
from fastreport_cloud_sdk.models.files_vm import FilesVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    subscription_id = 'subscription_id_example' # str | subscription id
    skip = 0 # int | number of folder and files to skip (optional) (default to 0)
    take = 10 # int | number of folder and files to take (optional) (default to 10)
    order_by = fastreport_cloud_sdk.FileSorting() # FileSorting | a field to sort by (optional)
    desc = False # bool | if true - sorting will be done in the descending order, otherwise - ascending (optional) (default to False)
    search_pattern = '' # str | search pattern used to only include matching files in the recycle bin<br />              (leave unspecified to list all files and folders) (optional) (default to '')
    use_regex = False # bool | set this to true if you want to use regular expression to search (optional) (default to False)

    try:
        # Get all folders and files from recycle bin
        api_response = api_instance.export_folder_and_file_get_recycle_bin_folders_and_files(subscription_id, skip=skip, take=take, order_by=order_by, desc=desc, search_pattern=search_pattern, use_regex=use_regex)
        print("The response of ExportsApi->export_folder_and_file_get_recycle_bin_folders_and_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->export_folder_and_file_get_recycle_bin_folders_and_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| subscription id | 
 **skip** | **int**| number of folder and files to skip | [optional] [default to 0]
 **take** | **int**| number of folder and files to take | [optional] [default to 10]
 **order_by** | [**FileSorting**](.md)| a field to sort by | [optional] 
 **desc** | **bool**| if true - sorting will be done in the descending order, otherwise - ascending | [optional] [default to False]
 **search_pattern** | **str**| search pattern used to only include matching files in the recycle bin&lt;br /&gt;              (leave unspecified to list all files and folders) | [optional] [default to &#39;&#39;]
 **use_regex** | **bool**| set this to true if you want to use regular expression to search | [optional] [default to False]

### Return type

[**FilesVM**](FilesVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Provided parameters did not pass the validation |  -  |
**402** | Subscription is blocked |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Subscription or folder not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_folder_and_file_move_files**
> export_folder_and_file_move_files(subscription_id, selected_files_vm=selected_files_vm)

Move folders and files to a specified folder

User with a Update Place permission for a files and Create permission for a destination folder can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.selected_files_vm import SelectedFilesVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    subscription_id = 'subscription_id_example' # str | id of current subscription
    selected_files_vm = fastreport_cloud_sdk.SelectedFilesVM() # SelectedFilesVM | File selection VM (optional)

    try:
        # Move folders and files to a specified folder
        api_instance.export_folder_and_file_move_files(subscription_id, selected_files_vm=selected_files_vm)
    except Exception as e:
        print("Exception when calling ExportsApi->export_folder_and_file_move_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| id of current subscription | 
 **selected_files_vm** | [**SelectedFilesVM**](SelectedFilesVM.md)| File selection VM | [optional] 

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
**204** | Success |  -  |
**400** | Parameters did not pass the validation |  -  |
**402** | Subscription is outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Folder or subscription not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_folder_and_file_move_files_to_bin**
> export_folder_and_file_move_files_to_bin(subscription_id, selected_files_vm=selected_files_vm)

Move folders and files to the recycle bin

User with a Delete Entity permission can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.selected_files_vm import SelectedFilesVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    subscription_id = 'subscription_id_example' # str | id of the subscription
    selected_files_vm = fastreport_cloud_sdk.SelectedFilesVM() # SelectedFilesVM | File selection VM (optional)

    try:
        # Move folders and files to the recycle bin
        api_instance.export_folder_and_file_move_files_to_bin(subscription_id, selected_files_vm=selected_files_vm)
    except Exception as e:
        print("Exception when calling ExportsApi->export_folder_and_file_move_files_to_bin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| id of the subscription | 
 **selected_files_vm** | [**SelectedFilesVM**](SelectedFilesVM.md)| File selection VM | [optional] 

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
**204** | Success |  -  |
**400** | Parameters did not pass the validation |  -  |
**402** | Subscription is outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Folder or subscription not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_folder_and_file_recover_all_from_recycle_bin**
> export_folder_and_file_recover_all_from_recycle_bin(subscription_id)

Recover all folders and files from recycle bin

User with a Create RecycleBin permission can access this method.

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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    subscription_id = 'subscription_id_example' # str | subscription id

    try:
        # Recover all folders and files from recycle bin
        api_instance.export_folder_and_file_recover_all_from_recycle_bin(subscription_id)
    except Exception as e:
        print("Exception when calling ExportsApi->export_folder_and_file_recover_all_from_recycle_bin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| subscription id | 

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
**400** | Provided parameters did not pass the validation |  -  |
**402** | Subscription is outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Subscription not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_folder_and_file_recover_files**
> export_folder_and_file_recover_files(subscription_id, selected_files_vm=selected_files_vm)

Recover folders and files from the recycle bin

User with a SubscriptionCreate permission can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.selected_files_vm import SelectedFilesVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    subscription_id = 'subscription_id_example' # str | id the subscription
    selected_files_vm = fastreport_cloud_sdk.SelectedFilesVM() # SelectedFilesVM | File selection VM (optional)

    try:
        # Recover folders and files from the recycle bin
        api_instance.export_folder_and_file_recover_files(subscription_id, selected_files_vm=selected_files_vm)
    except Exception as e:
        print("Exception when calling ExportsApi->export_folder_and_file_recover_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| id the subscription | 
 **selected_files_vm** | [**SelectedFilesVM**](SelectedFilesVM.md)| File selection VM | [optional] 

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
**204** | Success |  -  |
**400** | Parameters did not pass the validation |  -  |
**402** | Subscription is outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Folder or subscription not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_folders_calculate_folder_size**
> FolderSizeVM export_folders_calculate_folder_size(id)

Get specified folder, calculate it's size

User with a Get Entity permission can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.folder_size_vm import FolderSizeVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | folder id

    try:
        # Get specified folder, calculate it's size
        api_response = api_instance.export_folders_calculate_folder_size(id)
        print("The response of ExportsApi->export_folders_calculate_folder_size:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->export_folders_calculate_folder_size: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| folder id | 

### Return type

[**FolderSizeVM**](FolderSizeVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Parameters did not pass the validation |  -  |
**402** | Subscription is blocked |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Folder or subscription not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_folders_copy_folder**
> FileVM export_folders_copy_folder(id, folder_id)

Move folder to a specified folder

User with a Update Place permission for a folder and Create Entity  for a Parent Folder can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.file_vm import FileVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | moving folder id
    folder_id = 'folder_id_example' # str | destination folder id

    try:
        # Move folder to a specified folder
        api_response = api_instance.export_folders_copy_folder(id, folder_id)
        print("The response of ExportsApi->export_folders_copy_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->export_folders_copy_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| moving folder id | 
 **folder_id** | **str**| destination folder id | 

### Return type

[**FileVM**](FileVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Parameters did not pass the validation |  -  |
**402** | Subscription is outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Folder or subscription not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_folders_delete_folder**
> export_folders_delete_folder(id)

Delete specified folder

User with a Delete Entity permission can access this method.

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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | folder id

    try:
        # Delete specified folder
        api_instance.export_folders_delete_folder(id)
    except Exception as e:
        print("Exception when calling ExportsApi->export_folders_delete_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| folder id | 

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
**400** | Parameters did not pass the validation |  -  |
**402** | Subscription is outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Folder or subscription not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_folders_get_breadcrumbs**
> BreadcrumbsVM export_folders_get_breadcrumbs(id)

Get specified folder breadcrumbs

User with a Get Entity permission can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.breadcrumbs_vm import BreadcrumbsVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | folder id

    try:
        # Get specified folder breadcrumbs
        api_response = api_instance.export_folders_get_breadcrumbs(id)
        print("The response of ExportsApi->export_folders_get_breadcrumbs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->export_folders_get_breadcrumbs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| folder id | 

### Return type

[**BreadcrumbsVM**](BreadcrumbsVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Parameters did not pass the validation |  -  |
**402** | Subscription is blocked |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Folder or subscription not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_folders_get_folder**
> FileVM export_folders_get_folder(id)

Get specified folder

User with a Get Entity permission can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.file_vm import FileVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | folder id

    try:
        # Get specified folder
        api_response = api_instance.export_folders_get_folder(id)
        print("The response of ExportsApi->export_folders_get_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->export_folders_get_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| folder id | 

### Return type

[**FileVM**](FileVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Parameters did not pass the validation |  -  |
**402** | Subscription is blocked |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Folder or subscription not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_folders_get_folders**
> FilesVM export_folders_get_folders(id, skip=skip, take=take, order_by=order_by, desc=desc, search_pattern=search_pattern, use_regex=use_regex)

Get all folders from specified folder

User with a Get Entity permission can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.file_sorting import FileSorting
from fastreport_cloud_sdk.models.files_vm import FilesVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | folder id
    skip = 0 # int | number of folder and files to skip (optional) (default to 0)
    take = 10 # int | number of folder and files to take (optional) (default to 10)
    order_by = fastreport_cloud_sdk.FileSorting() # FileSorting | a field to sort by (optional)
    desc = False # bool | if true - sorting will be done in the descending order, otherwise - ascending (optional) (default to False)
    search_pattern = '' # str | search pattern used to only include matching files in the result<br />              (leave unspecified to list all files and folders) (optional) (default to '')
    use_regex = False # bool | set this to true if you want to use regular expression to search (optional) (default to False)

    try:
        # Get all folders from specified folder
        api_response = api_instance.export_folders_get_folders(id, skip=skip, take=take, order_by=order_by, desc=desc, search_pattern=search_pattern, use_regex=use_regex)
        print("The response of ExportsApi->export_folders_get_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->export_folders_get_folders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| folder id | 
 **skip** | **int**| number of folder and files to skip | [optional] [default to 0]
 **take** | **int**| number of folder and files to take | [optional] [default to 10]
 **order_by** | [**FileSorting**](.md)| a field to sort by | [optional] 
 **desc** | **bool**| if true - sorting will be done in the descending order, otherwise - ascending | [optional] [default to False]
 **search_pattern** | **str**| search pattern used to only include matching files in the result&lt;br /&gt;              (leave unspecified to list all files and folders) | [optional] [default to &#39;&#39;]
 **use_regex** | **bool**| set this to true if you want to use regular expression to search | [optional] [default to False]

### Return type

[**FilesVM**](FilesVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Parameters did not pass the validation |  -  |
**402** | Subscription is blocked |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Folder or subscription not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_folders_get_folders_count**
> CountVM export_folders_get_folders_count(id)

Get count of folders what contains in a specified folder

User with a Get Count permission can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.count_vm import CountVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | folder id

    try:
        # Get count of folders what contains in a specified folder
        api_response = api_instance.export_folders_get_folders_count(id)
        print("The response of ExportsApi->export_folders_get_folders_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->export_folders_get_folders_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| folder id | 

### Return type

[**CountVM**](CountVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Parameters did not pass the validation |  -  |
**402** | Subscription is blocked |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Folder or subscription not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_folders_get_my_permissions**
> FilePermissionCRUDVM export_folders_get_my_permissions(folder_id)

Get user's permissions for a folder by id

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.file_permission_crudvm import FilePermissionCRUDVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    folder_id = 'folder_id_example' # str | folder id

    try:
        # Get user's permissions for a folder by id
        api_response = api_instance.export_folders_get_my_permissions(folder_id)
        print("The response of ExportsApi->export_folders_get_my_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->export_folders_get_my_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| folder id | 

### Return type

[**FilePermissionCRUDVM**](FilePermissionCRUDVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succes |  -  |
**400** | Provided parameters did not pass the validation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_folders_get_or_create**
> FileVM export_folders_get_or_create(name=name, subscription_id=subscription_id, parent_id=parent_id)

Get specified folder

User with a Get (and/or Create) Entity permission can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.file_vm import FileVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    name = 'name_example' # str | folder name (optional)
    subscription_id = 'subscription_id_example' # str | subscriptionId (optional)
    parent_id = 'parent_id_example' # str | parent folder id (optional)

    try:
        # Get specified folder
        api_response = api_instance.export_folders_get_or_create(name=name, subscription_id=subscription_id, parent_id=parent_id)
        print("The response of ExportsApi->export_folders_get_or_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->export_folders_get_or_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| folder name | [optional] 
 **subscription_id** | **str**| subscriptionId | [optional] 
 **parent_id** | **str**| parent folder id | [optional] 

### Return type

[**FileVM**](FileVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Parameters did not pass the validation |  -  |
**402** | Subscription is blocked or outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Folder or subscription not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_folders_get_permissions**
> FilePermissionsVM export_folders_get_permissions(id)

Get all folder permissions

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.file_permissions_vm import FilePermissionsVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get all folder permissions
        api_response = api_instance.export_folders_get_permissions(id)
        print("The response of ExportsApi->export_folders_get_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->export_folders_get_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**FilePermissionsVM**](FilePermissionsVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Parameters did not pass the validation |  -  |
**402** | Subscription is blocked |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Folder or subscription not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_folders_get_root_folder**
> FileVM export_folders_get_root_folder(subscription_id=subscription_id)

Get workspace's root folder

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.file_vm import FileVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    subscription_id = 'subscription_id_example' # str |  (optional)

    try:
        # Get workspace's root folder
        api_response = api_instance.export_folders_get_root_folder(subscription_id=subscription_id)
        print("The response of ExportsApi->export_folders_get_root_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->export_folders_get_root_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | [optional] 

### Return type

[**FileVM**](FileVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Parameters did not pass the validation |  -  |
**402** | Subscription is blocked |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Folder or subscription not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_folders_move_folder**
> FileVM export_folders_move_folder(id, folder_id)

Move folder into a specified folder

User with a Update Place permission for a folder and Create Entity  for a destination Folder can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.file_vm import FileVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | folder id
    folder_id = 'folder_id_example' # str | destination folder id

    try:
        # Move folder into a specified folder
        api_response = api_instance.export_folders_move_folder(id, folder_id)
        print("The response of ExportsApi->export_folders_move_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->export_folders_move_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| folder id | 
 **folder_id** | **str**| destination folder id | 

### Return type

[**FileVM**](FileVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Parameters did not pass the validation |  -  |
**402** | Subscription is outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Folder or subscription not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_folders_move_folder_to_bin**
> export_folders_move_folder_to_bin(id)

Move specified folder to recycle bin

User with a Delete Entity permission can access this method.

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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | folder id

    try:
        # Move specified folder to recycle bin
        api_instance.export_folders_move_folder_to_bin(id)
    except Exception as e:
        print("Exception when calling ExportsApi->export_folders_move_folder_to_bin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| folder id | 

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
**400** | Parameters did not pass the validation |  -  |
**402** | Subscription is outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Folder or subscription not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_folders_post_folder**
> FileVM export_folders_post_folder(id, export_folder_create_vm=export_folder_create_vm)

Create folder

User with a Create Entity permission can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.export_folder_create_vm import ExportFolderCreateVM
from fastreport_cloud_sdk.models.file_vm import FileVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | Identifier of parent folder id
    export_folder_create_vm = fastreport_cloud_sdk.ExportFolderCreateVM() # ExportFolderCreateVM | create VM (optional)

    try:
        # Create folder
        api_response = api_instance.export_folders_post_folder(id, export_folder_create_vm=export_folder_create_vm)
        print("The response of ExportsApi->export_folders_post_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->export_folders_post_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of parent folder id | 
 **export_folder_create_vm** | [**ExportFolderCreateVM**](ExportFolderCreateVM.md)| create VM | [optional] 

### Return type

[**FileVM**](FileVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New folder has been created) |  -  |
**400** | Parent folder id or VM is not valid |  -  |
**402** | subscription is outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | parent folder/subscription not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_folders_recover_folder**
> export_folders_recover_folder(id, recovery_path=recovery_path)

Recover specified folder

User with a Create RecycleBin permission can access this method.

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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | folder id
    recovery_path = 'recovery_path_example' # str | id of the folder, that recovered folder should be placed in (optional)

    try:
        # Recover specified folder
        api_instance.export_folders_recover_folder(id, recovery_path=recovery_path)
    except Exception as e:
        print("Exception when calling ExportsApi->export_folders_recover_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| folder id | 
 **recovery_path** | **str**| id of the folder, that recovered folder should be placed in | [optional] 

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
**400** | Parameters did not pass the validation |  -  |
**402** | Subscription is outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Folder or subscription not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_folders_rename_folder**
> FileVM export_folders_rename_folder(id, folder_rename_vm=folder_rename_vm)

Rename a folder

User with a Update Name permission can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.file_vm import FileVM
from fastreport_cloud_sdk.models.folder_rename_vm import FolderRenameVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | 
    folder_rename_vm = fastreport_cloud_sdk.FolderRenameVM() # FolderRenameVM |  (optional)

    try:
        # Rename a folder
        api_response = api_instance.export_folders_rename_folder(id, folder_rename_vm=folder_rename_vm)
        print("The response of ExportsApi->export_folders_rename_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->export_folders_rename_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **folder_rename_vm** | [**FolderRenameVM**](FolderRenameVM.md)|  | [optional] 

### Return type

[**FileVM**](FileVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folder name has been updated |  -  |
**400** | folderId or VM is not valid |  -  |
**402** | subscription is outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Folder or subscription not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_folders_update_icon**
> FileVM export_folders_update_icon(id, folder_icon_vm=folder_icon_vm)

Update a folder's icon

User with a Update Icon permission can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.file_vm import FileVM
from fastreport_cloud_sdk.models.folder_icon_vm import FolderIconVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | Identifier of folder
    folder_icon_vm = fastreport_cloud_sdk.FolderIconVM() # FolderIconVM | Update icon model (optional)

    try:
        # Update a folder's icon
        api_response = api_instance.export_folders_update_icon(id, folder_icon_vm=folder_icon_vm)
        print("The response of ExportsApi->export_folders_update_icon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->export_folders_update_icon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of folder | 
 **folder_icon_vm** | [**FolderIconVM**](FolderIconVM.md)| Update icon model | [optional] 

### Return type

[**FileVM**](FileVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folder&#39;s icon has been updated |  -  |
**400** | folderId or VM is not valid |  -  |
**402** | subscription is outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Folder or subscription not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_folders_update_permissions**
> export_folders_update_permissions(id, update_file_permissions_vm=update_file_permissions_vm)

Update permissions

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.update_file_permissions_vm import UpdateFilePermissionsVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | folder id
    update_file_permissions_vm = fastreport_cloud_sdk.UpdateFilePermissionsVM() # UpdateFilePermissionsVM | new permissions VM (optional)

    try:
        # Update permissions
        api_instance.export_folders_update_permissions(id, update_file_permissions_vm=update_file_permissions_vm)
    except Exception as e:
        print("Exception when calling ExportsApi->export_folders_update_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| folder id | 
 **update_file_permissions_vm** | [**UpdateFilePermissionsVM**](UpdateFilePermissionsVM.md)| new permissions VM | [optional] 

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
**204** | Success |  -  |
**400** | Parameters did not pass the validation |  -  |
**402** | Subscription is outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Folder or subscription not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_folders_update_tags**
> FileVM export_folders_update_tags(id, folder_tags_update_vm=folder_tags_update_vm)

Update tags

User with a Update Tags permission can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.file_vm import FileVM
from fastreport_cloud_sdk.models.folder_tags_update_vm import FolderTagsUpdateVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | 
    folder_tags_update_vm = fastreport_cloud_sdk.FolderTagsUpdateVM() # FolderTagsUpdateVM |  (optional)

    try:
        # Update tags
        api_response = api_instance.export_folders_update_tags(id, folder_tags_update_vm=folder_tags_update_vm)
        print("The response of ExportsApi->export_folders_update_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->export_folders_update_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **folder_tags_update_vm** | [**FolderTagsUpdateVM**](FolderTagsUpdateVM.md)|  | [optional] 

### Return type

[**FileVM**](FileVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tags has been updated |  -  |
**400** | folderId or Tags is null |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**402** | subscription is outdated |  -  |
**404** | Folder or subscription not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exports_copy_file**
> ExportVM exports_copy_file(id, folder_id)

Copy a file into a specified folder

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.export_vm import ExportVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | file id
    folder_id = 'folder_id_example' # str | folder id

    try:
        # Copy a file into a specified folder
        api_response = api_instance.exports_copy_file(id, folder_id)
        print("The response of ExportsApi->exports_copy_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->exports_copy_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| file id | 
 **folder_id** | **str**| folder id | 

### Return type

[**ExportVM**](ExportVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Parameters did not pass the validation |  -  |
**402** | Subscription is outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | File, folder or a subscription was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exports_create_sharing_key**
> FileSharingKeysVM exports_create_sharing_key(id, create_file_share_vm=create_file_share_vm)

Create a new key, that can be used to share access to a file <br />  (You need Administrate.Anon permission to create a new key)

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.create_file_share_vm import CreateFileShareVM
from fastreport_cloud_sdk.models.file_sharing_keys_vm import FileSharingKeysVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | file id
    create_file_share_vm = fastreport_cloud_sdk.CreateFileShareVM() # CreateFileShareVM | parameters for sharing key creation (optional)

    try:
        # Create a new key, that can be used to share access to a file <br />  (You need Administrate.Anon permission to create a new key)
        api_response = api_instance.exports_create_sharing_key(id, create_file_share_vm=create_file_share_vm)
        print("The response of ExportsApi->exports_create_sharing_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->exports_create_sharing_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| file id | 
 **create_file_share_vm** | [**CreateFileShareVM**](CreateFileShareVM.md)| parameters for sharing key creation | [optional] 

### Return type

[**FileSharingKeysVM**](FileSharingKeysVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Parameters did not pass the validation |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**402** | Subscription is outdated |  -  |
**404** | File or subscription was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exports_delete_file**
> exports_delete_file(id)

Delete specified file

User with Delete permission can access the method.

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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | file id

    try:
        # Delete specified file
        api_instance.exports_delete_file(id)
    except Exception as e:
        print("Exception when calling ExportsApi->exports_delete_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| file id | 

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
**400** | Parameters did not pass the validation |  -  |
**402** | Subscription is outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | File or subscription was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exports_delete_sharing_key**
> exports_delete_sharing_key(id, key)

Deletes a sharing key, making links, that utilizing it no longer work

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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | file id
    key = 'key_example' # str | key to delete

    try:
        # Deletes a sharing key, making links, that utilizing it no longer work
        api_instance.exports_delete_sharing_key(id, key)
    except Exception as e:
        print("Exception when calling ExportsApi->exports_delete_sharing_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| file id | 
 **key** | **str**| key to delete | 

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
**400** | Parameters did not pass the validation |  -  |
**402** | Subscription is outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | File, sharing key or subscription was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exports_get_by_task_id**
> ExportsVM exports_get_by_task_id(task_id)

Get exports by specified task id

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.exports_vm import ExportsVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    task_id = 'task_id_example' # str | task id

    try:
        # Get exports by specified task id
        api_response = api_instance.exports_get_by_task_id(task_id)
        print("The response of ExportsApi->exports_get_by_task_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->exports_get_by_task_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| task id | 

### Return type

[**ExportsVM**](ExportsVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Exports are found |  -  |
**400** | id is not valid |  -  |
**402** | Subscription is outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Export or subscription is not found |  -  |
**500** | Try again, if error still here - text our support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exports_get_by_task_message_id**
> ExportVM exports_get_by_task_message_id(task_message_id)

Get export by specified task message id

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.export_vm import ExportVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    task_message_id = 'task_message_id_example' # str | task message id

    try:
        # Get export by specified task message id
        api_response = api_instance.exports_get_by_task_message_id(task_message_id)
        print("The response of ExportsApi->exports_get_by_task_message_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->exports_get_by_task_message_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_message_id** | **str**| task message id | 

### Return type

[**ExportVM**](ExportVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Export is found |  -  |
**400** | id is not valid |  -  |
**402** | Subscription is outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Export or subscription is not found |  -  |
**500** | Try again, if error still here - text our support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exports_get_file**
> ExportVM exports_get_file(id)

Get export by specified id

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.export_vm import ExportVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | id of export

    try:
        # Get export by specified id
        api_response = api_instance.exports_get_file(id)
        print("The response of ExportsApi->exports_get_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->exports_get_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of export | 

### Return type

[**ExportVM**](ExportVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Export is found |  -  |
**400** | id is not valid |  -  |
**402** | Subscription is outdated |  -  |
**403** | You have no get permission |  -  |
**404** | Export or subscription is not found |  -  |
**500** | Try again, if error still here - text our support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exports_get_file_history**
> AuditActionsVM exports_get_file_history(id, skip=skip, take=take)

Returns list of actions, performed on this file

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.audit_actions_vm import AuditActionsVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | file id
    skip = 0 # int | how many actions to skip (optional) (default to 0)
    take = 10 # int | how many actions to take (optional) (default to 10)

    try:
        # Returns list of actions, performed on this file
        api_response = api_instance.exports_get_file_history(id, skip=skip, take=take)
        print("The response of ExportsApi->exports_get_file_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->exports_get_file_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| file id | 
 **skip** | **int**| how many actions to skip | [optional] [default to 0]
 **take** | **int**| how many actions to take | [optional] [default to 10]

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
**400** | Parameters did not pass the validation |  -  |
**402** | Subscription is outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | File or subscription was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exports_get_files_count**
> CountVM exports_get_files_count(id)

Get count of files what contains in a specified folder

User with Get Count permission can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.count_vm import CountVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | folder id

    try:
        # Get count of files what contains in a specified folder
        api_response = api_instance.exports_get_files_count(id)
        print("The response of ExportsApi->exports_get_files_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->exports_get_files_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| folder id | 

### Return type

[**CountVM**](CountVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Parameters did not pass the validation |  -  |
**402** | Subscription is outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | File or subscription was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exports_get_files_list**
> ExportsVM exports_get_files_list(id, skip=skip, take=take, search_pattern=search_pattern, order_by=order_by, desc=desc, use_regex=use_regex)

Get files from the specified folder

User with a Get Entity permission can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.exports_vm import ExportsVM
from fastreport_cloud_sdk.models.file_sorting import FileSorting
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | folder id
    skip = 0 # int | number of files to skip (optional) (default to 0)
    take = 10 # int | number of files to take (optional) (default to 10)
    search_pattern = 'search_pattern_example' # str | search pattern used to only include matching files in the result<br />              (leave unspecified to list all files) (optional)
    order_by = fastreport_cloud_sdk.FileSorting() # FileSorting | a field to sort by (optional)
    desc = False # bool | if true - sorting will be done in the descending order, otherwise - ascending (optional) (default to False)
    use_regex = False # bool | set this to true if you want to use regular expression to search (optional) (default to False)

    try:
        # Get files from the specified folder
        api_response = api_instance.exports_get_files_list(id, skip=skip, take=take, search_pattern=search_pattern, order_by=order_by, desc=desc, use_regex=use_regex)
        print("The response of ExportsApi->exports_get_files_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->exports_get_files_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| folder id | 
 **skip** | **int**| number of files to skip | [optional] [default to 0]
 **take** | **int**| number of files to take | [optional] [default to 10]
 **search_pattern** | **str**| search pattern used to only include matching files in the result&lt;br /&gt;              (leave unspecified to list all files) | [optional] 
 **order_by** | [**FileSorting**](.md)| a field to sort by | [optional] 
 **desc** | **bool**| if true - sorting will be done in the descending order, otherwise - ascending | [optional] [default to False]
 **use_regex** | **bool**| set this to true if you want to use regular expression to search | [optional] [default to False]

### Return type

[**ExportsVM**](ExportsVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Provided parameters did not pass the validation |  -  |
**402** | Subscription is blocked |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Subscription or folder was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exports_get_my_permissions**
> FilePermissionCRUDVM exports_get_my_permissions(id)

Get current user's permissions to a file

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.file_permission_crudvm import FilePermissionCRUDVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | file id

    try:
        # Get current user's permissions to a file
        api_response = api_instance.exports_get_my_permissions(id)
        print("The response of ExportsApi->exports_get_my_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->exports_get_my_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| file id | 

### Return type

[**FilePermissionCRUDVM**](FilePermissionCRUDVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Provided parameters did not pass the validation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exports_get_permissions**
> FilePermissionsVM exports_get_permissions(id)

Get all permissions from a file. <br />

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.file_permissions_vm import FilePermissionsVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | folder id

    try:
        # Get all permissions from a file. <br />
        api_response = api_instance.exports_get_permissions(id)
        print("The response of ExportsApi->exports_get_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->exports_get_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| folder id | 

### Return type

[**FilePermissionsVM**](FilePermissionsVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Provided parameters did not pass the validation |  -  |
**402** | Subscription is blocked |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | File or subscription was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exports_get_sharing_keys**
> FileSharingKeysVM exports_get_sharing_keys(id)

Returns all sharing keys, associated with the file

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.file_sharing_keys_vm import FileSharingKeysVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | file id

    try:
        # Returns all sharing keys, associated with the file
        api_response = api_instance.exports_get_sharing_keys(id)
        print("The response of ExportsApi->exports_get_sharing_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->exports_get_sharing_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| file id | 

### Return type

[**FileSharingKeysVM**](FileSharingKeysVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Parameters did not pass the validation |  -  |
**402** | Subscription is blocked |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | File or subscription was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exports_move_file**
> ExportVM exports_move_file(id, folder_id)

Move file to a specified folder

User with a Update Place permission for a folder and Create Entity  for a Parent Folder can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.export_vm import ExportVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | file id
    folder_id = 'folder_id_example' # str | folder id

    try:
        # Move file to a specified folder
        api_response = api_instance.exports_move_file(id, folder_id)
        print("The response of ExportsApi->exports_move_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->exports_move_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| file id | 
 **folder_id** | **str**| folder id | 

### Return type

[**ExportVM**](ExportVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Provided parameters did not pass the validation |  -  |
**402** | Subscription is outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | File, folder or subscription was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exports_move_file_to_bin**
> exports_move_file_to_bin(id)

Move specified file to recycle bin

User with Delete permission can access the method.

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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | file id

    try:
        # Move specified file to recycle bin
        api_instance.exports_move_file_to_bin(id)
    except Exception as e:
        print("Exception when calling ExportsApi->exports_move_file_to_bin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| file id | 

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
**400** | Parameters did not pass the validation |  -  |
**402** | Subscription is outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | File or subscription was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exports_recover_file**
> exports_recover_file(id, recovery_path=recovery_path)

Recover specified file from bin



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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | file id
    recovery_path = 'recovery_path_example' # str | id of the folder, where the file should be restored to (optional)

    try:
        # Recover specified file from bin
        api_instance.exports_recover_file(id, recovery_path=recovery_path)
    except Exception as e:
        print("Exception when calling ExportsApi->exports_recover_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| file id | 
 **recovery_path** | **str**| id of the folder, where the file should be restored to | [optional] 

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
**400** | Parameters did not pass the validation |  -  |
**402** | Subscription is outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | File or subscription was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exports_rename_file**
> ExportVM exports_rename_file(id, file_rename_vm=file_rename_vm)

Rename a file

User with Update Name permission can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.export_vm import ExportVM
from fastreport_cloud_sdk.models.file_rename_vm import FileRenameVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | 
    file_rename_vm = fastreport_cloud_sdk.FileRenameVM() # FileRenameVM |  (optional)

    try:
        # Rename a file
        api_response = api_instance.exports_rename_file(id, file_rename_vm=file_rename_vm)
        print("The response of ExportsApi->exports_rename_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->exports_rename_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **file_rename_vm** | [**FileRenameVM**](FileRenameVM.md)|  | [optional] 

### Return type

[**ExportVM**](ExportVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Provided parameters did not pass the validation |  -  |
**402** | Subscription is outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | File or subscription was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exports_update_icon**
> ExportVM exports_update_icon(id, file_icon_vm=file_icon_vm)

Update a files's icon

User with Update Icon permission can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.export_vm import ExportVM
from fastreport_cloud_sdk.models.file_icon_vm import FileIconVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | 
    file_icon_vm = fastreport_cloud_sdk.FileIconVM() # FileIconVM |  (optional)

    try:
        # Update a files's icon
        api_response = api_instance.exports_update_icon(id, file_icon_vm=file_icon_vm)
        print("The response of ExportsApi->exports_update_icon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->exports_update_icon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **file_icon_vm** | [**FileIconVM**](FileIconVM.md)|  | [optional] 

### Return type

[**ExportVM**](ExportVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Provided parameters did not pass the validation |  -  |
**402** | Subscription is outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | File or subscription was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exports_update_permissions**
> exports_update_permissions(id, update_file_permissions_vm=update_file_permissions_vm)

Update permissions

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.update_file_permissions_vm import UpdateFilePermissionsVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | file id
    update_file_permissions_vm = fastreport_cloud_sdk.UpdateFilePermissionsVM() # UpdateFilePermissionsVM | new permissions VM (optional)

    try:
        # Update permissions
        api_instance.exports_update_permissions(id, update_file_permissions_vm=update_file_permissions_vm)
    except Exception as e:
        print("Exception when calling ExportsApi->exports_update_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| file id | 
 **update_file_permissions_vm** | [**UpdateFilePermissionsVM**](UpdateFilePermissionsVM.md)| new permissions VM | [optional] 

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
**400** | Provided parameters did not pass the validation |  -  |
**402** | Subscription is outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | File or subscription was not found |  -  |
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exports_update_tags**
> ExportVM exports_update_tags(id, file_tags_update_vm=file_tags_update_vm)

Update tags

User with Update Tags permission can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.export_vm import ExportVM
from fastreport_cloud_sdk.models.file_tags_update_vm import FileTagsUpdateVM
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
    api_instance = fastreport_cloud_sdk.ExportsApi(api_client)
    id = 'id_example' # str | 
    file_tags_update_vm = fastreport_cloud_sdk.FileTagsUpdateVM() # FileTagsUpdateVM |  (optional)

    try:
        # Update tags
        api_response = api_instance.exports_update_tags(id, file_tags_update_vm=file_tags_update_vm)
        print("The response of ExportsApi->exports_update_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->exports_update_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **file_tags_update_vm** | [**FileTagsUpdateVM**](FileTagsUpdateVM.md)|  | [optional] 

### Return type

[**ExportVM**](ExportVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Provided parameters did not pass the validation |  -  |
**402** | Subscription is outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | File or subscription was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

