# PrepareTemplateVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**folder_id** | **str** |  | [optional] 
**pages_count** | **int** |  | [optional] 
**report_parameters** | **Dict[str, Optional[str]]** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.prepare_template_vm import PrepareTemplateVM

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareTemplateVM from a JSON string
prepare_template_vm_instance = PrepareTemplateVM.from_json(json)
# print the JSON string representation of the object
print PrepareTemplateVM.to_json()

# convert the object into a dict
prepare_template_vm_dict = prepare_template_vm_instance.to_dict()
# create an instance of PrepareTemplateVM from a dict
prepare_template_vm_form_dict = prepare_template_vm.from_dict(prepare_template_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


