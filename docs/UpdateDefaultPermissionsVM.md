# UpdateDefaultPermissionsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_permissions** | [**UpdateFilePermissionsVM**](UpdateFilePermissionsVM.md) |  | [optional] 
**group_permissions** | [**UpdateGroupPermissionsVM**](UpdateGroupPermissionsVM.md) |  | [optional] 
**data_source_permissions** | [**UpdateDataSourcePermissionsVM**](UpdateDataSourcePermissionsVM.md) |  | [optional] 
**task_permissions** | [**UpdateTaskPermissionsVM**](UpdateTaskPermissionsVM.md) |  | [optional] 
**font_permissions** | [**UpdateUserFontPermissionsVM**](UpdateUserFontPermissionsVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.update_default_permissions_vm import UpdateDefaultPermissionsVM

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDefaultPermissionsVM from a JSON string
update_default_permissions_vm_instance = UpdateDefaultPermissionsVM.from_json(json)
# print the JSON string representation of the object
print UpdateDefaultPermissionsVM.to_json()

# convert the object into a dict
update_default_permissions_vm_dict = update_default_permissions_vm_instance.to_dict()
# create an instance of UpdateDefaultPermissionsVM from a dict
update_default_permissions_vm_form_dict = update_default_permissions_vm.from_dict(update_default_permissions_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


