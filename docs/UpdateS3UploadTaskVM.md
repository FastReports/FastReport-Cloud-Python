# UpdateS3UploadTaskVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**access_key** | **str** |  | [optional] 
**secret_key** | **str** |  | [optional] 
**bucket_name** | **str** |  | [optional] 
**destination_folder** | **str** |  | [optional] 
**use_aws** | **bool** |  | [optional] 
**enable_ssl** | **bool** |  | [optional] 
**region** | **str** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.update_s3_upload_task_vm import UpdateS3UploadTaskVM

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateS3UploadTaskVM from a JSON string
update_s3_upload_task_vm_instance = UpdateS3UploadTaskVM.from_json(json)
# print the JSON string representation of the object
print UpdateS3UploadTaskVM.to_json()

# convert the object into a dict
update_s3_upload_task_vm_dict = update_s3_upload_task_vm_instance.to_dict()
# create an instance of UpdateS3UploadTaskVM from a dict
update_s3_upload_task_vm_form_dict = update_s3_upload_task_vm.from_dict(update_s3_upload_task_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


