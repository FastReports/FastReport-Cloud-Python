# coding: utf-8

"""
    FastReport Cloud

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from fastreport_cloud_sdk.configuration import Configuration


class SelectedFilesVM(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'is_all_selected': 'bool',
        'files': 'list[str]',
        'folders': 'list[str]'
    }

    attribute_map = {
        'is_all_selected': 'isAllSelected',
        'files': 'files',
        'folders': 'folders'
    }

    def __init__(self, is_all_selected=None, files=None, folders=None, local_vars_configuration=None):  # noqa: E501
        """SelectedFilesVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._is_all_selected = None
        self._files = None
        self._folders = None
        self.discriminator = None

        if is_all_selected is not None:
            self.is_all_selected = is_all_selected
        self.files = files
        self.folders = folders

    @property
    def is_all_selected(self):
        """Gets the is_all_selected of this SelectedFilesVM.  # noqa: E501


        :return: The is_all_selected of this SelectedFilesVM.  # noqa: E501
        :rtype: bool
        """
        return self._is_all_selected

    @is_all_selected.setter
    def is_all_selected(self, is_all_selected):
        """Sets the is_all_selected of this SelectedFilesVM.


        :param is_all_selected: The is_all_selected of this SelectedFilesVM.  # noqa: E501
        :type is_all_selected: bool
        """

        self._is_all_selected = is_all_selected

    @property
    def files(self):
        """Gets the files of this SelectedFilesVM.  # noqa: E501


        :return: The files of this SelectedFilesVM.  # noqa: E501
        :rtype: list[str]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this SelectedFilesVM.


        :param files: The files of this SelectedFilesVM.  # noqa: E501
        :type files: list[str]
        """

        self._files = files

    @property
    def folders(self):
        """Gets the folders of this SelectedFilesVM.  # noqa: E501


        :return: The folders of this SelectedFilesVM.  # noqa: E501
        :rtype: list[str]
        """
        return self._folders

    @folders.setter
    def folders(self, folders):
        """Sets the folders of this SelectedFilesVM.


        :param folders: The folders of this SelectedFilesVM.  # noqa: E501
        :type folders: list[str]
        """

        self._folders = folders

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SelectedFilesVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SelectedFilesVM):
            return True

        return self.to_dict() != other.to_dict()
