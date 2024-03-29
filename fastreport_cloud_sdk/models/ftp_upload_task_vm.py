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


class FTPUploadTaskVM(object):
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
        'archive': 'bool',
        'archive_name': 'str',
        'destination_folder': 'str',
        'ftp_host': 'str',
        'ftp_port': 'int',
        'ftp_username': 'str',
        'use_sftp': 'bool'
    }

    attribute_map = {
        'archive': 'archive',
        'archive_name': 'archiveName',
        'destination_folder': 'destinationFolder',
        'ftp_host': 'ftpHost',
        'ftp_port': 'ftpPort',
        'ftp_username': 'ftpUsername',
        'use_sftp': 'useSFTP'
    }

    def __init__(self, archive=None, archive_name=None, destination_folder=None, ftp_host=None, ftp_port=None, ftp_username=None, use_sftp=None, local_vars_configuration=None):  # noqa: E501
        """FTPUploadTaskVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._archive = None
        self._archive_name = None
        self._destination_folder = None
        self._ftp_host = None
        self._ftp_port = None
        self._ftp_username = None
        self._use_sftp = None
        self.discriminator = None

        if archive is not None:
            self.archive = archive
        self.archive_name = archive_name
        self.destination_folder = destination_folder
        self.ftp_host = ftp_host
        if ftp_port is not None:
            self.ftp_port = ftp_port
        self.ftp_username = ftp_username
        if use_sftp is not None:
            self.use_sftp = use_sftp

    @property
    def archive(self):
        """Gets the archive of this FTPUploadTaskVM.  # noqa: E501


        :return: The archive of this FTPUploadTaskVM.  # noqa: E501
        :rtype: bool
        """
        return self._archive

    @archive.setter
    def archive(self, archive):
        """Sets the archive of this FTPUploadTaskVM.


        :param archive: The archive of this FTPUploadTaskVM.  # noqa: E501
        :type archive: bool
        """

        self._archive = archive

    @property
    def archive_name(self):
        """Gets the archive_name of this FTPUploadTaskVM.  # noqa: E501


        :return: The archive_name of this FTPUploadTaskVM.  # noqa: E501
        :rtype: str
        """
        return self._archive_name

    @archive_name.setter
    def archive_name(self, archive_name):
        """Sets the archive_name of this FTPUploadTaskVM.


        :param archive_name: The archive_name of this FTPUploadTaskVM.  # noqa: E501
        :type archive_name: str
        """

        self._archive_name = archive_name

    @property
    def destination_folder(self):
        """Gets the destination_folder of this FTPUploadTaskVM.  # noqa: E501


        :return: The destination_folder of this FTPUploadTaskVM.  # noqa: E501
        :rtype: str
        """
        return self._destination_folder

    @destination_folder.setter
    def destination_folder(self, destination_folder):
        """Sets the destination_folder of this FTPUploadTaskVM.


        :param destination_folder: The destination_folder of this FTPUploadTaskVM.  # noqa: E501
        :type destination_folder: str
        """

        self._destination_folder = destination_folder

    @property
    def ftp_host(self):
        """Gets the ftp_host of this FTPUploadTaskVM.  # noqa: E501


        :return: The ftp_host of this FTPUploadTaskVM.  # noqa: E501
        :rtype: str
        """
        return self._ftp_host

    @ftp_host.setter
    def ftp_host(self, ftp_host):
        """Sets the ftp_host of this FTPUploadTaskVM.


        :param ftp_host: The ftp_host of this FTPUploadTaskVM.  # noqa: E501
        :type ftp_host: str
        """
        if (self.local_vars_configuration.client_side_validation and
                ftp_host is not None and len(ftp_host) > 300):
            raise ValueError("Invalid value for `ftp_host`, length must be less than or equal to `300`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                ftp_host is not None and len(ftp_host) < 1):
            raise ValueError("Invalid value for `ftp_host`, length must be greater than or equal to `1`")  # noqa: E501

        self._ftp_host = ftp_host

    @property
    def ftp_port(self):
        """Gets the ftp_port of this FTPUploadTaskVM.  # noqa: E501


        :return: The ftp_port of this FTPUploadTaskVM.  # noqa: E501
        :rtype: int
        """
        return self._ftp_port

    @ftp_port.setter
    def ftp_port(self, ftp_port):
        """Sets the ftp_port of this FTPUploadTaskVM.


        :param ftp_port: The ftp_port of this FTPUploadTaskVM.  # noqa: E501
        :type ftp_port: int
        """

        self._ftp_port = ftp_port

    @property
    def ftp_username(self):
        """Gets the ftp_username of this FTPUploadTaskVM.  # noqa: E501


        :return: The ftp_username of this FTPUploadTaskVM.  # noqa: E501
        :rtype: str
        """
        return self._ftp_username

    @ftp_username.setter
    def ftp_username(self, ftp_username):
        """Sets the ftp_username of this FTPUploadTaskVM.


        :param ftp_username: The ftp_username of this FTPUploadTaskVM.  # noqa: E501
        :type ftp_username: str
        """
        if (self.local_vars_configuration.client_side_validation and
                ftp_username is not None and len(ftp_username) > 300):
            raise ValueError("Invalid value for `ftp_username`, length must be less than or equal to `300`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                ftp_username is not None and len(ftp_username) < 1):
            raise ValueError("Invalid value for `ftp_username`, length must be greater than or equal to `1`")  # noqa: E501

        self._ftp_username = ftp_username

    @property
    def use_sftp(self):
        """Gets the use_sftp of this FTPUploadTaskVM.  # noqa: E501


        :return: The use_sftp of this FTPUploadTaskVM.  # noqa: E501
        :rtype: bool
        """
        return self._use_sftp

    @use_sftp.setter
    def use_sftp(self, use_sftp):
        """Sets the use_sftp of this FTPUploadTaskVM.


        :param use_sftp: The use_sftp of this FTPUploadTaskVM.  # noqa: E501
        :type use_sftp: bool
        """

        self._use_sftp = use_sftp

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
        if not isinstance(other, FTPUploadTaskVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FTPUploadTaskVM):
            return True

        return self.to_dict() != other.to_dict()
