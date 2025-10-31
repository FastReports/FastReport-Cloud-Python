# DataSourceParameterTypeVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**value** | **int** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.data_source_parameter_type_vm import DataSourceParameterTypeVM

# TODO update the JSON string below
json = "{}"
# create an instance of DataSourceParameterTypeVM from a JSON string
data_source_parameter_type_vm_instance = DataSourceParameterTypeVM.from_json(json)
# print the JSON string representation of the object
print DataSourceParameterTypeVM.to_json()

# convert the object into a dict
data_source_parameter_type_vm_dict = data_source_parameter_type_vm_instance.to_dict()
# create an instance of DataSourceParameterTypeVM from a dict
data_source_parameter_type_vm_form_dict = data_source_parameter_type_vm.from_dict(data_source_parameter_type_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


