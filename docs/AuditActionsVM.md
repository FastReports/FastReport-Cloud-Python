# AuditActionsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AuditActionVM]**](AuditActionVM.md) |  | [optional] 
**has_more** | **bool** |  | [optional] 
**skip** | **int** |  | [optional] 
**take** | **int** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.audit_actions_vm import AuditActionsVM

# TODO update the JSON string below
json = "{}"
# create an instance of AuditActionsVM from a JSON string
audit_actions_vm_instance = AuditActionsVM.from_json(json)
# print the JSON string representation of the object
print AuditActionsVM.to_json()

# convert the object into a dict
audit_actions_vm_dict = audit_actions_vm_instance.to_dict()
# create an instance of AuditActionsVM from a dict
audit_actions_vm_form_dict = audit_actions_vm.from_dict(audit_actions_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


