# UserFontPermissionsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**UserFontPermissionsCRUDVM**](UserFontPermissionsCRUDVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.user_font_permissions_vm import UserFontPermissionsVM

# TODO update the JSON string below
json = "{}"
# create an instance of UserFontPermissionsVM from a JSON string
user_font_permissions_vm_instance = UserFontPermissionsVM.from_json(json)
# print the JSON string representation of the object
print UserFontPermissionsVM.to_json()

# convert the object into a dict
user_font_permissions_vm_dict = user_font_permissions_vm_instance.to_dict()
# create an instance of UserFontPermissionsVM from a dict
user_font_permissions_vm_form_dict = user_font_permissions_vm.from_dict(user_font_permissions_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


