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


class UpdateFilePermissionsVM(object):
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
        'new_permissions': 'FilePermissions',
        'administrate': 'FileAdministrate'
    }

    attribute_map = {
        'new_permissions': 'newPermissions',
        'administrate': 'administrate'
    }

    def __init__(self, new_permissions=None, administrate=None, local_vars_configuration=None):  # noqa: E501
        """UpdateFilePermissionsVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._new_permissions = None
        self._administrate = None
        self.discriminator = None

        self.new_permissions = new_permissions
        self.administrate = administrate

    @property
    def new_permissions(self):
        """Gets the new_permissions of this UpdateFilePermissionsVM.  # noqa: E501


        :return: The new_permissions of this UpdateFilePermissionsVM.  # noqa: E501
        :rtype: FilePermissions
        """
        return self._new_permissions

    @new_permissions.setter
    def new_permissions(self, new_permissions):
        """Sets the new_permissions of this UpdateFilePermissionsVM.


        :param new_permissions: The new_permissions of this UpdateFilePermissionsVM.  # noqa: E501
        :type new_permissions: FilePermissions
        """
        if self.local_vars_configuration.client_side_validation and new_permissions is None:  # noqa: E501
            raise ValueError("Invalid value for `new_permissions`, must not be `None`")  # noqa: E501

        self._new_permissions = new_permissions

    @property
    def administrate(self):
        """Gets the administrate of this UpdateFilePermissionsVM.  # noqa: E501


        :return: The administrate of this UpdateFilePermissionsVM.  # noqa: E501
        :rtype: FileAdministrate
        """
        return self._administrate

    @administrate.setter
    def administrate(self, administrate):
        """Sets the administrate of this UpdateFilePermissionsVM.


        :param administrate: The administrate of this UpdateFilePermissionsVM.  # noqa: E501
        :type administrate: FileAdministrate
        """
        if self.local_vars_configuration.client_side_validation and administrate is None:  # noqa: E501
            raise ValueError("Invalid value for `administrate`, must not be `None`")  # noqa: E501

        self._administrate = administrate

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
        if not isinstance(other, UpdateFilePermissionsVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateFilePermissionsVM):
            return True

        return self.to_dict() != other.to_dict()
