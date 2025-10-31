# TaskSettingsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_scheduler_enabled** | **bool** |  | [optional] 
**prepare** | **bool** |  | [optional] 
**export_template** | **bool** |  | [optional] 
**export_report** | **bool** |  | [optional] 
**send_via_email** | **bool** |  | [optional] 
**upload_to_ftp** | **bool** |  | [optional] 
**upload_to_s3** | **bool** |  | [optional] 
**upload_to_telegram** | **bool** |  | [optional] 
**send_via_webhook** | **bool** |  | [optional] 
**fetch_data** | **bool** |  | [optional] 
**thumbnail_report** | **bool** |  | [optional] 
**thumbnail_template** | **bool** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.task_settings_vm import TaskSettingsVM

# TODO update the JSON string below
json = "{}"
# create an instance of TaskSettingsVM from a JSON string
task_settings_vm_instance = TaskSettingsVM.from_json(json)
# print the JSON string representation of the object
print TaskSettingsVM.to_json()

# convert the object into a dict
task_settings_vm_dict = task_settings_vm_instance.to_dict()
# create an instance of TaskSettingsVM from a dict
task_settings_vm_form_dict = task_settings_vm.from_dict(task_settings_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


