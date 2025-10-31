# DataSourcePermissionsCRUDVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_id** | **str** |  | [optional] 
**owner** | [**DataSourcePermissionCRUDVM**](DataSourcePermissionCRUDVM.md) |  | [optional] 
**groups** | [**Dict[str, DataSourcePermissionCRUDVM]**](DataSourcePermissionCRUDVM.md) |  | [optional] 
**other** | [**DataSourcePermissionCRUDVM**](DataSourcePermissionCRUDVM.md) |  | [optional] 
**anon** | [**DataSourcePermissionCRUDVM**](DataSourcePermissionCRUDVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.data_source_permissions_crudvm import DataSourcePermissionsCRUDVM

# TODO update the JSON string below
json = "{}"
# create an instance of DataSourcePermissionsCRUDVM from a JSON string
data_source_permissions_crudvm_instance = DataSourcePermissionsCRUDVM.from_json(json)
# print the JSON string representation of the object
print DataSourcePermissionsCRUDVM.to_json()

# convert the object into a dict
data_source_permissions_crudvm_dict = data_source_permissions_crudvm_instance.to_dict()
# create an instance of DataSourcePermissionsCRUDVM from a dict
data_source_permissions_crudvm_form_dict = data_source_permissions_crudvm.from_dict(data_source_permissions_crudvm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


