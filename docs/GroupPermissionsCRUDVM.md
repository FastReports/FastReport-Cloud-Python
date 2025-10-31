# GroupPermissionsCRUDVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_id** | **str** |  | [optional] 
**owner** | [**GroupPermissionCRUDVM**](GroupPermissionCRUDVM.md) |  | [optional] 
**groups** | [**Dict[str, GroupPermissionCRUDVM]**](GroupPermissionCRUDVM.md) |  | [optional] 
**other** | [**GroupPermissionCRUDVM**](GroupPermissionCRUDVM.md) |  | [optional] 
**anon** | [**GroupPermissionCRUDVM**](GroupPermissionCRUDVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.group_permissions_crudvm import GroupPermissionsCRUDVM

# TODO update the JSON string below
json = "{}"
# create an instance of GroupPermissionsCRUDVM from a JSON string
group_permissions_crudvm_instance = GroupPermissionsCRUDVM.from_json(json)
# print the JSON string representation of the object
print GroupPermissionsCRUDVM.to_json()

# convert the object into a dict
group_permissions_crudvm_dict = group_permissions_crudvm_instance.to_dict()
# create an instance of GroupPermissionsCRUDVM from a dict
group_permissions_crudvm_form_dict = group_permissions_crudvm.from_dict(group_permissions_crudvm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


