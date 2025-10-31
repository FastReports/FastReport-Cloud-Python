# ExportTemplateVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** |  | [optional] 
**folder_id** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**pages_count** | **int** |  | [optional] 
**format** | [**ExportFormat**](ExportFormat.md) |  | [optional] 
**export_parameters** | **Dict[str, Optional[str]]** |  | [optional] 
**report_parameters** | **Dict[str, Optional[str]]** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.export_template_vm import ExportTemplateVM

# TODO update the JSON string below
json = "{}"
# create an instance of ExportTemplateVM from a JSON string
export_template_vm_instance = ExportTemplateVM.from_json(json)
# print the JSON string representation of the object
print ExportTemplateVM.to_json()

# convert the object into a dict
export_template_vm_dict = export_template_vm_instance.to_dict()
# create an instance of ExportTemplateVM from a dict
export_template_vm_form_dict = export_template_vm.from_dict(export_template_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


