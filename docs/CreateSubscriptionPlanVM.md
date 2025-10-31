# CreateSubscriptionPlanVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **bool** |  | [optional] 
**display_name** | **str** |  | [optional] 
**time_period_type** | [**TimePeriodType**](TimePeriodType.md) |  | [optional] 
**time_period** | **int** |  | [optional] 
**templates_space_limit** | **int** |  | [optional] 
**reports_space_limit** | **int** |  | [optional] 
**exports_space_limit** | **int** |  | [optional] 
**fonts_space_limit** | **int** |  | [optional] 
**file_upload_size_limit** | **int** |  | [optional] 
**data_source_limit** | **int** |  | [optional] 
**max_users_count** | **int** |  | [optional] 
**group_limit** | **int** |  | [optional] 
**online_designer** | **bool** |  | [optional] 
**is_demo** | **bool** |  | [optional] 
**url_to_buy** | **str** |  | [optional] 
**unlimited_page** | **bool** |  | [optional] 
**page_limit** | **int** |  | [optional] 
**readonly_time_limit_type** | [**TimePeriodType**](TimePeriodType.md) |  | [optional] 
**readonly_time_limit** | **int** |  | [optional] 
**tasks** | [**TaskSettingsVM**](TaskSettingsVM.md) |  | [optional] 
**t** | **str** |  | 

## Example

```python
from fastreport_cloud_sdk.models.create_subscription_plan_vm import CreateSubscriptionPlanVM

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscriptionPlanVM from a JSON string
create_subscription_plan_vm_instance = CreateSubscriptionPlanVM.from_json(json)
# print the JSON string representation of the object
print CreateSubscriptionPlanVM.to_json()

# convert the object into a dict
create_subscription_plan_vm_dict = create_subscription_plan_vm_instance.to_dict()
# create an instance of CreateSubscriptionPlanVM from a dict
create_subscription_plan_vm_form_dict = create_subscription_plan_vm.from_dict(create_subscription_plan_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


