# SubscriptionFolder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_id** | **str** |  | [optional] 
**bytes_used** | **int** |  | [optional] 

## Example

```python
from fastreport_cloud_sdk.models.subscription_folder import SubscriptionFolder

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionFolder from a JSON string
subscription_folder_instance = SubscriptionFolder.from_json(json)
# print the JSON string representation of the object
print SubscriptionFolder.to_json()

# convert the object into a dict
subscription_folder_dict = subscription_folder_instance.to_dict()
# create an instance of SubscriptionFolder from a dict
subscription_folder_form_dict = subscription_folder.from_dict(subscription_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


