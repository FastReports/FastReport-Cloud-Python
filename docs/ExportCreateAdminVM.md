# ExportCreateAdminVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_id** | **str** |  | 
**parent_id** | **str** |  | 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.export_create_admin_vm import ExportCreateAdminVM

# TODO update the JSON string below
json = "{}"
# create an instance of ExportCreateAdminVM from a JSON string
export_create_admin_vm_instance = ExportCreateAdminVM.from_json(json)
# print the JSON string representation of the object
print ExportCreateAdminVM.to_json()

# convert the object into a dict
export_create_admin_vm_dict = export_create_admin_vm_instance.to_dict()
# create an instance of ExportCreateAdminVM from a dict
export_create_admin_vm_form_dict = export_create_admin_vm.from_dict(export_create_admin_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


