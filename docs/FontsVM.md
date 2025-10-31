# FontsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip** | **int** |  | [optional] 
**take** | **int** |  | [optional] 
**count** | **int** |  | [optional] 
**fonts** | [**List[FontVM]**](FontVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.fonts_vm import FontsVM

# TODO update the JSON string below
json = "{}"
# create an instance of FontsVM from a JSON string
fonts_vm_instance = FontsVM.from_json(json)
# print the JSON string representation of the object
print FontsVM.to_json()

# convert the object into a dict
fonts_vm_dict = fonts_vm_instance.to_dict()
# create an instance of FontsVM from a dict
fonts_vm_form_dict = fonts_vm.from_dict(fonts_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


