# FilesVMBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**List[FileVM]**](FileVM.md) |  | [optional] 
**count** | **int** |  | [optional] 
**skip** | **int** |  | [optional] 
**take** | **int** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.files_vm_base import FilesVMBase

# TODO update the JSON string below
json = "{}"
# create an instance of FilesVMBase from a JSON string
files_vm_base_instance = FilesVMBase.from_json(json)
# print the JSON string representation of the object
print FilesVMBase.to_json()

# convert the object into a dict
files_vm_base_dict = files_vm_base_instance.to_dict()
# create an instance of FilesVMBase from a dict
files_vm_base_form_dict = files_vm_base.from_dict(files_vm_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


