# UserFontsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip** | **int** |  | [optional] 
**take** | **int** |  | [optional] 
**count** | **int** |  | [optional] 
**fonts** | [**List[UserFontVM]**](UserFontVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.user_fonts_vm import UserFontsVM

# TODO update the JSON string below
json = "{}"
# create an instance of UserFontsVM from a JSON string
user_fonts_vm_instance = UserFontsVM.from_json(json)
# print the JSON string representation of the object
print UserFontsVM.to_json()

# convert the object into a dict
user_fonts_vm_dict = user_fonts_vm_instance.to_dict()
# create an instance of UserFontsVM from a dict
user_fonts_vm_form_dict = user_fonts_vm.from_dict(user_fonts_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


