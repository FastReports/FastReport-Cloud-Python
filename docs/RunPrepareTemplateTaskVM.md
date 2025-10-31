# RunPrepareTemplateTaskVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exports** | [**List[RunExportReportTaskVM]**](RunExportReportTaskVM.md) |  | [optional] 
**pages_count** | **int** |  | [optional] 
**report_parameters** | **Dict[str, Optional[str]]** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.run_prepare_template_task_vm import RunPrepareTemplateTaskVM

# TODO update the JSON string below
json = "{}"
# create an instance of RunPrepareTemplateTaskVM from a JSON string
run_prepare_template_task_vm_instance = RunPrepareTemplateTaskVM.from_json(json)
# print the JSON string representation of the object
print RunPrepareTemplateTaskVM.to_json()

# convert the object into a dict
run_prepare_template_task_vm_dict = run_prepare_template_task_vm_instance.to_dict()
# create an instance of RunPrepareTemplateTaskVM from a dict
run_prepare_template_task_vm_form_dict = run_prepare_template_task_vm.from_dict(run_prepare_template_task_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


