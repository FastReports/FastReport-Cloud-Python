# DefaultPermissionsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_permissions** | [**FilePermissionsCRUDVM**](FilePermissionsCRUDVM.md) |  | [optional] 
**data_source_permissions** | [**DataSourcePermissionsCRUDVM**](DataSourcePermissionsCRUDVM.md) |  | [optional] 
**group_permissions** | [**GroupPermissionsCRUDVM**](GroupPermissionsCRUDVM.md) |  | [optional] 
**task_permissions** | [**TaskPermissionsCRUDVM**](TaskPermissionsCRUDVM.md) |  | [optional] 
**font_permissions** | [**UserFontPermissionsCRUDVM**](UserFontPermissionsCRUDVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.default_permissions_vm import DefaultPermissionsVM

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultPermissionsVM from a JSON string
default_permissions_vm_instance = DefaultPermissionsVM.from_json(json)
# print the JSON string representation of the object
print DefaultPermissionsVM.to_json()

# convert the object into a dict
default_permissions_vm_dict = default_permissions_vm_instance.to_dict()
# create an instance of DefaultPermissionsVM from a dict
default_permissions_vm_form_dict = default_permissions_vm.from_dict(default_permissions_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


