# GroupUsersVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[GroupUserVM]**](GroupUserVM.md) |  | [optional] 
**count** | **int** |  | [optional] 
**take** | **int** |  | [optional] 
**skip** | **int** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.group_users_vm import GroupUsersVM

# TODO update the JSON string below
json = "{}"
# create an instance of GroupUsersVM from a JSON string
group_users_vm_instance = GroupUsersVM.from_json(json)
# print the JSON string representation of the object
print GroupUsersVM.to_json()

# convert the object into a dict
group_users_vm_dict = group_users_vm_instance.to_dict()
# create an instance of GroupUsersVM from a dict
group_users_vm_form_dict = group_users_vm.from_dict(group_users_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


