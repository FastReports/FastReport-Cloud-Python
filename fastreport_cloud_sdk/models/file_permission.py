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


class FilePermission(object):
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
        'create': 'int',
        'delete': 'int',
        'execute': 'int',
        'get': 'int',
        'update': 'int',
        'administrate': 'int'
    }

    attribute_map = {
        'create': 'create',
        'delete': 'delete',
        'execute': 'execute',
        'get': 'get',
        'update': 'update',
        'administrate': 'administrate'
    }

    def __init__(self, create=None, delete=None, execute=None, get=None, update=None, administrate=None, local_vars_configuration=None):  # noqa: E501
        """FilePermission - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._create = None
        self._delete = None
        self._execute = None
        self._get = None
        self._update = None
        self._administrate = None
        self.discriminator = None

        if create is not None:
            self.create = create
        if delete is not None:
            self.delete = delete
        if execute is not None:
            self.execute = execute
        if get is not None:
            self.get = get
        if update is not None:
            self.update = update
        if administrate is not None:
            self.administrate = administrate

    @property
    def create(self):
        """Gets the create of this FilePermission.  # noqa: E501


        :return: The create of this FilePermission.  # noqa: E501
        :rtype: int
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this FilePermission.


        :param create: The create of this FilePermission.  # noqa: E501
        :type create: int
        """
        allowed_values = [0, 1, -1]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and create not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `create` ({0}), must be one of {1}"  # noqa: E501
                .format(create, allowed_values)
            )

        self._create = create

    @property
    def delete(self):
        """Gets the delete of this FilePermission.  # noqa: E501


        :return: The delete of this FilePermission.  # noqa: E501
        :rtype: int
        """
        return self._delete

    @delete.setter
    def delete(self, delete):
        """Sets the delete of this FilePermission.


        :param delete: The delete of this FilePermission.  # noqa: E501
        :type delete: int
        """
        allowed_values = [0, 1, -1]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and delete not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `delete` ({0}), must be one of {1}"  # noqa: E501
                .format(delete, allowed_values)
            )

        self._delete = delete

    @property
    def execute(self):
        """Gets the execute of this FilePermission.  # noqa: E501


        :return: The execute of this FilePermission.  # noqa: E501
        :rtype: int
        """
        return self._execute

    @execute.setter
    def execute(self, execute):
        """Sets the execute of this FilePermission.


        :param execute: The execute of this FilePermission.  # noqa: E501
        :type execute: int
        """
        allowed_values = [0, 1, 2, 4, -1]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and execute not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `execute` ({0}), must be one of {1}"  # noqa: E501
                .format(execute, allowed_values)
            )

        self._execute = execute

    @property
    def get(self):
        """Gets the get of this FilePermission.  # noqa: E501


        :return: The get of this FilePermission.  # noqa: E501
        :rtype: int
        """
        return self._get

    @get.setter
    def get(self, get):
        """Sets the get of this FilePermission.


        :param get: The get of this FilePermission.  # noqa: E501
        :type get: int
        """
        allowed_values = [0, 1, 2, 4, 8, 16, -1]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and get not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `get` ({0}), must be one of {1}"  # noqa: E501
                .format(get, allowed_values)
            )

        self._get = get

    @property
    def update(self):
        """Gets the update of this FilePermission.  # noqa: E501


        :return: The update of this FilePermission.  # noqa: E501
        :rtype: int
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this FilePermission.


        :param update: The update of this FilePermission.  # noqa: E501
        :type update: int
        """
        allowed_values = [0, 1, 2, 4, 8, -1]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and update not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `update` ({0}), must be one of {1}"  # noqa: E501
                .format(update, allowed_values)
            )

        self._update = update

    @property
    def administrate(self):
        """Gets the administrate of this FilePermission.  # noqa: E501


        :return: The administrate of this FilePermission.  # noqa: E501
        :rtype: int
        """
        return self._administrate

    @administrate.setter
    def administrate(self, administrate):
        """Sets the administrate of this FilePermission.


        :param administrate: The administrate of this FilePermission.  # noqa: E501
        :type administrate: int
        """
        allowed_values = [0, 1, 2, 4, 8, -1]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and administrate not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `administrate` ({0}), must be one of {1}"  # noqa: E501
                .format(administrate, allowed_values)
            )

        self._administrate = administrate

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
        if not isinstance(other, FilePermission):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FilePermission):
            return True

        return self.to_dict() != other.to_dict()