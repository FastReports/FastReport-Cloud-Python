# UploadUserFontVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **bytearray** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.upload_user_font_vm import UploadUserFontVM

# TODO update the JSON string below
json = "{}"
# create an instance of UploadUserFontVM from a JSON string
upload_user_font_vm_instance = UploadUserFontVM.from_json(json)
# print the JSON string representation of the object
print UploadUserFontVM.to_json()

# convert the object into a dict
upload_user_font_vm_dict = upload_user_font_vm_instance.to_dict()
# create an instance of UploadUserFontVM from a dict
upload_user_font_vm_form_dict = upload_user_font_vm.from_dict(upload_user_font_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


