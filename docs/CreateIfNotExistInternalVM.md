# CreateIfNotExistInternalVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**is_admin** | **bool** |  | [optional] 
**provider** | **str** |  | [optional] 
**referesh_token** | **str** |  | [optional] 
**access_token** | **str** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.create_if_not_exist_internal_vm import CreateIfNotExistInternalVM

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIfNotExistInternalVM from a JSON string
create_if_not_exist_internal_vm_instance = CreateIfNotExistInternalVM.from_json(json)
# print the JSON string representation of the object
print CreateIfNotExistInternalVM.to_json()

# convert the object into a dict
create_if_not_exist_internal_vm_dict = create_if_not_exist_internal_vm_instance.to_dict()
# create an instance of CreateIfNotExistInternalVM from a dict
create_if_not_exist_internal_vm_form_dict = create_if_not_exist_internal_vm.from_dict(create_if_not_exist_internal_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


