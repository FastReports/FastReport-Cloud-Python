# fastreport_cloud_sdk.DataSourcesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_sources_count_data_sources_async**](DataSourcesApi.md#data_sources_count_data_sources_async) | **GET** /api/data/v1/DataSources/{subscriptionId}/count | Returns a number of data sources in subscription
[**data_sources_create_data_source**](DataSourcesApi.md#data_sources_create_data_source) | **POST** /api/data/v1/DataSources | Create new data source
[**data_sources_delete_data_source**](DataSourcesApi.md#data_sources_delete_data_source) | **DELETE** /api/data/v1/DataSources/{id} | Delete data source by id
[**data_sources_fetch_data**](DataSourcesApi.md#data_sources_fetch_data) | **GET** /api/data/v1/DataSources/{id}/fetch | This should connect to a database and set data structure
[**data_sources_get_available_data_sources**](DataSourcesApi.md#data_sources_get_available_data_sources) | **GET** /api/data/v1/DataSources | Returns all of the data sources, that current user have permission for in a subscription &lt;br /&gt;  The method will return minimal infomration about the datasources: &lt;br /&gt;  id, name, editedTime, status.
[**data_sources_get_data_source**](DataSourcesApi.md#data_sources_get_data_source) | **GET** /api/data/v1/DataSources/{id} | Get data source by id
[**data_sources_get_my_permissions**](DataSourcesApi.md#data_sources_get_my_permissions) | **GET** /api/data/v1/DataSources/{id}/mypermissions | Get current user&#39;s permissions to Data source
[**data_sources_get_parameter_types**](DataSourcesApi.md#data_sources_get_parameter_types) | **GET** /api/data/v1/DataSources/parameterTypes/{dataSourceType} | Get data source parameter DataType&#39;s
[**data_sources_get_permissions**](DataSourcesApi.md#data_sources_get_permissions) | **GET** /api/data/v1/DataSources/{id}/permissions | Get all Data source permissions
[**data_sources_rename_data_source**](DataSourcesApi.md#data_sources_rename_data_source) | **PUT** /api/data/v1/DataSources/{id}/rename | Rename data source by id
[**data_sources_update_connection_string**](DataSourcesApi.md#data_sources_update_connection_string) | **PUT** /api/data/v1/DataSources/{id}/connectionString | Update data source&#39;s connection string by id
[**data_sources_update_permissions**](DataSourcesApi.md#data_sources_update_permissions) | **POST** /api/data/v1/DataSources/{id}/permissions | Update permissions
[**data_sources_update_select_commands**](DataSourcesApi.md#data_sources_update_select_commands) | **PUT** /api/data/v1/DataSources/{id}/selectCommands | Update data source&#39;s select commands by id
[**data_sources_update_subscription_data_source**](DataSourcesApi.md#data_sources_update_subscription_data_source) | **PUT** /api/data/v1/DataSources/{id}/updateSubscription | Update data source&#39;s subscription


# **data_sources_count_data_sources_async**
> int data_sources_count_data_sources_async(subscription_id)

Returns a number of data sources in subscription

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
    api_instance = fastreport_cloud_sdk.DataSourcesApi(api_client)
    subscription_id = 'subscription_id_example' # str | subscripiton id

    try:
        # Returns a number of data sources in subscription
        api_response = api_instance.data_sources_count_data_sources_async(subscription_id)
        print("The response of DataSourcesApi->data_sources_count_data_sources_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSourcesApi->data_sources_count_data_sources_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| subscripiton id | 

### Return type

**int**

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Everything is all right |  -  |
**400** | id is not hex24 |  -  |
**402** | Subscription is outdated |  -  |
**403** | You don&#39;t have permission to get data sources from this subscription (or in your default (1st) subscription) |  -  |
**404** | there is no subscription with provided id found, or user don&#39;t even have a subscription |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_sources_create_data_source**
> DataSourceVM data_sources_create_data_source(create_data_source_vm=create_data_source_vm)

Create new data source

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.create_data_source_vm import CreateDataSourceVM
from fastreport_cloud_sdk.models.data_source_vm import DataSourceVM
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
    api_instance = fastreport_cloud_sdk.DataSourcesApi(api_client)
    create_data_source_vm = fastreport_cloud_sdk.CreateDataSourceVM() # CreateDataSourceVM | create viewmodel (optional)

    try:
        # Create new data source
        api_response = api_instance.data_sources_create_data_source(create_data_source_vm=create_data_source_vm)
        print("The response of DataSourcesApi->data_sources_create_data_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSourcesApi->data_sources_create_data_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_data_source_vm** | [**CreateDataSourceVM**](CreateDataSourceVM.md)| create viewmodel | [optional] 

### Return type

[**DataSourceVM**](DataSourceVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Everything is all right |  -  |
**400** | VM is not valid |  -  |
**402** | Subscription is outdated or have not enough limits |  -  |
**403** | You don&#39;t have permission to create data sources from this subscription (or in your default (1st) subscription) |  -  |
**404** | There is no subscription with provided id found, or user don&#39;t even have a subscription |  -  |
**500** | Try again, if error still here - text our support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_sources_delete_data_source**
> data_sources_delete_data_source(id)

Delete data source by id

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
    api_instance = fastreport_cloud_sdk.DataSourcesApi(api_client)
    id = 'id_example' # str | data source id

    try:
        # Delete data source by id
        api_instance.data_sources_delete_data_source(id)
    except Exception as e:
        print("Exception when calling DataSourcesApi->data_sources_delete_data_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| data source id | 

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
**204** | Everything is all right |  -  |
**400** | id is not hex24 |  -  |
**402** | Subscription is outdated or have not enough limits |  -  |
**403** | You don&#39;t have permission to delete data sources from this subscription (or in your default (1st) subscription) |  -  |
**404** | There is no data source or subscription with provided id found |  -  |
**500** | Try again, if error still here - text our support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_sources_fetch_data**
> data_sources_fetch_data(id)

This should connect to a database and set data structure

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
    api_instance = fastreport_cloud_sdk.DataSourcesApi(api_client)
    id = 'id_example' # str | datasource's id

    try:
        # This should connect to a database and set data structure
        api_instance.data_sources_fetch_data(id)
    except Exception as e:
        print("Exception when calling DataSourcesApi->data_sources_fetch_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| datasource&#39;s id | 

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
**204** | Everything is all right |  -  |
**400** | id is not hex24 |  -  |
**402** | Subscription is outdated or have not enough limits |  -  |
**403** | You don&#39;t have permission to fetch data sources from this subscription (or in your default (1st) subscription) |  -  |
**404** | There is no data source or subscription with provided id found |  -  |
**500** | Try again, if error still here - text our support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_sources_get_available_data_sources**
> DataSourcesVM data_sources_get_available_data_sources(subscription_id=subscription_id, skip=skip, take=take, order_by=order_by, desc=desc)

Returns all of the data sources, that current user have permission for in a subscription <br />  The method will return minimal infomration about the datasources: <br />  id, name, editedTime, status.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.data_source_sorting import DataSourceSorting
from fastreport_cloud_sdk.models.data_sources_vm import DataSourcesVM
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
    api_instance = fastreport_cloud_sdk.DataSourcesApi(api_client)
    subscription_id = 'subscription_id_example' # str | id of subscription where the datasources are located (optional)
    skip = 0 # int | how many data sources will be skipped (optional) (default to 0)
    take = 10 # int | how many data sources will be taken (optional) (default to 10)
    order_by = fastreport_cloud_sdk.DataSourceSorting() # DataSourceSorting | field to order by (optional)
    desc = False # bool | descending sort (optional) (default to False)

    try:
        # Returns all of the data sources, that current user have permission for in a subscription <br />  The method will return minimal infomration about the datasources: <br />  id, name, editedTime, status.
        api_response = api_instance.data_sources_get_available_data_sources(subscription_id=subscription_id, skip=skip, take=take, order_by=order_by, desc=desc)
        print("The response of DataSourcesApi->data_sources_get_available_data_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSourcesApi->data_sources_get_available_data_sources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| id of subscription where the datasources are located | [optional] 
 **skip** | **int**| how many data sources will be skipped | [optional] [default to 0]
 **take** | **int**| how many data sources will be taken | [optional] [default to 10]
 **order_by** | [**DataSourceSorting**](.md)| field to order by | [optional] 
 **desc** | **bool**| descending sort | [optional] [default to False]

### Return type

[**DataSourcesVM**](DataSourcesVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Everything is all right |  -  |
**400** | One of params is not valid |  -  |
**402** | Subscription is outdated or have not enough limits |  -  |
**403** | You don&#39;t have permission to get data sources from this subscription (or in your default (1st) subscription) |  -  |
**404** | There is no subscription with provided id found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_sources_get_data_source**
> DataSourceVM data_sources_get_data_source(id)

Get data source by id

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.data_source_vm import DataSourceVM
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
    api_instance = fastreport_cloud_sdk.DataSourcesApi(api_client)
    id = 'id_example' # str | data source id

    try:
        # Get data source by id
        api_response = api_instance.data_sources_get_data_source(id)
        print("The response of DataSourcesApi->data_sources_get_data_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSourcesApi->data_sources_get_data_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| data source id | 

### Return type

[**DataSourceVM**](DataSourceVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Everything is all right |  -  |
**400** | id is not hex24 |  -  |
**402** | Subscription is outdated or have not enough limits |  -  |
**403** | You don&#39;t have permission to get data sources from this subscription (or in your default (1st) subscription) |  -  |
**404** | There is no data source or subscription with provided id found |  -  |
**500** | Try again, if error still here - text our support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_sources_get_my_permissions**
> DataSourcePermissionCRUDVM data_sources_get_my_permissions(id)

Get current user's permissions to Data source

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.data_source_permission_crudvm import DataSourcePermissionCRUDVM
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
    api_instance = fastreport_cloud_sdk.DataSourcesApi(api_client)
    id = 'id_example' # str | data source id

    try:
        # Get current user's permissions to Data source
        api_response = api_instance.data_sources_get_my_permissions(id)
        print("The response of DataSourcesApi->data_sources_get_my_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSourcesApi->data_sources_get_my_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| data source id | 

### Return type

[**DataSourcePermissionCRUDVM**](DataSourcePermissionCRUDVM.md)

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
**404** | There is no data source or subscription with provided id found |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_sources_get_parameter_types**
> DataSourceParameterTypesVM data_sources_get_parameter_types(data_source_type)

Get data source parameter DataType's

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.data_source_connection_type import DataSourceConnectionType
from fastreport_cloud_sdk.models.data_source_parameter_types_vm import DataSourceParameterTypesVM
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
    api_instance = fastreport_cloud_sdk.DataSourcesApi(api_client)
    data_source_type = fastreport_cloud_sdk.DataSourceConnectionType() # DataSourceConnectionType | data source type (MsSql, MySql, etc.)

    try:
        # Get data source parameter DataType's
        api_response = api_instance.data_sources_get_parameter_types(data_source_type)
        print("The response of DataSourcesApi->data_sources_get_parameter_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSourcesApi->data_sources_get_parameter_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_source_type** | [**DataSourceConnectionType**](.md)| data source type (MsSql, MySql, etc.) | 

### Return type

[**DataSourceParameterTypesVM**](DataSourceParameterTypesVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Everything is all right |  -  |
**400** | Data source doesn&#39;t support parameters or wrong data source name |  -  |
**500** | Try again, if error still here - text our support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_sources_get_permissions**
> DataSourcePermissionsVM data_sources_get_permissions(id)

Get all Data source permissions

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.data_source_permissions_vm import DataSourcePermissionsVM
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
    api_instance = fastreport_cloud_sdk.DataSourcesApi(api_client)
    id = 'id_example' # str | data source id

    try:
        # Get all Data source permissions
        api_response = api_instance.data_sources_get_permissions(id)
        print("The response of DataSourcesApi->data_sources_get_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSourcesApi->data_sources_get_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| data source id | 

### Return type

[**DataSourcePermissionsVM**](DataSourcePermissionsVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Everything is all right |  -  |
**400** | id is not hex24 |  -  |
**402** | Subscription is outdated or have not enough limits |  -  |
**403** | You don&#39;t have permission to get data sources&#39; permissions from this subscription (or in your default (1st) subscription) |  -  |
**404** | There is no data source or subscription with provided id found |  -  |
**500** | Try again, if error still here - text our support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_sources_rename_data_source**
> DataSourceVM data_sources_rename_data_source(id, rename_data_source_vm=rename_data_source_vm)

Rename data source by id

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.data_source_vm import DataSourceVM
from fastreport_cloud_sdk.models.rename_data_source_vm import RenameDataSourceVM
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
    api_instance = fastreport_cloud_sdk.DataSourcesApi(api_client)
    id = 'id_example' # str | data source id
    rename_data_source_vm = fastreport_cloud_sdk.RenameDataSourceVM() # RenameDataSourceVM | rename viewmodel (optional)

    try:
        # Rename data source by id
        api_response = api_instance.data_sources_rename_data_source(id, rename_data_source_vm=rename_data_source_vm)
        print("The response of DataSourcesApi->data_sources_rename_data_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSourcesApi->data_sources_rename_data_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| data source id | 
 **rename_data_source_vm** | [**RenameDataSourceVM**](RenameDataSourceVM.md)| rename viewmodel | [optional] 

### Return type

[**DataSourceVM**](DataSourceVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Everything is all right |  -  |
**400** | id is not hex24 or VM is not valid |  -  |
**402** | Subscription is outdated or have not enough limits |  -  |
**403** | You don&#39;t have permission to update data sources&#39; name from this subscription (or in your default (1st) subscription) |  -  |
**404** | There is no data source or subscription with provided id found |  -  |
**500** | Try again, if error still here - text our support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_sources_update_connection_string**
> DataSourceVM data_sources_update_connection_string(id, update_data_source_connection_string_vm=update_data_source_connection_string_vm)

Update data source's connection string by id

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.data_source_vm import DataSourceVM
from fastreport_cloud_sdk.models.update_data_source_connection_string_vm import UpdateDataSourceConnectionStringVM
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
    api_instance = fastreport_cloud_sdk.DataSourcesApi(api_client)
    id = 'id_example' # str | data source id
    update_data_source_connection_string_vm = fastreport_cloud_sdk.UpdateDataSourceConnectionStringVM() # UpdateDataSourceConnectionStringVM | update viewmodel (optional)

    try:
        # Update data source's connection string by id
        api_response = api_instance.data_sources_update_connection_string(id, update_data_source_connection_string_vm=update_data_source_connection_string_vm)
        print("The response of DataSourcesApi->data_sources_update_connection_string:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSourcesApi->data_sources_update_connection_string: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| data source id | 
 **update_data_source_connection_string_vm** | [**UpdateDataSourceConnectionStringVM**](UpdateDataSourceConnectionStringVM.md)| update viewmodel | [optional] 

### Return type

[**DataSourceVM**](DataSourceVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Everything is all right |  -  |
**400** | id is not hex24 or VM is not valid |  -  |
**402** | Subscription is outdated or have not enough limits |  -  |
**403** | You don&#39;t have permission to update data sources&#39; connection string from this subscription (or in your default (1st) subscription) |  -  |
**404** | There is no data source or subscription with provided id found |  -  |
**500** | Try again, if error still here - text our support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_sources_update_permissions**
> data_sources_update_permissions(id, update_data_source_permissions_vm=update_data_source_permissions_vm)

Update permissions

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.update_data_source_permissions_vm import UpdateDataSourcePermissionsVM
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
    api_instance = fastreport_cloud_sdk.DataSourcesApi(api_client)
    id = 'id_example' # str | 
    update_data_source_permissions_vm = fastreport_cloud_sdk.UpdateDataSourcePermissionsVM() # UpdateDataSourcePermissionsVM |  (optional)

    try:
        # Update permissions
        api_instance.data_sources_update_permissions(id, update_data_source_permissions_vm=update_data_source_permissions_vm)
    except Exception as e:
        print("Exception when calling DataSourcesApi->data_sources_update_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_data_source_permissions_vm** | [**UpdateDataSourcePermissionsVM**](UpdateDataSourcePermissionsVM.md)|  | [optional] 

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
**204** | Everything is all right |  -  |
**400** | id is not hex24 or VM is not valid |  -  |
**402** | Subscription is outdated or have not enough limits |  -  |
**403** | You don&#39;t have permission to update data sources&#39; permissions from this subscription (or in your default (1st) subscription) |  -  |
**404** | There is no data source or subscription with provided id found |  -  |
**500** | Try again, if error still here - text our support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_sources_update_select_commands**
> DataSourceVM data_sources_update_select_commands(id, update_data_source_select_commands_vm=update_data_source_select_commands_vm)

Update data source's select commands by id

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.data_source_vm import DataSourceVM
from fastreport_cloud_sdk.models.update_data_source_select_commands_vm import UpdateDataSourceSelectCommandsVM
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
    api_instance = fastreport_cloud_sdk.DataSourcesApi(api_client)
    id = 'id_example' # str | data source id
    update_data_source_select_commands_vm = fastreport_cloud_sdk.UpdateDataSourceSelectCommandsVM() # UpdateDataSourceSelectCommandsVM | update viewmodel (optional)

    try:
        # Update data source's select commands by id
        api_response = api_instance.data_sources_update_select_commands(id, update_data_source_select_commands_vm=update_data_source_select_commands_vm)
        print("The response of DataSourcesApi->data_sources_update_select_commands:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSourcesApi->data_sources_update_select_commands: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| data source id | 
 **update_data_source_select_commands_vm** | [**UpdateDataSourceSelectCommandsVM**](UpdateDataSourceSelectCommandsVM.md)| update viewmodel | [optional] 

### Return type

[**DataSourceVM**](DataSourceVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Everything is all right |  -  |
**400** | id is not hex24 or VM is not valid |  -  |
**402** | Subscription is outdated or have not enough limits |  -  |
**403** | You don&#39;t have permission to update data sources&#39; connection string from this subscription (or in your default (1st) subscription) |  -  |
**404** | There is no data source or subscription with provided id found |  -  |
**500** | Try again, if error still here - text our support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_sources_update_subscription_data_source**
> data_sources_update_subscription_data_source(id, update_data_source_subscription_vm=update_data_source_subscription_vm)

Update data source's subscription

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.update_data_source_subscription_vm import UpdateDataSourceSubscriptionVM
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
    api_instance = fastreport_cloud_sdk.DataSourcesApi(api_client)
    id = 'id_example' # str | data source id
    update_data_source_subscription_vm = fastreport_cloud_sdk.UpdateDataSourceSubscriptionVM() # UpdateDataSourceSubscriptionVM | update subscription viewmodel (optional)

    try:
        # Update data source's subscription
        api_instance.data_sources_update_subscription_data_source(id, update_data_source_subscription_vm=update_data_source_subscription_vm)
    except Exception as e:
        print("Exception when calling DataSourcesApi->data_sources_update_subscription_data_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| data source id | 
 **update_data_source_subscription_vm** | [**UpdateDataSourceSubscriptionVM**](UpdateDataSourceSubscriptionVM.md)| update subscription viewmodel | [optional] 

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
**200** | Everything is all right |  -  |
**400** | id is not hex24 or VM is not valid |  -  |
**402** | Subscription is outdated or have not enough limits |  -  |
**403** | You don&#39;t have permission to get data sources or create them in new subscription |  -  |
**404** | There is no data source or subscription with provided id found |  -  |
**500** | Try again, if error still here - text our support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

