# AnalysisResultsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[AnalysisResultVM]**](AnalysisResultVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.analysis_results_vm import AnalysisResultsVM

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisResultsVM from a JSON string
analysis_results_vm_instance = AnalysisResultsVM.from_json(json)
# print the JSON string representation of the object
print AnalysisResultsVM.to_json()

# convert the object into a dict
analysis_results_vm_dict = analysis_results_vm_instance.to_dict()
# create an instance of AnalysisResultsVM from a dict
analysis_results_vm_form_dict = analysis_results_vm.from_dict(analysis_results_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


