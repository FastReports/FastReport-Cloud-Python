# UpdateDataVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_data** | **str** |  | [optional] 
**editor_id** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.update_data_vm import UpdateDataVM

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDataVM from a JSON string
update_data_vm_instance = UpdateDataVM.from_json(json)
# print the JSON string representation of the object
print UpdateDataVM.to_json()

# convert the object into a dict
update_data_vm_dict = update_data_vm_instance.to_dict()
# create an instance of UpdateDataVM from a dict
update_data_vm_form_dict = update_data_vm.from_dict(update_data_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


