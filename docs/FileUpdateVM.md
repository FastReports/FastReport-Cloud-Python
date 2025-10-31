# FileUpdateVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**icon** | **bytearray** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.file_update_vm import FileUpdateVM

# TODO update the JSON string below
json = "{}"
# create an instance of FileUpdateVM from a JSON string
file_update_vm_instance = FileUpdateVM.from_json(json)
# print the JSON string representation of the object
print FileUpdateVM.to_json()

# convert the object into a dict
file_update_vm_dict = file_update_vm_instance.to_dict()
# create an instance of FileUpdateVM from a dict
file_update_vm_form_dict = file_update_vm.from_dict(file_update_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


