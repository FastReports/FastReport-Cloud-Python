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


class RunTransportTaskBaseVM(object):
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
        'files': 'list[RunInputFileVM]',
        'subscription_id': 'str',
        'type': 'TaskType'
    }

    attribute_map = {
        'files': 'files',
        'subscription_id': 'subscriptionId',
        'type': 'type'
    }

    def __init__(self, files=None, subscription_id=None, type=None, local_vars_configuration=None):  # noqa: E501
        """RunTransportTaskBaseVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._files = None
        self._subscription_id = None
        self._type = None
        self.discriminator = None

        self.files = files
        self.subscription_id = subscription_id
        if type is not None:
            self.type = type

    @property
    def files(self):
        """Gets the files of this RunTransportTaskBaseVM.  # noqa: E501


        :return: The files of this RunTransportTaskBaseVM.  # noqa: E501
        :rtype: list[RunInputFileVM]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this RunTransportTaskBaseVM.


        :param files: The files of this RunTransportTaskBaseVM.  # noqa: E501
        :type files: list[RunInputFileVM]
        """
        if (self.local_vars_configuration.client_side_validation and
                files is not None and len(files) > 10):
            raise ValueError("Invalid value for `files`, number of items must be less than or equal to `10`")  # noqa: E501

        self._files = files

    @property
    def subscription_id(self):
        """Gets the subscription_id of this RunTransportTaskBaseVM.  # noqa: E501


        :return: The subscription_id of this RunTransportTaskBaseVM.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this RunTransportTaskBaseVM.


        :param subscription_id: The subscription_id of this RunTransportTaskBaseVM.  # noqa: E501
        :type subscription_id: str
        """
        if (self.local_vars_configuration.client_side_validation and
                subscription_id is not None and not re.search(r'(^$)|(^[A-Fa-f0-9]{24}$)', subscription_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `subscription_id`, must be a follow pattern or equal to `/(^$)|(^[A-Fa-f0-9]{24}$)/`")  # noqa: E501

        self._subscription_id = subscription_id

    @property
    def type(self):
        """Gets the type of this RunTransportTaskBaseVM.  # noqa: E501


        :return: The type of this RunTransportTaskBaseVM.  # noqa: E501
        :rtype: TaskType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RunTransportTaskBaseVM.


        :param type: The type of this RunTransportTaskBaseVM.  # noqa: E501
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
        if not isinstance(other, RunTransportTaskBaseVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RunTransportTaskBaseVM):
            return True

        return self.to_dict() != other.to_dict()