# CreateDataSourceVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**connection_string** | **str** |  | 
**subscription_id** | **str** |  | 
**connection_type** | [**DataSourceConnectionType**](DataSourceConnectionType.md) |  | [optional] 
**select_commands** | [**List[DataSourceSelectCommandVM]**](DataSourceSelectCommandVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.create_data_source_vm import CreateDataSourceVM

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDataSourceVM from a JSON string
create_data_source_vm_instance = CreateDataSourceVM.from_json(json)
# print the JSON string representation of the object
print CreateDataSourceVM.to_json()

# convert the object into a dict
create_data_source_vm_dict = create_data_source_vm_instance.to_dict()
# create an instance of CreateDataSourceVM from a dict
create_data_source_vm_form_dict = create_data_source_vm.from_dict(create_data_source_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


