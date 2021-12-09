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


class ThumbnailReportTaskVM(object):
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
        'subscription_id': 'str',
        'type': 'TaskType'
    }

    attribute_map = {
        'name': 'name',
        'subscription_id': 'subscriptionId',
        'type': 'type'
    }

    def __init__(self, name=None, subscription_id=None, type=None, local_vars_configuration=None):  # noqa: E501
        """ThumbnailReportTaskVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._subscription_id = None
        self._type = None
        self.discriminator = None

        self.name = name
        self.subscription_id = subscription_id
        if type is not None:
            self.type = type

    @property
    def name(self):
        """Gets the name of this ThumbnailReportTaskVM.  # noqa: E501


        :return: The name of this ThumbnailReportTaskVM.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ThumbnailReportTaskVM.


        :param name: The name of this ThumbnailReportTaskVM.  # noqa: E501
        :type name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 50):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def subscription_id(self):
        """Gets the subscription_id of this ThumbnailReportTaskVM.  # noqa: E501


        :return: The subscription_id of this ThumbnailReportTaskVM.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this ThumbnailReportTaskVM.


        :param subscription_id: The subscription_id of this ThumbnailReportTaskVM.  # noqa: E501
        :type subscription_id: str
        """
        if (self.local_vars_configuration.client_side_validation and
                subscription_id is not None and not re.search(r'(^$)|(^[A-Fa-f0-9]{24}$)', subscription_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `subscription_id`, must be a follow pattern or equal to `/(^$)|(^[A-Fa-f0-9]{24}$)/`")  # noqa: E501

        self._subscription_id = subscription_id

    @property
    def type(self):
        """Gets the type of this ThumbnailReportTaskVM.  # noqa: E501


        :return: The type of this ThumbnailReportTaskVM.  # noqa: E501
        :rtype: TaskType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ThumbnailReportTaskVM.


        :param type: The type of this ThumbnailReportTaskVM.  # noqa: E501
        :type type: TaskType
        """

        self._type = type

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
        if not isinstance(other, ThumbnailReportTaskVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ThumbnailReportTaskVM):
            return True

        return self.to_dict() != other.to_dict()
