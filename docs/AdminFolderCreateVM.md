# AdminFolderCreateVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_id** | **str** |  | 
**owner_id** | **str** |  | 
**force** | **bool** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.admin_folder_create_vm import AdminFolderCreateVM

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFolderCreateVM from a JSON string
admin_folder_create_vm_instance = AdminFolderCreateVM.from_json(json)
# print the JSON string representation of the object
print AdminFolderCreateVM.to_json()

# convert the object into a dict
admin_folder_create_vm_dict = admin_folder_create_vm_instance.to_dict()
# create an instance of AdminFolderCreateVM from a dict
admin_folder_create_vm_form_dict = admin_folder_create_vm.from_dict(admin_folder_create_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


