# ReportVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **str** |  | [optional] 
**report_info** | [**ReportInfo**](ReportInfo.md) |  | [optional] 
**task_id** | **str** |  | [optional] 
**task_message_id** | **str** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.report_vm import ReportVM

# TODO update the JSON string below
json = "{}"
# create an instance of ReportVM from a JSON string
report_vm_instance = ReportVM.from_json(json)
# print the JSON string representation of the object
print ReportVM.to_json()

# convert the object into a dict
report_vm_dict = report_vm_instance.to_dict()
# create an instance of ReportVM from a dict
report_vm_form_dict = report_vm.from_dict(report_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


