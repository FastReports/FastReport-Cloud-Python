# UpdateSubscriptionPreviewTypeVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preview_type** | [**PreviewType**](PreviewType.md) |  | 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.update_subscription_preview_type_vm import UpdateSubscriptionPreviewTypeVM

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSubscriptionPreviewTypeVM from a JSON string
update_subscription_preview_type_vm_instance = UpdateSubscriptionPreviewTypeVM.from_json(json)
# print the JSON string representation of the object
print UpdateSubscriptionPreviewTypeVM.to_json()

# convert the object into a dict
update_subscription_preview_type_vm_dict = update_subscription_preview_type_vm_instance.to_dict()
# create an instance of UpdateSubscriptionPreviewTypeVM from a dict
update_subscription_preview_type_vm_form_dict = update_subscription_preview_type_vm.from_dict(update_subscription_preview_type_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


