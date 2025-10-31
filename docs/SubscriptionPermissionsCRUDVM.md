# SubscriptionPermissionsCRUDVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_id** | **str** |  | [optional] 
**owner** | [**SubscriptionPermissionCRUDVM**](SubscriptionPermissionCRUDVM.md) |  | [optional] 
**groups** | [**Dict[str, SubscriptionPermissionCRUDVM]**](SubscriptionPermissionCRUDVM.md) |  | [optional] 
**other** | [**SubscriptionPermissionCRUDVM**](SubscriptionPermissionCRUDVM.md) |  | [optional] 
**anon** | [**SubscriptionPermissionCRUDVM**](SubscriptionPermissionCRUDVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.subscription_permissions_crudvm import SubscriptionPermissionsCRUDVM

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPermissionsCRUDVM from a JSON string
subscription_permissions_crudvm_instance = SubscriptionPermissionsCRUDVM.from_json(json)
# print the JSON string representation of the object
print SubscriptionPermissionsCRUDVM.to_json()

# convert the object into a dict
subscription_permissions_crudvm_dict = subscription_permissions_crudvm_instance.to_dict()
# create an instance of SubscriptionPermissionsCRUDVM from a dict
subscription_permissions_crudvm_form_dict = subscription_permissions_crudvm.from_dict(subscription_permissions_crudvm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


