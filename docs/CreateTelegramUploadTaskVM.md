# CreateTelegramUploadTaskVM


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
from fastreport_cloud_sdk.models.create_telegram_upload_task_vm import CreateTelegramUploadTaskVM

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTelegramUploadTaskVM from a JSON string
create_telegram_upload_task_vm_instance = CreateTelegramUploadTaskVM.from_json(json)
# print the JSON string representation of the object
print CreateTelegramUploadTaskVM.to_json()

# convert the object into a dict
create_telegram_upload_task_vm_dict = create_telegram_upload_task_vm_instance.to_dict()
# create an instance of CreateTelegramUploadTaskVM from a dict
create_telegram_upload_task_vm_form_dict = create_telegram_upload_task_vm.from_dict(create_telegram_upload_task_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


