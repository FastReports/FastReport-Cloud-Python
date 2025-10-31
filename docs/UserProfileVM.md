# UserProfileVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**is_read_only** | **bool** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.user_profile_vm import UserProfileVM

# TODO update the JSON string below
json = "{}"
# create an instance of UserProfileVM from a JSON string
user_profile_vm_instance = UserProfileVM.from_json(json)
# print the JSON string representation of the object
print UserProfileVM.to_json()

# convert the object into a dict
user_profile_vm_dict = user_profile_vm_instance.to_dict()
# create an instance of UserProfileVM from a dict
user_profile_vm_form_dict = user_profile_vm.from_dict(user_profile_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


