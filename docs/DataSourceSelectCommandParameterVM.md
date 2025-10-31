# DataSourceSelectCommandParameterVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**data_type** | **str** |  | 
**default_value** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.data_source_select_command_parameter_vm import DataSourceSelectCommandParameterVM

# TODO update the JSON string below
json = "{}"
# create an instance of DataSourceSelectCommandParameterVM from a JSON string
data_source_select_command_parameter_vm_instance = DataSourceSelectCommandParameterVM.from_json(json)
# print the JSON string representation of the object
print DataSourceSelectCommandParameterVM.to_json()

# convert the object into a dict
data_source_select_command_parameter_vm_dict = data_source_select_command_parameter_vm_instance.to_dict()
# create an instance of DataSourceSelectCommandParameterVM from a dict
data_source_select_command_parameter_vm_form_dict = data_source_select_command_parameter_vm.from_dict(data_source_select_command_parameter_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


