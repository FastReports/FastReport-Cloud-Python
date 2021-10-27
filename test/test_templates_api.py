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
from fastreport_cloud_sdk.api.templates_api import TemplatesApi  # noqa: E501
from fastreport_cloud_sdk.rest import ApiException


class TestTemplatesApi(unittest.TestCase):
    """TemplatesApi unit test stubs"""

    def setUp(self):
        self.api = fastreport_cloud_sdk.api.templates_api.TemplatesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_template_folder_and_file_get_count(self):
        """Test case for template_folder_and_file_get_count

        Get count of files and folders what contains in a specified folder  # noqa: E501
        """
        pass

    def test_template_folder_and_file_get_folders_and_files(self):
        """Test case for template_folder_and_file_get_folders_and_files

        Get all folders and files from specified folder  # noqa: E501
        """
        pass

    def test_template_folders_copy_folder(self):
        """Test case for template_folders_copy_folder

        Move folder to a specified folder  # noqa: E501
        """
        pass

    def test_template_folders_delete_folder(self):
        """Test case for template_folders_delete_folder

        Delete specified folder  # noqa: E501
        """
        pass

    def test_template_folders_get_breadcrumbs(self):
        """Test case for template_folders_get_breadcrumbs

        Get specified folder breadcrumbs  # noqa: E501
        """
        pass

    def test_template_folders_get_folder(self):
        """Test case for template_folders_get_folder

        Get specified folder  # noqa: E501
        """
        pass

    def test_template_folders_get_folders(self):
        """Test case for template_folders_get_folders

        Get all folders from specified folder  # noqa: E501
        """
        pass

    def test_template_folders_get_folders_count(self):
        """Test case for template_folders_get_folders_count

        Get count of folders what contains in a specified folder  # noqa: E501
        """
        pass

    def test_template_folders_get_permissions(self):
        """Test case for template_folders_get_permissions

        Get all folder permissions  # noqa: E501
        """
        pass

    def test_template_folders_get_root_folder(self):
        """Test case for template_folders_get_root_folder

        Get user's root folder (without parents)  # noqa: E501
        """
        pass

    def test_template_folders_move_folder(self):
        """Test case for template_folders_move_folder

        Move folder to a specified folder  # noqa: E501
        """
        pass

    def test_template_folders_post_folder(self):
        """Test case for template_folders_post_folder

        Create folder  # noqa: E501
        """
        pass

    def test_template_folders_rename_folder(self):
        """Test case for template_folders_rename_folder

        Rename a folder  # noqa: E501
        """
        pass

    def test_template_folders_update_icon(self):
        """Test case for template_folders_update_icon

        Update a folder's icon  # noqa: E501
        """
        pass

    def test_template_folders_update_permissions(self):
        """Test case for template_folders_update_permissions

        Update permissions  # noqa: E501
        """
        pass

    def test_template_folders_update_tags(self):
        """Test case for template_folders_update_tags

        Update tags  # noqa: E501
        """
        pass

    def test_templates_copy_file(self):
        """Test case for templates_copy_file

        Copy file to a specified folder  # noqa: E501
        """
        pass

    def test_templates_delete_file(self):
        """Test case for templates_delete_file

        Delete specified file  # noqa: E501
        """
        pass

    def test_templates_export(self):
        """Test case for templates_export

        Export specified report template to a specified format  # noqa: E501
        """
        pass

    def test_templates_get_file(self):
        """Test case for templates_get_file

        Get specified file  # noqa: E501
        """
        pass

    def test_templates_get_files_count(self):
        """Test case for templates_get_files_count

        Get count of files what contains in a specified folder  # noqa: E501
        """
        pass

    def test_templates_get_files_list(self):
        """Test case for templates_get_files_list

        Get all files from specified folder. <br />  User with Get Entity permission can access this method. <br />  The method will returns minimal infomration about the file: <br />  id, name, size, editedTime, createdTime, tags, status, statusReason.  # noqa: E501
        """
        pass

    def test_templates_get_permissions(self):
        """Test case for templates_get_permissions

        Get all file permissions  # noqa: E501
        """
        pass

    def test_templates_move_file(self):
        """Test case for templates_move_file

        Move file to a specified folder  # noqa: E501
        """
        pass

    def test_templates_prepare(self):
        """Test case for templates_prepare

        Prepare specified template to report  # noqa: E501
        """
        pass

    def test_templates_rename_file(self):
        """Test case for templates_rename_file

        Rename a file  # noqa: E501
        """
        pass

    def test_templates_update_icon(self):
        """Test case for templates_update_icon

        Update a files's icon  # noqa: E501
        """
        pass

    def test_templates_update_permissions(self):
        """Test case for templates_update_permissions

        Update permissions  # noqa: E501
        """
        pass

    def test_templates_update_tags(self):
        """Test case for templates_update_tags

        Update tags  # noqa: E501
        """
        pass

    def test_templates_upload_file(self):
        """Test case for templates_upload_file

        Upload a file to the specified folder  !  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
