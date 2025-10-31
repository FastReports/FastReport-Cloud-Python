# ReportInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**creator_version** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**modified** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**picture** | **bytearray** |  | [optional] 
**preview_picture_ratio** | **float** |  | [optional] 
**save_mode** | [**SaveMode**](SaveMode.md) |  | [optional] 
**save_preview_picture** | **bool** |  | [optional] 
**tag** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from fastreport_cloud_sdk.models.report_info import ReportInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ReportInfo from a JSON string
report_info_instance = ReportInfo.from_json(json)
# print the JSON string representation of the object
print ReportInfo.to_json()

# convert the object into a dict
report_info_dict = report_info_instance.to_dict()
# create an instance of ReportInfo from a dict
report_info_form_dict = report_info.from_dict(report_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


