# coding: utf-8

"""
    FastReport Cloud

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from fastreport_cloud_sdk.configuration import Configuration


class CreateApiKeyVM(object):
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
        'description': 'str',
        'expired': 'datetime'
    }

    attribute_map = {
        'description': 'description',
        'expired': 'expired'
    }

    def __init__(self, description=None, expired=None, local_vars_configuration=None):  # noqa: E501
        """CreateApiKeyVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._expired = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.expired = expired

    @property
    def description(self):
        """Gets the description of this CreateApiKeyVM.  # noqa: E501


        :return: The description of this CreateApiKeyVM.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateApiKeyVM.


        :param description: The description of this CreateApiKeyVM.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def expired(self):
        """Gets the expired of this CreateApiKeyVM.  # noqa: E501


        :return: The expired of this CreateApiKeyVM.  # noqa: E501
        :rtype: datetime
        """
        return self._expired

    @expired.setter
    def expired(self, expired):
        """Sets the expired of this CreateApiKeyVM.


        :param expired: The expired of this CreateApiKeyVM.  # noqa: E501
        :type expired: datetime
        """
        if self.local_vars_configuration.client_side_validation and expired is None:  # noqa: E501
            raise ValueError("Invalid value for `expired`, must not be `None`")  # noqa: E501

        self._expired = expired

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
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
        if not isinstance(other, CreateApiKeyVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateApiKeyVM):
            return True

        return self.to_dict() != other.to_dict()