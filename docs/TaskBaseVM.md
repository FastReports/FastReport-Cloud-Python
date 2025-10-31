# TaskBaseVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cron_expression** | **str** |  | [optional] 
**starts_on** | **datetime** |  | [optional] 
**ends** | [**TaskEnd**](TaskEnd.md) |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**recurrent_run_time** | **datetime** |  | [optional] 
**recurrent_was_run_time** | **datetime** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.task_base_vm import TaskBaseVM

# TODO update the JSON string below
json = "{}"
# create an instance of TaskBaseVM from a JSON string
task_base_vm_instance = TaskBaseVM.from_json(json)
# print the JSON string representation of the object
print TaskBaseVM.to_json()

# convert the object into a dict
task_base_vm_dict = task_base_vm_instance.to_dict()
# create an instance of TaskBaseVM from a dict
task_base_vm_form_dict = task_base_vm.from_dict(task_base_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


