# FileVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**created_time** | **datetime** |  | [optional] 
**creator_user_id** | **str** |  | [optional] 
**edited_time** | **datetime** |  | [optional] 
**editor_user_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**icon** | **bytearray** |  | [optional] 
**type** | [**FileType**](FileType.md) |  | [optional] 
**size** | **int** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**status** | [**FileStatus**](FileStatus.md) |  | [optional] 
**status_reason** | [**FileStatusReason**](FileStatusReason.md) |  | [optional] 
**error_message** | **str** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.file_vm import FileVM

# TODO update the JSON string below
json = "{}"
# create an instance of FileVM from a JSON string
file_vm_instance = FileVM.from_json(json)
# print the JSON string representation of the object
print FileVM.to_json()

# convert the object into a dict
file_vm_dict = file_vm_instance.to_dict()
# create an instance of FileVM from a dict
file_vm_form_dict = file_vm.from_dict(file_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


