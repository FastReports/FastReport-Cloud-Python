# AuditActionVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**entity_id** | **str** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**type** | [**AuditType**](AuditType.md) |  | [optional] 
**id** | **str** |  | [optional] 
**created_time** | **datetime** |  | [optional] 
**creator_user_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**admin_action** | **bool** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.audit_action_vm import AuditActionVM

# TODO update the JSON string below
json = "{}"
# create an instance of AuditActionVM from a JSON string
audit_action_vm_instance = AuditActionVM.from_json(json)
# print the JSON string representation of the object
print AuditActionVM.to_json()

# convert the object into a dict
audit_action_vm_dict = audit_action_vm_instance.to_dict()
# create an instance of AuditActionVM from a dict
audit_action_vm_form_dict = audit_action_vm.from_dict(audit_action_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


