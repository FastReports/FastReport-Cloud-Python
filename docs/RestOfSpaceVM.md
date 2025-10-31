# RestOfSpaceVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rest_of_space** | **int** |  | [optional] 
**subscription_plan** | [**SubscriptionPlanVM**](SubscriptionPlanVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.rest_of_space_vm import RestOfSpaceVM

# TODO update the JSON string below
json = "{}"
# create an instance of RestOfSpaceVM from a JSON string
rest_of_space_vm_instance = RestOfSpaceVM.from_json(json)
# print the JSON string representation of the object
print RestOfSpaceVM.to_json()

# convert the object into a dict
rest_of_space_vm_dict = rest_of_space_vm_instance.to_dict()
# create an instance of RestOfSpaceVM from a dict
rest_of_space_vm_form_dict = rest_of_space_vm.from_dict(rest_of_space_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


