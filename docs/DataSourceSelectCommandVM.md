# DataSourceSelectCommandVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**command** | **str** |  | 
**parameters** | [**List[DataSourceSelectCommandParameterVM]**](DataSourceSelectCommandParameterVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.data_source_select_command_vm import DataSourceSelectCommandVM

# TODO update the JSON string below
json = "{}"
# create an instance of DataSourceSelectCommandVM from a JSON string
data_source_select_command_vm_instance = DataSourceSelectCommandVM.from_json(json)
# print the JSON string representation of the object
print DataSourceSelectCommandVM.to_json()

# convert the object into a dict
data_source_select_command_vm_dict = data_source_select_command_vm_instance.to_dict()
# create an instance of DataSourceSelectCommandVM from a dict
data_source_select_command_vm_form_dict = data_source_select_command_vm.from_dict(data_source_select_command_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


