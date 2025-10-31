# TaskEnd


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after** | **int** |  | [optional] 
**on** | **datetime** |  | [optional] 

## Example

```python
from fastreport_cloud_sdk.models.task_end import TaskEnd

# TODO update the JSON string below
json = "{}"
# create an instance of TaskEnd from a JSON string
task_end_instance = TaskEnd.from_json(json)
# print the JSON string representation of the object
print TaskEnd.to_json()

# convert the object into a dict
task_end_dict = task_end_instance.to_dict()
# create an instance of TaskEnd from a dict
task_end_form_dict = task_end.from_dict(task_end_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


