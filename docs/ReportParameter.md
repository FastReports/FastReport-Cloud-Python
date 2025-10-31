# ReportParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**data_type** | **str** |  | [optional] 
**expression** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**parameters** | [**List[ReportParameter]**](ReportParameter.md) |  | [optional] 

## Example

```python
from fastreport_cloud_sdk.models.report_parameter import ReportParameter

# TODO update the JSON string below
json = "{}"
# create an instance of ReportParameter from a JSON string
report_parameter_instance = ReportParameter.from_json(json)
# print the JSON string representation of the object
print ReportParameter.to_json()

# convert the object into a dict
report_parameter_dict = report_parameter_instance.to_dict()
# create an instance of ReportParameter from a dict
report_parameter_form_dict = report_parameter.from_dict(report_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


