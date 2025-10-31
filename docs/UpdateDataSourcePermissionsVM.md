# UpdateDataSourcePermissionsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_permissions** | [**DataSourcePermissionsCRUDVM**](DataSourcePermissionsCRUDVM.md) |  | 
**administrate** | [**DataSourceAdministrate**](DataSourceAdministrate.md) |  | 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.update_data_source_permissions_vm import UpdateDataSourcePermissionsVM

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDataSourcePermissionsVM from a JSON string
update_data_source_permissions_vm_instance = UpdateDataSourcePermissionsVM.from_json(json)
# print the JSON string representation of the object
print UpdateDataSourcePermissionsVM.to_json()

# convert the object into a dict
update_data_source_permissions_vm_dict = update_data_source_permissions_vm_instance.to_dict()
# create an instance of UpdateDataSourcePermissionsVM from a dict
update_data_source_permissions_vm_form_dict = update_data_source_permissions_vm.from_dict(update_data_source_permissions_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


