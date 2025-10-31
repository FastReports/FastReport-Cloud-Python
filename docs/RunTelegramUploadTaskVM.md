# RunTelegramUploadTaskVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bot_token** | **str** |  | [optional] 
**contacts** | **List[str]** |  | [optional] 
**text** | **str** |  | [optional] 
**parse_mode** | **str** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.run_telegram_upload_task_vm import RunTelegramUploadTaskVM

# TODO update the JSON string below
json = "{}"
# create an instance of RunTelegramUploadTaskVM from a JSON string
run_telegram_upload_task_vm_instance = RunTelegramUploadTaskVM.from_json(json)
# print the JSON string representation of the object
print RunTelegramUploadTaskVM.to_json()

# convert the object into a dict
run_telegram_upload_task_vm_dict = run_telegram_upload_task_vm_instance.to_dict()
# create an instance of RunTelegramUploadTaskVM from a dict
run_telegram_upload_task_vm_form_dict = run_telegram_upload_task_vm.from_dict(run_telegram_upload_task_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


