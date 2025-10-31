# TasksVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**skip** | **int** |  | [optional] 
**take** | **int** |  | [optional] 
**tasks** | [**List[TaskBaseVM]**](TaskBaseVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.tasks_vm import TasksVM

# TODO update the JSON string below
json = "{}"
# create an instance of TasksVM from a JSON string
tasks_vm_instance = TasksVM.from_json(json)
# print the JSON string representation of the object
print TasksVM.to_json()

# convert the object into a dict
tasks_vm_dict = tasks_vm_instance.to_dict()
# create an instance of TasksVM from a dict
tasks_vm_form_dict = tasks_vm.from_dict(tasks_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


