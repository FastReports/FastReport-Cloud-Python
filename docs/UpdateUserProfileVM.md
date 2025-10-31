# UpdateUserProfileVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**password_new** | **str** |  | [optional] 
**password_new2** | **str** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.update_user_profile_vm import UpdateUserProfileVM

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserProfileVM from a JSON string
update_user_profile_vm_instance = UpdateUserProfileVM.from_json(json)
# print the JSON string representation of the object
print UpdateUserProfileVM.to_json()

# convert the object into a dict
update_user_profile_vm_dict = update_user_profile_vm_instance.to_dict()
# create an instance of UpdateUserProfileVM from a dict
update_user_profile_vm_form_dict = update_user_profile_vm.from_dict(update_user_profile_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


