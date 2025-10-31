# TaskIdsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**ids** | **List[str]** |  | [optional] 
**skip** | **int** |  | [optional] 
**take** | **int** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.task_ids_vm import TaskIdsVM

# TODO update the JSON string below
json = "{}"
# create an instance of TaskIdsVM from a JSON string
task_ids_vm_instance = TaskIdsVM.from_json(json)
# print the JSON string representation of the object
print TaskIdsVM.to_json()

# convert the object into a dict
task_ids_vm_dict = task_ids_vm_instance.to_dict()
# create an instance of TaskIdsVM from a dict
task_ids_vm_form_dict = task_ids_vm.from_dict(task_ids_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


