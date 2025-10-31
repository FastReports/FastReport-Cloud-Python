# UsersVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[UserVM]**](UserVM.md) |  | [optional] 
**count** | **int** |  | [optional] 
**skip** | **int** |  | [optional] 
**take** | **int** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.users_vm import UsersVM

# TODO update the JSON string below
json = "{}"
# create an instance of UsersVM from a JSON string
users_vm_instance = UsersVM.from_json(json)
# print the JSON string representation of the object
print UsersVM.to_json()

# convert the object into a dict
users_vm_dict = users_vm_instance.to_dict()
# create an instance of UsersVM from a dict
users_vm_form_dict = users_vm.from_dict(users_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


