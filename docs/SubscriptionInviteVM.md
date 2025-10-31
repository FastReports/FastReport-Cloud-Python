# SubscriptionInviteVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usages** | **int** |  | [optional] 
**durable** | **bool** |  | [optional] 
**access_token** | **str** |  | [optional] 
**expired_date** | **datetime** |  | [optional] 
**added_users** | [**List[InvitedUser]**](InvitedUser.md) |  | [optional] 
**creator_user_id** | **str** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.subscription_invite_vm import SubscriptionInviteVM

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionInviteVM from a JSON string
subscription_invite_vm_instance = SubscriptionInviteVM.from_json(json)
# print the JSON string representation of the object
print SubscriptionInviteVM.to_json()

# convert the object into a dict
subscription_invite_vm_dict = subscription_invite_vm_instance.to_dict()
# create an instance of SubscriptionInviteVM from a dict
subscription_invite_vm_form_dict = subscription_invite_vm.from_dict(subscription_invite_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


