# FolderSizeVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** |  | [optional] 
**real_size** | **int** |  | [optional] 
**documents_count** | **int** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.folder_size_vm import FolderSizeVM

# TODO update the JSON string below
json = "{}"
# create an instance of FolderSizeVM from a JSON string
folder_size_vm_instance = FolderSizeVM.from_json(json)
# print the JSON string representation of the object
print FolderSizeVM.to_json()

# convert the object into a dict
folder_size_vm_dict = folder_size_vm_instance.to_dict()
# create an instance of FolderSizeVM from a dict
folder_size_vm_form_dict = folder_size_vm.from_dict(folder_size_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


