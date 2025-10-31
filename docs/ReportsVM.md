# ReportsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**List[ReportVM]**](ReportVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.reports_vm import ReportsVM

# TODO update the JSON string below
json = "{}"
# create an instance of ReportsVM from a JSON string
reports_vm_instance = ReportsVM.from_json(json)
# print the JSON string representation of the object
print ReportsVM.to_json()

# convert the object into a dict
reports_vm_dict = reports_vm_instance.to_dict()
# create an instance of ReportsVM from a dict
reports_vm_form_dict = reports_vm.from_dict(reports_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


