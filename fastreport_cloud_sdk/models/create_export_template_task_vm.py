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


class CreateExportTemplateTaskVM(object):
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
        'report_parameters': 'dict[str, str]'
    }

    attribute_map = {
        'report_parameters': 'reportParameters'
    }

    def __init__(self, report_parameters=None, local_vars_configuration=None):  # noqa: E501
        """CreateExportTemplateTaskVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._report_parameters = None
        self.discriminator = None

        self.report_parameters = report_parameters

    @property
    def report_parameters(self):
        """Gets the report_parameters of this CreateExportTemplateTaskVM.  # noqa: E501


        :return: The report_parameters of this CreateExportTemplateTaskVM.  # noqa: E501
        :rtype: dict[str, str]
        """
        return self._report_parameters

    @report_parameters.setter
    def report_parameters(self, report_parameters):
        """Sets the report_parameters of this CreateExportTemplateTaskVM.


        :param report_parameters: The report_parameters of this CreateExportTemplateTaskVM.  # noqa: E501
        :type report_parameters: dict[str, str]
        """

        self._report_parameters = report_parameters

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
        if not isinstance(other, CreateExportTemplateTaskVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateExportTemplateTaskVM):
            return True

        return self.to_dict() != other.to_dict()
