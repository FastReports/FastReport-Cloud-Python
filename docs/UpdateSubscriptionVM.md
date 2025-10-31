# UpdateSubscriptionVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**domains** | **List[str]** |  | [optional] 
**preview_type** | [**PreviewType**](PreviewType.md) |  | [optional] 
**default_permissions** | [**DefaultPermissionsVM**](DefaultPermissionsVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.update_subscription_vm import UpdateSubscriptionVM

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSubscriptionVM from a JSON string
update_subscription_vm_instance = UpdateSubscriptionVM.from_json(json)
# print the JSON string representation of the object
print UpdateSubscriptionVM.to_json()

# convert the object into a dict
update_subscription_vm_dict = update_subscription_vm_instance.to_dict()
# create an instance of UpdateSubscriptionVM from a dict
update_subscription_vm_form_dict = update_subscription_vm.from_dict(update_subscription_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


