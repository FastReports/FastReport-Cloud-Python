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


class ContactsVM(object):
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
        'contacts': 'list[ContactVM]',
        'skip': 'int',
        'take': 'int',
        'count': 'int'
    }

    attribute_map = {
        'contacts': 'contacts',
        'skip': 'skip',
        'take': 'take',
        'count': 'count'
    }

    def __init__(self, contacts=None, skip=None, take=None, count=None, local_vars_configuration=None):  # noqa: E501
        """ContactsVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._contacts = None
        self._skip = None
        self._take = None
        self._count = None
        self.discriminator = None

        self.contacts = contacts
        if skip is not None:
            self.skip = skip
        if take is not None:
            self.take = take
        if count is not None:
            self.count = count

    @property
    def contacts(self):
        """Gets the contacts of this ContactsVM.  # noqa: E501


        :return: The contacts of this ContactsVM.  # noqa: E501
        :rtype: list[ContactVM]
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        """Sets the contacts of this ContactsVM.


        :param contacts: The contacts of this ContactsVM.  # noqa: E501
        :type contacts: list[ContactVM]
        """

        self._contacts = contacts

    @property
    def skip(self):
        """Gets the skip of this ContactsVM.  # noqa: E501


        :return: The skip of this ContactsVM.  # noqa: E501
        :rtype: int
        """
        return self._skip

    @skip.setter
    def skip(self, skip):
        """Sets the skip of this ContactsVM.


        :param skip: The skip of this ContactsVM.  # noqa: E501
        :type skip: int
        """

        self._skip = skip

    @property
    def take(self):
        """Gets the take of this ContactsVM.  # noqa: E501


        :return: The take of this ContactsVM.  # noqa: E501
        :rtype: int
        """
        return self._take

    @take.setter
    def take(self, take):
        """Sets the take of this ContactsVM.


        :param take: The take of this ContactsVM.  # noqa: E501
        :type take: int
        """

        self._take = take

    @property
    def count(self):
        """Gets the count of this ContactsVM.  # noqa: E501


        :return: The count of this ContactsVM.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ContactsVM.


        :param count: The count of this ContactsVM.  # noqa: E501
        :type count: int
        """

        self._count = count

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
        if not isinstance(other, ContactsVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContactsVM):
            return True

        return self.to_dict() != other.to_dict()
