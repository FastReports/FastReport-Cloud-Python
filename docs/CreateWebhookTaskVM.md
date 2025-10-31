# CreateWebhookTaskVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | **Dict[str, Optional[str]]** |  | [optional] 
**url** | **str** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.create_webhook_task_vm import CreateWebhookTaskVM

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebhookTaskVM from a JSON string
create_webhook_task_vm_instance = CreateWebhookTaskVM.from_json(json)
# print the JSON string representation of the object
print CreateWebhookTaskVM.to_json()

# convert the object into a dict
create_webhook_task_vm_dict = create_webhook_task_vm_instance.to_dict()
# create an instance of CreateWebhookTaskVM from a dict
create_webhook_task_vm_form_dict = create_webhook_task_vm.from_dict(create_webhook_task_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


