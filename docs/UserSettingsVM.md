# UserSettingsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_visibility** | [**ProfileVisibility**](ProfileVisibility.md) |  | [optional] 
**default_subscription** | **str** |  | [optional] 
**show_hidden_files_and_folders** | **bool** |  | [optional] 
**sla_accepted_date_time** | **datetime** |  | [optional] 
**subscribed_notifications** | [**List[AuditType]**](AuditType.md) |  | [optional] 
**preview_type** | [**PreviewType**](PreviewType.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.user_settings_vm import UserSettingsVM

# TODO update the JSON string below
json = "{}"
# create an instance of UserSettingsVM from a JSON string
user_settings_vm_instance = UserSettingsVM.from_json(json)
# print the JSON string representation of the object
print UserSettingsVM.to_json()

# convert the object into a dict
user_settings_vm_dict = user_settings_vm_instance.to_dict()
# create an instance of UserSettingsVM from a dict
user_settings_vm_form_dict = user_settings_vm.from_dict(user_settings_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


