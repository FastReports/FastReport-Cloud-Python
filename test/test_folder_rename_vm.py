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
from fastreport_cloud_sdk.models.folder_rename_vm import FolderRenameVM  # noqa: E501
from fastreport_cloud_sdk.rest import ApiException

class TestFolderRenameVM(unittest.TestCase):
    """FolderRenameVM unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FolderRenameVM
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = fastreport_cloud_sdk.models.folder_rename_vm.FolderRenameVM()  # noqa: E501
        if include_optional :
            return FolderRenameVM(
                name = ''
            )
        else :
            return FolderRenameVM(
        )

    def testFolderRenameVM(self):
        """Test FolderRenameVM"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()