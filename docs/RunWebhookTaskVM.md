# RunWebhookTaskVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | **Dict[str, Optional[str]]** |  | [optional] 
**url** | **str** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.run_webhook_task_vm import RunWebhookTaskVM

# TODO update the JSON string below
json = "{}"
# create an instance of RunWebhookTaskVM from a JSON string
run_webhook_task_vm_instance = RunWebhookTaskVM.from_json(json)
# print the JSON string representation of the object
print RunWebhookTaskVM.to_json()

# convert the object into a dict
run_webhook_task_vm_dict = run_webhook_task_vm_instance.to_dict()
# create an instance of RunWebhookTaskVM from a dict
run_webhook_task_vm_form_dict = run_webhook_task_vm.from_dict(run_webhook_task_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


