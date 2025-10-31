# ServerConfigurationVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**logo_link** | **str** |  | [optional] 
**favicon_link** | **str** |  | [optional] 
**copyright** | **str** |  | [optional] 
**corporate_server_mode** | **bool** |  | [optional] 
**last_sla_version** | **datetime** |  | [optional] 
**is_disabled** | **bool** |  | [optional] 
**frontend** | [**FrontendAppVM**](FrontendAppVM.md) |  | [optional] 
**invariant_locale** | **str** |  | [optional] 
**auth** | [**AuthConfigVM**](AuthConfigVM.md) |  | [optional] 
**designer_for_anons** | **bool** |  | [optional] 
**sla_link** | **str** |  | [optional] 
**first_steps_video_link** | **str** |  | [optional] 
**about_link** | **str** |  | [optional] 
**home_page_link** | **str** |  | [optional] 
**auth_server_name** | **str** |  | [optional] 
**update_workspace_link** | **str** |  | [optional] 
**sharing_enabled** | **bool** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.server_configuration_vm import ServerConfigurationVM

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigurationVM from a JSON string
server_configuration_vm_instance = ServerConfigurationVM.from_json(json)
# print the JSON string representation of the object
print ServerConfigurationVM.to_json()

# convert the object into a dict
server_configuration_vm_dict = server_configuration_vm_instance.to_dict()
# create an instance of ServerConfigurationVM from a dict
server_configuration_vm_form_dict = server_configuration_vm.from_dict(server_configuration_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


