# SubscriptionPermissionCRUDVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create** | [**SubscriptionCreate**](SubscriptionCreate.md) |  | [optional] 
**delete** | [**SubscriptionDelete**](SubscriptionDelete.md) |  | [optional] 
**execute** | [**SubscriptionExecute**](SubscriptionExecute.md) |  | [optional] 
**get** | [**SubscriptionGet**](SubscriptionGet.md) |  | [optional] 
**update** | [**SubscriptionUpdate**](SubscriptionUpdate.md) |  | [optional] 
**administrate** | [**SubscriptionAdministrate**](SubscriptionAdministrate.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.subscription_permission_crudvm import SubscriptionPermissionCRUDVM

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPermissionCRUDVM from a JSON string
subscription_permission_crudvm_instance = SubscriptionPermissionCRUDVM.from_json(json)
# print the JSON string representation of the object
print SubscriptionPermissionCRUDVM.to_json()

# convert the object into a dict
subscription_permission_crudvm_dict = subscription_permission_crudvm_instance.to_dict()
# create an instance of SubscriptionPermissionCRUDVM from a dict
subscription_permission_crudvm_form_dict = subscription_permission_crudvm.from_dict(subscription_permission_crudvm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


