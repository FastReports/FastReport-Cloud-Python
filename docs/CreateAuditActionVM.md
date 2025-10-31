# CreateAuditActionVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**entity_id** | **str** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**type** | [**AuditType**](AuditType.md) |  | [optional] 
**message_id** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.create_audit_action_vm import CreateAuditActionVM

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAuditActionVM from a JSON string
create_audit_action_vm_instance = CreateAuditActionVM.from_json(json)
# print the JSON string representation of the object
print CreateAuditActionVM.to_json()

# convert the object into a dict
create_audit_action_vm_dict = create_audit_action_vm_instance.to_dict()
# create an instance of CreateAuditActionVM from a dict
create_audit_action_vm_form_dict = create_audit_action_vm.from_dict(create_audit_action_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


