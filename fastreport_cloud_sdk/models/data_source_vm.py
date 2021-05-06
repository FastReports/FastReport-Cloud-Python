# coding: utf-8

"""
    FastReport Cloud

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from fastreport_cloud_sdk.configuration import Configuration


class DataSourceVM(object):
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
        'id': 'str',
        'name': 'str',
        'connection_type': 'str',
        'connection_string': 'str',
        'data_structure': 'str',
        'subscription_id': 'str',
        'edited_time': 'datetime',
        'editor_user_id': 'str',
        'created_time': 'datetime',
        'creator_user_id': 'str',
        'is_connected': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'connection_type': 'connectionType',
        'connection_string': 'connectionString',
        'data_structure': 'dataStructure',
        'subscription_id': 'subscriptionId',
        'edited_time': 'editedTime',
        'editor_user_id': 'editorUserId',
        'created_time': 'createdTime',
        'creator_user_id': 'creatorUserId',
        'is_connected': 'isConnected'
    }

    def __init__(self, id=None, name=None, connection_type=None, connection_string=None, data_structure=None, subscription_id=None, edited_time=None, editor_user_id=None, created_time=None, creator_user_id=None, is_connected=None, local_vars_configuration=None):  # noqa: E501
        """DataSourceVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._connection_type = None
        self._connection_string = None
        self._data_structure = None
        self._subscription_id = None
        self._edited_time = None
        self._editor_user_id = None
        self._created_time = None
        self._creator_user_id = None
        self._is_connected = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if connection_type is not None:
            self.connection_type = connection_type
        if connection_string is not None:
            self.connection_string = connection_string
        if data_structure is not None:
            self.data_structure = data_structure
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if edited_time is not None:
            self.edited_time = edited_time
        if editor_user_id is not None:
            self.editor_user_id = editor_user_id
        if created_time is not None:
            self.created_time = created_time
        if creator_user_id is not None:
            self.creator_user_id = creator_user_id
        if is_connected is not None:
            self.is_connected = is_connected

    @property
    def id(self):
        """Gets the id of this DataSourceVM.  # noqa: E501


        :return: The id of this DataSourceVM.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataSourceVM.


        :param id: The id of this DataSourceVM.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DataSourceVM.  # noqa: E501


        :return: The name of this DataSourceVM.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataSourceVM.


        :param name: The name of this DataSourceVM.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def connection_type(self):
        """Gets the connection_type of this DataSourceVM.  # noqa: E501


        :return: The connection_type of this DataSourceVM.  # noqa: E501
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        """Sets the connection_type of this DataSourceVM.


        :param connection_type: The connection_type of this DataSourceVM.  # noqa: E501
        :type connection_type: str
        """
        allowed_values = ["JSON", "MSSQL", "CSV", "XML", "MySQL", "Postgres"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and connection_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `connection_type` ({0}), must be one of {1}"  # noqa: E501
                .format(connection_type, allowed_values)
            )

        self._connection_type = connection_type

    @property
    def connection_string(self):
        """Gets the connection_string of this DataSourceVM.  # noqa: E501


        :return: The connection_string of this DataSourceVM.  # noqa: E501
        :rtype: str
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """Sets the connection_string of this DataSourceVM.


        :param connection_string: The connection_string of this DataSourceVM.  # noqa: E501
        :type connection_string: str
        """

        self._connection_string = connection_string

    @property
    def data_structure(self):
        """Gets the data_structure of this DataSourceVM.  # noqa: E501


        :return: The data_structure of this DataSourceVM.  # noqa: E501
        :rtype: str
        """
        return self._data_structure

    @data_structure.setter
    def data_structure(self, data_structure):
        """Sets the data_structure of this DataSourceVM.


        :param data_structure: The data_structure of this DataSourceVM.  # noqa: E501
        :type data_structure: str
        """

        self._data_structure = data_structure

    @property
    def subscription_id(self):
        """Gets the subscription_id of this DataSourceVM.  # noqa: E501


        :return: The subscription_id of this DataSourceVM.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this DataSourceVM.


        :param subscription_id: The subscription_id of this DataSourceVM.  # noqa: E501
        :type subscription_id: str
        """

        self._subscription_id = subscription_id

    @property
    def edited_time(self):
        """Gets the edited_time of this DataSourceVM.  # noqa: E501


        :return: The edited_time of this DataSourceVM.  # noqa: E501
        :rtype: datetime
        """
        return self._edited_time

    @edited_time.setter
    def edited_time(self, edited_time):
        """Sets the edited_time of this DataSourceVM.


        :param edited_time: The edited_time of this DataSourceVM.  # noqa: E501
        :type edited_time: datetime
        """

        self._edited_time = edited_time

    @property
    def editor_user_id(self):
        """Gets the editor_user_id of this DataSourceVM.  # noqa: E501


        :return: The editor_user_id of this DataSourceVM.  # noqa: E501
        :rtype: str
        """
        return self._editor_user_id

    @editor_user_id.setter
    def editor_user_id(self, editor_user_id):
        """Sets the editor_user_id of this DataSourceVM.


        :param editor_user_id: The editor_user_id of this DataSourceVM.  # noqa: E501
        :type editor_user_id: str
        """

        self._editor_user_id = editor_user_id

    @property
    def created_time(self):
        """Gets the created_time of this DataSourceVM.  # noqa: E501


        :return: The created_time of this DataSourceVM.  # noqa: E501
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this DataSourceVM.


        :param created_time: The created_time of this DataSourceVM.  # noqa: E501
        :type created_time: datetime
        """

        self._created_time = created_time

    @property
    def creator_user_id(self):
        """Gets the creator_user_id of this DataSourceVM.  # noqa: E501


        :return: The creator_user_id of this DataSourceVM.  # noqa: E501
        :rtype: str
        """
        return self._creator_user_id

    @creator_user_id.setter
    def creator_user_id(self, creator_user_id):
        """Sets the creator_user_id of this DataSourceVM.


        :param creator_user_id: The creator_user_id of this DataSourceVM.  # noqa: E501
        :type creator_user_id: str
        """

        self._creator_user_id = creator_user_id

    @property
    def is_connected(self):
        """Gets the is_connected of this DataSourceVM.  # noqa: E501


        :return: The is_connected of this DataSourceVM.  # noqa: E501
        :rtype: bool
        """
        return self._is_connected

    @is_connected.setter
    def is_connected(self, is_connected):
        """Sets the is_connected of this DataSourceVM.


        :param is_connected: The is_connected of this DataSourceVM.  # noqa: E501
        :type is_connected: bool
        """

        self._is_connected = is_connected

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
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
        if not isinstance(other, DataSourceVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataSourceVM):
            return True

        return self.to_dict() != other.to_dict()