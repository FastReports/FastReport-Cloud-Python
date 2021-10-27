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


class EmailTaskVM(object):
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
        'body': 'str',
        'is_body_html': 'bool',
        'subject': 'str',
        'to': 'list[str]',
        '_from': 'str',
        'username': 'str',
        'server': 'str',
        'port': 'int',
        'enable_ssl': 'bool',
        'name': 'str',
        'subscription_id': 'str',
        'type': 'TaskType'
    }

    attribute_map = {
        'body': 'body',
        'is_body_html': 'isBodyHtml',
        'subject': 'subject',
        'to': 'to',
        '_from': 'from',
        'username': 'username',
        'server': 'server',
        'port': 'port',
        'enable_ssl': 'enableSsl',
        'name': 'name',
        'subscription_id': 'subscriptionId',
        'type': 'type'
    }

    def __init__(self, body=None, is_body_html=None, subject=None, to=None, _from=None, username=None, server=None, port=None, enable_ssl=None, name=None, subscription_id=None, type=None, local_vars_configuration=None):  # noqa: E501
        """EmailTaskVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._body = None
        self._is_body_html = None
        self._subject = None
        self._to = None
        self.__from = None
        self._username = None
        self._server = None
        self._port = None
        self._enable_ssl = None
        self._name = None
        self._subscription_id = None
        self._type = None
        self.discriminator = None

        self.body = body
        if is_body_html is not None:
            self.is_body_html = is_body_html
        self.subject = subject
        self.to = to
        self._from = _from
        self.username = username
        self.server = server
        if port is not None:
            self.port = port
        if enable_ssl is not None:
            self.enable_ssl = enable_ssl
        self.name = name
        self.subscription_id = subscription_id
        if type is not None:
            self.type = type

    @property
    def body(self):
        """Gets the body of this EmailTaskVM.  # noqa: E501


        :return: The body of this EmailTaskVM.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this EmailTaskVM.


        :param body: The body of this EmailTaskVM.  # noqa: E501
        :type body: str
        """
        if (self.local_vars_configuration.client_side_validation and
                body is not None and len(body) > 384000):
            raise ValueError("Invalid value for `body`, length must be less than or equal to `384000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                body is not None and len(body) < 1):
            raise ValueError("Invalid value for `body`, length must be greater than or equal to `1`")  # noqa: E501

        self._body = body

    @property
    def is_body_html(self):
        """Gets the is_body_html of this EmailTaskVM.  # noqa: E501


        :return: The is_body_html of this EmailTaskVM.  # noqa: E501
        :rtype: bool
        """
        return self._is_body_html

    @is_body_html.setter
    def is_body_html(self, is_body_html):
        """Sets the is_body_html of this EmailTaskVM.


        :param is_body_html: The is_body_html of this EmailTaskVM.  # noqa: E501
        :type is_body_html: bool
        """

        self._is_body_html = is_body_html

    @property
    def subject(self):
        """Gets the subject of this EmailTaskVM.  # noqa: E501


        :return: The subject of this EmailTaskVM.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this EmailTaskVM.


        :param subject: The subject of this EmailTaskVM.  # noqa: E501
        :type subject: str
        """
        if (self.local_vars_configuration.client_side_validation and
                subject is not None and len(subject) > 1000):
            raise ValueError("Invalid value for `subject`, length must be less than or equal to `1000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                subject is not None and len(subject) < 1):
            raise ValueError("Invalid value for `subject`, length must be greater than or equal to `1`")  # noqa: E501

        self._subject = subject

    @property
    def to(self):
        """Gets the to of this EmailTaskVM.  # noqa: E501


        :return: The to of this EmailTaskVM.  # noqa: E501
        :rtype: list[str]
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this EmailTaskVM.


        :param to: The to of this EmailTaskVM.  # noqa: E501
        :type to: list[str]
        """
        if (self.local_vars_configuration.client_side_validation and
                to is not None and len(to) > 200):
            raise ValueError("Invalid value for `to`, number of items must be less than or equal to `200`")  # noqa: E501

        self._to = to

    @property
    def _from(self):
        """Gets the _from of this EmailTaskVM.  # noqa: E501


        :return: The _from of this EmailTaskVM.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this EmailTaskVM.


        :param _from: The _from of this EmailTaskVM.  # noqa: E501
        :type _from: str
        """

        self.__from = _from

    @property
    def username(self):
        """Gets the username of this EmailTaskVM.  # noqa: E501


        :return: The username of this EmailTaskVM.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this EmailTaskVM.


        :param username: The username of this EmailTaskVM.  # noqa: E501
        :type username: str
        """
        if (self.local_vars_configuration.client_side_validation and
                username is not None and len(username) > 100):
            raise ValueError("Invalid value for `username`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                username is not None and len(username) < 1):
            raise ValueError("Invalid value for `username`, length must be greater than or equal to `1`")  # noqa: E501

        self._username = username

    @property
    def server(self):
        """Gets the server of this EmailTaskVM.  # noqa: E501


        :return: The server of this EmailTaskVM.  # noqa: E501
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this EmailTaskVM.


        :param server: The server of this EmailTaskVM.  # noqa: E501
        :type server: str
        """
        if (self.local_vars_configuration.client_side_validation and
                server is not None and len(server) > 5000):
            raise ValueError("Invalid value for `server`, length must be less than or equal to `5000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                server is not None and len(server) < 1):
            raise ValueError("Invalid value for `server`, length must be greater than or equal to `1`")  # noqa: E501

        self._server = server

    @property
    def port(self):
        """Gets the port of this EmailTaskVM.  # noqa: E501


        :return: The port of this EmailTaskVM.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this EmailTaskVM.


        :param port: The port of this EmailTaskVM.  # noqa: E501
        :type port: int
        """
        if (self.local_vars_configuration.client_side_validation and
                port is not None and port > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                port is not None and port < 0):  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value greater than or equal to `0`")  # noqa: E501

        self._port = port

    @property
    def enable_ssl(self):
        """Gets the enable_ssl of this EmailTaskVM.  # noqa: E501


        :return: The enable_ssl of this EmailTaskVM.  # noqa: E501
        :rtype: bool
        """
        return self._enable_ssl

    @enable_ssl.setter
    def enable_ssl(self, enable_ssl):
        """Sets the enable_ssl of this EmailTaskVM.


        :param enable_ssl: The enable_ssl of this EmailTaskVM.  # noqa: E501
        :type enable_ssl: bool
        """

        self._enable_ssl = enable_ssl

    @property
    def name(self):
        """Gets the name of this EmailTaskVM.  # noqa: E501


        :return: The name of this EmailTaskVM.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EmailTaskVM.


        :param name: The name of this EmailTaskVM.  # noqa: E501
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
        """Gets the subscription_id of this EmailTaskVM.  # noqa: E501


        :return: The subscription_id of this EmailTaskVM.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this EmailTaskVM.


        :param subscription_id: The subscription_id of this EmailTaskVM.  # noqa: E501
        :type subscription_id: str
        """
        if (self.local_vars_configuration.client_side_validation and
                subscription_id is not None and not re.search(r'(^$)|(^[A-Fa-f0-9]{24}$)', subscription_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `subscription_id`, must be a follow pattern or equal to `/(^$)|(^[A-Fa-f0-9]{24}$)/`")  # noqa: E501

        self._subscription_id = subscription_id

    @property
    def type(self):
        """Gets the type of this EmailTaskVM.  # noqa: E501


        :return: The type of this EmailTaskVM.  # noqa: E501
        :rtype: TaskType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EmailTaskVM.


        :param type: The type of this EmailTaskVM.  # noqa: E501
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
        if not isinstance(other, EmailTaskVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EmailTaskVM):
            return True

        return self.to_dict() != other.to_dict()
