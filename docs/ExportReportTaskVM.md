# ExportReportTaskVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**export_parameters** | **Dict[str, Optional[str]]** |  | [optional] 
**format** | [**ExportFormat**](ExportFormat.md) |  | [optional] 
**pages_count** | **int** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.export_report_task_vm import ExportReportTaskVM

# TODO update the JSON string below
json = "{}"
# create an instance of ExportReportTaskVM from a JSON string
export_report_task_vm_instance = ExportReportTaskVM.from_json(json)
# print the JSON string representation of the object
print ExportReportTaskVM.to_json()

# convert the object into a dict
export_report_task_vm_dict = export_report_task_vm_instance.to_dict()
# create an instance of ExportReportTaskVM from a dict
export_report_task_vm_form_dict = export_report_task_vm.from_dict(export_report_task_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


