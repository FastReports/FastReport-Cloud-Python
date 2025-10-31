# UpdateWebhookTaskVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | **Dict[str, Optional[str]]** |  | [optional] 
**url** | **str** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.update_webhook_task_vm import UpdateWebhookTaskVM

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWebhookTaskVM from a JSON string
update_webhook_task_vm_instance = UpdateWebhookTaskVM.from_json(json)
# print the JSON string representation of the object
print UpdateWebhookTaskVM.to_json()

# convert the object into a dict
update_webhook_task_vm_dict = update_webhook_task_vm_instance.to_dict()
# create an instance of UpdateWebhookTaskVM from a dict
update_webhook_task_vm_form_dict = update_webhook_task_vm.from_dict(update_webhook_task_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


