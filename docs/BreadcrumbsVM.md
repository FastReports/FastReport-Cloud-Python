# BreadcrumbsVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breadcrumbs** | [**List[BreadcrumbsModel]**](BreadcrumbsModel.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.breadcrumbs_vm import BreadcrumbsVM

# TODO update the JSON string below
json = "{}"
# create an instance of BreadcrumbsVM from a JSON string
breadcrumbs_vm_instance = BreadcrumbsVM.from_json(json)
# print the JSON string representation of the object
print BreadcrumbsVM.to_json()

# convert the object into a dict
breadcrumbs_vm_dict = breadcrumbs_vm_instance.to_dict()
# create an instance of BreadcrumbsVM from a dict
breadcrumbs_vm_form_dict = breadcrumbs_vm.from_dict(breadcrumbs_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


