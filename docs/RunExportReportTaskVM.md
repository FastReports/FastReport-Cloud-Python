# RunExportReportTaskVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**export_parameters** | **Dict[str, Optional[str]]** |  | [optional] 
**format** | [**ExportFormat**](ExportFormat.md) |  | [optional] 
**pages_count** | **int** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.run_export_report_task_vm import RunExportReportTaskVM

# TODO update the JSON string below
json = "{}"
# create an instance of RunExportReportTaskVM from a JSON string
run_export_report_task_vm_instance = RunExportReportTaskVM.from_json(json)
# print the JSON string representation of the object
print RunExportReportTaskVM.to_json()

# convert the object into a dict
run_export_report_task_vm_dict = run_export_report_task_vm_instance.to_dict()
# create an instance of RunExportReportTaskVM from a dict
run_export_report_task_vm_form_dict = run_export_report_task_vm.from_dict(run_export_report_task_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


