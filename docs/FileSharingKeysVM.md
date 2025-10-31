# FileSharingKeysVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | [**List[FileShareVM]**](FileShareVM.md) |  | [optional] 

## Example

```python
from fastreport_cloud_sdk.models.file_sharing_keys_vm import FileSharingKeysVM

# TODO update the JSON string below
json = "{}"
# create an instance of FileSharingKeysVM from a JSON string
file_sharing_keys_vm_instance = FileSharingKeysVM.from_json(json)
# print the JSON string representation of the object
print FileSharingKeysVM.to_json()

# convert the object into a dict
file_sharing_keys_vm_dict = file_sharing_keys_vm_instance.to_dict()
# create an instance of FileSharingKeysVM from a dict
file_sharing_keys_vm_form_dict = file_sharing_keys_vm.from_dict(file_sharing_keys_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


