# UpdateTaskBaseVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cron_expression** | **str** |  | [optional] 
**starts_on** | **datetime** |  | [optional] 
**ends** | [**CreateTaskEndVM**](CreateTaskEndVM.md) |  | [optional] 
**name** | **str** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.update_task_base_vm import UpdateTaskBaseVM

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTaskBaseVM from a JSON string
update_task_base_vm_instance = UpdateTaskBaseVM.from_json(json)
# print the JSON string representation of the object
print UpdateTaskBaseVM.to_json()

# convert the object into a dict
update_task_base_vm_dict = update_task_base_vm_instance.to_dict()
# create an instance of UpdateTaskBaseVM from a dict
update_task_base_vm_form_dict = update_task_base_vm.from_dict(update_task_base_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


