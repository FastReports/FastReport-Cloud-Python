# CreateTaskEndVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after** | **int** |  | [optional] 
**on** | **datetime** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.create_task_end_vm import CreateTaskEndVM

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTaskEndVM from a JSON string
create_task_end_vm_instance = CreateTaskEndVM.from_json(json)
# print the JSON string representation of the object
print CreateTaskEndVM.to_json()

# convert the object into a dict
create_task_end_vm_dict = create_task_end_vm_instance.to_dict()
# create an instance of CreateTaskEndVM from a dict
create_task_end_vm_form_dict = create_task_end_vm.from_dict(create_task_end_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


