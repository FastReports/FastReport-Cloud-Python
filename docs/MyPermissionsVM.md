# MyPermissionsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription** | [**SubscriptionPermissionCRUDVM**](SubscriptionPermissionCRUDVM.md) |  | [optional] 
**files** | [**FilePermissionCRUDVM**](FilePermissionCRUDVM.md) |  | [optional] 
**datasources** | [**DataSourcePermissionCRUDVM**](DataSourcePermissionCRUDVM.md) |  | [optional] 
**groups** | [**GroupPermissionCRUDVM**](GroupPermissionCRUDVM.md) |  | [optional] 
**tasks** | [**TaskPermissionCRUDVM**](TaskPermissionCRUDVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.my_permissions_vm import MyPermissionsVM

# TODO update the JSON string below
json = "{}"
# create an instance of MyPermissionsVM from a JSON string
my_permissions_vm_instance = MyPermissionsVM.from_json(json)
# print the JSON string representation of the object
print MyPermissionsVM.to_json()

# convert the object into a dict
my_permissions_vm_dict = my_permissions_vm_instance.to_dict()
# create an instance of MyPermissionsVM from a dict
my_permissions_vm_form_dict = my_permissions_vm.from_dict(my_permissions_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


