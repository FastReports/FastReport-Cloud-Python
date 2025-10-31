# GroupVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.group_vm import GroupVM

# TODO update the JSON string below
json = "{}"
# create an instance of GroupVM from a JSON string
group_vm_instance = GroupVM.from_json(json)
# print the JSON string representation of the object
print GroupVM.to_json()

# convert the object into a dict
group_vm_dict = group_vm_instance.to_dict()
# create an instance of GroupVM from a dict
group_vm_form_dict = group_vm.from_dict(group_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


