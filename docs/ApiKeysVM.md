# ApiKeysVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_keys** | [**List[ApiKeyVM]**](ApiKeyVM.md) |  | [optional] 
**count** | **int** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.api_keys_vm import ApiKeysVM

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeysVM from a JSON string
api_keys_vm_instance = ApiKeysVM.from_json(json)
# print the JSON string representation of the object
print ApiKeysVM.to_json()

# convert the object into a dict
api_keys_vm_dict = api_keys_vm_instance.to_dict()
# create an instance of ApiKeysVM from a dict
api_keys_vm_form_dict = api_keys_vm.from_dict(api_keys_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


