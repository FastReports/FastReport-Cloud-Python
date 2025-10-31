# AuditFilePropertyChangedVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_name** | **str** |  | [optional] 
**old_value** | **object** |  | [optional] 
**new_value** | **object** |  | [optional] 
**entity_type** | [**EntityType**](EntityType.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.audit_file_property_changed_vm import AuditFilePropertyChangedVM

# TODO update the JSON string below
json = "{}"
# create an instance of AuditFilePropertyChangedVM from a JSON string
audit_file_property_changed_vm_instance = AuditFilePropertyChangedVM.from_json(json)
# print the JSON string representation of the object
print AuditFilePropertyChangedVM.to_json()

# convert the object into a dict
audit_file_property_changed_vm_dict = audit_file_property_changed_vm_instance.to_dict()
# create an instance of AuditFilePropertyChangedVM from a dict
audit_file_property_changed_vm_form_dict = audit_file_property_changed_vm.from_dict(audit_file_property_changed_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


