# TemplatesVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**List[TemplateVM]**](TemplateVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.templates_vm import TemplatesVM

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatesVM from a JSON string
templates_vm_instance = TemplatesVM.from_json(json)
# print the JSON string representation of the object
print TemplatesVM.to_json()

# convert the object into a dict
templates_vm_dict = templates_vm_instance.to_dict()
# create an instance of TemplatesVM from a dict
templates_vm_form_dict = templates_vm.from_dict(templates_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


