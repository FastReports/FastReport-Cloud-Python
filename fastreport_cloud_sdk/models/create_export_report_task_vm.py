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


class CreateExportReportTaskVM(object):
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
        'export_parameters': 'dict[str, str]',
        'format': 'ExportFormat',
        'pages_count': 'int',
        't': 'str'
    }

    attribute_map = {
        'export_parameters': 'exportParameters',
        'format': 'format',
        'pages_count': 'pagesCount',
        't': '$t'
    }

    discriminator_value_class_map = {
        'CreateExportTemplateTaskVM': 'CreateExportTemplateTaskVM'
    }

    def __init__(self, export_parameters=None, format=None, pages_count=None, t=None, local_vars_configuration=None):  # noqa: E501
        """CreateExportReportTaskVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._export_parameters = None
        self._format = None
        self._pages_count = None
        self._t = None
        self.discriminator = 't'

        self.export_parameters = export_parameters
        if format is not None:
            self.format = format
        if pages_count is not None:
            self.pages_count = pages_count
        self.t = t

    @property
    def export_parameters(self):
        """Gets the export_parameters of this CreateExportReportTaskVM.  # noqa: E501


        :return: The export_parameters of this CreateExportReportTaskVM.  # noqa: E501
        :rtype: dict[str, str]
        """
        return self._export_parameters

    @export_parameters.setter
    def export_parameters(self, export_parameters):
        """Sets the export_parameters of this CreateExportReportTaskVM.


        :param export_parameters: The export_parameters of this CreateExportReportTaskVM.  # noqa: E501
        :type export_parameters: dict[str, str]
        """

        self._export_parameters = export_parameters

    @property
    def format(self):
        """Gets the format of this CreateExportReportTaskVM.  # noqa: E501


        :return: The format of this CreateExportReportTaskVM.  # noqa: E501
        :rtype: ExportFormat
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this CreateExportReportTaskVM.


        :param format: The format of this CreateExportReportTaskVM.  # noqa: E501
        :type format: ExportFormat
        """

        self._format = format

    @property
    def pages_count(self):
        """Gets the pages_count of this CreateExportReportTaskVM.  # noqa: E501


        :return: The pages_count of this CreateExportReportTaskVM.  # noqa: E501
        :rtype: int
        """
        return self._pages_count

    @pages_count.setter
    def pages_count(self, pages_count):
        """Sets the pages_count of this CreateExportReportTaskVM.


        :param pages_count: The pages_count of this CreateExportReportTaskVM.  # noqa: E501
        :type pages_count: int
        """
        if (self.local_vars_configuration.client_side_validation and
                pages_count is not None and pages_count > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `pages_count`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                pages_count is not None and pages_count < 0):  # noqa: E501
            raise ValueError("Invalid value for `pages_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._pages_count = pages_count

    @property
    def t(self):
        """Gets the t of this CreateExportReportTaskVM.  # noqa: E501


        :return: The t of this CreateExportReportTaskVM.  # noqa: E501
        :rtype: str
        """
        return self._t

    @t.setter
    def t(self, t):
        """Sets the t of this CreateExportReportTaskVM.


        :param t: The t of this CreateExportReportTaskVM.  # noqa: E501
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
        if not isinstance(other, CreateExportReportTaskVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateExportReportTaskVM):
            return True

        return self.to_dict() != other.to_dict()
