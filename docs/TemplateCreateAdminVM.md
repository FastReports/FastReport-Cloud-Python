# TemplateCreateAdminVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_id** | **str** |  | 
**parent_id** | **str** |  | 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.template_create_admin_vm import TemplateCreateAdminVM

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateCreateAdminVM from a JSON string
template_create_admin_vm_instance = TemplateCreateAdminVM.from_json(json)
# print the JSON string representation of the object
print TemplateCreateAdminVM.to_json()

# convert the object into a dict
template_create_admin_vm_dict = template_create_admin_vm_instance.to_dict()
# create an instance of TemplateCreateAdminVM from a dict
template_create_admin_vm_form_dict = template_create_admin_vm.from_dict(template_create_admin_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


