# GroupsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**List[GroupVM]**](GroupVM.md) |  | [optional] 
**count** | **int** |  | [optional] 
**skip** | **int** |  | [optional] 
**take** | **int** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.groups_vm import GroupsVM

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsVM from a JSON string
groups_vm_instance = GroupsVM.from_json(json)
# print the JSON string representation of the object
print GroupsVM.to_json()

# convert the object into a dict
groups_vm_dict = groups_vm_instance.to_dict()
# create an instance of GroupsVM from a dict
groups_vm_form_dict = groups_vm.from_dict(groups_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


