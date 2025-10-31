# CreateSubscriptionPeriodVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_id** | **str** |  | 
**start** | **datetime** |  | [optional] 
**end** | **datetime** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.create_subscription_period_vm import CreateSubscriptionPeriodVM

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscriptionPeriodVM from a JSON string
create_subscription_period_vm_instance = CreateSubscriptionPeriodVM.from_json(json)
# print the JSON string representation of the object
print CreateSubscriptionPeriodVM.to_json()

# convert the object into a dict
create_subscription_period_vm_dict = create_subscription_period_vm_instance.to_dict()
# create an instance of CreateSubscriptionPeriodVM from a dict
create_subscription_period_vm_form_dict = create_subscription_period_vm.from_dict(create_subscription_period_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


