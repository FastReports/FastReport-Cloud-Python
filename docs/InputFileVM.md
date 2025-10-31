# InputFileVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** |  | [optional] 
**type** | [**FileKind**](FileKind.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.input_file_vm import InputFileVM

# TODO update the JSON string below
json = "{}"
# create an instance of InputFileVM from a JSON string
input_file_vm_instance = InputFileVM.from_json(json)
# print the JSON string representation of the object
print InputFileVM.to_json()

# convert the object into a dict
input_file_vm_dict = input_file_vm_instance.to_dict()
# create an instance of InputFileVM from a dict
input_file_vm_form_dict = input_file_vm.from_dict(input_file_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


