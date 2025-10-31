# DataSourcePermissionCRUDVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create** | [**DataSourceCreate**](DataSourceCreate.md) |  | [optional] 
**delete** | [**DataSourceDelete**](DataSourceDelete.md) |  | [optional] 
**execute** | [**DataSourceExecute**](DataSourceExecute.md) |  | [optional] 
**get** | [**DataSourceGet**](DataSourceGet.md) |  | [optional] 
**update** | [**DataSourceUpdate**](DataSourceUpdate.md) |  | [optional] 
**administrate** | [**DataSourceAdministrate**](DataSourceAdministrate.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.data_source_permission_crudvm import DataSourcePermissionCRUDVM

# TODO update the JSON string below
json = "{}"
# create an instance of DataSourcePermissionCRUDVM from a JSON string
data_source_permission_crudvm_instance = DataSourcePermissionCRUDVM.from_json(json)
# print the JSON string representation of the object
print DataSourcePermissionCRUDVM.to_json()

# convert the object into a dict
data_source_permission_crudvm_dict = data_source_permission_crudvm_instance.to_dict()
# create an instance of DataSourcePermissionCRUDVM from a dict
data_source_permission_crudvm_form_dict = data_source_permission_crudvm.from_dict(data_source_permission_crudvm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


