# TaskPermissionsCRUDVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_id** | **str** |  | [optional] 
**owner** | [**TaskPermissionCRUDVM**](TaskPermissionCRUDVM.md) |  | [optional] 
**groups** | [**Dict[str, TaskPermissionCRUDVM]**](TaskPermissionCRUDVM.md) |  | [optional] 
**other** | [**TaskPermissionCRUDVM**](TaskPermissionCRUDVM.md) |  | [optional] 
**anon** | [**TaskPermissionCRUDVM**](TaskPermissionCRUDVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.task_permissions_crudvm import TaskPermissionsCRUDVM

# TODO update the JSON string below
json = "{}"
# create an instance of TaskPermissionsCRUDVM from a JSON string
task_permissions_crudvm_instance = TaskPermissionsCRUDVM.from_json(json)
# print the JSON string representation of the object
print TaskPermissionsCRUDVM.to_json()

# convert the object into a dict
task_permissions_crudvm_dict = task_permissions_crudvm_instance.to_dict()
# create an instance of TaskPermissionsCRUDVM from a dict
task_permissions_crudvm_form_dict = task_permissions_crudvm.from_dict(task_permissions_crudvm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


