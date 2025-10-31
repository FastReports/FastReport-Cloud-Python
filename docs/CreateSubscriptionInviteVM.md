# CreateSubscriptionInviteVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usages** | **int** |  | [optional] 
**durable** | **bool** |  | [optional] 
**expired_date** | **datetime** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.create_subscription_invite_vm import CreateSubscriptionInviteVM

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscriptionInviteVM from a JSON string
create_subscription_invite_vm_instance = CreateSubscriptionInviteVM.from_json(json)
# print the JSON string representation of the object
print CreateSubscriptionInviteVM.to_json()

# convert the object into a dict
create_subscription_invite_vm_dict = create_subscription_invite_vm_instance.to_dict()
# create an instance of CreateSubscriptionInviteVM from a dict
create_subscription_invite_vm_form_dict = create_subscription_invite_vm.from_dict(create_subscription_invite_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


