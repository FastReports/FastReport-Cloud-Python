# UpdateDataSourceSelectCommandsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**select_commands** | [**List[DataSourceSelectCommandVM]**](DataSourceSelectCommandVM.md) |  | 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.update_data_source_select_commands_vm import UpdateDataSourceSelectCommandsVM

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDataSourceSelectCommandsVM from a JSON string
update_data_source_select_commands_vm_instance = UpdateDataSourceSelectCommandsVM.from_json(json)
# print the JSON string representation of the object
print UpdateDataSourceSelectCommandsVM.to_json()

# convert the object into a dict
update_data_source_select_commands_vm_dict = update_data_source_select_commands_vm_instance.to_dict()
# create an instance of UpdateDataSourceSelectCommandsVM from a dict
update_data_source_select_commands_vm_form_dict = update_data_source_select_commands_vm.from_dict(update_data_source_select_commands_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


