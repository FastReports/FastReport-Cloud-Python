# UpdateUserSettingsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_visibility** | [**ProfileVisibility**](ProfileVisibility.md) |  | [optional] 
**default_subscription** | **str** |  | [optional] 
**show_hidden_files_and_folders** | **bool** |  | [optional] 
**subscribed_notifications** | [**List[AuditType]**](AuditType.md) |  | [optional] 
**preview_type** | [**PreviewType**](PreviewType.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.update_user_settings_vm import UpdateUserSettingsVM

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserSettingsVM from a JSON string
update_user_settings_vm_instance = UpdateUserSettingsVM.from_json(json)
# print the JSON string representation of the object
print UpdateUserSettingsVM.to_json()

# convert the object into a dict
update_user_settings_vm_dict = update_user_settings_vm_instance.to_dict()
# create an instance of UpdateUserSettingsVM from a dict
update_user_settings_vm_form_dict = update_user_settings_vm.from_dict(update_user_settings_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


