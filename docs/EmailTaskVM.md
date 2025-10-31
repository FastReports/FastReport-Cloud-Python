# EmailTaskVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 
**enable_ssl** | **bool** |  | [optional] 
**var_from** | **str** |  | [optional] 
**is_body_html** | **bool** |  | [optional] 
**port** | **int** |  | [optional] 
**server** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**to** | **List[str]** |  | [optional] 
**username** | **str** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.email_task_vm import EmailTaskVM

# TODO update the JSON string below
json = "{}"
# create an instance of EmailTaskVM from a JSON string
email_task_vm_instance = EmailTaskVM.from_json(json)
# print the JSON string representation of the object
print EmailTaskVM.to_json()

# convert the object into a dict
email_task_vm_dict = email_task_vm_instance.to_dict()
# create an instance of EmailTaskVM from a dict
email_task_vm_form_dict = email_task_vm.from_dict(email_task_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


