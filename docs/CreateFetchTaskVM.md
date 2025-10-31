# CreateFetchTaskVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_source_id** | **str** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.create_fetch_task_vm import CreateFetchTaskVM

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFetchTaskVM from a JSON string
create_fetch_task_vm_instance = CreateFetchTaskVM.from_json(json)
# print the JSON string representation of the object
print CreateFetchTaskVM.to_json()

# convert the object into a dict
create_fetch_task_vm_dict = create_fetch_task_vm_instance.to_dict()
# create an instance of CreateFetchTaskVM from a dict
create_fetch_task_vm_form_dict = create_fetch_task_vm.from_dict(create_fetch_task_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


