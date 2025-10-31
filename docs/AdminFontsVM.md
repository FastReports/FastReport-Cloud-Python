# AdminFontsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip** | **int** |  | [optional] 
**take** | **int** |  | [optional] 
**count** | **int** |  | [optional] 
**fonts** | [**List[AdminFontVM]**](AdminFontVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.admin_fonts_vm import AdminFontsVM

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFontsVM from a JSON string
admin_fonts_vm_instance = AdminFontsVM.from_json(json)
# print the JSON string representation of the object
print AdminFontsVM.to_json()

# convert the object into a dict
admin_fonts_vm_dict = admin_fonts_vm_instance.to_dict()
# create an instance of AdminFontsVM from a dict
admin_fonts_vm_form_dict = admin_fonts_vm.from_dict(admin_fonts_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


