# RunInputFileVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **bytearray** |  | [optional] 
**file_name** | **str** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.run_input_file_vm import RunInputFileVM

# TODO update the JSON string below
json = "{}"
# create an instance of RunInputFileVM from a JSON string
run_input_file_vm_instance = RunInputFileVM.from_json(json)
# print the JSON string representation of the object
print RunInputFileVM.to_json()

# convert the object into a dict
run_input_file_vm_dict = run_input_file_vm_instance.to_dict()
# create an instance of RunInputFileVM from a dict
run_input_file_vm_form_dict = run_input_file_vm.from_dict(run_input_file_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


