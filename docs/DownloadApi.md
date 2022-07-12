# fastreport_cloud_sdk.DownloadApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_get_export**](DownloadApi.md#download_get_export) | **GET** /download/e/{id} | Returns a export file with specified id
[**download_get_export_thumbnail**](DownloadApi.md#download_get_export_thumbnail) | **GET** /download/e/{id}/thumbnail | Returns export&#39;s thumbnail
[**download_get_exports**](DownloadApi.md#download_get_exports) | **GET** /download/es/{archiveName} | Returns a zip archive with selected ids
[**download_get_report**](DownloadApi.md#download_get_report) | **GET** /download/r/{id} | Returns a prepared file with specified id
[**download_get_report_thumbnail**](DownloadApi.md#download_get_report_thumbnail) | **GET** /download/r/{id}/thumbnail | Returns report&#39;s thumbnail
[**download_get_reports**](DownloadApi.md#download_get_reports) | **GET** /download/rs/{archiveName} | Returns a zip archive with selected files
[**download_get_template**](DownloadApi.md#download_get_template) | **GET** /download/t/{id} | Returns a Template file with specified id
[**download_get_template_thumbnail**](DownloadApi.md#download_get_template_thumbnail) | **GET** /download/t/{id}/thumbnail | Returns template&#39;s thumbnail
[**download_get_templates**](DownloadApi.md#download_get_templates) | **GET** /download/ts/{archiveName} | Returns a zip archive with selected files


# **download_get_export**
> file download_get_export(id, preview=preview)

Returns a export file with specified id

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
    api_instance = fastreport_cloud_sdk.DownloadApi(api_client)
    id = 'id_example' # str | 
preview = False # bool |  (optional) (default to False)

    try:
        # Returns a export file with specified id
        api_response = api_instance.download_get_export(id, preview=preview)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DownloadApi->download_get_export: %s\n" % e)
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
    api_instance = fastreport_cloud_sdk.DownloadApi(api_client)
    id = 'id_example' # str | 
preview = False # bool |  (optional) (default to False)

    try:
        # Returns a export file with specified id
        api_response = api_instance.download_get_export(id, preview=preview)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DownloadApi->download_get_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **preview** | **bool**|  | [optional] [default to False]

### Return type

**file**

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, application/octet-stream, application/pdf

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Specified file was found |  -  |
**404** | Specified file was not found or user do not has access to the file |  -  |
**400** | Bad id provided |  -  |
**402** | Subscription is blocked |  -  |
**403** | Not enough permissions for the operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_get_export_thumbnail**
> file download_get_export_thumbnail(id)

Returns export's thumbnail

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
    api_instance = fastreport_cloud_sdk.DownloadApi(api_client)
    id = 'id_example' # str | 

    try:
        # Returns export's thumbnail
        api_response = api_instance.download_get_export_thumbnail(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DownloadApi->download_get_export_thumbnail: %s\n" % e)
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
    api_instance = fastreport_cloud_sdk.DownloadApi(api_client)
    id = 'id_example' # str | 

    try:
        # Returns export's thumbnail
        api_response = api_instance.download_get_export_thumbnail(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DownloadApi->download_get_export_thumbnail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**file**

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, image/png, image/jpeg

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Specified thumbnail was found |  -  |
**404** | Specified thumbnail was not found or user do not has access to it |  -  |
**400** | Bad id provided |  -  |
**402** | Subscription is blocked |  -  |
**403** | Not enough permissions for the operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_get_exports**
> file download_get_exports(archive_name, ids=ids)

Returns a zip archive with selected ids

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
    api_instance = fastreport_cloud_sdk.DownloadApi(api_client)
    archive_name = 'archive_name_example' # str | name of the created archive
ids = 'ids_example' # str | ids separated with a ',' sign (optional)

    try:
        # Returns a zip archive with selected ids
        api_response = api_instance.download_get_exports(archive_name, ids=ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DownloadApi->download_get_exports: %s\n" % e)
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
    api_instance = fastreport_cloud_sdk.DownloadApi(api_client)
    archive_name = 'archive_name_example' # str | name of the created archive
ids = 'ids_example' # str | ids separated with a ',' sign (optional)

    try:
        # Returns a zip archive with selected ids
        api_response = api_instance.download_get_exports(archive_name, ids=ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DownloadApi->download_get_exports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **archive_name** | **str**| name of the created archive | 
 **ids** | **str**| ids separated with a &#39;,&#39; sign | [optional] 

### Return type

**file**

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, application/zip

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Specified file was found |  -  |
**400** | Bad id provided |  -  |
**402** | Subscription is blocked |  -  |
**403** | Not enough permissions for the operation |  -  |
**404** | Specified file was not found or user do not has access to the file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_get_report**
> file download_get_report(id)

Returns a prepared file with specified id

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
    api_instance = fastreport_cloud_sdk.DownloadApi(api_client)
    id = 'id_example' # str | 

    try:
        # Returns a prepared file with specified id
        api_response = api_instance.download_get_report(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DownloadApi->download_get_report: %s\n" % e)
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
    api_instance = fastreport_cloud_sdk.DownloadApi(api_client)
    id = 'id_example' # str | 

    try:
        # Returns a prepared file with specified id
        api_response = api_instance.download_get_report(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DownloadApi->download_get_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**file**

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Specified file was found |  -  |
**404** | Specified file was not found or user do not has access to the file |  -  |
**400** | bad id provided |  -  |
**402** | Subscription is blocked |  -  |
**403** | Not enough permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_get_report_thumbnail**
> file download_get_report_thumbnail(id)

Returns report's thumbnail

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
    api_instance = fastreport_cloud_sdk.DownloadApi(api_client)
    id = 'id_example' # str | 

    try:
        # Returns report's thumbnail
        api_response = api_instance.download_get_report_thumbnail(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DownloadApi->download_get_report_thumbnail: %s\n" % e)
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
    api_instance = fastreport_cloud_sdk.DownloadApi(api_client)
    id = 'id_example' # str | 

    try:
        # Returns report's thumbnail
        api_response = api_instance.download_get_report_thumbnail(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DownloadApi->download_get_report_thumbnail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**file**

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, image/png, image/jpeg

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Specified thumbnail was found |  -  |
**404** | Specified thumbnail was not found or user do not has access to it |  -  |
**400** | Bad id provided |  -  |
**402** | Subscription is blocked |  -  |
**403** | Not enough permissions for the operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_get_reports**
> file download_get_reports(archive_name, ids=ids)

Returns a zip archive with selected files

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
    api_instance = fastreport_cloud_sdk.DownloadApi(api_client)
    archive_name = 'archive_name_example' # str | name of the created archive
ids = 'ids_example' # str | ids separated with a ',' sign (optional)

    try:
        # Returns a zip archive with selected files
        api_response = api_instance.download_get_reports(archive_name, ids=ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DownloadApi->download_get_reports: %s\n" % e)
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
    api_instance = fastreport_cloud_sdk.DownloadApi(api_client)
    archive_name = 'archive_name_example' # str | name of the created archive
ids = 'ids_example' # str | ids separated with a ',' sign (optional)

    try:
        # Returns a zip archive with selected files
        api_response = api_instance.download_get_reports(archive_name, ids=ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DownloadApi->download_get_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **archive_name** | **str**| name of the created archive | 
 **ids** | **str**| ids separated with a &#39;,&#39; sign | [optional] 

### Return type

**file**

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, application/zip

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File has been downloaded |  -  |
**404** | files is not found |  -  |
**400** | wrong parameters provided |  -  |
**402** | Subscription is blocked |  -  |
**403** | You don&#39;t have rights for the operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_get_template**
> file download_get_template(id)

Returns a Template file with specified id

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
    api_instance = fastreport_cloud_sdk.DownloadApi(api_client)
    id = 'id_example' # str | template id

    try:
        # Returns a Template file with specified id
        api_response = api_instance.download_get_template(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DownloadApi->download_get_template: %s\n" % e)
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
    api_instance = fastreport_cloud_sdk.DownloadApi(api_client)
    id = 'id_example' # str | template id

    try:
        # Returns a Template file with specified id
        api_response = api_instance.download_get_template(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DownloadApi->download_get_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| template id | 

### Return type

**file**

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Specified file was found |  -  |
**404** | Specified file was not found or user do not has access to the file |  -  |
**400** | bad id provided |  -  |
**402** | Subscription is blocked |  -  |
**403** | Not enough permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_get_template_thumbnail**
> file download_get_template_thumbnail(id)

Returns template's thumbnail

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
    api_instance = fastreport_cloud_sdk.DownloadApi(api_client)
    id = 'id_example' # str | 

    try:
        # Returns template's thumbnail
        api_response = api_instance.download_get_template_thumbnail(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DownloadApi->download_get_template_thumbnail: %s\n" % e)
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
    api_instance = fastreport_cloud_sdk.DownloadApi(api_client)
    id = 'id_example' # str | 

    try:
        # Returns template's thumbnail
        api_response = api_instance.download_get_template_thumbnail(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DownloadApi->download_get_template_thumbnail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**file**

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, image/png, image/jpeg

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Specified thumbnail was found |  -  |
**404** | Specified thumbnail was not found or user do not has access to it |  -  |
**400** | Bad id provided |  -  |
**402** | Subscription is blocked |  -  |
**403** | Not enough permissions for the operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_get_templates**
> file download_get_templates(archive_name, ids=ids)

Returns a zip archive with selected files

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
    api_instance = fastreport_cloud_sdk.DownloadApi(api_client)
    archive_name = 'archive_name_example' # str | name of the created archive
ids = 'ids_example' # str | ids separated with a ',' sign (optional)

    try:
        # Returns a zip archive with selected files
        api_response = api_instance.download_get_templates(archive_name, ids=ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DownloadApi->download_get_templates: %s\n" % e)
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
    api_instance = fastreport_cloud_sdk.DownloadApi(api_client)
    archive_name = 'archive_name_example' # str | name of the created archive
ids = 'ids_example' # str | ids separated with a ',' sign (optional)

    try:
        # Returns a zip archive with selected files
        api_response = api_instance.download_get_templates(archive_name, ids=ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DownloadApi->download_get_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **archive_name** | **str**| name of the created archive | 
 **ids** | **str**| ids separated with a &#39;,&#39; sign | [optional] 

### Return type

**file**

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, application/zip

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File has been downloaded |  -  |
**400** | wrong parameters provided |  -  |
**402** | Subscription is blocked |  -  |
**403** | You don&#39;t have rights for the operation |  -  |
**404** | files is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

