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


class SelectedFilesForDeletingVM(object):
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
        'is_bin': 'bool',
        'folder_id': 'str',
        'search_pattern': 'str',
        'use_regex': 'bool'
    }

    attribute_map = {
        'is_bin': 'isBin',
        'folder_id': 'folderId',
        'search_pattern': 'searchPattern',
        'use_regex': 'useRegex'
    }

    def __init__(self, is_bin=None, folder_id=None, search_pattern=None, use_regex=None, local_vars_configuration=None):  # noqa: E501
        """SelectedFilesForDeletingVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._is_bin = None
        self._folder_id = None
        self._search_pattern = None
        self._use_regex = None
        self.discriminator = None

        if is_bin is not None:
            self.is_bin = is_bin
        self.folder_id = folder_id
        self.search_pattern = search_pattern
        if use_regex is not None:
            self.use_regex = use_regex

    @property
    def is_bin(self):
        """Gets the is_bin of this SelectedFilesForDeletingVM.  # noqa: E501


        :return: The is_bin of this SelectedFilesForDeletingVM.  # noqa: E501
        :rtype: bool
        """
        return self._is_bin

    @is_bin.setter
    def is_bin(self, is_bin):
        """Sets the is_bin of this SelectedFilesForDeletingVM.


        :param is_bin: The is_bin of this SelectedFilesForDeletingVM.  # noqa: E501
        :type is_bin: bool
        """

        self._is_bin = is_bin

    @property
    def folder_id(self):
        """Gets the folder_id of this SelectedFilesForDeletingVM.  # noqa: E501


        :return: The folder_id of this SelectedFilesForDeletingVM.  # noqa: E501
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this SelectedFilesForDeletingVM.


        :param folder_id: The folder_id of this SelectedFilesForDeletingVM.  # noqa: E501
        :type folder_id: str
        """
        if (self.local_vars_configuration.client_side_validation and
                folder_id is not None and not re.search(r'^[A-Fa-f0-9]{24}$', folder_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `folder_id`, must be a follow pattern or equal to `/^[A-Fa-f0-9]{24}$/`")  # noqa: E501

        self._folder_id = folder_id

    @property
    def search_pattern(self):
        """Gets the search_pattern of this SelectedFilesForDeletingVM.  # noqa: E501


        :return: The search_pattern of this SelectedFilesForDeletingVM.  # noqa: E501
        :rtype: str
        """
        return self._search_pattern

    @search_pattern.setter
    def search_pattern(self, search_pattern):
        """Sets the search_pattern of this SelectedFilesForDeletingVM.


        :param search_pattern: The search_pattern of this SelectedFilesForDeletingVM.  # noqa: E501
        :type search_pattern: str
        """

        self._search_pattern = search_pattern

    @property
    def use_regex(self):
        """Gets the use_regex of this SelectedFilesForDeletingVM.  # noqa: E501


        :return: The use_regex of this SelectedFilesForDeletingVM.  # noqa: E501
        :rtype: bool
        """
        return self._use_regex

    @use_regex.setter
    def use_regex(self, use_regex):
        """Sets the use_regex of this SelectedFilesForDeletingVM.


        :param use_regex: The use_regex of this SelectedFilesForDeletingVM.  # noqa: E501
        :type use_regex: bool
        """

        self._use_regex = use_regex

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
        if not isinstance(other, SelectedFilesForDeletingVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SelectedFilesForDeletingVM):
            return True

        return self.to_dict() != other.to_dict()
