# CreateExportReportTaskVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**export_parameters** | **Dict[str, Optional[str]]** |  | [optional] 
**format** | [**ExportFormat**](ExportFormat.md) |  | [optional] 
**pages_count** | **int** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.create_export_report_task_vm import CreateExportReportTaskVM

# TODO update the JSON string below
json = "{}"
# create an instance of CreateExportReportTaskVM from a JSON string
create_export_report_task_vm_instance = CreateExportReportTaskVM.from_json(json)
# print the JSON string representation of the object
print CreateExportReportTaskVM.to_json()

# convert the object into a dict
create_export_report_task_vm_dict = create_export_report_task_vm_instance.to_dict()
# create an instance of CreateExportReportTaskVM from a dict
create_export_report_task_vm_form_dict = create_export_report_task_vm.from_dict(create_export_report_task_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


