# SubscriptionsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscriptions** | [**List[SubscriptionVM]**](SubscriptionVM.md) |  | [optional] 
**count** | **int** |  | [optional] 
**skip** | **int** |  | [optional] 
**take** | **int** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.subscriptions_vm import SubscriptionsVM

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionsVM from a JSON string
subscriptions_vm_instance = SubscriptionsVM.from_json(json)
# print the JSON string representation of the object
print SubscriptionsVM.to_json()

# convert the object into a dict
subscriptions_vm_dict = subscriptions_vm_instance.to_dict()
# create an instance of SubscriptionsVM from a dict
subscriptions_vm_form_dict = subscriptions_vm.from_dict(subscriptions_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


