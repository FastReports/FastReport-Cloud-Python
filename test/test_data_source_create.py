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
from fastreport_cloud_sdk.models.data_source_create import DataSourceCreate  # noqa: E501
from fastreport_cloud_sdk.rest import ApiException

class TestDataSourceCreate(unittest.TestCase):
    """DataSourceCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DataSourceCreate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = fastreport_cloud_sdk.models.data_source_create.DataSourceCreate()  # noqa: E501
        if include_optional :
            return DataSourceCreate(
            )
        else :
            return DataSourceCreate(
        )

    def testDataSourceCreate(self):
        """Test DataSourceCreate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
