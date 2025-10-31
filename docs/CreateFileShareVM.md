# CreateFileShareVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**permission** | [**FilePermissionCRUDVM**](FilePermissionCRUDVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.create_file_share_vm import CreateFileShareVM

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFileShareVM from a JSON string
create_file_share_vm_instance = CreateFileShareVM.from_json(json)
# print the JSON string representation of the object
print CreateFileShareVM.to_json()

# convert the object into a dict
create_file_share_vm_dict = create_file_share_vm_instance.to_dict()
# create an instance of CreateFileShareVM from a dict
create_file_share_vm_form_dict = create_file_share_vm.from_dict(create_file_share_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


