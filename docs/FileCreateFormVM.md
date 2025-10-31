# FileCreateFormVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | **List[str]** |  | [optional] 
**icon** | **bytearray** |  | [optional] 
**file_content** | **bytearray** |  | 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.file_create_form_vm import FileCreateFormVM

# TODO update the JSON string below
json = "{}"
# create an instance of FileCreateFormVM from a JSON string
file_create_form_vm_instance = FileCreateFormVM.from_json(json)
# print the JSON string representation of the object
print FileCreateFormVM.to_json()

# convert the object into a dict
file_create_form_vm_dict = file_create_form_vm_instance.to_dict()
# create an instance of FileCreateFormVM from a dict
file_create_form_vm_form_dict = file_create_form_vm.from_dict(file_create_form_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


