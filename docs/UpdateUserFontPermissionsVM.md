# UpdateUserFontPermissionsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_permissions** | [**UserFontPermissionsCRUDVM**](UserFontPermissionsCRUDVM.md) |  | 
**administrate** | [**FontAdministrate**](FontAdministrate.md) |  | 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.update_user_font_permissions_vm import UpdateUserFontPermissionsVM

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserFontPermissionsVM from a JSON string
update_user_font_permissions_vm_instance = UpdateUserFontPermissionsVM.from_json(json)
# print the JSON string representation of the object
print UpdateUserFontPermissionsVM.to_json()

# convert the object into a dict
update_user_font_permissions_vm_dict = update_user_font_permissions_vm_instance.to_dict()
# create an instance of UpdateUserFontPermissionsVM from a dict
update_user_font_permissions_vm_form_dict = update_user_font_permissions_vm.from_dict(update_user_font_permissions_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


