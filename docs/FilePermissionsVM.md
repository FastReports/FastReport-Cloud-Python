# FilePermissionsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**FilePermissionsCRUDVM**](FilePermissionsCRUDVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.file_permissions_vm import FilePermissionsVM

# TODO update the JSON string below
json = "{}"
# create an instance of FilePermissionsVM from a JSON string
file_permissions_vm_instance = FilePermissionsVM.from_json(json)
# print the JSON string representation of the object
print FilePermissionsVM.to_json()

# convert the object into a dict
file_permissions_vm_dict = file_permissions_vm_instance.to_dict()
# create an instance of FilePermissionsVM from a dict
file_permissions_vm_form_dict = file_permissions_vm.from_dict(file_permissions_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


