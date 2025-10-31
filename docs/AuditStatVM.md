# AuditStatVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**type** | [**AuditType**](AuditType.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.audit_stat_vm import AuditStatVM

# TODO update the JSON string below
json = "{}"
# create an instance of AuditStatVM from a JSON string
audit_stat_vm_instance = AuditStatVM.from_json(json)
# print the JSON string representation of the object
print AuditStatVM.to_json()

# convert the object into a dict
audit_stat_vm_dict = audit_stat_vm_instance.to_dict()
# create an instance of AuditStatVM from a dict
audit_stat_vm_form_dict = audit_stat_vm.from_dict(audit_stat_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


