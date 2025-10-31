# ExportTemplateTaskVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_parameters** | **Dict[str, Optional[str]]** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.export_template_task_vm import ExportTemplateTaskVM

# TODO update the JSON string below
json = "{}"
# create an instance of ExportTemplateTaskVM from a JSON string
export_template_task_vm_instance = ExportTemplateTaskVM.from_json(json)
# print the JSON string representation of the object
print ExportTemplateTaskVM.to_json()

# convert the object into a dict
export_template_task_vm_dict = export_template_task_vm_instance.to_dict()
# create an instance of ExportTemplateTaskVM from a dict
export_template_task_vm_form_dict = export_template_task_vm.from_dict(export_template_task_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


