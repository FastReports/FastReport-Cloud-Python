# CreateTransportTaskBaseVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_file** | [**InputFileVM**](InputFileVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.create_transport_task_base_vm import CreateTransportTaskBaseVM

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTransportTaskBaseVM from a JSON string
create_transport_task_base_vm_instance = CreateTransportTaskBaseVM.from_json(json)
# print the JSON string representation of the object
print CreateTransportTaskBaseVM.to_json()

# convert the object into a dict
create_transport_task_base_vm_dict = create_transport_task_base_vm_instance.to_dict()
# create an instance of CreateTransportTaskBaseVM from a dict
create_transport_task_base_vm_form_dict = create_transport_task_base_vm.from_dict(create_transport_task_base_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


