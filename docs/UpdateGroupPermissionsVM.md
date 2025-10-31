# UpdateGroupPermissionsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_permissions** | [**GroupPermissionsCRUDVM**](GroupPermissionsCRUDVM.md) |  | 
**administrate** | [**GroupAdministrate**](GroupAdministrate.md) |  | 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.update_group_permissions_vm import UpdateGroupPermissionsVM

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGroupPermissionsVM from a JSON string
update_group_permissions_vm_instance = UpdateGroupPermissionsVM.from_json(json)
# print the JSON string representation of the object
print UpdateGroupPermissionsVM.to_json()

# convert the object into a dict
update_group_permissions_vm_dict = update_group_permissions_vm_instance.to_dict()
# create an instance of UpdateGroupPermissionsVM from a dict
update_group_permissions_vm_form_dict = update_group_permissions_vm.from_dict(update_group_permissions_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


