# UpdateFilePermissionsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_permissions** | [**FilePermissionsCRUDVM**](FilePermissionsCRUDVM.md) |  | 
**administrate** | [**FileAdministrate**](FileAdministrate.md) |  | 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.update_file_permissions_vm import UpdateFilePermissionsVM

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFilePermissionsVM from a JSON string
update_file_permissions_vm_instance = UpdateFilePermissionsVM.from_json(json)
# print the JSON string representation of the object
print UpdateFilePermissionsVM.to_json()

# convert the object into a dict
update_file_permissions_vm_dict = update_file_permissions_vm_instance.to_dict()
# create an instance of UpdateFilePermissionsVM from a dict
update_file_permissions_vm_form_dict = update_file_permissions_vm.from_dict(update_file_permissions_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


