# FileStatusUpdateInternalVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**FileStatus**](FileStatus.md) |  | [optional] 
**reason** | [**FileStatusReason**](FileStatusReason.md) |  | [optional] 
**editor_id** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.file_status_update_internal_vm import FileStatusUpdateInternalVM

# TODO update the JSON string below
json = "{}"
# create an instance of FileStatusUpdateInternalVM from a JSON string
file_status_update_internal_vm_instance = FileStatusUpdateInternalVM.from_json(json)
# print the JSON string representation of the object
print FileStatusUpdateInternalVM.to_json()

# convert the object into a dict
file_status_update_internal_vm_dict = file_status_update_internal_vm_instance.to_dict()
# create an instance of FileStatusUpdateInternalVM from a dict
file_status_update_internal_vm_form_dict = file_status_update_internal_vm.from_dict(file_status_update_internal_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


