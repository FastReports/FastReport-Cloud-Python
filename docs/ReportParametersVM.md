# ReportParametersVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**List[ReportParameter]**](ReportParameter.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.report_parameters_vm import ReportParametersVM

# TODO update the JSON string below
json = "{}"
# create an instance of ReportParametersVM from a JSON string
report_parameters_vm_instance = ReportParametersVM.from_json(json)
# print the JSON string representation of the object
print ReportParametersVM.to_json()

# convert the object into a dict
report_parameters_vm_dict = report_parameters_vm_instance.to_dict()
# create an instance of ReportParametersVM from a dict
report_parameters_vm_form_dict = report_parameters_vm.from_dict(report_parameters_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


