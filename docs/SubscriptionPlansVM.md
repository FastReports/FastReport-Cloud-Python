# SubscriptionPlansVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_plans** | [**List[SubscriptionPlanVM]**](SubscriptionPlanVM.md) |  | [optional] 
**count** | **int** |  | [optional] 
**skip** | **int** |  | [optional] 
**take** | **int** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.subscription_plans_vm import SubscriptionPlansVM

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPlansVM from a JSON string
subscription_plans_vm_instance = SubscriptionPlansVM.from_json(json)
# print the JSON string representation of the object
print SubscriptionPlansVM.to_json()

# convert the object into a dict
subscription_plans_vm_dict = subscription_plans_vm_instance.to_dict()
# create an instance of SubscriptionPlansVM from a dict
subscription_plans_vm_form_dict = subscription_plans_vm.from_dict(subscription_plans_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


