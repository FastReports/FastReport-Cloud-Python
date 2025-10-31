# ContactGroupsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**List[ContactGroupVM]**](ContactGroupVM.md) |  | [optional] 
**skip** | **int** |  | [optional] 
**take** | **int** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from fastreport_cloud_sdk.models.contact_groups_vm import ContactGroupsVM

# TODO update the JSON string below
json = "{}"
# create an instance of ContactGroupsVM from a JSON string
contact_groups_vm_instance = ContactGroupsVM.from_json(json)
# print the JSON string representation of the object
print ContactGroupsVM.to_json()

# convert the object into a dict
contact_groups_vm_dict = contact_groups_vm_instance.to_dict()
# create an instance of ContactGroupsVM from a dict
contact_groups_vm_form_dict = contact_groups_vm.from_dict(contact_groups_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


