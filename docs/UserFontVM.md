# UserFontVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**font** | [**FontVM**](FontVM.md) |  | [optional] 
**created_time** | **datetime** |  | [optional] 
**creator_user_id** | **str** |  | [optional] 
**edited_time** | **datetime** |  | [optional] 
**editor_user_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.user_font_vm import UserFontVM

# TODO update the JSON string below
json = "{}"
# create an instance of UserFontVM from a JSON string
user_font_vm_instance = UserFontVM.from_json(json)
# print the JSON string representation of the object
print UserFontVM.to_json()

# convert the object into a dict
user_font_vm_dict = user_font_vm_instance.to_dict()
# create an instance of UserFontVM from a dict
user_font_vm_form_dict = user_font_vm.from_dict(user_font_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


