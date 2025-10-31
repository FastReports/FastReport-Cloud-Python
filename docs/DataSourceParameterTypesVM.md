# DataSourceParameterTypesVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_types** | [**List[DataSourceParameterTypeVM]**](DataSourceParameterTypeVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.data_source_parameter_types_vm import DataSourceParameterTypesVM

# TODO update the JSON string below
json = "{}"
# create an instance of DataSourceParameterTypesVM from a JSON string
data_source_parameter_types_vm_instance = DataSourceParameterTypesVM.from_json(json)
# print the JSON string representation of the object
print DataSourceParameterTypesVM.to_json()

# convert the object into a dict
data_source_parameter_types_vm_dict = data_source_parameter_types_vm_instance.to_dict()
# create an instance of DataSourceParameterTypesVM from a dict
data_source_parameter_types_vm_form_dict = data_source_parameter_types_vm.from_dict(data_source_parameter_types_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


