# UpdateUserVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_permission** | [**AdminPermission**](AdminPermission.md) |  | [optional] 
**email** | **str** |  | [optional] 
**groups** | **List[str]** |  | [optional] 
**is_admin** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 
**subscriptions** | **List[str]** |  | [optional] 
**username** | **str** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.update_user_vm import UpdateUserVM

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserVM from a JSON string
update_user_vm_instance = UpdateUserVM.from_json(json)
# print the JSON string representation of the object
print UpdateUserVM.to_json()

# convert the object into a dict
update_user_vm_dict = update_user_vm_instance.to_dict()
# create an instance of UpdateUserVM from a dict
update_user_vm_form_dict = update_user_vm.from_dict(update_user_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


