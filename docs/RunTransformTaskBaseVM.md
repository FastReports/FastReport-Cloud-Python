# RunTransformTaskBaseVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_file** | [**RunInputFileVM**](RunInputFileVM.md) |  | [optional] 
**locale** | **str** |  | [optional] 
**output_file** | [**OutputFileVM**](OutputFileVM.md) |  | [optional] 
**transports** | [**List[RunTransportTaskBaseVM]**](RunTransportTaskBaseVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.run_transform_task_base_vm import RunTransformTaskBaseVM

# TODO update the JSON string below
json = "{}"
# create an instance of RunTransformTaskBaseVM from a JSON string
run_transform_task_base_vm_instance = RunTransformTaskBaseVM.from_json(json)
# print the JSON string representation of the object
print RunTransformTaskBaseVM.to_json()

# convert the object into a dict
run_transform_task_base_vm_dict = run_transform_task_base_vm_instance.to_dict()
# create an instance of RunTransformTaskBaseVM from a dict
run_transform_task_base_vm_form_dict = run_transform_task_base_vm.from_dict(run_transform_task_base_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


