# CreateTaskBaseVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cron_expression** | **str** |  | [optional] 
**starts_on** | **datetime** |  | [optional] 
**ends** | [**CreateTaskEndVM**](CreateTaskEndVM.md) |  | [optional] 
**name** | **str** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.create_task_base_vm import CreateTaskBaseVM

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTaskBaseVM from a JSON string
create_task_base_vm_instance = CreateTaskBaseVM.from_json(json)
# print the JSON string representation of the object
print CreateTaskBaseVM.to_json()

# convert the object into a dict
create_task_base_vm_dict = create_task_base_vm_instance.to_dict()
# create an instance of CreateTaskBaseVM from a dict
create_task_base_vm_form_dict = create_task_base_vm.from_dict(create_task_base_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


