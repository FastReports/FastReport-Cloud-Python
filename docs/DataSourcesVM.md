# DataSourcesVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_sources** | [**List[DataSourceVM]**](DataSourceVM.md) |  | [optional] 
**count** | **int** |  | [optional] 
**skip** | **int** |  | [optional] 
**take** | **int** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.data_sources_vm import DataSourcesVM

# TODO update the JSON string below
json = "{}"
# create an instance of DataSourcesVM from a JSON string
data_sources_vm_instance = DataSourcesVM.from_json(json)
# print the JSON string representation of the object
print DataSourcesVM.to_json()

# convert the object into a dict
data_sources_vm_dict = data_sources_vm_instance.to_dict()
# create an instance of DataSourcesVM from a dict
data_sources_vm_form_dict = data_sources_vm.from_dict(data_sources_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


