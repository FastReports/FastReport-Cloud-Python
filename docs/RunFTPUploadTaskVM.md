# RunFTPUploadTaskVM


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
from fastreport_cloud_sdk.models.run_ftp_upload_task_vm import RunFTPUploadTaskVM

# TODO update the JSON string below
json = "{}"
# create an instance of RunFTPUploadTaskVM from a JSON string
run_ftp_upload_task_vm_instance = RunFTPUploadTaskVM.from_json(json)
# print the JSON string representation of the object
print RunFTPUploadTaskVM.to_json()

# convert the object into a dict
run_ftp_upload_task_vm_dict = run_ftp_upload_task_vm_instance.to_dict()
# create an instance of RunFTPUploadTaskVM from a dict
run_ftp_upload_task_vm_form_dict = run_ftp_upload_task_vm.from_dict(run_ftp_upload_task_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


