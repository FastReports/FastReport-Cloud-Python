# RestrictionsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expired_at** | **datetime** |  | [optional] 
**valid_to** | **datetime** |  | [optional] 
**pages_count** | **int** |  | [optional] 
**admins_count** | **int** |  | [optional] 
**subscriptions_count** | **int** |  | [optional] 
**designer_for_anons** | **bool** |  | [optional] 
**white_label** | **bool** |  | [optional] 
**is_demo** | **bool** |  | [optional] 
**sharing_enabled** | **bool** |  | [optional] 
**scheduler_enabled** | **bool** |  | [optional] 
**max_users_count** | **int** |  | [optional] 
**max_data_sources_count** | **int** |  | [optional] 
**max_groups_count** | **int** |  | [optional] 
**license** | **str** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.restrictions_vm import RestrictionsVM

# TODO update the JSON string below
json = "{}"
# create an instance of RestrictionsVM from a JSON string
restrictions_vm_instance = RestrictionsVM.from_json(json)
# print the JSON string representation of the object
print RestrictionsVM.to_json()

# convert the object into a dict
restrictions_vm_dict = restrictions_vm_instance.to_dict()
# create an instance of RestrictionsVM from a dict
restrictions_vm_form_dict = restrictions_vm.from_dict(restrictions_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


