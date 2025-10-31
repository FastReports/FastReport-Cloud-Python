# DataSourceVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**connection_type** | [**DataSourceConnectionType**](DataSourceConnectionType.md) |  | [optional] 
**connection_string** | **str** |  | [optional] 
**data_structure** | **str** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**edited_time** | **datetime** |  | [optional] 
**editor_user_id** | **str** |  | [optional] 
**created_time** | **datetime** |  | [optional] 
**creator_user_id** | **str** |  | [optional] 
**status** | [**DataSourceStatus**](DataSourceStatus.md) |  | [optional] 
**error_message** | **str** |  | [optional] 
**select_commands** | [**List[DataSourceSelectCommandVM]**](DataSourceSelectCommandVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.data_source_vm import DataSourceVM

# TODO update the JSON string below
json = "{}"
# create an instance of DataSourceVM from a JSON string
data_source_vm_instance = DataSourceVM.from_json(json)
# print the JSON string representation of the object
print DataSourceVM.to_json()

# convert the object into a dict
data_source_vm_dict = data_source_vm_instance.to_dict()
# create an instance of DataSourceVM from a dict
data_source_vm_form_dict = data_source_vm.from_dict(data_source_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


