# TransformTaskBaseVM


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
from fastreport_cloud_sdk.models.transform_task_base_vm import TransformTaskBaseVM

# TODO update the JSON string below
json = "{}"
# create an instance of TransformTaskBaseVM from a JSON string
transform_task_base_vm_instance = TransformTaskBaseVM.from_json(json)
# print the JSON string representation of the object
print TransformTaskBaseVM.to_json()

# convert the object into a dict
transform_task_base_vm_dict = transform_task_base_vm_instance.to_dict()
# create an instance of TransformTaskBaseVM from a dict
transform_task_base_vm_form_dict = transform_task_base_vm.from_dict(transform_task_base_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


