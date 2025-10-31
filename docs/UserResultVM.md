# UserResultVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_authenticated** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**is_admin** | **bool** |  | [optional] 
**admin_permission** | [**AdminPermission**](AdminPermission.md) |  | [optional] 
**subscriptions** | **List[str]** |  | [optional] 
**groups** | **List[str]** |  | [optional] 
**domains** | **List[str]** |  | [optional] 
**provider** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**settings** | [**UserSettingsVM**](UserSettingsVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.user_result_vm import UserResultVM

# TODO update the JSON string below
json = "{}"
# create an instance of UserResultVM from a JSON string
user_result_vm_instance = UserResultVM.from_json(json)
# print the JSON string representation of the object
print UserResultVM.to_json()

# convert the object into a dict
user_result_vm_dict = user_result_vm_instance.to_dict()
# create an instance of UserResultVM from a dict
user_result_vm_form_dict = user_result_vm.from_dict(user_result_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


