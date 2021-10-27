# coding: utf-8

"""
    FastReport Cloud

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import fastreport_cloud_sdk
from fastreport_cloud_sdk.models.subscription_permission_subscription_create_subscription_get_subscription_update_subscription_delete_subscription_execute_subscription_administrate_permissions import SubscriptionPermissionSubscriptionCreateSubscriptionGetSubscriptionUpdateSubscriptionDeleteSubscriptionExecuteSubscriptionAdministratePermissions  # noqa: E501
from fastreport_cloud_sdk.rest import ApiException

class TestSubscriptionPermissionSubscriptionCreateSubscriptionGetSubscriptionUpdateSubscriptionDeleteSubscriptionExecuteSubscriptionAdministratePermissions(unittest.TestCase):
    """SubscriptionPermissionSubscriptionCreateSubscriptionGetSubscriptionUpdateSubscriptionDeleteSubscriptionExecuteSubscriptionAdministratePermissions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SubscriptionPermissionSubscriptionCreateSubscriptionGetSubscriptionUpdateSubscriptionDeleteSubscriptionExecuteSubscriptionAdministratePermissions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = fastreport_cloud_sdk.models.subscription_permission_subscription_create_subscription_get_subscription_update_subscription_delete_subscription_execute_subscription_administrate_permissions.SubscriptionPermissionSubscriptionCreateSubscriptionGetSubscriptionUpdateSubscriptionDeleteSubscriptionExecuteSubscriptionAdministratePermissions()  # noqa: E501
        if include_optional :
            return SubscriptionPermissionSubscriptionCreateSubscriptionGetSubscriptionUpdateSubscriptionDeleteSubscriptionExecuteSubscriptionAdministratePermissions(
                owner_id = 'f325375e-30fc-ba00-1731-c574773100bf', 
                owner = fastreport_cloud_sdk.models.subscription_permission.SubscriptionPermission(), 
                groups = {
                    'key' : fastreport_cloud_sdk.models.subscription_permission.SubscriptionPermission()
                    }, 
                other = fastreport_cloud_sdk.models.subscription_permission.SubscriptionPermission(), 
                anon = fastreport_cloud_sdk.models.subscription_permission.SubscriptionPermission()
            )
        else :
            return SubscriptionPermissionSubscriptionCreateSubscriptionGetSubscriptionUpdateSubscriptionDeleteSubscriptionExecuteSubscriptionAdministratePermissions(
        )

    def testSubscriptionPermissionSubscriptionCreateSubscriptionGetSubscriptionUpdateSubscriptionDeleteSubscriptionExecuteSubscriptionAdministratePermissions(self):
        """Test SubscriptionPermissionSubscriptionCreateSubscriptionGetSubscriptionUpdateSubscriptionDeleteSubscriptionExecuteSubscriptionAdministratePermissions"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
