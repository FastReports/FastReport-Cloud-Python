# AdminFontVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**font_families** | **List[str]** |  | [optional] 
**preferred_family** | **str** |  | [optional] 
**preferred_sub_family** | **str** |  | [optional] 
**properties** | **Dict[str, Optional[str]]** |  | [optional] 
**license_text** | **str** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.admin_font_vm import AdminFontVM

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFontVM from a JSON string
admin_font_vm_instance = AdminFontVM.from_json(json)
# print the JSON string representation of the object
print AdminFontVM.to_json()

# convert the object into a dict
admin_font_vm_dict = admin_font_vm_instance.to_dict()
# create an instance of AdminFontVM from a dict
admin_font_vm_form_dict = admin_font_vm.from_dict(admin_font_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


