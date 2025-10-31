# UserVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**subscriptions** | **List[str]** |  | [optional] 
**groups** | **List[str]** |  | [optional] 
**admin_permission** | [**AdminPermission**](AdminPermission.md) |  | [optional] 
**is_admin** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**created_time** | **datetime** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.user_vm import UserVM

# TODO update the JSON string below
json = "{}"
# create an instance of UserVM from a JSON string
user_vm_instance = UserVM.from_json(json)
# print the JSON string representation of the object
print UserVM.to_json()

# convert the object into a dict
user_vm_dict = user_vm_instance.to_dict()
# create an instance of UserVM from a dict
user_vm_form_dict = user_vm.from_dict(user_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


