# CreateSubscriptionVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_id** | **str** |  | 
**start** | **datetime** |  | [optional] 
**end** | **datetime** |  | [optional] 
**name** | **str** |  | 
**user_id** | **str** |  | 
**tags** | **List[str]** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.create_subscription_vm import CreateSubscriptionVM

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscriptionVM from a JSON string
create_subscription_vm_instance = CreateSubscriptionVM.from_json(json)
# print the JSON string representation of the object
print CreateSubscriptionVM.to_json()

# convert the object into a dict
create_subscription_vm_dict = create_subscription_vm_instance.to_dict()
# create an instance of CreateSubscriptionVM from a dict
create_subscription_vm_form_dict = create_subscription_vm.from_dict(create_subscription_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


