# AdminFontUpdateVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**publicly_accessible** | **bool** |  | [optional] 
**font_families** | **List[str]** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.admin_font_update_vm import AdminFontUpdateVM

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFontUpdateVM from a JSON string
admin_font_update_vm_instance = AdminFontUpdateVM.from_json(json)
# print the JSON string representation of the object
print AdminFontUpdateVM.to_json()

# convert the object into a dict
admin_font_update_vm_dict = admin_font_update_vm_instance.to_dict()
# create an instance of AdminFontUpdateVM from a dict
admin_font_update_vm_form_dict = admin_font_update_vm.from_dict(admin_font_update_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


