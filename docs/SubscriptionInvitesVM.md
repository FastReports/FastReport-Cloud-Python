# SubscriptionInvitesVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invites** | [**List[SubscriptionInviteVM]**](SubscriptionInviteVM.md) |  | [optional] 
**count** | **int** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.subscription_invites_vm import SubscriptionInvitesVM

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionInvitesVM from a JSON string
subscription_invites_vm_instance = SubscriptionInvitesVM.from_json(json)
# print the JSON string representation of the object
print SubscriptionInvitesVM.to_json()

# convert the object into a dict
subscription_invites_vm_dict = subscription_invites_vm_instance.to_dict()
# create an instance of SubscriptionInvitesVM from a dict
subscription_invites_vm_form_dict = subscription_invites_vm.from_dict(subscription_invites_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


