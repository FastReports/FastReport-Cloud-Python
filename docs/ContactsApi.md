# fastreport_cloud_sdk.ContactsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contacts_create**](ContactsApi.md#contacts_create) | **POST** /api/v1/Contacts/contact | Creates new contact
[**contacts_delete**](ContactsApi.md#contacts_delete) | **DELETE** /api/v1/Contacts/{id} | Removes contact by id
[**contacts_get**](ContactsApi.md#contacts_get) | **GET** /api/v1/Contacts/{id} | Returns contact group by id
[**contacts_get_by_group**](ContactsApi.md#contacts_get_by_group) | **GET** /api/v1/Contacts/group/{groupId}/contacts | Returns contacts by group id
[**contacts_get_list**](ContactsApi.md#contacts_get_list) | **GET** /api/v1/Contacts/subscription/{subscriptionId}/contacts | Allows to search for contacts
[**contacts_update**](ContactsApi.md#contacts_update) | **PUT** /api/v1/Contacts/{id} | Updates contact by id


# **contacts_create**
> ContactVM contacts_create(create_contact_vm=create_contact_vm)

Creates new contact

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.contact_vm import ContactVM
from fastreport_cloud_sdk.models.create_contact_vm import CreateContactVM
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
    api_instance = fastreport_cloud_sdk.ContactsApi(api_client)
    create_contact_vm = fastreport_cloud_sdk.CreateContactVM() # CreateContactVM |  (optional)

    try:
        # Creates new contact
        api_response = api_instance.contacts_create(create_contact_vm=create_contact_vm)
        print("The response of ContactsApi->contacts_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->contacts_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_contact_vm** | [**CreateContactVM**](CreateContactVM.md)|  | [optional] 

### Return type

[**ContactVM**](ContactVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contact was created |  -  |
**400** | Bad VM provided |  -  |
**402** | Subscription is outdated |  -  |
**403** | Not enough permissions for the operation |  -  |
**404** | Subscription was not found |  -  |
**500** | Try again, if error still here - text our support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contacts_delete**
> contacts_delete(id)

Removes contact by id

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
    api_instance = fastreport_cloud_sdk.ContactsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Removes contact by id
        api_instance.contacts_delete(id)
    except Exception as e:
        print("Exception when calling ContactsApi->contacts_delete: %s\n" % e)
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
**400** | Bad id provided |  -  |
**402** | Subscription is outdated |  -  |
**403** | Not enough permissions for the operation |  -  |
**404** | Subscription or contact was not found |  -  |
**500** | Try again, if error still here - text our support |  -  |
**200** | Contact was deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contacts_get**
> ContactVM contacts_get(id)

Returns contact group by id

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.contact_vm import ContactVM
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
    api_instance = fastreport_cloud_sdk.ContactsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Returns contact group by id
        api_response = api_instance.contacts_get(id)
        print("The response of ContactsApi->contacts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->contacts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ContactVM**](ContactVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contact was found |  -  |
**400** | Bad id provided |  -  |
**402** | Subscription is outdated |  -  |
**403** | Not enough permissions for the operation |  -  |
**404** | Subscription or contact was not found |  -  |
**500** | Try again, if error still here - text our support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contacts_get_by_group**
> ContactsVM contacts_get_by_group(group_id, skip=skip, take=take)

Returns contacts by group id

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.contacts_vm import ContactsVM
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
    api_instance = fastreport_cloud_sdk.ContactsApi(api_client)
    group_id = 'group_id_example' # str | 
    skip = 0 # int |  (optional) (default to 0)
    take = 10 # int |  (optional) (default to 10)

    try:
        # Returns contacts by group id
        api_response = api_instance.contacts_get_by_group(group_id, skip=skip, take=take)
        print("The response of ContactsApi->contacts_get_by_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->contacts_get_by_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **skip** | **int**|  | [optional] [default to 0]
 **take** | **int**|  | [optional] [default to 10]

### Return type

[**ContactsVM**](ContactsVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contacts were found |  -  |
**400** | Bad id provided |  -  |
**402** | Subscription is outdated |  -  |
**403** | Not enough permissions for the operation |  -  |
**404** | Subscription or group was not found |  -  |
**500** | Try again, if error still here - text our support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contacts_get_list**
> ContactsVM contacts_get_list(subscription_id, skip=skip, take=take, search_pattern=search_pattern)

Allows to search for contacts

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.contacts_vm import ContactsVM
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
    api_instance = fastreport_cloud_sdk.ContactsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    skip = 0 # int |  (optional) (default to 0)
    take = 10 # int |  (optional) (default to 10)
    search_pattern = 'search_pattern_example' # str |  (optional)

    try:
        # Allows to search for contacts
        api_response = api_instance.contacts_get_list(subscription_id, skip=skip, take=take, search_pattern=search_pattern)
        print("The response of ContactsApi->contacts_get_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->contacts_get_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **skip** | **int**|  | [optional] [default to 0]
 **take** | **int**|  | [optional] [default to 10]
 **search_pattern** | **str**|  | [optional] 

### Return type

[**ContactsVM**](ContactsVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contacts were found |  -  |
**400** | Bad id provided |  -  |
**402** | Subscription is outdated |  -  |
**403** | Not enough permissions for the operation |  -  |
**404** | Subscription was not found |  -  |
**500** | Try again, if error still here - text our support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contacts_update**
> ContactVM contacts_update(id, update_contact_vm=update_contact_vm)

Updates contact by id

### Example

* Basic Authentication (ApiKey):
* Bearer (JWT) Authentication (JWT):

```python
import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.contact_vm import ContactVM
from fastreport_cloud_sdk.models.update_contact_vm import UpdateContactVM
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
    api_instance = fastreport_cloud_sdk.ContactsApi(api_client)
    id = 'id_example' # str | 
    update_contact_vm = fastreport_cloud_sdk.UpdateContactVM() # UpdateContactVM |  (optional)

    try:
        # Updates contact by id
        api_response = api_instance.contacts_update(id, update_contact_vm=update_contact_vm)
        print("The response of ContactsApi->contacts_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->contacts_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_contact_vm** | [**UpdateContactVM**](UpdateContactVM.md)|  | [optional] 

### Return type

[**ContactVM**](ContactVM.md)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contact was updated |  -  |
**400** | Bad VM or id provided |  -  |
**402** | Subscription is outdated |  -  |
**403** | Not enough permissions for the operation |  -  |
**404** | Subscription or contact was not found |  -  |
**500** | Try again, if error still here - text our support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

