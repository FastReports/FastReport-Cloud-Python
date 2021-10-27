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


class ReportFolderCreateVM(object):
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
        'name': 'str',
        'tags': 'list[str]',
        'icon': 'str'
    }

    attribute_map = {
        'name': 'name',
        'tags': 'tags',
        'icon': 'icon'
    }

    def __init__(self, name=None, tags=None, icon=None, local_vars_configuration=None):  # noqa: E501
        """ReportFolderCreateVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._tags = None
        self._icon = None
        self.discriminator = None

        self.name = name
        self.tags = tags
        self.icon = icon

    @property
    def name(self):
        """Gets the name of this ReportFolderCreateVM.  # noqa: E501


        :return: The name of this ReportFolderCreateVM.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReportFolderCreateVM.


        :param name: The name of this ReportFolderCreateVM.  # noqa: E501
        :type name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 250):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `250`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def tags(self):
        """Gets the tags of this ReportFolderCreateVM.  # noqa: E501


        :return: The tags of this ReportFolderCreateVM.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ReportFolderCreateVM.


        :param tags: The tags of this ReportFolderCreateVM.  # noqa: E501
        :type tags: list[str]
        """
        if (self.local_vars_configuration.client_side_validation and
                tags is not None and len(tags) > 3):
            raise ValueError("Invalid value for `tags`, number of items must be less than or equal to `3`")  # noqa: E501

        self._tags = tags

    @property
    def icon(self):
        """Gets the icon of this ReportFolderCreateVM.  # noqa: E501


        :return: The icon of this ReportFolderCreateVM.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this ReportFolderCreateVM.


        :param icon: The icon of this ReportFolderCreateVM.  # noqa: E501
        :type icon: str
        """
        if (self.local_vars_configuration.client_side_validation and
                icon is not None and len(icon) > 65536):
            raise ValueError("Invalid value for `icon`, length must be less than or equal to `65536`")  # noqa: E501

        self._icon = icon

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
        if not isinstance(other, ReportFolderCreateVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReportFolderCreateVM):
            return True

        return self.to_dict() != other.to_dict()
