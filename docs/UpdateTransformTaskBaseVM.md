# UpdateTransformTaskBaseVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_file** | [**InputFileVM**](InputFileVM.md) |  | [optional] 
**locale** | **str** |  | [optional] 
**output_file** | [**OutputFileVM**](OutputFileVM.md) |  | [optional] 
**transport_ids** | **List[str]** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.update_transform_task_base_vm import UpdateTransformTaskBaseVM

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTransformTaskBaseVM from a JSON string
update_transform_task_base_vm_instance = UpdateTransformTaskBaseVM.from_json(json)
# print the JSON string representation of the object
print UpdateTransformTaskBaseVM.to_json()

# convert the object into a dict
update_transform_task_base_vm_dict = update_transform_task_base_vm_instance.to_dict()
# create an instance of UpdateTransformTaskBaseVM from a dict
update_transform_task_base_vm_form_dict = update_transform_task_base_vm.from_dict(update_transform_task_base_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


