# fastreport_cloud_sdk.AdminSubscriptionProblemSolvingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_subscription_problem_solving_solve_problems**](AdminSubscriptionProblemSolvingApi.md#admin_subscription_problem_solving_solve_problems) | **POST** /api/admin/v1/Analytics/Solve | Solve problems provided by FastReport.Cloud.Admin.Controllers.SubscriptionAnalyticsController


# **admin_subscription_problem_solving_solve_problems**
> admin_subscription_problem_solving_solve_problems(analysis_results=analysis_results)

Solve problems provided by FastReport.Cloud.Admin.Controllers.SubscriptionAnalyticsController

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
    api_instance = fastreport_cloud_sdk.AdminSubscriptionProblemSolvingApi(api_client)
    analysis_results = fastreport_cloud_sdk.AnalysisResultsVM() # AnalysisResultsVM |  (optional)

    try:
        # Solve problems provided by FastReport.Cloud.Admin.Controllers.SubscriptionAnalyticsController
        api_instance.admin_subscription_problem_solving_solve_problems(analysis_results=analysis_results)
    except ApiException as e:
        print("Exception when calling AdminSubscriptionProblemSolvingApi->admin_subscription_problem_solving_solve_problems: %s\n" % e)
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
    api_instance = fastreport_cloud_sdk.AdminSubscriptionProblemSolvingApi(api_client)
    analysis_results = fastreport_cloud_sdk.AnalysisResultsVM() # AnalysisResultsVM |  (optional)

    try:
        # Solve problems provided by FastReport.Cloud.Admin.Controllers.SubscriptionAnalyticsController
        api_instance.admin_subscription_problem_solving_solve_problems(analysis_results=analysis_results)
    except ApiException as e:
        print("Exception when calling AdminSubscriptionProblemSolvingApi->admin_subscription_problem_solving_solve_problems: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_results** | [**AnalysisResultsVM**](AnalysisResultsVM.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

