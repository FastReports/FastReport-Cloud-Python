# UpdateContentInternalVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**editor_id** | **str** |  | [optional] 
**file_content** | **bytearray** |  | [optional] 
**thumbnail** | **bytearray** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.update_content_internal_vm import UpdateContentInternalVM

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateContentInternalVM from a JSON string
update_content_internal_vm_instance = UpdateContentInternalVM.from_json(json)
# print the JSON string representation of the object
print UpdateContentInternalVM.to_json()

# convert the object into a dict
update_content_internal_vm_dict = update_content_internal_vm_instance.to_dict()
# create an instance of UpdateContentInternalVM from a dict
update_content_internal_vm_form_dict = update_content_internal_vm.from_dict(update_content_internal_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


