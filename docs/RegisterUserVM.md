# RegisterUserVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**subscriptions** | **List[str]** |  | [optional] 
**groups** | **List[str]** |  | [optional] 
**admin_permission** | [**AdminPermission**](AdminPermission.md) |  | [optional] 
**name** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**is_admin** | **bool** |  | [optional] 
**provider** | **str** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.register_user_vm import RegisterUserVM

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterUserVM from a JSON string
register_user_vm_instance = RegisterUserVM.from_json(json)
# print the JSON string representation of the object
print RegisterUserVM.to_json()

# convert the object into a dict
register_user_vm_dict = register_user_vm_instance.to_dict()
# create an instance of RegisterUserVM from a dict
register_user_vm_form_dict = register_user_vm.from_dict(register_user_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


