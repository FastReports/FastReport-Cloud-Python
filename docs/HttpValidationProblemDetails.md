# HttpValidationProblemDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **Dict[str, List[str]]** |  | [optional] 
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**detail** | **str** |  | [optional] 
**instance** | **str** |  | [optional] 

## Example

```python
from fastreport_cloud_sdk.models.http_validation_problem_details import HttpValidationProblemDetails

# TODO update the JSON string below
json = "{}"
# create an instance of HttpValidationProblemDetails from a JSON string
http_validation_problem_details_instance = HttpValidationProblemDetails.from_json(json)
# print the JSON string representation of the object
print HttpValidationProblemDetails.to_json()

# convert the object into a dict
http_validation_problem_details_dict = http_validation_problem_details_instance.to_dict()
# create an instance of HttpValidationProblemDetails from a dict
http_validation_problem_details_form_dict = http_validation_problem_details.from_dict(http_validation_problem_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


