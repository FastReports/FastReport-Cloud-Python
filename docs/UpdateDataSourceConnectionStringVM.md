# UpdateDataSourceConnectionStringVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_string** | **str** |  | 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.update_data_source_connection_string_vm import UpdateDataSourceConnectionStringVM

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDataSourceConnectionStringVM from a JSON string
update_data_source_connection_string_vm_instance = UpdateDataSourceConnectionStringVM.from_json(json)
# print the JSON string representation of the object
print UpdateDataSourceConnectionStringVM.to_json()

# convert the object into a dict
update_data_source_connection_string_vm_dict = update_data_source_connection_string_vm_instance.to_dict()
# create an instance of UpdateDataSourceConnectionStringVM from a dict
update_data_source_connection_string_vm_form_dict = update_data_source_connection_string_vm.from_dict(update_data_source_connection_string_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


