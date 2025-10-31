# DataSourcePermissionsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**DataSourcePermissionsCRUDVM**](DataSourcePermissionsCRUDVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.data_source_permissions_vm import DataSourcePermissionsVM

# TODO update the JSON string below
json = "{}"
# create an instance of DataSourcePermissionsVM from a JSON string
data_source_permissions_vm_instance = DataSourcePermissionsVM.from_json(json)
# print the JSON string representation of the object
print DataSourcePermissionsVM.to_json()

# convert the object into a dict
data_source_permissions_vm_dict = data_source_permissions_vm_instance.to_dict()
# create an instance of DataSourcePermissionsVM from a dict
data_source_permissions_vm_form_dict = data_source_permissions_vm.from_dict(data_source_permissions_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


