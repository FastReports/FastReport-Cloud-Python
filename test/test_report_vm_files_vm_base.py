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
from fastreport_cloud_sdk.models.report_vm_files_vm_base import ReportVMFilesVMBase  # noqa: E501
from fastreport_cloud_sdk.rest import ApiException

class TestReportVMFilesVMBase(unittest.TestCase):
    """ReportVMFilesVMBase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ReportVMFilesVMBase
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = fastreport_cloud_sdk.models.report_vm_files_vm_base.ReportVMFilesVMBase()  # noqa: E501
        if include_optional :
            return ReportVMFilesVMBase(
                files = [
                    fastreport_cloud_sdk.models.report_vm.ReportVM(
                        template_id = '', 
                        report_info = fastreport_cloud_sdk.models.report_info.ReportInfo(
                            author = '', 
                            created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            creator_version = '', 
                            description = '', 
                            modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            name = '', 
                            picture = 'YQ==', 
                            preview_picture_ratio = 1.337, 
                            save_mode = 'All', 
                            save_preview_picture = True, 
                            tag = '', 
                            version = '', ), )
                    ], 
                count = 56, 
                skip = 56, 
                take = 56
            )
        else :
            return ReportVMFilesVMBase(
        )

    def testReportVMFilesVMBase(self):
        """Test ReportVMFilesVMBase"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
