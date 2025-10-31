# S3UploadTaskVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**access_key** | **str** |  | [optional] 
**bucket_name** | **str** |  | [optional] 
**destination_folder** | **str** |  | [optional] 
**use_aws** | **bool** |  | [optional] 
**enable_ssl** | **bool** |  | [optional] 
**region** | **str** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.s3_upload_task_vm import S3UploadTaskVM

# TODO update the JSON string below
json = "{}"
# create an instance of S3UploadTaskVM from a JSON string
s3_upload_task_vm_instance = S3UploadTaskVM.from_json(json)
# print the JSON string representation of the object
print S3UploadTaskVM.to_json()

# convert the object into a dict
s3_upload_task_vm_dict = s3_upload_task_vm_instance.to_dict()
# create an instance of S3UploadTaskVM from a dict
s3_upload_task_vm_form_dict = s3_upload_task_vm.from_dict(s3_upload_task_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


