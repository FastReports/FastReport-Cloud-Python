# CreateS3UploadTaskVM


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
from fastreport_cloud_sdk.models.create_s3_upload_task_vm import CreateS3UploadTaskVM

# TODO update the JSON string below
json = "{}"
# create an instance of CreateS3UploadTaskVM from a JSON string
create_s3_upload_task_vm_instance = CreateS3UploadTaskVM.from_json(json)
# print the JSON string representation of the object
print CreateS3UploadTaskVM.to_json()

# convert the object into a dict
create_s3_upload_task_vm_dict = create_s3_upload_task_vm_instance.to_dict()
# create an instance of CreateS3UploadTaskVM from a dict
create_s3_upload_task_vm_form_dict = create_s3_upload_task_vm.from_dict(create_s3_upload_task_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


