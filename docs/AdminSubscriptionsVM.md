# AdminSubscriptionsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscriptions** | [**List[AdminSubscriptionVM]**](AdminSubscriptionVM.md) |  | [optional] 
**count** | **int** |  | [optional] 
**skip** | **int** |  | [optional] 
**take** | **int** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.admin_subscriptions_vm import AdminSubscriptionsVM

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSubscriptionsVM from a JSON string
admin_subscriptions_vm_instance = AdminSubscriptionsVM.from_json(json)
# print the JSON string representation of the object
print AdminSubscriptionsVM.to_json()

# convert the object into a dict
admin_subscriptions_vm_dict = admin_subscriptions_vm_instance.to_dict()
# create an instance of AdminSubscriptionsVM from a dict
admin_subscriptions_vm_form_dict = admin_subscriptions_vm.from_dict(admin_subscriptions_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


