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
from fastreport_cloud_sdk.models.create_subscription_invite_vm import CreateSubscriptionInviteVM  # noqa: E501
from fastreport_cloud_sdk.rest import ApiException

class TestCreateSubscriptionInviteVM(unittest.TestCase):
    """CreateSubscriptionInviteVM unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateSubscriptionInviteVM
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = fastreport_cloud_sdk.models.create_subscription_invite_vm.CreateSubscriptionInviteVM()  # noqa: E501
        if include_optional :
            return CreateSubscriptionInviteVM(
                usages = 56, 
                durable = True, 
                expired_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return CreateSubscriptionInviteVM(
        )

    def testCreateSubscriptionInviteVM(self):
        """Test CreateSubscriptionInviteVM"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()