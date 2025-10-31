# OutputFileVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** |  | [optional] 
**folder_id** | **str** |  | [optional] 
**type** | [**FileKind**](FileKind.md) |  | [optional] 
**is_temporary** | **bool** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.output_file_vm import OutputFileVM

# TODO update the JSON string below
json = "{}"
# create an instance of OutputFileVM from a JSON string
output_file_vm_instance = OutputFileVM.from_json(json)
# print the JSON string representation of the object
print OutputFileVM.to_json()

# convert the object into a dict
output_file_vm_dict = output_file_vm_instance.to_dict()
# create an instance of OutputFileVM from a dict
output_file_vm_form_dict = output_file_vm.from_dict(output_file_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


