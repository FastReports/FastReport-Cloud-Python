# FontVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**post_script_name** | **str** |  | [optional] 
**names** | **List[str]** |  | [optional] 
**weight** | **int** |  | [optional] 
**italic** | **bool** |  | [optional] 
**publicly_accessible** | **bool** |  | [optional] 
**created_time** | **datetime** |  | [optional] 
**creator_user_id** | **str** |  | [optional] 
**edited_time** | **datetime** |  | [optional] 
**editor_user_id** | **str** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.font_vm import FontVM

# TODO update the JSON string below
json = "{}"
# create an instance of FontVM from a JSON string
font_vm_instance = FontVM.from_json(json)
# print the JSON string representation of the object
print FontVM.to_json()

# convert the object into a dict
font_vm_dict = font_vm_instance.to_dict()
# create an instance of FontVM from a dict
font_vm_form_dict = font_vm.from_dict(font_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


