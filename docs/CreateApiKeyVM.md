# CreateApiKeyVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**expired** | **datetime** |  | 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.create_api_key_vm import CreateApiKeyVM

# TODO update the JSON string below
json = "{}"
# create an instance of CreateApiKeyVM from a JSON string
create_api_key_vm_instance = CreateApiKeyVM.from_json(json)
# print the JSON string representation of the object
print CreateApiKeyVM.to_json()

# convert the object into a dict
create_api_key_vm_dict = create_api_key_vm_instance.to_dict()
# create an instance of CreateApiKeyVM from a dict
create_api_key_vm_form_dict = create_api_key_vm.from_dict(create_api_key_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


