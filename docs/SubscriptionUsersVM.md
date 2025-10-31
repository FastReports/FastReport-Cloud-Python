# SubscriptionUsersVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[SubscriptionUserVM]**](SubscriptionUserVM.md) |  | [optional] 
**count** | **int** |  | [optional] 
**take** | **int** |  | [optional] 
**skip** | **int** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.subscription_users_vm import SubscriptionUsersVM

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionUsersVM from a JSON string
subscription_users_vm_instance = SubscriptionUsersVM.from_json(json)
# print the JSON string representation of the object
print SubscriptionUsersVM.to_json()

# convert the object into a dict
subscription_users_vm_dict = subscription_users_vm_instance.to_dict()
# create an instance of SubscriptionUsersVM from a dict
subscription_users_vm_form_dict = subscription_users_vm.from_dict(subscription_users_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


