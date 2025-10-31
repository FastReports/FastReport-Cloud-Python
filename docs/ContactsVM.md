# ContactsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contacts** | [**List[ContactVM]**](ContactVM.md) |  | [optional] 
**skip** | **int** |  | [optional] 
**take** | **int** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from fastreport_cloud_sdk.models.contacts_vm import ContactsVM

# TODO update the JSON string below
json = "{}"
# create an instance of ContactsVM from a JSON string
contacts_vm_instance = ContactsVM.from_json(json)
# print the JSON string representation of the object
print ContactsVM.to_json()

# convert the object into a dict
contacts_vm_dict = contacts_vm_instance.to_dict()
# create an instance of ContactsVM from a dict
contacts_vm_form_dict = contacts_vm.from_dict(contacts_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


