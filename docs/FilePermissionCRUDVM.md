# FilePermissionCRUDVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create** | [**FileCreate**](FileCreate.md) |  | [optional] 
**delete** | [**FileDelete**](FileDelete.md) |  | [optional] 
**execute** | [**FileExecute**](FileExecute.md) |  | [optional] 
**get** | [**FileGet**](FileGet.md) |  | [optional] 
**update** | [**FileUpdate**](FileUpdate.md) |  | [optional] 
**administrate** | [**FileAdministrate**](FileAdministrate.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.file_permission_crudvm import FilePermissionCRUDVM

# TODO update the JSON string below
json = "{}"
# create an instance of FilePermissionCRUDVM from a JSON string
file_permission_crudvm_instance = FilePermissionCRUDVM.from_json(json)
# print the JSON string representation of the object
print FilePermissionCRUDVM.to_json()

# convert the object into a dict
file_permission_crudvm_dict = file_permission_crudvm_instance.to_dict()
# create an instance of FilePermissionCRUDVM from a dict
file_permission_crudvm_form_dict = file_permission_crudvm.from_dict(file_permission_crudvm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


