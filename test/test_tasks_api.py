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
from fastreport_cloud_sdk.api.tasks_api import TasksApi  # noqa: E501
from fastreport_cloud_sdk.rest import ApiException


class TestTasksApi(unittest.TestCase):
    """TasksApi unit test stubs"""

    def setUp(self):
        self.api = fastreport_cloud_sdk.api.tasks_api.TasksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_tasks_create_task(self):
        """Test case for tasks_create_task

        Create a new task  # noqa: E501
        """
        pass

    def test_tasks_delete_task(self):
        """Test case for tasks_delete_task

        Delete a task from a storage  # noqa: E501
        """
        pass

    def test_tasks_get(self):
        """Test case for tasks_get

        Get a task by a specified id  # noqa: E501
        """
        pass

    def test_tasks_get_list(self):
        """Test case for tasks_get_list

        Get tasks list  # noqa: E501
        """
        pass

    def test_tasks_run_task(self):
        """Test case for tasks_run_task

        Run a task from request body  # noqa: E501
        """
        pass

    def test_tasks_run_task_by_id(self):
        """Test case for tasks_run_task_by_id

        Run a task by id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()