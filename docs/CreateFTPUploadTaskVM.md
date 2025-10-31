# CreateFTPUploadTaskVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive** | **bool** |  | [optional] 
**archive_name** | **str** |  | [optional] 
**destination_folder** | **str** |  | [optional] 
**ftp_host** | **str** |  | [optional] 
**ftp_password** | **str** |  | [optional] 
**ftp_port** | **int** |  | [optional] 
**ftp_username** | **str** |  | [optional] 
**use_sftp** | **bool** |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.create_ftp_upload_task_vm import CreateFTPUploadTaskVM

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFTPUploadTaskVM from a JSON string
create_ftp_upload_task_vm_instance = CreateFTPUploadTaskVM.from_json(json)
# print the JSON string representation of the object
print CreateFTPUploadTaskVM.to_json()

# convert the object into a dict
create_ftp_upload_task_vm_dict = create_ftp_upload_task_vm_instance.to_dict()
# create an instance of CreateFTPUploadTaskVM from a dict
create_ftp_upload_task_vm_form_dict = create_ftp_upload_task_vm.from_dict(create_ftp_upload_task_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


