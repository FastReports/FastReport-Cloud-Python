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


class AuditActionVM(object):
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
        'user_id': 'str',
        'entity_id': 'str',
        'subscription_id': 'str',
        'type': 'AuditType',
        'id': 'str',
        'created_time': 'datetime',
        'creator_user_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'user_id': 'userId',
        'entity_id': 'entityId',
        'subscription_id': 'subscriptionId',
        'type': 'type',
        'id': 'id',
        'created_time': 'createdTime',
        'creator_user_id': 'creatorUserId',
        'name': 'name'
    }

    def __init__(self, user_id=None, entity_id=None, subscription_id=None, type=None, id=None, created_time=None, creator_user_id=None, name=None, local_vars_configuration=None):  # noqa: E501
        """AuditActionVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._user_id = None
        self._entity_id = None
        self._subscription_id = None
        self._type = None
        self._id = None
        self._created_time = None
        self._creator_user_id = None
        self._name = None
        self.discriminator = None

        self.user_id = user_id
        self.entity_id = entity_id
        self.subscription_id = subscription_id
        if type is not None:
            self.type = type
        self.id = id
        if created_time is not None:
            self.created_time = created_time
        self.creator_user_id = creator_user_id
        self.name = name

    @property
    def user_id(self):
        """Gets the user_id of this AuditActionVM.  # noqa: E501


        :return: The user_id of this AuditActionVM.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AuditActionVM.


        :param user_id: The user_id of this AuditActionVM.  # noqa: E501
        :type user_id: str
        """

        self._user_id = user_id

    @property
    def entity_id(self):
        """Gets the entity_id of this AuditActionVM.  # noqa: E501


        :return: The entity_id of this AuditActionVM.  # noqa: E501
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this AuditActionVM.


        :param entity_id: The entity_id of this AuditActionVM.  # noqa: E501
        :type entity_id: str
        """

        self._entity_id = entity_id

    @property
    def subscription_id(self):
        """Gets the subscription_id of this AuditActionVM.  # noqa: E501


        :return: The subscription_id of this AuditActionVM.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this AuditActionVM.


        :param subscription_id: The subscription_id of this AuditActionVM.  # noqa: E501
        :type subscription_id: str
        """

        self._subscription_id = subscription_id

    @property
    def type(self):
        """Gets the type of this AuditActionVM.  # noqa: E501


        :return: The type of this AuditActionVM.  # noqa: E501
        :rtype: AuditType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AuditActionVM.


        :param type: The type of this AuditActionVM.  # noqa: E501
        :type type: AuditType
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this AuditActionVM.  # noqa: E501


        :return: The id of this AuditActionVM.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuditActionVM.


        :param id: The id of this AuditActionVM.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this AuditActionVM.  # noqa: E501


        :return: The created_time of this AuditActionVM.  # noqa: E501
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this AuditActionVM.


        :param created_time: The created_time of this AuditActionVM.  # noqa: E501
        :type created_time: datetime
        """

        self._created_time = created_time

    @property
    def creator_user_id(self):
        """Gets the creator_user_id of this AuditActionVM.  # noqa: E501


        :return: The creator_user_id of this AuditActionVM.  # noqa: E501
        :rtype: str
        """
        return self._creator_user_id

    @creator_user_id.setter
    def creator_user_id(self, creator_user_id):
        """Sets the creator_user_id of this AuditActionVM.


        :param creator_user_id: The creator_user_id of this AuditActionVM.  # noqa: E501
        :type creator_user_id: str
        """

        self._creator_user_id = creator_user_id

    @property
    def name(self):
        """Gets the name of this AuditActionVM.  # noqa: E501


        :return: The name of this AuditActionVM.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AuditActionVM.


        :param name: The name of this AuditActionVM.  # noqa: E501
        :type name: str
        """

        self._name = name

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
        if not isinstance(other, AuditActionVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuditActionVM):
            return True

        return self.to_dict() != other.to_dict()
