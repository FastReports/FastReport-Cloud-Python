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


class ExportReportVM(object):
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
        'file_name': 'str',
        'folder_id': 'str',
        'locale': 'str',
        'pages_count': 'int',
        'format': 'ExportFormat',
        'export_parameters': 'dict[str, str]'
    }

    attribute_map = {
        'file_name': 'fileName',
        'folder_id': 'folderId',
        'locale': 'locale',
        'pages_count': 'pagesCount',
        'format': 'format',
        'export_parameters': 'exportParameters'
    }

    def __init__(self, file_name=None, folder_id=None, locale=None, pages_count=None, format=None, export_parameters=None, local_vars_configuration=None):  # noqa: E501
        """ExportReportVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._file_name = None
        self._folder_id = None
        self._locale = None
        self._pages_count = None
        self._format = None
        self._export_parameters = None
        self.discriminator = None

        self.file_name = file_name
        self.folder_id = folder_id
        self.locale = locale
        self.pages_count = pages_count
        if format is not None:
            self.format = format
        self.export_parameters = export_parameters

    @property
    def file_name(self):
        """Gets the file_name of this ExportReportVM.  # noqa: E501


        :return: The file_name of this ExportReportVM.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this ExportReportVM.


        :param file_name: The file_name of this ExportReportVM.  # noqa: E501
        :type file_name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                file_name is not None and len(file_name) > 250):
            raise ValueError("Invalid value for `file_name`, length must be less than or equal to `250`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                file_name is not None and len(file_name) < 0):
            raise ValueError("Invalid value for `file_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._file_name = file_name

    @property
    def folder_id(self):
        """Gets the folder_id of this ExportReportVM.  # noqa: E501


        :return: The folder_id of this ExportReportVM.  # noqa: E501
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this ExportReportVM.


        :param folder_id: The folder_id of this ExportReportVM.  # noqa: E501
        :type folder_id: str
        """
        if (self.local_vars_configuration.client_side_validation and
                folder_id is not None and not re.search(r'(^$)|(^[A-Fa-f0-9]{24}$)', folder_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `folder_id`, must be a follow pattern or equal to `/(^$)|(^[A-Fa-f0-9]{24}$)/`")  # noqa: E501

        self._folder_id = folder_id

    @property
    def locale(self):
        """Gets the locale of this ExportReportVM.  # noqa: E501


        :return: The locale of this ExportReportVM.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this ExportReportVM.


        :param locale: The locale of this ExportReportVM.  # noqa: E501
        :type locale: str
        """
        if (self.local_vars_configuration.client_side_validation and
                locale is not None and not re.search(r'^[a-zA-Z]{2,4}(-[a-zA-Z]{2,4}){0,2}$', locale)):  # noqa: E501
            raise ValueError(r"Invalid value for `locale`, must be a follow pattern or equal to `/^[a-zA-Z]{2,4}(-[a-zA-Z]{2,4}){0,2}$/`")  # noqa: E501

        self._locale = locale

    @property
    def pages_count(self):
        """Gets the pages_count of this ExportReportVM.  # noqa: E501


        :return: The pages_count of this ExportReportVM.  # noqa: E501
        :rtype: int
        """
        return self._pages_count

    @pages_count.setter
    def pages_count(self, pages_count):
        """Sets the pages_count of this ExportReportVM.


        :param pages_count: The pages_count of this ExportReportVM.  # noqa: E501
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
    def format(self):
        """Gets the format of this ExportReportVM.  # noqa: E501


        :return: The format of this ExportReportVM.  # noqa: E501
        :rtype: ExportFormat
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this ExportReportVM.


        :param format: The format of this ExportReportVM.  # noqa: E501
        :type format: ExportFormat
        """

        self._format = format

    @property
    def export_parameters(self):
        """Gets the export_parameters of this ExportReportVM.  # noqa: E501


        :return: The export_parameters of this ExportReportVM.  # noqa: E501
        :rtype: dict[str, str]
        """
        return self._export_parameters

    @export_parameters.setter
    def export_parameters(self, export_parameters):
        """Sets the export_parameters of this ExportReportVM.


        :param export_parameters: The export_parameters of this ExportReportVM.  # noqa: E501
        :type export_parameters: dict[str, str]
        """

        self._export_parameters = export_parameters

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
        if not isinstance(other, ExportReportVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExportReportVM):
            return True

        return self.to_dict() != other.to_dict()
