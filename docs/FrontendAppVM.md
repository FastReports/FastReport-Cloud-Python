# FrontendAppVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mixins** | [**AppMixinsVM**](AppMixinsVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.frontend_app_vm import FrontendAppVM

# TODO update the JSON string below
json = "{}"
# create an instance of FrontendAppVM from a JSON string
frontend_app_vm_instance = FrontendAppVM.from_json(json)
# print the JSON string representation of the object
print FrontendAppVM.to_json()

# convert the object into a dict
frontend_app_vm_dict = frontend_app_vm_instance.to_dict()
# create an instance of FrontendAppVM from a dict
frontend_app_vm_form_dict = frontend_app_vm.from_dict(frontend_app_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


