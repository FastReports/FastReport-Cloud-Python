# FolderCreateVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**icon** | **bytearray** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.folder_create_vm import FolderCreateVM

# TODO update the JSON string below
json = "{}"
# create an instance of FolderCreateVM from a JSON string
folder_create_vm_instance = FolderCreateVM.from_json(json)
# print the JSON string representation of the object
print FolderCreateVM.to_json()

# convert the object into a dict
folder_create_vm_dict = folder_create_vm_instance.to_dict()
# create an instance of FolderCreateVM from a dict
folder_create_vm_form_dict = folder_create_vm.from_dict(folder_create_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


