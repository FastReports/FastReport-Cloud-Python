# SubscriptionVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**current** | [**SubscriptionPeriodVM**](SubscriptionPeriodVM.md) |  | [optional] 
**old** | [**List[SubscriptionPeriodVM]**](SubscriptionPeriodVM.md) |  | [optional] 
**templates_folder** | [**SubscriptionFolder**](SubscriptionFolder.md) |  | [optional] 
**reports_folder** | [**SubscriptionFolder**](SubscriptionFolder.md) |  | [optional] 
**exports_folder** | [**SubscriptionFolder**](SubscriptionFolder.md) |  | [optional] 
**preview_type** | [**PreviewType**](PreviewType.md) |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**domains** | **List[str]** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.subscription_vm import SubscriptionVM

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionVM from a JSON string
subscription_vm_instance = SubscriptionVM.from_json(json)
# print the JSON string representation of the object
print SubscriptionVM.to_json()

# convert the object into a dict
subscription_vm_dict = subscription_vm_instance.to_dict()
# create an instance of SubscriptionVM from a dict
subscription_vm_form_dict = subscription_vm.from_dict(subscription_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


