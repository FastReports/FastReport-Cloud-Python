# CreateGroupAdminVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_id** | **str** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.create_group_admin_vm import CreateGroupAdminVM

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGroupAdminVM from a JSON string
create_group_admin_vm_instance = CreateGroupAdminVM.from_json(json)
# print the JSON string representation of the object
print CreateGroupAdminVM.to_json()

# convert the object into a dict
create_group_admin_vm_dict = create_group_admin_vm_instance.to_dict()
# create an instance of CreateGroupAdminVM from a dict
create_group_admin_vm_form_dict = create_group_admin_vm.from_dict(create_group_admin_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


