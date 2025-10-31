# SubscriptionPermissionsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**SubscriptionPermissionsCRUDVM**](SubscriptionPermissionsCRUDVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.subscription_permissions_vm import SubscriptionPermissionsVM

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPermissionsVM from a JSON string
subscription_permissions_vm_instance = SubscriptionPermissionsVM.from_json(json)
# print the JSON string representation of the object
print SubscriptionPermissionsVM.to_json()

# convert the object into a dict
subscription_permissions_vm_dict = subscription_permissions_vm_instance.to_dict()
# create an instance of SubscriptionPermissionsVM from a dict
subscription_permissions_vm_form_dict = subscription_permissions_vm.from_dict(subscription_permissions_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


