# AdminFontUploadVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**form_file** | **bytearray** |  | 
**publicly_accessible** | **bool** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.admin_font_upload_vm import AdminFontUploadVM

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFontUploadVM from a JSON string
admin_font_upload_vm_instance = AdminFontUploadVM.from_json(json)
# print the JSON string representation of the object
print AdminFontUploadVM.to_json()

# convert the object into a dict
admin_font_upload_vm_dict = admin_font_upload_vm_instance.to_dict()
# create an instance of AdminFontUploadVM from a dict
admin_font_upload_vm_form_dict = admin_font_upload_vm.from_dict(admin_font_upload_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


