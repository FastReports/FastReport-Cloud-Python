# AuditStatsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **Dict[str, Optional[List[AuditStatVM]]]** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.audit_stats_vm import AuditStatsVM

# TODO update the JSON string below
json = "{}"
# create an instance of AuditStatsVM from a JSON string
audit_stats_vm_instance = AuditStatsVM.from_json(json)
# print the JSON string representation of the object
print AuditStatsVM.to_json()

# convert the object into a dict
audit_stats_vm_dict = audit_stats_vm_instance.to_dict()
# create an instance of AuditStatsVM from a dict
audit_stats_vm_form_dict = audit_stats_vm.from_dict(audit_stats_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


