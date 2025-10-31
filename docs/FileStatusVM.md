# FileStatusVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_status** | [**FileStatus**](FileStatus.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.file_status_vm import FileStatusVM

# TODO update the JSON string below
json = "{}"
# create an instance of FileStatusVM from a JSON string
file_status_vm_instance = FileStatusVM.from_json(json)
# print the JSON string representation of the object
print FileStatusVM.to_json()

# convert the object into a dict
file_status_vm_dict = file_status_vm_instance.to_dict()
# create an instance of FileStatusVM from a dict
file_status_vm_form_dict = file_status_vm.from_dict(file_status_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


