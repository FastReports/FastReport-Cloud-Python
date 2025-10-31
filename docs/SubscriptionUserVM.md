# SubscriptionUserVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**groups** | [**List[GroupVM]**](GroupVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.subscription_user_vm import SubscriptionUserVM

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionUserVM from a JSON string
subscription_user_vm_instance = SubscriptionUserVM.from_json(json)
# print the JSON string representation of the object
print SubscriptionUserVM.to_json()

# convert the object into a dict
subscription_user_vm_dict = subscription_user_vm_instance.to_dict()
# create an instance of SubscriptionUserVM from a dict
subscription_user_vm_form_dict = subscription_user_vm.from_dict(subscription_user_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


