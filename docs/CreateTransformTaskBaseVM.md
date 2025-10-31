# CreateTransformTaskBaseVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_file** | [**InputFileVM**](InputFileVM.md) |  | [optional] 
**locale** | **str** |  | [optional] 
**output_file** | [**OutputFileVM**](OutputFileVM.md) |  | [optional] 
**transports** | [**List[CreateTransportTaskBaseVM]**](CreateTransportTaskBaseVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.create_transform_task_base_vm import CreateTransformTaskBaseVM

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTransformTaskBaseVM from a JSON string
create_transform_task_base_vm_instance = CreateTransformTaskBaseVM.from_json(json)
# print the JSON string representation of the object
print CreateTransformTaskBaseVM.to_json()

# convert the object into a dict
create_transform_task_base_vm_dict = create_transform_task_base_vm_instance.to_dict()
# create an instance of CreateTransformTaskBaseVM from a dict
create_transform_task_base_vm_form_dict = create_transform_task_base_vm.from_dict(create_transform_task_base_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


