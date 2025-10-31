# fastreport_cloud_sdk.TemplatesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**template_folder_and_file_clear_recycle_bin**](TemplatesApi.md#template_folder_and_file_clear_recycle_bin) | **DELETE** /api/rp/v1/Templates/{subscriptionId}/ClearRecycleBin | Delete all folders and files from recycle bin
[**template_folder_and_file_copy_files**](TemplatesApi.md#template_folder_and_file_copy_files) | **POST** /api/rp/v1/Templates/{subscriptionId}/CopyFiles | Copy folders and files to a specified folder
[**template_folder_and_file_count_recycle_bin_folders_and_files**](TemplatesApi.md#template_folder_and_file_count_recycle_bin_folders_and_files) | **GET** /api/rp/v1/Templates/{subscriptionId}/CountRecycleBinFolderAndFiles | Count all folders and files from recycle bin
[**template_folder_and_file_delete_files**](TemplatesApi.md#template_folder_and_file_delete_files) | **POST** /api/rp/v1/Templates/{subscriptionId}/DeleteFiles | Delete folders and files from a folder or the recycle bin
[**template_folder_and_file_get_count**](TemplatesApi.md#template_folder_and_file_get_count) | **GET** /api/rp/v1/Templates/Folder/{id}/CountFolderAndFiles | Count folders and files in a folder
[**template_folder_and_file_get_folders_and_files**](TemplatesApi.md#template_folder_and_file_get_folders_and_files) | **GET** /api/rp/v1/Templates/Folder/{id}/ListFolderAndFiles | Get all folders and files from specified folder
[**template_folder_and_file_get_recycle_bin_folders_and_files**](TemplatesApi.md#template_folder_and_file_get_recycle_bin_folders_and_files) | **GET** /api/rp/v1/Templates/{subscriptionId}/ListRecycleBinFolderAndFiles | Get all folders and files from recycle bin
[**template_folder_and_file_move_files**](TemplatesApi.md#template_folder_and_file_move_files) | **POST** /api/rp/v1/Templates/{subscriptionId}/MoveFiles | Move folders and files to a specified folder
[**template_folder_and_file_move_files_to_bin**](TemplatesApi.md#template_folder_and_file_move_files_to_bin) | **POST** /api/rp/v1/Templates/{subscriptionId}/ToBin | Move folders and files to the recycle bin
[**template_folder_and_file_recover_all_from_recycle_bin**](TemplatesApi.md#template_folder_and_file_recover_all_from_recycle_bin) | **POST** /api/rp/v1/Templates/{subscriptionId}/RecoverRecycleBin | Recover all folders and files from recycle bin
[**template_folder_and_file_recover_files**](TemplatesApi.md#template_folder_and_file_recover_files) | **POST** /api/rp/v1/Templates/{subscriptionId}/RecoverFiles | Recover folders and files from the recycle bin
[**template_folders_calculate_folder_size**](TemplatesApi.md#template_folders_calculate_folder_size) | **GET** /api/rp/v1/Templates/Folder/{id}/size | Get specified folder, calculate it&#39;s size
[**template_folders_copy_folder**](TemplatesApi.md#template_folders_copy_folder) | **POST** /api/rp/v1/Templates/Folder/{id}/Copy/{folderId} | Move folder to a specified folder
[**template_folders_delete_folder**](TemplatesApi.md#template_folders_delete_folder) | **DELETE** /api/rp/v1/Templates/Folder/{id} | Delete specified folder
[**template_folders_export**](TemplatesApi.md#template_folders_export) | **POST** /api/rp/v1/Templates/Folder/{id}/Export | Export specified template folder to a specified format
[**template_folders_get_breadcrumbs**](TemplatesApi.md#template_folders_get_breadcrumbs) | **GET** /api/rp/v1/Templates/Folder/{id}/Breadcrumbs | Get specified folder breadcrumbs
[**template_folders_get_folder**](TemplatesApi.md#template_folders_get_folder) | **GET** /api/rp/v1/Templates/Folder/{id} | Get specified folder
[**template_folders_get_folders**](TemplatesApi.md#template_folders_get_folders) | **GET** /api/rp/v1/Templates/Folder/{id}/ListFolders | Get all folders from specified folder
[**template_folders_get_folders_count**](TemplatesApi.md#template_folders_get_folders_count) | **GET** /api/rp/v1/Templates/Folder/{id}/CountFolders | Get count of folders what contains in a specified folder
[**template_folders_get_my_permissions**](TemplatesApi.md#template_folders_get_my_permissions) | **GET** /api/rp/v1/Templates/Folder/{folderId}/mypermissions | Get user&#39;s permissions for a folder by id
[**template_folders_get_or_create**](TemplatesApi.md#template_folders_get_or_create) | **GET** /api/rp/v1/Templates/Folder/getOrCreate | Get specified folder
[**template_folders_get_permissions**](TemplatesApi.md#template_folders_get_permissions) | **GET** /api/rp/v1/Templates/Folder/{id}/permissions | Get all folder permissions
[**template_folders_get_root_folder**](TemplatesApi.md#template_folders_get_root_folder) | **GET** /api/rp/v1/Templates/Root | Get workspace&#39;s root folder
[**template_folders_move_folder**](TemplatesApi.md#template_folders_move_folder) | **POST** /api/rp/v1/Templates/Folder/{id}/Move/{folderId} | Move folder into a specified folder
[**template_folders_move_folder_to_bin**](TemplatesApi.md#template_folders_move_folder_to_bin) | **DELETE** /api/rp/v1/Templates/Folder/{id}/ToBin | Move specified folder to recycle bin
[**template_folders_post_folder**](TemplatesApi.md#template_folders_post_folder) | **POST** /api/rp/v1/Templates/Folder/{id}/Folder | Create folder
[**template_folders_prepare**](TemplatesApi.md#template_folders_prepare) | **POST** /api/rp/v1/Templates/Folder/{id}/Prepare | Prepare specified template folder to report folder
[**template_folders_recover_folder**](TemplatesApi.md#template_folders_recover_folder) | **POST** /api/rp/v1/Templates/Folder/{id}/Recover | Recover specified folder
[**template_folders_rename_folder**](TemplatesApi.md#template_folders_rename_folder) | **PUT** /api/rp/v1/Templates/Folder/{id}/Rename | Rename a folder
[**template_folders_update_icon**](TemplatesApi.md#template_folders_update_icon) | **PUT** /api/rp/v1/Templates/Folder/{id}/Icon | Update a folder&#39;s icon
[**template_folders_update_permissions**](TemplatesApi.md#template_folders_update_permissions) | **POST** /api/rp/v1/Templates/{id}/permissions | Update permissions
[**template_folders_update_tags**](TemplatesApi.md#template_folders_update_tags) | **PUT** /api/rp/v1/Templates/Folder/{id}/UpdateTags | Update tags
[**templates_copy_file**](TemplatesApi.md#templates_copy_file) | **POST** /api/rp/v1/Templates/File/{id}/Copy/{folderId} | Copy a file into a specified folder
[**templates_create_sharing_key**](TemplatesApi.md#templates_create_sharing_key) | **POST** /api/rp/v1/Templates/File/{id}/sharingKey | Create a new key, that can be used to share access to a file &lt;br /&gt;  (You need Administrate.Anon permission to create a new key)
[**templates_delete_file**](TemplatesApi.md#templates_delete_file) | **DELETE** /api/rp/v1/Templates/File/{id} | Delete specified file
[**templates_delete_sharing_key**](TemplatesApi.md#templates_delete_sharing_key) | **DELETE** /api/rp/v1/Templates/File/{id}/sharingKey | Deletes a sharing key, making links, that utilizing it no longer work
[**templates_export**](TemplatesApi.md#templates_export) | **POST** /api/rp/v1/Templates/File/{id}/Export | Export specified report template to a specified format
[**templates_get_file**](TemplatesApi.md#templates_get_file) | **GET** /api/rp/v1/Templates/File/{id} | Get specified file
[**templates_get_file_history**](TemplatesApi.md#templates_get_file_history) | **GET** /api/rp/v1/Templates/File/{id}/History | Returns list of actions, performed on this file
[**templates_get_files_count**](TemplatesApi.md#templates_get_files_count) | **GET** /api/rp/v1/Templates/Folder/{id}/CountFiles | Get count of files what contains in a specified folder
[**templates_get_files_list**](TemplatesApi.md#templates_get_files_list) | **GET** /api/rp/v1/Templates/Folder/{id}/ListFiles | Get files from the specified folder
[**templates_get_my_permissions**](TemplatesApi.md#templates_get_my_permissions) | **GET** /api/rp/v1/Templates/File/{id}/mypermissions | Get current user&#39;s permissions to a file
[**templates_get_permissions**](TemplatesApi.md#templates_get_permissions) | **GET** /api/rp/v1/Templates/File/{id}/permissions | Get all permissions from a file. &lt;br /&gt;
[**templates_get_sharing_keys**](TemplatesApi.md#templates_get_sharing_keys) | **GET** /api/rp/v1/Templates/File/{id}/sharingKeys | Returns all sharing keys, associated with the file
[**templates_move_file**](TemplatesApi.md#templates_move_file) | **POST** /api/rp/v1/Templates/File/{id}/Move/{folderId} | Move file to a specified folder
[**templates_move_file_to_bin**](TemplatesApi.md#templates_move_file_to_bin) | **DELETE** /api/rp/v1/Templates/File/{id}/ToBin | Move specified file to recycle bin
[**templates_prepare**](TemplatesApi.md#templates_prepare) | **POST** /api/rp/v1/Templates/File/{id}/Prepare | Prepare specified template to report
[**templates_recover_file**](TemplatesApi.md#templates_recover_file) | **POST** /api/rp/v1/Templates/File/{id}/Recover | Recover specified file from bin
[**templates_rename_file**](TemplatesApi.md#templates_rename_file) | **PUT** /api/rp/v1/Templates/File/{id}/Rename | Rename a file
[**templates_static_preview**](TemplatesApi.md#templates_static_preview) | **POST** /api/rp/v1/Templates/File/{id}/StaticPreview | Make preview for the report.  Generate a new or return exist prepared svg files.  If template was changed will be returned a new.  Pass the &#x60;&#x60; parameter to check prepared timestamp
[**templates_update_content**](TemplatesApi.md#templates_update_content) | **PUT** /api/rp/v1/Templates/File/{id}/Content | Updates contnet of the template. The method is deprecated, use the UpdateContentV2 method instead!
[**templates_update_content_v2**](TemplatesApi.md#templates_update_content_v2) | **PUT** /api/rp/v2/Templates/File/{id}/Content | Updates contnet of the template.
[**templates_update_icon**](TemplatesApi.md#templates_update_icon) | **PUT** /api/rp/v1/Templates/File/{id}/Icon | Update a files&#39;s icon
[**templates_update_parameters**](TemplatesApi.md#templates_update_parameters) | **PUT** /api/rp/v1/Templates/File/{id}/parameters | 
[**templates_update_permissions**](TemplatesApi.md#templates_update_permissions) | **POST** /api/rp/v1/Templates/File/{id}/permissions | Update permissions
[**templates_update_tags**](TemplatesApi.md#templates_update_tags) | **PUT** /api/rp/v1/Templates/File/{id}/UpdateTags | Update tags
[**templates_upload_file**](TemplatesApi.md#templates_upload_file) | **POST** /api/rp/v1/Templates/Folder/{id}/File | Upload a file to the specified folder. The method is deprecated, use the UploadFileV2 method instead!
[**templates_upload_file_v2**](TemplatesApi.md#templates_upload_file_v2) | **POST** /api/rp/v2/Templates/Folder/{id}/File | Alternative api for upload a file to the specified folder!
[**templates_wasm_static_preview**](TemplatesApi.md#templates_wasm_static_preview) | **POST** /api/rp/v1/Templates/File/{id}/WasmStaticPreview | Make preview for the report (template).  Generate a new or return exist prepared fpx file.  If template was changed will be returned a new.


# **template_folder_and_file_clear_recycle_bin**
> template_folder_and_file_clear_recycle_bin(subscription_id)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    subscription_id = 'subscription_id_example' # str | subscription id

    try:
        # Delete all folders and files from recycle bin
        api_instance.template_folder_and_file_clear_recycle_bin(subscription_id)
    except Exception as e:
        print("Exception when calling TemplatesApi->template_folder_and_file_clear_recycle_bin: %s\n" % e)
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

# **template_folder_and_file_copy_files**
> template_folder_and_file_copy_files(subscription_id, selected_files_vm=selected_files_vm)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    subscription_id = 'subscription_id_example' # str | id of current subscription
    selected_files_vm = fastreport_cloud_sdk.SelectedFilesVM() # SelectedFilesVM | File selection VM (optional)

    try:
        # Copy folders and files to a specified folder
        api_instance.template_folder_and_file_copy_files(subscription_id, selected_files_vm=selected_files_vm)
    except Exception as e:
        print("Exception when calling TemplatesApi->template_folder_and_file_copy_files: %s\n" % e)
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

# **template_folder_and_file_count_recycle_bin_folders_and_files**
> CountVM template_folder_and_file_count_recycle_bin_folders_and_files(subscription_id, search_pattern=search_pattern, use_regex=use_regex)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    subscription_id = 'subscription_id_example' # str | subscription id
    search_pattern = '' # str | search pattern used to only include matching files in the recycle bin count<br />              (leave unspecified to count all files and folders) (optional) (default to '')
    use_regex = False # bool | set this to true if you want to use regular expression to search (optional) (default to False)

    try:
        # Count all folders and files from recycle bin
        api_response = api_instance.template_folder_and_file_count_recycle_bin_folders_and_files(subscription_id, search_pattern=search_pattern, use_regex=use_regex)
        print("The response of TemplatesApi->template_folder_and_file_count_recycle_bin_folders_and_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->template_folder_and_file_count_recycle_bin_folders_and_files: %s\n" % e)
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

# **template_folder_and_file_delete_files**
> template_folder_and_file_delete_files(subscription_id, selected_files_vm=selected_files_vm)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    subscription_id = 'subscription_id_example' # str | id of the subscription
    selected_files_vm = fastreport_cloud_sdk.SelectedFilesVM() # SelectedFilesVM | File selection VM (optional)

    try:
        # Delete folders and files from a folder or the recycle bin
        api_instance.template_folder_and_file_delete_files(subscription_id, selected_files_vm=selected_files_vm)
    except Exception as e:
        print("Exception when calling TemplatesApi->template_folder_and_file_delete_files: %s\n" % e)
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

# **template_folder_and_file_get_count**
> CountVM template_folder_and_file_get_count(id, search_pattern=search_pattern, use_regex=use_regex)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | folder id
    search_pattern = 'search_pattern_example' # str | search pattern used to only include matching files in the count<br />              (leave unspecified to count all files and folders) (optional)
    use_regex = False # bool | set this to true if you want to use regular expression to search (optional) (default to False)

    try:
        # Count folders and files in a folder
        api_response = api_instance.template_folder_and_file_get_count(id, search_pattern=search_pattern, use_regex=use_regex)
        print("The response of TemplatesApi->template_folder_and_file_get_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->template_folder_and_file_get_count: %s\n" % e)
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

# **template_folder_and_file_get_folders_and_files**
> FilesVM template_folder_and_file_get_folders_and_files(id, skip=skip, take=take, order_by=order_by, desc=desc, search_pattern=search_pattern, use_regex=use_regex)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | folder id
    skip = 0 # int | number of folder and files to skip (optional) (default to 0)
    take = 10 # int | number of folder and files to take (optional) (default to 10)
    order_by = fastreport_cloud_sdk.FileSorting() # FileSorting | a field to sort by (optional)
    desc = False # bool | if true - sorting will be done in the descending order, otherwise - ascending (optional) (default to False)
    search_pattern = '' # str | search pattern used to only include matching files in the result<br />              (leave unspecified to list all files and folders) (optional) (default to '')
    use_regex = False # bool | set this to true if you want to use regular expression to search (optional) (default to False)

    try:
        # Get all folders and files from specified folder
        api_response = api_instance.template_folder_and_file_get_folders_and_files(id, skip=skip, take=take, order_by=order_by, desc=desc, search_pattern=search_pattern, use_regex=use_regex)
        print("The response of TemplatesApi->template_folder_and_file_get_folders_and_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->template_folder_and_file_get_folders_and_files: %s\n" % e)
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

# **template_folder_and_file_get_recycle_bin_folders_and_files**
> FilesVM template_folder_and_file_get_recycle_bin_folders_and_files(subscription_id, skip=skip, take=take, order_by=order_by, desc=desc, search_pattern=search_pattern, use_regex=use_regex)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    subscription_id = 'subscription_id_example' # str | subscription id
    skip = 0 # int | number of folder and files to skip (optional) (default to 0)
    take = 10 # int | number of folder and files to take (optional) (default to 10)
    order_by = fastreport_cloud_sdk.FileSorting() # FileSorting | a field to sort by (optional)
    desc = False # bool | if true - sorting will be done in the descending order, otherwise - ascending (optional) (default to False)
    search_pattern = '' # str | search pattern used to only include matching files in the recycle bin<br />              (leave unspecified to list all files and folders) (optional) (default to '')
    use_regex = False # bool | set this to true if you want to use regular expression to search (optional) (default to False)

    try:
        # Get all folders and files from recycle bin
        api_response = api_instance.template_folder_and_file_get_recycle_bin_folders_and_files(subscription_id, skip=skip, take=take, order_by=order_by, desc=desc, search_pattern=search_pattern, use_regex=use_regex)
        print("The response of TemplatesApi->template_folder_and_file_get_recycle_bin_folders_and_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->template_folder_and_file_get_recycle_bin_folders_and_files: %s\n" % e)
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

# **template_folder_and_file_move_files**
> template_folder_and_file_move_files(subscription_id, selected_files_vm=selected_files_vm)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    subscription_id = 'subscription_id_example' # str | id of current subscription
    selected_files_vm = fastreport_cloud_sdk.SelectedFilesVM() # SelectedFilesVM | File selection VM (optional)

    try:
        # Move folders and files to a specified folder
        api_instance.template_folder_and_file_move_files(subscription_id, selected_files_vm=selected_files_vm)
    except Exception as e:
        print("Exception when calling TemplatesApi->template_folder_and_file_move_files: %s\n" % e)
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

# **template_folder_and_file_move_files_to_bin**
> template_folder_and_file_move_files_to_bin(subscription_id, selected_files_vm=selected_files_vm)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    subscription_id = 'subscription_id_example' # str | id of the subscription
    selected_files_vm = fastreport_cloud_sdk.SelectedFilesVM() # SelectedFilesVM | File selection VM (optional)

    try:
        # Move folders and files to the recycle bin
        api_instance.template_folder_and_file_move_files_to_bin(subscription_id, selected_files_vm=selected_files_vm)
    except Exception as e:
        print("Exception when calling TemplatesApi->template_folder_and_file_move_files_to_bin: %s\n" % e)
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

# **template_folder_and_file_recover_all_from_recycle_bin**
> template_folder_and_file_recover_all_from_recycle_bin(subscription_id)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    subscription_id = 'subscription_id_example' # str | subscription id

    try:
        # Recover all folders and files from recycle bin
        api_instance.template_folder_and_file_recover_all_from_recycle_bin(subscription_id)
    except Exception as e:
        print("Exception when calling TemplatesApi->template_folder_and_file_recover_all_from_recycle_bin: %s\n" % e)
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

# **template_folder_and_file_recover_files**
> template_folder_and_file_recover_files(subscription_id, selected_files_vm=selected_files_vm)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    subscription_id = 'subscription_id_example' # str | id the subscription
    selected_files_vm = fastreport_cloud_sdk.SelectedFilesVM() # SelectedFilesVM | File selection VM (optional)

    try:
        # Recover folders and files from the recycle bin
        api_instance.template_folder_and_file_recover_files(subscription_id, selected_files_vm=selected_files_vm)
    except Exception as e:
        print("Exception when calling TemplatesApi->template_folder_and_file_recover_files: %s\n" % e)
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

# **template_folders_calculate_folder_size**
> FolderSizeVM template_folders_calculate_folder_size(id)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | folder id

    try:
        # Get specified folder, calculate it's size
        api_response = api_instance.template_folders_calculate_folder_size(id)
        print("The response of TemplatesApi->template_folders_calculate_folder_size:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->template_folders_calculate_folder_size: %s\n" % e)
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

# **template_folders_copy_folder**
> FileVM template_folders_copy_folder(id, folder_id)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | moving folder id
    folder_id = 'folder_id_example' # str | destination folder id

    try:
        # Move folder to a specified folder
        api_response = api_instance.template_folders_copy_folder(id, folder_id)
        print("The response of TemplatesApi->template_folders_copy_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->template_folders_copy_folder: %s\n" % e)
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

# **template_folders_delete_folder**
> template_folders_delete_folder(id)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | folder id

    try:
        # Delete specified folder
        api_instance.template_folders_delete_folder(id)
    except Exception as e:
        print("Exception when calling TemplatesApi->template_folders_delete_folder: %s\n" % e)
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

# **template_folders_export**
> FileVM template_folders_export(id, export_template_vm=export_template_vm)

Export specified template folder to a specified format

User with Execute Export permission on template folder and  Create Entity on an export folder can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.export_template_vm import ExportTemplateVM
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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | template folder id
    export_template_vm = fastreport_cloud_sdk.ExportTemplateVM() # ExportTemplateVM | export parameters (string only) (optional)

    try:
        # Export specified template folder to a specified format
        api_response = api_instance.template_folders_export(id, export_template_vm=export_template_vm)
        print("The response of TemplatesApi->template_folders_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->template_folders_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| template folder id | 
 **export_template_vm** | [**ExportTemplateVM**](ExportTemplateVM.md)| export parameters (string only) | [optional] 

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
**200** | Specified template folder has been exported |  -  |
**400** | Template folder Id is null |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**402** | Subscription is outdated |  -  |
**404** | Exports folder not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template_folders_get_breadcrumbs**
> BreadcrumbsVM template_folders_get_breadcrumbs(id)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | folder id

    try:
        # Get specified folder breadcrumbs
        api_response = api_instance.template_folders_get_breadcrumbs(id)
        print("The response of TemplatesApi->template_folders_get_breadcrumbs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->template_folders_get_breadcrumbs: %s\n" % e)
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

# **template_folders_get_folder**
> FileVM template_folders_get_folder(id)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | folder id

    try:
        # Get specified folder
        api_response = api_instance.template_folders_get_folder(id)
        print("The response of TemplatesApi->template_folders_get_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->template_folders_get_folder: %s\n" % e)
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

# **template_folders_get_folders**
> FilesVM template_folders_get_folders(id, skip=skip, take=take, order_by=order_by, desc=desc, search_pattern=search_pattern, use_regex=use_regex)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | folder id
    skip = 0 # int | number of folder and files to skip (optional) (default to 0)
    take = 10 # int | number of folder and files to take (optional) (default to 10)
    order_by = fastreport_cloud_sdk.FileSorting() # FileSorting | a field to sort by (optional)
    desc = False # bool | if true - sorting will be done in the descending order, otherwise - ascending (optional) (default to False)
    search_pattern = '' # str | search pattern used to only include matching files in the result<br />              (leave unspecified to list all files and folders) (optional) (default to '')
    use_regex = False # bool | set this to true if you want to use regular expression to search (optional) (default to False)

    try:
        # Get all folders from specified folder
        api_response = api_instance.template_folders_get_folders(id, skip=skip, take=take, order_by=order_by, desc=desc, search_pattern=search_pattern, use_regex=use_regex)
        print("The response of TemplatesApi->template_folders_get_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->template_folders_get_folders: %s\n" % e)
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

# **template_folders_get_folders_count**
> CountVM template_folders_get_folders_count(id)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | folder id

    try:
        # Get count of folders what contains in a specified folder
        api_response = api_instance.template_folders_get_folders_count(id)
        print("The response of TemplatesApi->template_folders_get_folders_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->template_folders_get_folders_count: %s\n" % e)
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

# **template_folders_get_my_permissions**
> FilePermissionCRUDVM template_folders_get_my_permissions(folder_id)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    folder_id = 'folder_id_example' # str | folder id

    try:
        # Get user's permissions for a folder by id
        api_response = api_instance.template_folders_get_my_permissions(folder_id)
        print("The response of TemplatesApi->template_folders_get_my_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->template_folders_get_my_permissions: %s\n" % e)
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

# **template_folders_get_or_create**
> FileVM template_folders_get_or_create(name=name, subscription_id=subscription_id, parent_id=parent_id)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    name = 'name_example' # str | folder name (optional)
    subscription_id = 'subscription_id_example' # str | subscriptionId (optional)
    parent_id = 'parent_id_example' # str | parent folder id (optional)

    try:
        # Get specified folder
        api_response = api_instance.template_folders_get_or_create(name=name, subscription_id=subscription_id, parent_id=parent_id)
        print("The response of TemplatesApi->template_folders_get_or_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->template_folders_get_or_create: %s\n" % e)
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

# **template_folders_get_permissions**
> FilePermissionsVM template_folders_get_permissions(id)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get all folder permissions
        api_response = api_instance.template_folders_get_permissions(id)
        print("The response of TemplatesApi->template_folders_get_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->template_folders_get_permissions: %s\n" % e)
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

# **template_folders_get_root_folder**
> FileVM template_folders_get_root_folder(subscription_id=subscription_id)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    subscription_id = 'subscription_id_example' # str |  (optional)

    try:
        # Get workspace's root folder
        api_response = api_instance.template_folders_get_root_folder(subscription_id=subscription_id)
        print("The response of TemplatesApi->template_folders_get_root_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->template_folders_get_root_folder: %s\n" % e)
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

# **template_folders_move_folder**
> FileVM template_folders_move_folder(id, folder_id)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | folder id
    folder_id = 'folder_id_example' # str | destination folder id

    try:
        # Move folder into a specified folder
        api_response = api_instance.template_folders_move_folder(id, folder_id)
        print("The response of TemplatesApi->template_folders_move_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->template_folders_move_folder: %s\n" % e)
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

# **template_folders_move_folder_to_bin**
> template_folders_move_folder_to_bin(id)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | folder id

    try:
        # Move specified folder to recycle bin
        api_instance.template_folders_move_folder_to_bin(id)
    except Exception as e:
        print("Exception when calling TemplatesApi->template_folders_move_folder_to_bin: %s\n" % e)
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

# **template_folders_post_folder**
> FileVM template_folders_post_folder(id, template_folder_create_vm=template_folder_create_vm)

Create folder

User with a Create Entity permission can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.file_vm import FileVM
from fastreport_cloud_sdk.models.template_folder_create_vm import TemplateFolderCreateVM
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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | Identifier of parent folder id
    template_folder_create_vm = fastreport_cloud_sdk.TemplateFolderCreateVM() # TemplateFolderCreateVM | create VM (optional)

    try:
        # Create folder
        api_response = api_instance.template_folders_post_folder(id, template_folder_create_vm=template_folder_create_vm)
        print("The response of TemplatesApi->template_folders_post_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->template_folders_post_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of parent folder id | 
 **template_folder_create_vm** | [**TemplateFolderCreateVM**](TemplateFolderCreateVM.md)| create VM | [optional] 

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

# **template_folders_prepare**
> FileVM template_folders_prepare(id, prepare_template_vm=prepare_template_vm)

Prepare specified template folder to report folder

User with Execute Prepare permission on report and  Create Entity on a prepared report folder can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.file_vm import FileVM
from fastreport_cloud_sdk.models.prepare_template_vm import PrepareTemplateVM
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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | template id
    prepare_template_vm = fastreport_cloud_sdk.PrepareTemplateVM() # PrepareTemplateVM | Template folder prepare view model (optional)

    try:
        # Prepare specified template folder to report folder
        api_response = api_instance.template_folders_prepare(id, prepare_template_vm=prepare_template_vm)
        print("The response of TemplatesApi->template_folders_prepare:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->template_folders_prepare: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| template id | 
 **prepare_template_vm** | [**PrepareTemplateVM**](PrepareTemplateVM.md)| Template folder prepare view model | [optional] 

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
**200** | Specified template folder has been prepared |  -  |
**400** | Template folder Id is null |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**402** | subscription is outdated |  -  |
**404** | Template or report folder not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template_folders_recover_folder**
> template_folders_recover_folder(id, recovery_path=recovery_path)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | folder id
    recovery_path = 'recovery_path_example' # str | id of the folder, that recovered folder should be placed in (optional)

    try:
        # Recover specified folder
        api_instance.template_folders_recover_folder(id, recovery_path=recovery_path)
    except Exception as e:
        print("Exception when calling TemplatesApi->template_folders_recover_folder: %s\n" % e)
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

# **template_folders_rename_folder**
> FileVM template_folders_rename_folder(id, folder_rename_vm=folder_rename_vm)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | 
    folder_rename_vm = fastreport_cloud_sdk.FolderRenameVM() # FolderRenameVM |  (optional)

    try:
        # Rename a folder
        api_response = api_instance.template_folders_rename_folder(id, folder_rename_vm=folder_rename_vm)
        print("The response of TemplatesApi->template_folders_rename_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->template_folders_rename_folder: %s\n" % e)
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

# **template_folders_update_icon**
> FileVM template_folders_update_icon(id, folder_icon_vm=folder_icon_vm)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | Identifier of folder
    folder_icon_vm = fastreport_cloud_sdk.FolderIconVM() # FolderIconVM | Update icon model (optional)

    try:
        # Update a folder's icon
        api_response = api_instance.template_folders_update_icon(id, folder_icon_vm=folder_icon_vm)
        print("The response of TemplatesApi->template_folders_update_icon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->template_folders_update_icon: %s\n" % e)
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

# **template_folders_update_permissions**
> template_folders_update_permissions(id, update_file_permissions_vm=update_file_permissions_vm)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | folder id
    update_file_permissions_vm = fastreport_cloud_sdk.UpdateFilePermissionsVM() # UpdateFilePermissionsVM | new permissions VM (optional)

    try:
        # Update permissions
        api_instance.template_folders_update_permissions(id, update_file_permissions_vm=update_file_permissions_vm)
    except Exception as e:
        print("Exception when calling TemplatesApi->template_folders_update_permissions: %s\n" % e)
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

# **template_folders_update_tags**
> FileVM template_folders_update_tags(id, folder_tags_update_vm=folder_tags_update_vm)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | 
    folder_tags_update_vm = fastreport_cloud_sdk.FolderTagsUpdateVM() # FolderTagsUpdateVM |  (optional)

    try:
        # Update tags
        api_response = api_instance.template_folders_update_tags(id, folder_tags_update_vm=folder_tags_update_vm)
        print("The response of TemplatesApi->template_folders_update_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->template_folders_update_tags: %s\n" % e)
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

# **templates_copy_file**
> TemplateVM templates_copy_file(id, folder_id)

Copy a file into a specified folder

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.template_vm import TemplateVM
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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | file id
    folder_id = 'folder_id_example' # str | folder id

    try:
        # Copy a file into a specified folder
        api_response = api_instance.templates_copy_file(id, folder_id)
        print("The response of TemplatesApi->templates_copy_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_copy_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| file id | 
 **folder_id** | **str**| folder id | 

### Return type

[**TemplateVM**](TemplateVM.md)

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

# **templates_create_sharing_key**
> FileSharingKeysVM templates_create_sharing_key(id, create_file_share_vm=create_file_share_vm)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | file id
    create_file_share_vm = fastreport_cloud_sdk.CreateFileShareVM() # CreateFileShareVM | parameters for sharing key creation (optional)

    try:
        # Create a new key, that can be used to share access to a file <br />  (You need Administrate.Anon permission to create a new key)
        api_response = api_instance.templates_create_sharing_key(id, create_file_share_vm=create_file_share_vm)
        print("The response of TemplatesApi->templates_create_sharing_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_create_sharing_key: %s\n" % e)
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

# **templates_delete_file**
> templates_delete_file(id)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | file id

    try:
        # Delete specified file
        api_instance.templates_delete_file(id)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_delete_file: %s\n" % e)
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

# **templates_delete_sharing_key**
> templates_delete_sharing_key(id, key)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | file id
    key = 'key_example' # str | key to delete

    try:
        # Deletes a sharing key, making links, that utilizing it no longer work
        api_instance.templates_delete_sharing_key(id, key)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_delete_sharing_key: %s\n" % e)
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

# **templates_export**
> ExportVM templates_export(id, export_template_vm=export_template_vm)

Export specified report template to a specified format

User with Execute Export permission on prepared report and  Create Entity on an export folder can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.export_template_vm import ExportTemplateVM
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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | template id
    export_template_vm = fastreport_cloud_sdk.ExportTemplateVM() # ExportTemplateVM | export parameters (string only) (optional)

    try:
        # Export specified report template to a specified format
        api_response = api_instance.templates_export(id, export_template_vm=export_template_vm)
        print("The response of TemplatesApi->templates_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| template id | 
 **export_template_vm** | [**ExportTemplateVM**](ExportTemplateVM.md)| export parameters (string only) | [optional] 

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
**200** | Specified report has been exported |  -  |
**204** | Specified report has been exported |  -  |
**400** | Report Id is null |  -  |
**402** | Subscription is outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Exports folder not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_get_file**
> TemplateVM templates_get_file(id)

Get specified file

User with Get Entity permission can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.template_vm import TemplateVM
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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | file id

    try:
        # Get specified file
        api_response = api_instance.templates_get_file(id)
        print("The response of TemplatesApi->templates_get_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_get_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| file id | 

### Return type

[**TemplateVM**](TemplateVM.md)

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

# **templates_get_file_history**
> AuditActionsVM templates_get_file_history(id, skip=skip, take=take)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | file id
    skip = 0 # int | how many actions to skip (optional) (default to 0)
    take = 10 # int | how many actions to take (optional) (default to 10)

    try:
        # Returns list of actions, performed on this file
        api_response = api_instance.templates_get_file_history(id, skip=skip, take=take)
        print("The response of TemplatesApi->templates_get_file_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_get_file_history: %s\n" % e)
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

# **templates_get_files_count**
> CountVM templates_get_files_count(id)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | folder id

    try:
        # Get count of files what contains in a specified folder
        api_response = api_instance.templates_get_files_count(id)
        print("The response of TemplatesApi->templates_get_files_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_get_files_count: %s\n" % e)
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

# **templates_get_files_list**
> TemplatesVM templates_get_files_list(id, skip=skip, take=take, search_pattern=search_pattern, order_by=order_by, desc=desc, use_regex=use_regex)

Get files from the specified folder

User with a Get Entity permission can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.file_sorting import FileSorting
from fastreport_cloud_sdk.models.templates_vm import TemplatesVM
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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | folder id
    skip = 0 # int | number of files to skip (optional) (default to 0)
    take = 10 # int | number of files to take (optional) (default to 10)
    search_pattern = 'search_pattern_example' # str | search pattern used to only include matching files in the result<br />              (leave unspecified to list all files) (optional)
    order_by = fastreport_cloud_sdk.FileSorting() # FileSorting | a field to sort by (optional)
    desc = False # bool | if true - sorting will be done in the descending order, otherwise - ascending (optional) (default to False)
    use_regex = False # bool | set this to true if you want to use regular expression to search (optional) (default to False)

    try:
        # Get files from the specified folder
        api_response = api_instance.templates_get_files_list(id, skip=skip, take=take, search_pattern=search_pattern, order_by=order_by, desc=desc, use_regex=use_regex)
        print("The response of TemplatesApi->templates_get_files_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_get_files_list: %s\n" % e)
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

[**TemplatesVM**](TemplatesVM.md)

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

# **templates_get_my_permissions**
> FilePermissionCRUDVM templates_get_my_permissions(id)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | file id

    try:
        # Get current user's permissions to a file
        api_response = api_instance.templates_get_my_permissions(id)
        print("The response of TemplatesApi->templates_get_my_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_get_my_permissions: %s\n" % e)
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

# **templates_get_permissions**
> FilePermissionsVM templates_get_permissions(id)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | folder id

    try:
        # Get all permissions from a file. <br />
        api_response = api_instance.templates_get_permissions(id)
        print("The response of TemplatesApi->templates_get_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_get_permissions: %s\n" % e)
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

# **templates_get_sharing_keys**
> FileSharingKeysVM templates_get_sharing_keys(id)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | file id

    try:
        # Returns all sharing keys, associated with the file
        api_response = api_instance.templates_get_sharing_keys(id)
        print("The response of TemplatesApi->templates_get_sharing_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_get_sharing_keys: %s\n" % e)
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

# **templates_move_file**
> TemplateVM templates_move_file(id, folder_id)

Move file to a specified folder

User with a Update Place permission for a folder and Create Entity  for a Parent Folder can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.template_vm import TemplateVM
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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | file id
    folder_id = 'folder_id_example' # str | folder id

    try:
        # Move file to a specified folder
        api_response = api_instance.templates_move_file(id, folder_id)
        print("The response of TemplatesApi->templates_move_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_move_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| file id | 
 **folder_id** | **str**| folder id | 

### Return type

[**TemplateVM**](TemplateVM.md)

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

# **templates_move_file_to_bin**
> templates_move_file_to_bin(id)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | file id

    try:
        # Move specified file to recycle bin
        api_instance.templates_move_file_to_bin(id)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_move_file_to_bin: %s\n" % e)
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

# **templates_prepare**
> ReportVM templates_prepare(id, prepare_template_vm=prepare_template_vm)

Prepare specified template to report

User with Execute Prepare permission on report and  Create Entity on a prepared report folder can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.prepare_template_vm import PrepareTemplateVM
from fastreport_cloud_sdk.models.report_vm import ReportVM
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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | template id
    prepare_template_vm = fastreport_cloud_sdk.PrepareTemplateVM() # PrepareTemplateVM | Template prepare view model (optional)

    try:
        # Prepare specified template to report
        api_response = api_instance.templates_prepare(id, prepare_template_vm=prepare_template_vm)
        print("The response of TemplatesApi->templates_prepare:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_prepare: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| template id | 
 **prepare_template_vm** | [**PrepareTemplateVM**](PrepareTemplateVM.md)| Template prepare view model | [optional] 

### Return type

[**ReportVM**](ReportVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Specified template has been prepared |  -  |
**204** | Specified template has been prepared |  -  |
**400** | Report Id is null |  -  |
**402** | subscription is outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Template or folder not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_recover_file**
> templates_recover_file(id, recovery_path=recovery_path)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | file id
    recovery_path = 'recovery_path_example' # str | id of the folder, where the file should be restored to (optional)

    try:
        # Recover specified file from bin
        api_instance.templates_recover_file(id, recovery_path=recovery_path)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_recover_file: %s\n" % e)
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

# **templates_rename_file**
> TemplateVM templates_rename_file(id, file_rename_vm=file_rename_vm)

Rename a file

User with Update Name permission can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.file_rename_vm import FileRenameVM
from fastreport_cloud_sdk.models.template_vm import TemplateVM
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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | 
    file_rename_vm = fastreport_cloud_sdk.FileRenameVM() # FileRenameVM |  (optional)

    try:
        # Rename a file
        api_response = api_instance.templates_rename_file(id, file_rename_vm=file_rename_vm)
        print("The response of TemplatesApi->templates_rename_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_rename_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **file_rename_vm** | [**FileRenameVM**](FileRenameVM.md)|  | [optional] 

### Return type

[**TemplateVM**](TemplateVM.md)

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

# **templates_static_preview**
> ExportVM templates_static_preview(id, preview_template_vm=preview_template_vm)

Make preview for the report.  Generate a new or return exist prepared svg files.  If template was changed will be returned a new.  Pass the `` parameter to check prepared timestamp

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.export_vm import ExportVM
from fastreport_cloud_sdk.models.preview_template_vm import PreviewTemplateVM
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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | template id
    preview_template_vm = fastreport_cloud_sdk.PreviewTemplateVM() # PreviewTemplateVM | Model with parameters (optional)

    try:
        # Make preview for the report.  Generate a new or return exist prepared svg files.  If template was changed will be returned a new.  Pass the `` parameter to check prepared timestamp
        api_response = api_instance.templates_static_preview(id, preview_template_vm=preview_template_vm)
        print("The response of TemplatesApi->templates_static_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_static_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| template id | 
 **preview_template_vm** | [**PreviewTemplateVM**](PreviewTemplateVM.md)| Model with parameters | [optional] 

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
**200** | Specified template has been prepared |  -  |
**204** | Specified template has been prepared |  -  |
**400** | Template Id is null |  -  |
**402** | Subscription is outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Template or folder not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_update_content**
> templates_update_content(id, update_file_content_vm=update_file_content_vm)

Updates contnet of the template. The method is deprecated, use the UpdateContentV2 method instead!

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.update_file_content_vm import UpdateFileContentVM
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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | template id
    update_file_content_vm = fastreport_cloud_sdk.UpdateFileContentVM() # UpdateFileContentVM | VM with only byte[] with new content (optional)

    try:
        # Updates contnet of the template. The method is deprecated, use the UpdateContentV2 method instead!
        api_instance.templates_update_content(id, update_file_content_vm=update_file_content_vm)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_update_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| template id | 
 **update_file_content_vm** | [**UpdateFileContentVM**](UpdateFileContentVM.md)| VM with only byte[] with new content | [optional] 

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
**402** | Client Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_update_content_v2**
> templates_update_content_v2(id, file_content)

Updates contnet of the template.

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | template id
    file_content = None # bytearray | 

    try:
        # Updates contnet of the template.
        api_instance.templates_update_content_v2(id, file_content)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_update_content_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| template id | 
 **file_content** | **bytearray**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Template has been updated |  -  |
**404** | Template or subscription are not found |  -  |
**400** | Id or VM is not valid |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**402** | subscription is outdated |  -  |
**500** | Try again, if error still here - text our support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_update_icon**
> TemplateVM templates_update_icon(id, file_icon_vm=file_icon_vm)

Update a files's icon

User with Update Icon permission can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.file_icon_vm import FileIconVM
from fastreport_cloud_sdk.models.template_vm import TemplateVM
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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | 
    file_icon_vm = fastreport_cloud_sdk.FileIconVM() # FileIconVM |  (optional)

    try:
        # Update a files's icon
        api_response = api_instance.templates_update_icon(id, file_icon_vm=file_icon_vm)
        print("The response of TemplatesApi->templates_update_icon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_update_icon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **file_icon_vm** | [**FileIconVM**](FileIconVM.md)|  | [optional] 

### Return type

[**TemplateVM**](TemplateVM.md)

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

# **templates_update_parameters**
> TemplateVM templates_update_parameters(id, report_parameters_vm)



### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.report_parameters_vm import ReportParametersVM
from fastreport_cloud_sdk.models.template_vm import TemplateVM
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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | 
    report_parameters_vm = fastreport_cloud_sdk.ReportParametersVM() # ReportParametersVM | 

    try:
        api_response = api_instance.templates_update_parameters(id, report_parameters_vm)
        print("The response of TemplatesApi->templates_update_parameters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_update_parameters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **report_parameters_vm** | [**ReportParametersVM**](ReportParametersVM.md)|  | 

### Return type

[**TemplateVM**](TemplateVM.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_update_permissions**
> templates_update_permissions(id, update_file_permissions_vm=update_file_permissions_vm)

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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | file id
    update_file_permissions_vm = fastreport_cloud_sdk.UpdateFilePermissionsVM() # UpdateFilePermissionsVM | new permissions VM (optional)

    try:
        # Update permissions
        api_instance.templates_update_permissions(id, update_file_permissions_vm=update_file_permissions_vm)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_update_permissions: %s\n" % e)
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

# **templates_update_tags**
> TemplateVM templates_update_tags(id, file_tags_update_vm=file_tags_update_vm)

Update tags

User with Update Tags permission can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.file_tags_update_vm import FileTagsUpdateVM
from fastreport_cloud_sdk.models.template_vm import TemplateVM
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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | 
    file_tags_update_vm = fastreport_cloud_sdk.FileTagsUpdateVM() # FileTagsUpdateVM |  (optional)

    try:
        # Update tags
        api_response = api_instance.templates_update_tags(id, file_tags_update_vm=file_tags_update_vm)
        print("The response of TemplatesApi->templates_update_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_update_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **file_tags_update_vm** | [**FileTagsUpdateVM**](FileTagsUpdateVM.md)|  | [optional] 

### Return type

[**TemplateVM**](TemplateVM.md)

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

# **templates_upload_file**
> TemplateVM templates_upload_file(id, template_create_vm=template_create_vm)

Upload a file to the specified folder. The method is deprecated, use the UploadFileV2 method instead!

User with Create Entity permission can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.template_create_vm import TemplateCreateVM
from fastreport_cloud_sdk.models.template_vm import TemplateVM
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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | folder id
    template_create_vm = fastreport_cloud_sdk.TemplateCreateVM() # TemplateCreateVM | new file's view model (optional)

    try:
        # Upload a file to the specified folder. The method is deprecated, use the UploadFileV2 method instead!
        api_response = api_instance.templates_upload_file(id, template_create_vm=template_create_vm)
        print("The response of TemplatesApi->templates_upload_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_upload_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| folder id | 
 **template_create_vm** | [**TemplateCreateVM**](TemplateCreateVM.md)| new file&#39;s view model | [optional] 

### Return type

[**TemplateVM**](TemplateVM.md)

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
**403** | You don&#39;t have permissions for the operation |  -  |
**402** | Subscription is outdated |  -  |
**404** | Folder or subscription was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_upload_file_v2**
> TemplateVM templates_upload_file_v2(id, file_content, tags=tags, icon=icon)

Alternative api for upload a file to the specified folder!

User with Create Entity permission can access this method.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.template_vm import TemplateVM
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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | Identifier of folder
    file_content = None # bytearray | 
    tags = ['tags_example'] # List[str] |  (optional)
    icon = None # bytearray |  (optional)

    try:
        # Alternative api for upload a file to the specified folder!
        api_response = api_instance.templates_upload_file_v2(id, file_content, tags=tags, icon=icon)
        print("The response of TemplatesApi->templates_upload_file_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_upload_file_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of folder | 
 **file_content** | **bytearray**|  | 
 **tags** | [**List[str]**](str.md)|  | [optional] 
 **icon** | **bytearray**|  | [optional] 

### Return type

[**TemplateVM**](TemplateVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File has been uploaded |  -  |
**400** | fileVM view model is not valid |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**402** | subscription is outdated |  -  |
**404** | folder/subscription is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_wasm_static_preview**
> ReportVM templates_wasm_static_preview(id, preview_template_vm=preview_template_vm)

Make preview for the report (template).  Generate a new or return exist prepared fpx file.  If template was changed will be returned a new.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.preview_template_vm import PreviewTemplateVM
from fastreport_cloud_sdk.models.report_vm import ReportVM
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
    api_instance = fastreport_cloud_sdk.TemplatesApi(api_client)
    id = 'id_example' # str | Template id
    preview_template_vm = fastreport_cloud_sdk.PreviewTemplateVM() # PreviewTemplateVM | Model with parameters (optional)

    try:
        # Make preview for the report (template).  Generate a new or return exist prepared fpx file.  If template was changed will be returned a new.
        api_response = api_instance.templates_wasm_static_preview(id, preview_template_vm=preview_template_vm)
        print("The response of TemplatesApi->templates_wasm_static_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_wasm_static_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **preview_template_vm** | [**PreviewTemplateVM**](PreviewTemplateVM.md)| Model with parameters | [optional] 

### Return type

[**ReportVM**](ReportVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Specified template has been prepared |  -  |
**204** | Specified template has been prepared |  -  |
**400** | Template Id is null |  -  |
**402** | Subscription is outdated |  -  |
**403** | You don&#39;t have permissions for the operation |  -  |
**404** | Template or folder not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

