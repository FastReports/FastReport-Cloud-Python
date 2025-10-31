# BreadcrumbsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fastreport_cloud_sdk.models.breadcrumbs_model import BreadcrumbsModel

# TODO update the JSON string below
json = "{}"
# create an instance of BreadcrumbsModel from a JSON string
breadcrumbs_model_instance = BreadcrumbsModel.from_json(json)
# print the JSON string representation of the object
print BreadcrumbsModel.to_json()

# convert the object into a dict
breadcrumbs_model_dict = breadcrumbs_model_instance.to_dict()
# create an instance of BreadcrumbsModel from a dict
breadcrumbs_model_form_dict = breadcrumbs_model.from_dict(breadcrumbs_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


