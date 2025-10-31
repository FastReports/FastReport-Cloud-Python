# TemplateVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_info** | [**ReportInfo**](ReportInfo.md) |  | [optional] 
**parameters** | [**List[ReportParameter]**](ReportParameter.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.template_vm import TemplateVM

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateVM from a JSON string
template_vm_instance = TemplateVM.from_json(json)
# print the JSON string representation of the object
print TemplateVM.to_json()

# convert the object into a dict
template_vm_dict = template_vm_instance.to_dict()
# create an instance of TemplateVM from a dict
template_vm_form_dict = template_vm.from_dict(template_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


