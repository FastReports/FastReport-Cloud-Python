# GroupPermissionCRUDVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create** | [**GroupCreate**](GroupCreate.md) |  | [optional] 
**delete** | [**GroupDelete**](GroupDelete.md) |  | [optional] 
**execute** | [**GroupExecute**](GroupExecute.md) |  | [optional] 
**get** | [**GroupGet**](GroupGet.md) |  | [optional] 
**update** | [**GroupUpdate**](GroupUpdate.md) |  | [optional] 
**administrate** | [**GroupAdministrate**](GroupAdministrate.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.group_permission_crudvm import GroupPermissionCRUDVM

# TODO update the JSON string below
json = "{}"
# create an instance of GroupPermissionCRUDVM from a JSON string
group_permission_crudvm_instance = GroupPermissionCRUDVM.from_json(json)
# print the JSON string representation of the object
print GroupPermissionCRUDVM.to_json()

# convert the object into a dict
group_permission_crudvm_dict = group_permission_crudvm_instance.to_dict()
# create an instance of GroupPermissionCRUDVM from a dict
group_permission_crudvm_form_dict = group_permission_crudvm.from_dict(group_permission_crudvm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


