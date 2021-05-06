# coding: utf-8

"""
    FastReport Cloud

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import fastreport_cloud_sdk
from fastreport_cloud_sdk.api.admin_api_keys_api import AdminApiKeysApi  # noqa: E501
from fastreport_cloud_sdk.rest import ApiException


class TestAdminApiKeysApi(unittest.TestCase):
    """AdminApiKeysApi unit test stubs"""

    def setUp(self):
        self.api = fastreport_cloud_sdk.api.admin_api_keys_api.AdminApiKeysApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_admin_api_keys_create_api_key(self):
        """Test case for admin_api_keys_create_api_key

        Create a new apikey, 5 apikeys for user. Hardcoded for ddos.  # noqa: E501
        """
        pass

    def test_admin_api_keys_delete_api_key(self):
        """Test case for admin_api_keys_delete_api_key

        Delete an apikey  # noqa: E501
        """
        pass

    def test_admin_api_keys_get_api_keys(self):
        """Test case for admin_api_keys_get_api_keys

        Returns list with all api keys of a specified user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()