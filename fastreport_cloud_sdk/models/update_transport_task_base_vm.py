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


class UpdateTransportTaskBaseVM(object):
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
        'input_file': 'InputFileVM',
        't': 'str'
    }

    attribute_map = {
        'input_file': 'inputFile',
        't': '$t'
    }

    discriminator_value_class_map = {
        'UpdateEmailTaskVM': 'UpdateEmailTaskVM',
        'UpdateFTPUploadTaskVM': 'UpdateFTPUploadTaskVM',
        'UpdateWebhookTaskVM': 'UpdateWebhookTaskVM'
    }

    def __init__(self, input_file=None, t=None, local_vars_configuration=None):  # noqa: E501
        """UpdateTransportTaskBaseVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._input_file = None
        self._t = None
        self.discriminator = 't'

        if input_file is not None:
            self.input_file = input_file
        self.t = t

    @property
    def input_file(self):
        """Gets the input_file of this UpdateTransportTaskBaseVM.  # noqa: E501


        :return: The input_file of this UpdateTransportTaskBaseVM.  # noqa: E501
        :rtype: InputFileVM
        """
        return self._input_file

    @input_file.setter
    def input_file(self, input_file):
        """Sets the input_file of this UpdateTransportTaskBaseVM.


        :param input_file: The input_file of this UpdateTransportTaskBaseVM.  # noqa: E501
        :type input_file: InputFileVM
        """

        self._input_file = input_file

    @property
    def t(self):
        """Gets the t of this UpdateTransportTaskBaseVM.  # noqa: E501


        :return: The t of this UpdateTransportTaskBaseVM.  # noqa: E501
        :rtype: str
        """
        return self._t

    @t.setter
    def t(self, t):
        """Sets the t of this UpdateTransportTaskBaseVM.


        :param t: The t of this UpdateTransportTaskBaseVM.  # noqa: E501
        :type t: str
        """
        if self.local_vars_configuration.client_side_validation and t is None:  # noqa: E501
            raise ValueError("Invalid value for `t`, must not be `None`")  # noqa: E501

        self._t = t

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, UpdateTransportTaskBaseVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateTransportTaskBaseVM):
            return True

        return self.to_dict() != other.to_dict()
