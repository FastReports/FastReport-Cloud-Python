# FilePermissionsCRUDVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_id** | **str** |  | [optional] 
**owner** | [**FilePermissionCRUDVM**](FilePermissionCRUDVM.md) |  | [optional] 
**groups** | [**Dict[str, FilePermissionCRUDVM]**](FilePermissionCRUDVM.md) |  | [optional] 
**other** | [**FilePermissionCRUDVM**](FilePermissionCRUDVM.md) |  | [optional] 
**anon** | [**FilePermissionCRUDVM**](FilePermissionCRUDVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.file_permissions_crudvm import FilePermissionsCRUDVM

# TODO update the JSON string below
json = "{}"
# create an instance of FilePermissionsCRUDVM from a JSON string
file_permissions_crudvm_instance = FilePermissionsCRUDVM.from_json(json)
# print the JSON string representation of the object
print FilePermissionsCRUDVM.to_json()

# convert the object into a dict
file_permissions_crudvm_dict = file_permissions_crudvm_instance.to_dict()
# create an instance of FilePermissionsCRUDVM from a dict
file_permissions_crudvm_form_dict = file_permissions_crudvm.from_dict(file_permissions_crudvm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


