# ExportsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**List[ExportVM]**](ExportVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.exports_vm import ExportsVM

# TODO update the JSON string below
json = "{}"
# create an instance of ExportsVM from a JSON string
exports_vm_instance = ExportsVM.from_json(json)
# print the JSON string representation of the object
print ExportsVM.to_json()

# convert the object into a dict
exports_vm_dict = exports_vm_instance.to_dict()
# create an instance of ExportsVM from a dict
exports_vm_form_dict = exports_vm.from_dict(exports_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


