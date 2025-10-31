# PreviewTemplateVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale** | **str** |  | [optional] 
**report_parameters** | **Dict[str, Optional[str]]** |  | [optional] 
**cache_tolerance** | **float** |  | [optional] [default to 300]
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.preview_template_vm import PreviewTemplateVM

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewTemplateVM from a JSON string
preview_template_vm_instance = PreviewTemplateVM.from_json(json)
# print the JSON string representation of the object
print PreviewTemplateVM.to_json()

# convert the object into a dict
preview_template_vm_dict = preview_template_vm_instance.to_dict()
# create an instance of PreviewTemplateVM from a dict
preview_template_vm_form_dict = preview_template_vm.from_dict(preview_template_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


