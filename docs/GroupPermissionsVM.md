# GroupPermissionsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**GroupPermissionsCRUDVM**](GroupPermissionsCRUDVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.group_permissions_vm import GroupPermissionsVM

# TODO update the JSON string below
json = "{}"
# create an instance of GroupPermissionsVM from a JSON string
group_permissions_vm_instance = GroupPermissionsVM.from_json(json)
# print the JSON string representation of the object
print GroupPermissionsVM.to_json()

# convert the object into a dict
group_permissions_vm_dict = group_permissions_vm_instance.to_dict()
# create an instance of GroupPermissionsVM from a dict
group_permissions_vm_form_dict = group_permissions_vm.from_dict(group_permissions_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


