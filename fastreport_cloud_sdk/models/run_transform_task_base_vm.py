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


class RunTransformTaskBaseVM(object):
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
        'input_file': 'RunInputFileVM',
        'locale': 'str',
        'output_file': 'OutputFileVM',
        'transports': 'list[RunTransportTaskBaseVM]',
        't': 'str'
    }

    attribute_map = {
        'input_file': 'inputFile',
        'locale': 'locale',
        'output_file': 'outputFile',
        'transports': 'transports',
        't': '$t'
    }

    discriminator_value_class_map = {
        'RunExportReportTaskVM': 'RunExportReportTaskVM',
        'RunPrepareTemplateTaskVM': 'RunPrepareTemplateTaskVM'
    }

    def __init__(self, input_file=None, locale=None, output_file=None, transports=None, t=None, local_vars_configuration=None):  # noqa: E501
        """RunTransformTaskBaseVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._input_file = None
        self._locale = None
        self._output_file = None
        self._transports = None
        self._t = None
        self.discriminator = 't'

        if input_file is not None:
            self.input_file = input_file
        self.locale = locale
        if output_file is not None:
            self.output_file = output_file
        self.transports = transports
        self.t = t

    @property
    def input_file(self):
        """Gets the input_file of this RunTransformTaskBaseVM.  # noqa: E501


        :return: The input_file of this RunTransformTaskBaseVM.  # noqa: E501
        :rtype: RunInputFileVM
        """
        return self._input_file

    @input_file.setter
    def input_file(self, input_file):
        """Sets the input_file of this RunTransformTaskBaseVM.


        :param input_file: The input_file of this RunTransformTaskBaseVM.  # noqa: E501
        :type input_file: RunInputFileVM
        """

        self._input_file = input_file

    @property
    def locale(self):
        """Gets the locale of this RunTransformTaskBaseVM.  # noqa: E501


        :return: The locale of this RunTransformTaskBaseVM.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this RunTransformTaskBaseVM.


        :param locale: The locale of this RunTransformTaskBaseVM.  # noqa: E501
        :type locale: str
        """
        if (self.local_vars_configuration.client_side_validation and
                locale is not None and not re.search(r'^[a-zA-Z]{2,4}(-[a-zA-Z]{2,4}){0,2}$', locale)):  # noqa: E501
            raise ValueError(r"Invalid value for `locale`, must be a follow pattern or equal to `/^[a-zA-Z]{2,4}(-[a-zA-Z]{2,4}){0,2}$/`")  # noqa: E501

        self._locale = locale

    @property
    def output_file(self):
        """Gets the output_file of this RunTransformTaskBaseVM.  # noqa: E501


        :return: The output_file of this RunTransformTaskBaseVM.  # noqa: E501
        :rtype: OutputFileVM
        """
        return self._output_file

    @output_file.setter
    def output_file(self, output_file):
        """Sets the output_file of this RunTransformTaskBaseVM.


        :param output_file: The output_file of this RunTransformTaskBaseVM.  # noqa: E501
        :type output_file: OutputFileVM
        """

        self._output_file = output_file

    @property
    def transports(self):
        """Gets the transports of this RunTransformTaskBaseVM.  # noqa: E501


        :return: The transports of this RunTransformTaskBaseVM.  # noqa: E501
        :rtype: list[RunTransportTaskBaseVM]
        """
        return self._transports

    @transports.setter
    def transports(self, transports):
        """Sets the transports of this RunTransformTaskBaseVM.


        :param transports: The transports of this RunTransformTaskBaseVM.  # noqa: E501
        :type transports: list[RunTransportTaskBaseVM]
        """
        if (self.local_vars_configuration.client_side_validation and
                transports is not None and len(transports) > 10):
            raise ValueError("Invalid value for `transports`, number of items must be less than or equal to `10`")  # noqa: E501

        self._transports = transports

    @property
    def t(self):
        """Gets the t of this RunTransformTaskBaseVM.  # noqa: E501


        :return: The t of this RunTransformTaskBaseVM.  # noqa: E501
        :rtype: str
        """
        return self._t

    @t.setter
    def t(self, t):
        """Sets the t of this RunTransformTaskBaseVM.


        :param t: The t of this RunTransformTaskBaseVM.  # noqa: E501
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
        if not isinstance(other, RunTransformTaskBaseVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RunTransformTaskBaseVM):
            return True

        return self.to_dict() != other.to_dict()
