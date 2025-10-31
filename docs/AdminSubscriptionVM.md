# AdminSubscriptionVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_permissions** | [**DefaultPermissionsVM**](DefaultPermissionsVM.md) |  | [optional] 
**owner_id** | **str** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.admin_subscription_vm import AdminSubscriptionVM

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSubscriptionVM from a JSON string
admin_subscription_vm_instance = AdminSubscriptionVM.from_json(json)
# print the JSON string representation of the object
print AdminSubscriptionVM.to_json()

# convert the object into a dict
admin_subscription_vm_dict = admin_subscription_vm_instance.to_dict()
# create an instance of AdminSubscriptionVM from a dict
admin_subscription_vm_form_dict = admin_subscription_vm.from_dict(admin_subscription_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


