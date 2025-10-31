# fastreport_cloud_sdk.FontsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fonts_add_public_font**](FontsApi.md#fonts_add_public_font) | **POST** /api/v1/fonts/add | Allows user to add a font from a list of public fonts to their subscription
[**fonts_count_fonts_async**](FontsApi.md#fonts_count_fonts_async) | **GET** /api/v1/fonts/count | Returns a number of fonts in a subscription
[**fonts_count_occupied_space**](FontsApi.md#fonts_count_occupied_space) | **GET** /api/v1/fonts/counttotalsizebysubscription | returns storage space occupied by fonts in the subscription
[**fonts_count_public_fonts_async**](FontsApi.md#fonts_count_public_fonts_async) | **GET** /api/v1/fonts/public/count | Returns a number of pulbic fonts
[**fonts_delete_font**](FontsApi.md#fonts_delete_font) | **DELETE** /api/v1/fonts/{id} | deletes a font from the subscirption by id
[**fonts_download_font**](FontsApi.md#fonts_download_font) | **GET** /api/v1/fonts/{id}/download | Downloads font by it&#39;s id
[**fonts_download_public_font**](FontsApi.md#fonts_download_public_font) | **GET** /api/v1/fonts/public/{id}/download | Downloads a public font by it&#39;s id
[**fonts_get_font_families**](FontsApi.md#fonts_get_font_families) | **GET** /api/v1/fonts/families | Returns distinct font names from public and private font lists (excluding disabled fonts)
[**fonts_get_fonts**](FontsApi.md#fonts_get_fonts) | **GET** /api/v1/fonts/list | returns a list of fonts in the subscription
[**fonts_get_fonts_by_report**](FontsApi.md#fonts_get_fonts_by_report) | **GET** /api/v1/fonts/ListByReport/{reportId} | Returns a list of fonts in the subscription by report id.
[**fonts_get_fonts_by_template**](FontsApi.md#fonts_get_fonts_by_template) | **GET** /api/v1/fonts/ListByTemplate/{templateId} | Returns a list of fonts in the subscription by report id.
[**fonts_get_fonts_css**](FontsApi.md#fonts_get_fonts_css) | **GET** /api/v1/fonts/css | Creates a css stylesheet for a public font
[**fonts_get_fonts_css_by_report**](FontsApi.md#fonts_get_fonts_css_by_report) | **GET** /api/v1/fonts/CssByReport/{reportId} | Creates a css stylesheet for a public fonts by report.
[**fonts_get_fonts_css_by_template**](FontsApi.md#fonts_get_fonts_css_by_template) | **GET** /api/v1/fonts/CssByTemplate/{templateId} | Creates a css stylesheet for a public font by template.
[**fonts_get_my_permissions**](FontsApi.md#fonts_get_my_permissions) | **GET** /api/v1/fonts/{id}/mypermissions | Get current user&#39;s permissions to a font
[**fonts_get_permissions**](FontsApi.md#fonts_get_permissions) | **GET** /api/v1/fonts/{id}/permissions | Get font&#39;s permissions
[**fonts_get_public_fonts**](FontsApi.md#fonts_get_public_fonts) | **GET** /api/v1/fonts/public/list | Returns a list of public fonts
[**fonts_get_public_fonts_css**](FontsApi.md#fonts_get_public_fonts_css) | **GET** /api/v1/fonts/public/css | Creates a css stylesheet for a public font
[**fonts_update_font**](FontsApi.md#fonts_update_font) | **PUT** /api/v1/fonts/{id} | updates a user font model
[**fonts_update_permissions**](FontsApi.md#fonts_update_permissions) | **PUT** /api/v1/fonts/{id}/permissions | Update permissions
[**fonts_upload_font**](FontsApi.md#fonts_upload_font) | **POST** /api/v1/fonts/upload | Allows user to upload a new truetype font to their subscription


# **fonts_add_public_font**
> UserFontVM fonts_add_public_font(add_public_font_vm=add_public_font_vm)

Allows user to add a font from a list of public fonts to their subscription

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.add_public_font_vm import AddPublicFontVM
from fastreport_cloud_sdk.models.user_font_vm import UserFontVM
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
    api_instance = fastreport_cloud_sdk.FontsApi(api_client)
    add_public_font_vm = fastreport_cloud_sdk.AddPublicFontVM() # AddPublicFontVM | a body with font id and workspace id (optional)

    try:
        # Allows user to add a font from a list of public fonts to their subscription
        api_response = api_instance.fonts_add_public_font(add_public_font_vm=add_public_font_vm)
        print("The response of FontsApi->fonts_add_public_font:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FontsApi->fonts_add_public_font: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_public_font_vm** | [**AddPublicFontVM**](AddPublicFontVM.md)| a body with font id and workspace id | [optional] 

### Return type

[**UserFontVM**](UserFontVM.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fonts_count_fonts_async**
> CountVM fonts_count_fonts_async(subscription_id=subscription_id)

Returns a number of fonts in a subscription

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
    api_instance = fastreport_cloud_sdk.FontsApi(api_client)
    subscription_id = 'subscription_id_example' # str | subscripiton id (optional)

    try:
        # Returns a number of fonts in a subscription
        api_response = api_instance.fonts_count_fonts_async(subscription_id=subscription_id)
        print("The response of FontsApi->fonts_count_fonts_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FontsApi->fonts_count_fonts_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| subscripiton id | [optional] 

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
**200** | Everything is all right |  -  |
**400** | id is not hex24 |  -  |
**402** | Subscription is outdated |  -  |
**403** | You don&#39;t have permission to get fonts from this subscription (or in your default (1st) subscription) |  -  |
**404** | there is no subscription with provided id found, or user don&#39;t even have a subscription |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fonts_count_occupied_space**
> FontSizeVM fonts_count_occupied_space(subscription_id=subscription_id)

returns storage space occupied by fonts in the subscription

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.font_size_vm import FontSizeVM
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
    api_instance = fastreport_cloud_sdk.FontsApi(api_client)
    subscription_id = 'subscription_id_example' # str | subscription id (optional)

    try:
        # returns storage space occupied by fonts in the subscription
        api_response = api_instance.fonts_count_occupied_space(subscription_id=subscription_id)
        print("The response of FontsApi->fonts_count_occupied_space:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FontsApi->fonts_count_occupied_space: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| subscription id | [optional] 

### Return type

[**FontSizeVM**](FontSizeVM.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fonts_count_public_fonts_async**
> CountVM fonts_count_public_fonts_async()

Returns a number of pulbic fonts

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
    api_instance = fastreport_cloud_sdk.FontsApi(api_client)

    try:
        # Returns a number of pulbic fonts
        api_response = api_instance.fonts_count_public_fonts_async()
        print("The response of FontsApi->fonts_count_public_fonts_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FontsApi->fonts_count_public_fonts_async: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | Everything is all right |  -  |
**402** | Subscription is outdated |  -  |
**403** | You don&#39;t have permission to get fonts from this subscription (or in your default (1st) subscription) |  -  |
**404** | there is no subscription with provided id found, or user don&#39;t even have a subscription |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fonts_delete_font**
> fonts_delete_font(id)

deletes a font from the subscirption by id

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
    api_instance = fastreport_cloud_sdk.FontsApi(api_client)
    id = 'id_example' # str | font id

    try:
        # deletes a font from the subscirption by id
        api_instance.fonts_delete_font(id)
    except Exception as e:
        print("Exception when calling FontsApi->fonts_delete_font: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| font id | 

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
**400** | Bad Request |  -  |
**402** | Client Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fonts_download_font**
> bytearray fonts_download_font(id)

Downloads font by it's id

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
    api_instance = fastreport_cloud_sdk.FontsApi(api_client)
    id = 'id_example' # str | id of the font

    try:
        # Downloads font by it's id
        api_response = api_instance.fonts_download_font(id)
        print("The response of FontsApi->fonts_download_font:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FontsApi->fonts_download_font: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of the font | 

### Return type

**bytearray**

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |
**402** | Client Error |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fonts_download_public_font**
> bytearray fonts_download_public_font(id)

Downloads a public font by it's id

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
    api_instance = fastreport_cloud_sdk.FontsApi(api_client)
    id = 'id_example' # str | id of the font

    try:
        # Downloads a public font by it's id
        api_response = api_instance.fonts_download_public_font(id)
        print("The response of FontsApi->fonts_download_public_font:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FontsApi->fonts_download_public_font: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of the font | 

### Return type

**bytearray**

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fonts_get_font_families**
> FontNamesVM fonts_get_font_families(subscription_id=subscription_id, skip=skip, take=take)

Returns distinct font names from public and private font lists (excluding disabled fonts)

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.font_names_vm import FontNamesVM
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
    api_instance = fastreport_cloud_sdk.FontsApi(api_client)
    subscription_id = 'subscription_id_example' # str | id of a subscription, to pull the font names from. If null or the subscription has no fonts, only the public fonts will be returned (optional)
    skip = 0 # int | how many names to skip (optional) (default to 0)
    take = 10 # int | how many namrs to take (optional) (default to 10)

    try:
        # Returns distinct font names from public and private font lists (excluding disabled fonts)
        api_response = api_instance.fonts_get_font_families(subscription_id=subscription_id, skip=skip, take=take)
        print("The response of FontsApi->fonts_get_font_families:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FontsApi->fonts_get_font_families: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| id of a subscription, to pull the font names from. If null or the subscription has no fonts, only the public fonts will be returned | [optional] 
 **skip** | **int**| how many names to skip | [optional] [default to 0]
 **take** | **int**| how many namrs to take | [optional] [default to 10]

### Return type

[**FontNamesVM**](FontNamesVM.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fonts_get_fonts**
> UserFontsVM fonts_get_fonts(subscription_id=subscription_id, skip=skip, take=take)

returns a list of fonts in the subscription

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.user_fonts_vm import UserFontsVM
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
    api_instance = fastreport_cloud_sdk.FontsApi(api_client)
    subscription_id = 'subscription_id_example' # str | id of a subscription, to pull the fonts from. If null, only the public fonts will be returned (optional)
    skip = 0 # int | how many fonts to skip (optional) (default to 0)
    take = 10 # int | how many fonts to take (optional) (default to 10)

    try:
        # returns a list of fonts in the subscription
        api_response = api_instance.fonts_get_fonts(subscription_id=subscription_id, skip=skip, take=take)
        print("The response of FontsApi->fonts_get_fonts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FontsApi->fonts_get_fonts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| id of a subscription, to pull the fonts from. If null, only the public fonts will be returned | [optional] 
 **skip** | **int**| how many fonts to skip | [optional] [default to 0]
 **take** | **int**| how many fonts to take | [optional] [default to 10]

### Return type

[**UserFontsVM**](UserFontsVM.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fonts_get_fonts_by_report**
> UserFontsVM fonts_get_fonts_by_report(report_id, skip=skip, take=take)

Returns a list of fonts in the subscription by report id.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.user_fonts_vm import UserFontsVM
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
    api_instance = fastreport_cloud_sdk.FontsApi(api_client)
    report_id = 'report_id_example' # str | id of a report
    skip = 0 # int | how many fonts to skip (optional) (default to 0)
    take = 10 # int | how many fonts to take (optional) (default to 10)

    try:
        # Returns a list of fonts in the subscription by report id.
        api_response = api_instance.fonts_get_fonts_by_report(report_id, skip=skip, take=take)
        print("The response of FontsApi->fonts_get_fonts_by_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FontsApi->fonts_get_fonts_by_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| id of a report | 
 **skip** | **int**| how many fonts to skip | [optional] [default to 0]
 **take** | **int**| how many fonts to take | [optional] [default to 10]

### Return type

[**UserFontsVM**](UserFontsVM.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fonts_get_fonts_by_template**
> UserFontsVM fonts_get_fonts_by_template(template_id, skip=skip, take=take)

Returns a list of fonts in the subscription by report id.

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.user_fonts_vm import UserFontsVM
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
    api_instance = fastreport_cloud_sdk.FontsApi(api_client)
    template_id = 'template_id_example' # str | id of a report
    skip = 0 # int | how many fonts to skip (optional) (default to 0)
    take = 10 # int | how many fonts to take (optional) (default to 10)

    try:
        # Returns a list of fonts in the subscription by report id.
        api_response = api_instance.fonts_get_fonts_by_template(template_id, skip=skip, take=take)
        print("The response of FontsApi->fonts_get_fonts_by_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FontsApi->fonts_get_fonts_by_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| id of a report | 
 **skip** | **int**| how many fonts to skip | [optional] [default to 0]
 **take** | **int**| how many fonts to take | [optional] [default to 10]

### Return type

[**UserFontsVM**](UserFontsVM.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fonts_get_fonts_css**
> str fonts_get_fonts_css(subscription_id=subscription_id)

Creates a css stylesheet for a public font

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
    api_instance = fastreport_cloud_sdk.FontsApi(api_client)
    subscription_id = 'subscription_id_example' # str |  (optional)

    try:
        # Creates a css stylesheet for a public font
        api_response = api_instance.fonts_get_fonts_css(subscription_id=subscription_id)
        print("The response of FontsApi->fonts_get_fonts_css:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FontsApi->fonts_get_fonts_css: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/css

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**402** | Client Error |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fonts_get_fonts_css_by_report**
> str fonts_get_fonts_css_by_report(report_id)

Creates a css stylesheet for a public fonts by report.

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
    api_instance = fastreport_cloud_sdk.FontsApi(api_client)
    report_id = 'report_id_example' # str | id of a report

    try:
        # Creates a css stylesheet for a public fonts by report.
        api_response = api_instance.fonts_get_fonts_css_by_report(report_id)
        print("The response of FontsApi->fonts_get_fonts_css_by_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FontsApi->fonts_get_fonts_css_by_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| id of a report | 

### Return type

**str**

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fonts_get_fonts_css_by_template**
> str fonts_get_fonts_css_by_template(template_id)

Creates a css stylesheet for a public font by template.

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
    api_instance = fastreport_cloud_sdk.FontsApi(api_client)
    template_id = 'template_id_example' # str | id of a report

    try:
        # Creates a css stylesheet for a public font by template.
        api_response = api_instance.fonts_get_fonts_css_by_template(template_id)
        print("The response of FontsApi->fonts_get_fonts_css_by_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FontsApi->fonts_get_fonts_css_by_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| id of a report | 

### Return type

**str**

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fonts_get_my_permissions**
> UserFontPermissionCRUDVM fonts_get_my_permissions(id)

Get current user's permissions to a font

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.user_font_permission_crudvm import UserFontPermissionCRUDVM
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
    api_instance = fastreport_cloud_sdk.FontsApi(api_client)
    id = 'id_example' # str | user font id

    try:
        # Get current user's permissions to a font
        api_response = api_instance.fonts_get_my_permissions(id)
        print("The response of FontsApi->fonts_get_my_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FontsApi->fonts_get_my_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| user font id | 

### Return type

[**UserFontPermissionCRUDVM**](UserFontPermissionCRUDVM.md)

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
**404** | There is no font or a subscription with provided id found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fonts_get_permissions**
> UserFontPermissionsVM fonts_get_permissions(id)

Get font's permissions

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.user_font_permissions_vm import UserFontPermissionsVM
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
    api_instance = fastreport_cloud_sdk.FontsApi(api_client)
    id = 'id_example' # str | user font id

    try:
        # Get font's permissions
        api_response = api_instance.fonts_get_permissions(id)
        print("The response of FontsApi->fonts_get_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FontsApi->fonts_get_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| user font id | 

### Return type

[**UserFontPermissionsVM**](UserFontPermissionsVM.md)

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

# **fonts_get_public_fonts**
> FontsVM fonts_get_public_fonts(skip=skip, take=take)

Returns a list of public fonts

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.fonts_vm import FontsVM
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
    api_instance = fastreport_cloud_sdk.FontsApi(api_client)
    skip = 0 # int |  (optional) (default to 0)
    take = 10 # int |  (optional) (default to 10)

    try:
        # Returns a list of public fonts
        api_response = api_instance.fonts_get_public_fonts(skip=skip, take=take)
        print("The response of FontsApi->fonts_get_public_fonts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FontsApi->fonts_get_public_fonts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**|  | [optional] [default to 0]
 **take** | **int**|  | [optional] [default to 10]

### Return type

[**FontsVM**](FontsVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fonts_get_public_fonts_css**
> str fonts_get_public_fonts_css()

Creates a css stylesheet for a public font

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
    api_instance = fastreport_cloud_sdk.FontsApi(api_client)

    try:
        # Creates a css stylesheet for a public font
        api_response = api_instance.fonts_get_public_fonts_css()
        print("The response of FontsApi->fonts_get_public_fonts_css:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FontsApi->fonts_get_public_fonts_css: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/css

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fonts_update_font**
> UserFontVM fonts_update_font(id, update_user_font_vm=update_user_font_vm)

updates a user font model

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.update_user_font_vm import UpdateUserFontVM
from fastreport_cloud_sdk.models.user_font_vm import UserFontVM
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
    api_instance = fastreport_cloud_sdk.FontsApi(api_client)
    id = 'id_example' # str | id of the font
    update_user_font_vm = fastreport_cloud_sdk.UpdateUserFontVM() # UpdateUserFontVM | update VM body (optional)

    try:
        # updates a user font model
        api_response = api_instance.fonts_update_font(id, update_user_font_vm=update_user_font_vm)
        print("The response of FontsApi->fonts_update_font:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FontsApi->fonts_update_font: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of the font | 
 **update_user_font_vm** | [**UpdateUserFontVM**](UpdateUserFontVM.md)| update VM body | [optional] 

### Return type

[**UserFontVM**](UserFontVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**402** | Client Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fonts_update_permissions**
> fonts_update_permissions(id, update_user_font_permissions_vm=update_user_font_permissions_vm)

Update permissions

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.update_user_font_permissions_vm import UpdateUserFontPermissionsVM
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
    api_instance = fastreport_cloud_sdk.FontsApi(api_client)
    id = 'id_example' # str | 
    update_user_font_permissions_vm = fastreport_cloud_sdk.UpdateUserFontPermissionsVM() # UpdateUserFontPermissionsVM |  (optional)

    try:
        # Update permissions
        api_instance.fonts_update_permissions(id, update_user_font_permissions_vm=update_user_font_permissions_vm)
    except Exception as e:
        print("Exception when calling FontsApi->fonts_update_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_user_font_permissions_vm** | [**UpdateUserFontPermissionsVM**](UpdateUserFontPermissionsVM.md)|  | [optional] 

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

# **fonts_upload_font**
> UserFontsVM fonts_upload_font(file=file, subscription_id=subscription_id, enabled=enabled)

Allows user to upload a new truetype font to their subscription

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.user_fonts_vm import UserFontsVM
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
    api_instance = fastreport_cloud_sdk.FontsApi(api_client)
    file = None # bytearray |  (optional)
    subscription_id = 'subscription_id_example' # str |  (optional)
    enabled = True # bool |  (optional)

    try:
        # Allows user to upload a new truetype font to their subscription
        api_response = api_instance.fonts_upload_font(file=file, subscription_id=subscription_id, enabled=enabled)
        print("The response of FontsApi->fonts_upload_font:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FontsApi->fonts_upload_font: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | [optional] 
 **subscription_id** | **str**|  | [optional] 
 **enabled** | **bool**|  | [optional] 

### Return type

[**UserFontsVM**](UserFontsVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**402** | Client Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

