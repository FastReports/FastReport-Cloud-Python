# UpdateSubscriptionPermissionsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_permissions** | [**SubscriptionPermissionsCRUDVM**](SubscriptionPermissionsCRUDVM.md) |  | 
**administrate** | [**SubscriptionAdministrate**](SubscriptionAdministrate.md) |  | 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.update_subscription_permissions_vm import UpdateSubscriptionPermissionsVM

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSubscriptionPermissionsVM from a JSON string
update_subscription_permissions_vm_instance = UpdateSubscriptionPermissionsVM.from_json(json)
# print the JSON string representation of the object
print UpdateSubscriptionPermissionsVM.to_json()

# convert the object into a dict
update_subscription_permissions_vm_dict = update_subscription_permissions_vm_instance.to_dict()
# create an instance of UpdateSubscriptionPermissionsVM from a dict
update_subscription_permissions_vm_form_dict = update_subscription_permissions_vm.from_dict(update_subscription_permissions_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


