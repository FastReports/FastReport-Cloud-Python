# SolvationReportVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**solved_problems** | **Dict[str, Optional[int]]** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.solvation_report_vm import SolvationReportVM

# TODO update the JSON string below
json = "{}"
# create an instance of SolvationReportVM from a JSON string
solvation_report_vm_instance = SolvationReportVM.from_json(json)
# print the JSON string representation of the object
print SolvationReportVM.to_json()

# convert the object into a dict
solvation_report_vm_dict = solvation_report_vm_instance.to_dict()
# create an instance of SolvationReportVM from a dict
solvation_report_vm_form_dict = solvation_report_vm.from_dict(solvation_report_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


