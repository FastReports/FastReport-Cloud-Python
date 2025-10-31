# AuthConfigVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_local** | **bool** |  | [optional] 
**use_open_id** | **bool** |  | [optional] 
**authority** | **str** |  | [optional] 
**allow_local_sign_up** | **bool** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.auth_config_vm import AuthConfigVM

# TODO update the JSON string below
json = "{}"
# create an instance of AuthConfigVM from a JSON string
auth_config_vm_instance = AuthConfigVM.from_json(json)
# print the JSON string representation of the object
print AuthConfigVM.to_json()

# convert the object into a dict
auth_config_vm_dict = auth_config_vm_instance.to_dict()
# create an instance of AuthConfigVM from a dict
auth_config_vm_form_dict = auth_config_vm.from_dict(auth_config_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


