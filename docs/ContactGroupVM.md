# ContactGroupVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**created_time** | **datetime** |  | [optional] 
**creator_user_id** | **str** |  | [optional] 
**edited_time** | **datetime** |  | [optional] 
**editor_user_id** | **str** |  | [optional] 

## Example

```python
from fastreport_cloud_sdk.models.contact_group_vm import ContactGroupVM

# TODO update the JSON string below
json = "{}"
# create an instance of ContactGroupVM from a JSON string
contact_group_vm_instance = ContactGroupVM.from_json(json)
# print the JSON string representation of the object
print ContactGroupVM.to_json()

# convert the object into a dict
contact_group_vm_dict = contact_group_vm_instance.to_dict()
# create an instance of ContactGroupVM from a dict
contact_group_vm_form_dict = contact_group_vm.from_dict(contact_group_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


