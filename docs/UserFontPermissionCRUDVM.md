# UserFontPermissionCRUDVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create** | [**FontCreate**](FontCreate.md) |  | [optional] 
**delete** | [**FontDelete**](FontDelete.md) |  | [optional] 
**execute** | [**FontExecute**](FontExecute.md) |  | [optional] 
**get** | [**FontGet**](FontGet.md) |  | [optional] 
**update** | [**FontUpdate**](FontUpdate.md) |  | [optional] 
**administrate** | [**FontAdministrate**](FontAdministrate.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.user_font_permission_crudvm import UserFontPermissionCRUDVM

# TODO update the JSON string below
json = "{}"
# create an instance of UserFontPermissionCRUDVM from a JSON string
user_font_permission_crudvm_instance = UserFontPermissionCRUDVM.from_json(json)
# print the JSON string representation of the object
print UserFontPermissionCRUDVM.to_json()

# convert the object into a dict
user_font_permission_crudvm_dict = user_font_permission_crudvm_instance.to_dict()
# create an instance of UserFontPermissionCRUDVM from a dict
user_font_permission_crudvm_form_dict = user_font_permission_crudvm.from_dict(user_font_permission_crudvm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


