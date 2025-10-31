# UserFontPermissionsCRUDVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_id** | **str** |  | [optional] 
**owner** | [**UserFontPermissionCRUDVM**](UserFontPermissionCRUDVM.md) |  | [optional] 
**groups** | [**Dict[str, UserFontPermissionCRUDVM]**](UserFontPermissionCRUDVM.md) |  | [optional] 
**other** | [**UserFontPermissionCRUDVM**](UserFontPermissionCRUDVM.md) |  | [optional] 
**anon** | [**UserFontPermissionCRUDVM**](UserFontPermissionCRUDVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.user_font_permissions_crudvm import UserFontPermissionsCRUDVM

# TODO update the JSON string below
json = "{}"
# create an instance of UserFontPermissionsCRUDVM from a JSON string
user_font_permissions_crudvm_instance = UserFontPermissionsCRUDVM.from_json(json)
# print the JSON string representation of the object
print UserFontPermissionsCRUDVM.to_json()

# convert the object into a dict
user_font_permissions_crudvm_dict = user_font_permissions_crudvm_instance.to_dict()
# create an instance of UserFontPermissionsCRUDVM from a dict
user_font_permissions_crudvm_form_dict = user_font_permissions_crudvm.from_dict(user_font_permissions_crudvm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


