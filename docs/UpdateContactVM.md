# UpdateContactVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**groups** | **List[str]** |  | [optional] 
**subscription_id** | **str** |  | [optional] 

## Example

```python
from fastreport_cloud_sdk.models.update_contact_vm import UpdateContactVM

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateContactVM from a JSON string
update_contact_vm_instance = UpdateContactVM.from_json(json)
# print the JSON string representation of the object
print UpdateContactVM.to_json()

# convert the object into a dict
update_contact_vm_dict = update_contact_vm_instance.to_dict()
# create an instance of UpdateContactVM from a dict
update_contact_vm_form_dict = update_contact_vm.from_dict(update_contact_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


