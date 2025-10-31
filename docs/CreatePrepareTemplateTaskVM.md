# CreatePrepareTemplateTaskVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exports** | [**List[CreateExportReportTaskVM]**](CreateExportReportTaskVM.md) |  | [optional] 
**pages_count** | **int** |  | [optional] 
**report_parameters** | **Dict[str, Optional[str]]** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.create_prepare_template_task_vm import CreatePrepareTemplateTaskVM

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePrepareTemplateTaskVM from a JSON string
create_prepare_template_task_vm_instance = CreatePrepareTemplateTaskVM.from_json(json)
# print the JSON string representation of the object
print CreatePrepareTemplateTaskVM.to_json()

# convert the object into a dict
create_prepare_template_task_vm_dict = create_prepare_template_task_vm_instance.to_dict()
# create an instance of CreatePrepareTemplateTaskVM from a dict
create_prepare_template_task_vm_form_dict = create_prepare_template_task_vm.from_dict(create_prepare_template_task_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


