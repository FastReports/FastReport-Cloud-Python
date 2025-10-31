# FileShareVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**permission** | [**FilePermissionCRUDVM**](FilePermissionCRUDVM.md) |  | [optional] 
**key** | **str** |  | [optional] 

## Example

```python
from fastreport_cloud_sdk.models.file_share_vm import FileShareVM

# TODO update the JSON string below
json = "{}"
# create an instance of FileShareVM from a JSON string
file_share_vm_instance = FileShareVM.from_json(json)
# print the JSON string representation of the object
print FileShareVM.to_json()

# convert the object into a dict
file_share_vm_dict = file_share_vm_instance.to_dict()
# create an instance of FileShareVM from a dict
file_share_vm_form_dict = file_share_vm.from_dict(file_share_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


