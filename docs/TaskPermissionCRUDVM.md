# TaskPermissionCRUDVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create** | [**TaskCreate**](TaskCreate.md) |  | [optional] 
**delete** | [**TaskDelete**](TaskDelete.md) |  | [optional] 
**execute** | [**TaskExecute**](TaskExecute.md) |  | [optional] 
**get** | [**TaskGet**](TaskGet.md) |  | [optional] 
**update** | [**TaskUpdate**](TaskUpdate.md) |  | [optional] 
**administrate** | [**TaskAdministrate**](TaskAdministrate.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.task_permission_crudvm import TaskPermissionCRUDVM

# TODO update the JSON string below
json = "{}"
# create an instance of TaskPermissionCRUDVM from a JSON string
task_permission_crudvm_instance = TaskPermissionCRUDVM.from_json(json)
# print the JSON string representation of the object
print TaskPermissionCRUDVM.to_json()

# convert the object into a dict
task_permission_crudvm_dict = task_permission_crudvm_instance.to_dict()
# create an instance of TaskPermissionCRUDVM from a dict
task_permission_crudvm_form_dict = task_permission_crudvm.from_dict(task_permission_crudvm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


