# TaskPermissionsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**TaskPermissionsCRUDVM**](TaskPermissionsCRUDVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.task_permissions_vm import TaskPermissionsVM

# TODO update the JSON string below
json = "{}"
# create an instance of TaskPermissionsVM from a JSON string
task_permissions_vm_instance = TaskPermissionsVM.from_json(json)
# print the JSON string representation of the object
print TaskPermissionsVM.to_json()

# convert the object into a dict
task_permissions_vm_dict = task_permissions_vm_instance.to_dict()
# create an instance of TaskPermissionsVM from a dict
task_permissions_vm_form_dict = task_permissions_vm.from_dict(task_permissions_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


