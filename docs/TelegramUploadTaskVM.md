# TelegramUploadTaskVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contacts** | **List[str]** |  | [optional] 
**text** | **str** |  | [optional] 
**parse_mode** | **str** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.telegram_upload_task_vm import TelegramUploadTaskVM

# TODO update the JSON string below
json = "{}"
# create an instance of TelegramUploadTaskVM from a JSON string
telegram_upload_task_vm_instance = TelegramUploadTaskVM.from_json(json)
# print the JSON string representation of the object
print TelegramUploadTaskVM.to_json()

# convert the object into a dict
telegram_upload_task_vm_dict = telegram_upload_task_vm_instance.to_dict()
# create an instance of TelegramUploadTaskVM from a dict
telegram_upload_task_vm_form_dict = telegram_upload_task_vm.from_dict(telegram_upload_task_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


