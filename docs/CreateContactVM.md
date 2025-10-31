# CreateContactVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**groups** | **List[str]** |  | [optional] 
**subscription_id** | **str** |  | [optional] 

## Example

```python
from fastreport_cloud_sdk.models.create_contact_vm import CreateContactVM

# TODO update the JSON string below
json = "{}"
# create an instance of CreateContactVM from a JSON string
create_contact_vm_instance = CreateContactVM.from_json(json)
# print the JSON string representation of the object
print CreateContactVM.to_json()

# convert the object into a dict
create_contact_vm_dict = create_contact_vm_instance.to_dict()
# create an instance of CreateContactVM from a dict
create_contact_vm_form_dict = create_contact_vm.from_dict(create_contact_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


