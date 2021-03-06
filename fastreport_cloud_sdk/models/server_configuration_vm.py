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


class ServerConfigurationVM(object):
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
        'title': 'str',
        'logo_link': 'str',
        'copyright': 'str',
        'corporate_server_mode': 'bool',
        'is_disabled': 'bool',
        'frontend': 'FrontendApp',
        'auth': 'AuthConfigVM',
        'designer_for_anons': 'bool'
    }

    attribute_map = {
        'title': 'title',
        'logo_link': 'logoLink',
        'copyright': 'copyright',
        'corporate_server_mode': 'corporateServerMode',
        'is_disabled': 'isDisabled',
        'frontend': 'frontend',
        'auth': 'auth',
        'designer_for_anons': 'designerForAnons'
    }

    def __init__(self, title=None, logo_link=None, copyright=None, corporate_server_mode=None, is_disabled=None, frontend=None, auth=None, designer_for_anons=None, local_vars_configuration=None):  # noqa: E501
        """ServerConfigurationVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._title = None
        self._logo_link = None
        self._copyright = None
        self._corporate_server_mode = None
        self._is_disabled = None
        self._frontend = None
        self._auth = None
        self._designer_for_anons = None
        self.discriminator = None

        self.title = title
        self.logo_link = logo_link
        self.copyright = copyright
        if corporate_server_mode is not None:
            self.corporate_server_mode = corporate_server_mode
        if is_disabled is not None:
            self.is_disabled = is_disabled
        if frontend is not None:
            self.frontend = frontend
        if auth is not None:
            self.auth = auth
        if designer_for_anons is not None:
            self.designer_for_anons = designer_for_anons

    @property
    def title(self):
        """Gets the title of this ServerConfigurationVM.  # noqa: E501


        :return: The title of this ServerConfigurationVM.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ServerConfigurationVM.


        :param title: The title of this ServerConfigurationVM.  # noqa: E501
        :type title: str
        """

        self._title = title

    @property
    def logo_link(self):
        """Gets the logo_link of this ServerConfigurationVM.  # noqa: E501


        :return: The logo_link of this ServerConfigurationVM.  # noqa: E501
        :rtype: str
        """
        return self._logo_link

    @logo_link.setter
    def logo_link(self, logo_link):
        """Sets the logo_link of this ServerConfigurationVM.


        :param logo_link: The logo_link of this ServerConfigurationVM.  # noqa: E501
        :type logo_link: str
        """

        self._logo_link = logo_link

    @property
    def copyright(self):
        """Gets the copyright of this ServerConfigurationVM.  # noqa: E501


        :return: The copyright of this ServerConfigurationVM.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this ServerConfigurationVM.


        :param copyright: The copyright of this ServerConfigurationVM.  # noqa: E501
        :type copyright: str
        """

        self._copyright = copyright

    @property
    def corporate_server_mode(self):
        """Gets the corporate_server_mode of this ServerConfigurationVM.  # noqa: E501


        :return: The corporate_server_mode of this ServerConfigurationVM.  # noqa: E501
        :rtype: bool
        """
        return self._corporate_server_mode

    @corporate_server_mode.setter
    def corporate_server_mode(self, corporate_server_mode):
        """Sets the corporate_server_mode of this ServerConfigurationVM.


        :param corporate_server_mode: The corporate_server_mode of this ServerConfigurationVM.  # noqa: E501
        :type corporate_server_mode: bool
        """

        self._corporate_server_mode = corporate_server_mode

    @property
    def is_disabled(self):
        """Gets the is_disabled of this ServerConfigurationVM.  # noqa: E501


        :return: The is_disabled of this ServerConfigurationVM.  # noqa: E501
        :rtype: bool
        """
        return self._is_disabled

    @is_disabled.setter
    def is_disabled(self, is_disabled):
        """Sets the is_disabled of this ServerConfigurationVM.


        :param is_disabled: The is_disabled of this ServerConfigurationVM.  # noqa: E501
        :type is_disabled: bool
        """

        self._is_disabled = is_disabled

    @property
    def frontend(self):
        """Gets the frontend of this ServerConfigurationVM.  # noqa: E501


        :return: The frontend of this ServerConfigurationVM.  # noqa: E501
        :rtype: FrontendApp
        """
        return self._frontend

    @frontend.setter
    def frontend(self, frontend):
        """Sets the frontend of this ServerConfigurationVM.


        :param frontend: The frontend of this ServerConfigurationVM.  # noqa: E501
        :type frontend: FrontendApp
        """

        self._frontend = frontend

    @property
    def auth(self):
        """Gets the auth of this ServerConfigurationVM.  # noqa: E501


        :return: The auth of this ServerConfigurationVM.  # noqa: E501
        :rtype: AuthConfigVM
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        """Sets the auth of this ServerConfigurationVM.


        :param auth: The auth of this ServerConfigurationVM.  # noqa: E501
        :type auth: AuthConfigVM
        """

        self._auth = auth

    @property
    def designer_for_anons(self):
        """Gets the designer_for_anons of this ServerConfigurationVM.  # noqa: E501


        :return: The designer_for_anons of this ServerConfigurationVM.  # noqa: E501
        :rtype: bool
        """
        return self._designer_for_anons

    @designer_for_anons.setter
    def designer_for_anons(self, designer_for_anons):
        """Sets the designer_for_anons of this ServerConfigurationVM.


        :param designer_for_anons: The designer_for_anons of this ServerConfigurationVM.  # noqa: E501
        :type designer_for_anons: bool
        """

        self._designer_for_anons = designer_for_anons

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
        if not isinstance(other, ServerConfigurationVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ServerConfigurationVM):
            return True

        return self.to_dict() != other.to_dict()
