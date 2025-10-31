# UpdateTaskPermissionsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**administrate** | [**TaskAdministrate**](TaskAdministrate.md) |  | 
**new_permissions** | [**TaskPermissionsCRUDVM**](TaskPermissionsCRUDVM.md) |  | 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.update_task_permissions_vm import UpdateTaskPermissionsVM

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTaskPermissionsVM from a JSON string
update_task_permissions_vm_instance = UpdateTaskPermissionsVM.from_json(json)
# print the JSON string representation of the object
print UpdateTaskPermissionsVM.to_json()

# convert the object into a dict
update_task_permissions_vm_dict = update_task_permissions_vm_instance.to_dict()
# create an instance of UpdateTaskPermissionsVM from a dict
update_task_permissions_vm_form_dict = update_task_permissions_vm.from_dict(update_task_permissions_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


