# UpdateExportTemplateTaskVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_parameters** | **Dict[str, Optional[str]]** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.update_export_template_task_vm import UpdateExportTemplateTaskVM

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateExportTemplateTaskVM from a JSON string
update_export_template_task_vm_instance = UpdateExportTemplateTaskVM.from_json(json)
# print the JSON string representation of the object
print UpdateExportTemplateTaskVM.to_json()

# convert the object into a dict
update_export_template_task_vm_dict = update_export_template_task_vm_instance.to_dict()
# create an instance of UpdateExportTemplateTaskVM from a dict
update_export_template_task_vm_form_dict = update_export_template_task_vm.from_dict(update_export_template_task_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


