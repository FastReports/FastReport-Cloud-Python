# CreateEmailTaskVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 
**enable_ssl** | **bool** |  | [optional] 
**var_from** | **str** |  | [optional] 
**is_body_html** | **bool** |  | [optional] 
**password** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**server** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**to** | **List[str]** |  | [optional] 
**username** | **str** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.create_email_task_vm import CreateEmailTaskVM

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEmailTaskVM from a JSON string
create_email_task_vm_instance = CreateEmailTaskVM.from_json(json)
# print the JSON string representation of the object
print CreateEmailTaskVM.to_json()

# convert the object into a dict
create_email_task_vm_dict = create_email_task_vm_instance.to_dict()
# create an instance of CreateEmailTaskVM from a dict
create_email_task_vm_form_dict = create_email_task_vm.from_dict(create_email_task_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


