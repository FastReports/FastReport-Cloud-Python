# ApiKeyVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**expired** | **datetime** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.api_key_vm import ApiKeyVM

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyVM from a JSON string
api_key_vm_instance = ApiKeyVM.from_json(json)
# print the JSON string representation of the object
print ApiKeyVM.to_json()

# convert the object into a dict
api_key_vm_dict = api_key_vm_instance.to_dict()
# create an instance of ApiKeyVM from a dict
api_key_vm_form_dict = api_key_vm.from_dict(api_key_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


