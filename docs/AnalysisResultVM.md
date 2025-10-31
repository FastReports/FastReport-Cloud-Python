# AnalysisResultVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | [**ProblemLevel**](ProblemLevel.md) |  | [optional] 
**detail** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**suggestion** | **str** |  | [optional] 
**items** | **List[str]** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**file_id** | **str** |  | [optional] 
**collection_name** | **str** |  | [optional] 
**type** | [**ProblemType**](ProblemType.md) |  | [optional] 
**signature** | **str** |  | [optional] 
**new_size** | **int** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.analysis_result_vm import AnalysisResultVM

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisResultVM from a JSON string
analysis_result_vm_instance = AnalysisResultVM.from_json(json)
# print the JSON string representation of the object
print AnalysisResultVM.to_json()

# convert the object into a dict
analysis_result_vm_dict = analysis_result_vm_instance.to_dict()
# create an instance of AnalysisResultVM from a dict
analysis_result_vm_form_dict = analysis_result_vm.from_dict(analysis_result_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


