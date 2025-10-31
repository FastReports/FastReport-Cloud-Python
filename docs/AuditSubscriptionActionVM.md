# AuditSubscriptionActionVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_start** | **datetime** |  | [optional] 
**period_end** | **datetime** |  | [optional] 
**plan_id** | **str** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.audit_subscription_action_vm import AuditSubscriptionActionVM

# TODO update the JSON string below
json = "{}"
# create an instance of AuditSubscriptionActionVM from a JSON string
audit_subscription_action_vm_instance = AuditSubscriptionActionVM.from_json(json)
# print the JSON string representation of the object
print AuditSubscriptionActionVM.to_json()

# convert the object into a dict
audit_subscription_action_vm_dict = audit_subscription_action_vm_instance.to_dict()
# create an instance of AuditSubscriptionActionVM from a dict
audit_subscription_action_vm_form_dict = audit_subscription_action_vm.from_dict(audit_subscription_action_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


