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
from fastreport_cloud_sdk.models.subscription_users_vm import SubscriptionUsersVM  # noqa: E501
from fastreport_cloud_sdk.rest import ApiException

class TestSubscriptionUsersVM(unittest.TestCase):
    """SubscriptionUsersVM unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SubscriptionUsersVM
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = fastreport_cloud_sdk.models.subscription_users_vm.SubscriptionUsersVM()  # noqa: E501
        if include_optional :
            return SubscriptionUsersVM(
                users = [
                    fastreport_cloud_sdk.models.subscription_user_vm.SubscriptionUserVM(
                        user_id = '', 
                        groups = [
                            fastreport_cloud_sdk.models.group_vm.GroupVM(
                                id = '', 
                                name = '', 
                                subscription_id = '', )
                            ], )
                    ], 
                count = 56, 
                take = 56, 
                skip = 56
            )
        else :
            return SubscriptionUsersVM(
        )

    def testSubscriptionUsersVM(self):
        """Test SubscriptionUsersVM"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()