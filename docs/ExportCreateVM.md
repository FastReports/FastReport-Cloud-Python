# ExportCreateVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **str** |  | [optional] 
**report_id** | **str** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.export_create_vm import ExportCreateVM

# TODO update the JSON string below
json = "{}"
# create an instance of ExportCreateVM from a JSON string
export_create_vm_instance = ExportCreateVM.from_json(json)
# print the JSON string representation of the object
print ExportCreateVM.to_json()

# convert the object into a dict
export_create_vm_dict = export_create_vm_instance.to_dict()
# create an instance of ExportCreateVM from a dict
export_create_vm_form_dict = export_create_vm.from_dict(export_create_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


