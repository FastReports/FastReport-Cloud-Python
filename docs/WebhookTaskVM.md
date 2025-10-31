# WebhookTaskVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | **Dict[str, Optional[str]]** |  | [optional] 
**url** | **str** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.webhook_task_vm import WebhookTaskVM

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookTaskVM from a JSON string
webhook_task_vm_instance = WebhookTaskVM.from_json(json)
# print the JSON string representation of the object
print WebhookTaskVM.to_json()

# convert the object into a dict
webhook_task_vm_dict = webhook_task_vm_instance.to_dict()
# create an instance of WebhookTaskVM from a dict
webhook_task_vm_form_dict = webhook_task_vm.from_dict(webhook_task_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


