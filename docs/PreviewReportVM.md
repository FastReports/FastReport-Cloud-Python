# PreviewReportVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale** | **str** |  | [optional] 
**cache_tolerance** | **float** |  | [optional] [default to 300]
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.preview_report_vm import PreviewReportVM

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewReportVM from a JSON string
preview_report_vm_instance = PreviewReportVM.from_json(json)
# print the JSON string representation of the object
print PreviewReportVM.to_json()

# convert the object into a dict
preview_report_vm_dict = preview_report_vm_instance.to_dict()
# create an instance of PreviewReportVM from a dict
preview_report_vm_form_dict = preview_report_vm.from_dict(preview_report_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


