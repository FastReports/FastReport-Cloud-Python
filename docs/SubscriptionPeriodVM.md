# SubscriptionPeriodVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **datetime** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**plan** | [**SubscriptionPlanVM**](SubscriptionPlanVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.subscription_period_vm import SubscriptionPeriodVM

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPeriodVM from a JSON string
subscription_period_vm_instance = SubscriptionPeriodVM.from_json(json)
# print the JSON string representation of the object
print SubscriptionPeriodVM.to_json()

# convert the object into a dict
subscription_period_vm_dict = subscription_period_vm_instance.to_dict()
# create an instance of SubscriptionPeriodVM from a dict
subscription_period_vm_form_dict = subscription_period_vm.from_dict(subscription_period_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


