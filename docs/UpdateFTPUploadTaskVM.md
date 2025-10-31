# UpdateFTPUploadTaskVM


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
from fastreport_cloud_sdk.models.update_ftp_upload_task_vm import UpdateFTPUploadTaskVM

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFTPUploadTaskVM from a JSON string
update_ftp_upload_task_vm_instance = UpdateFTPUploadTaskVM.from_json(json)
# print the JSON string representation of the object
print UpdateFTPUploadTaskVM.to_json()

# convert the object into a dict
update_ftp_upload_task_vm_dict = update_ftp_upload_task_vm_instance.to_dict()
# create an instance of UpdateFTPUploadTaskVM from a dict
update_ftp_upload_task_vm_form_dict = update_ftp_upload_task_vm.from_dict(update_ftp_upload_task_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


