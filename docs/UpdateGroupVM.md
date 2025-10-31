# UpdateGroupVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.update_group_vm import UpdateGroupVM

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGroupVM from a JSON string
update_group_vm_instance = UpdateGroupVM.from_json(json)
# print the JSON string representation of the object
print UpdateGroupVM.to_json()

# convert the object into a dict
update_group_vm_dict = update_group_vm_instance.to_dict()
# create an instance of UpdateGroupVM from a dict
update_group_vm_form_dict = update_group_vm.from_dict(update_group_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


