# AdminUpdateCurrentSubscriptionPlanVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan** | [**UpdateSubscriptionPlanVM**](UpdateSubscriptionPlanVM.md) |  | 
**start** | **datetime** |  | [optional] 
**end** | **datetime** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.admin_update_current_subscription_plan_vm import AdminUpdateCurrentSubscriptionPlanVM

# TODO update the JSON string below
json = "{}"
# create an instance of AdminUpdateCurrentSubscriptionPlanVM from a JSON string
admin_update_current_subscription_plan_vm_instance = AdminUpdateCurrentSubscriptionPlanVM.from_json(json)
# print the JSON string representation of the object
print AdminUpdateCurrentSubscriptionPlanVM.to_json()

# convert the object into a dict
admin_update_current_subscription_plan_vm_dict = admin_update_current_subscription_plan_vm_instance.to_dict()
# create an instance of AdminUpdateCurrentSubscriptionPlanVM from a dict
admin_update_current_subscription_plan_vm_form_dict = admin_update_current_subscription_plan_vm.from_dict(admin_update_current_subscription_plan_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


