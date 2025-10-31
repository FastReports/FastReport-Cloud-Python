# UpdateDataSourceVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**connection_string** | **str** |  | [optional] 
**select_commands** | [**List[DataSourceSelectCommandVM]**](DataSourceSelectCommandVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.update_data_source_vm import UpdateDataSourceVM

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDataSourceVM from a JSON string
update_data_source_vm_instance = UpdateDataSourceVM.from_json(json)
# print the JSON string representation of the object
print UpdateDataSourceVM.to_json()

# convert the object into a dict
update_data_source_vm_dict = update_data_source_vm_instance.to_dict()
# create an instance of UpdateDataSourceVM from a dict
update_data_source_vm_form_dict = update_data_source_vm.from_dict(update_data_source_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


