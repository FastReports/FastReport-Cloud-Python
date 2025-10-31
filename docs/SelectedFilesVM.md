# SelectedFilesVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_all_selected** | **bool** |  | [optional] 
**folder_id** | **str** |  | [optional] 
**search_pattern** | **str** |  | [optional] 
**use_regex** | **bool** |  | [optional] 
**files** | **List[str]** |  | [optional] 
**folders** | **List[str]** |  | [optional] 
**path** | **str** |  | [optional] 
**is_bin** | **bool** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.selected_files_vm import SelectedFilesVM

# TODO update the JSON string below
json = "{}"
# create an instance of SelectedFilesVM from a JSON string
selected_files_vm_instance = SelectedFilesVM.from_json(json)
# print the JSON string representation of the object
print SelectedFilesVM.to_json()

# convert the object into a dict
selected_files_vm_dict = selected_files_vm_instance.to_dict()
# create an instance of SelectedFilesVM from a dict
selected_files_vm_form_dict = selected_files_vm.from_dict(selected_files_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


