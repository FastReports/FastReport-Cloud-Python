# AuditTaskActionVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.audit_task_action_vm import AuditTaskActionVM

# TODO update the JSON string below
json = "{}"
# create an instance of AuditTaskActionVM from a JSON string
audit_task_action_vm_instance = AuditTaskActionVM.from_json(json)
# print the JSON string representation of the object
print AuditTaskActionVM.to_json()

# convert the object into a dict
audit_task_action_vm_dict = audit_task_action_vm_instance.to_dict()
# create an instance of AuditTaskActionVM from a dict
audit_task_action_vm_form_dict = audit_task_action_vm.from_dict(audit_task_action_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


