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


class SubscriptionInviteVM(object):
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
        'usages': 'int',
        'durable': 'bool',
        'access_token': 'str',
        'expired_date': 'datetime',
        'added_users': 'list[InvitedUser]',
        'creator_user_id': 'str'
    }

    attribute_map = {
        'usages': 'usages',
        'durable': 'durable',
        'access_token': 'accessToken',
        'expired_date': 'expiredDate',
        'added_users': 'addedUsers',
        'creator_user_id': 'creatorUserId'
    }

    def __init__(self, usages=None, durable=None, access_token=None, expired_date=None, added_users=None, creator_user_id=None, local_vars_configuration=None):  # noqa: E501
        """SubscriptionInviteVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._usages = None
        self._durable = None
        self._access_token = None
        self._expired_date = None
        self._added_users = None
        self._creator_user_id = None
        self.discriminator = None

        if usages is not None:
            self.usages = usages
        if durable is not None:
            self.durable = durable
        if access_token is not None:
            self.access_token = access_token
        if expired_date is not None:
            self.expired_date = expired_date
        if added_users is not None:
            self.added_users = added_users
        if creator_user_id is not None:
            self.creator_user_id = creator_user_id

    @property
    def usages(self):
        """Gets the usages of this SubscriptionInviteVM.  # noqa: E501


        :return: The usages of this SubscriptionInviteVM.  # noqa: E501
        :rtype: int
        """
        return self._usages

    @usages.setter
    def usages(self, usages):
        """Sets the usages of this SubscriptionInviteVM.


        :param usages: The usages of this SubscriptionInviteVM.  # noqa: E501
        :type usages: int
        """

        self._usages = usages

    @property
    def durable(self):
        """Gets the durable of this SubscriptionInviteVM.  # noqa: E501


        :return: The durable of this SubscriptionInviteVM.  # noqa: E501
        :rtype: bool
        """
        return self._durable

    @durable.setter
    def durable(self, durable):
        """Sets the durable of this SubscriptionInviteVM.


        :param durable: The durable of this SubscriptionInviteVM.  # noqa: E501
        :type durable: bool
        """

        self._durable = durable

    @property
    def access_token(self):
        """Gets the access_token of this SubscriptionInviteVM.  # noqa: E501


        :return: The access_token of this SubscriptionInviteVM.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this SubscriptionInviteVM.


        :param access_token: The access_token of this SubscriptionInviteVM.  # noqa: E501
        :type access_token: str
        """

        self._access_token = access_token

    @property
    def expired_date(self):
        """Gets the expired_date of this SubscriptionInviteVM.  # noqa: E501


        :return: The expired_date of this SubscriptionInviteVM.  # noqa: E501
        :rtype: datetime
        """
        return self._expired_date

    @expired_date.setter
    def expired_date(self, expired_date):
        """Sets the expired_date of this SubscriptionInviteVM.


        :param expired_date: The expired_date of this SubscriptionInviteVM.  # noqa: E501
        :type expired_date: datetime
        """

        self._expired_date = expired_date

    @property
    def added_users(self):
        """Gets the added_users of this SubscriptionInviteVM.  # noqa: E501


        :return: The added_users of this SubscriptionInviteVM.  # noqa: E501
        :rtype: list[InvitedUser]
        """
        return self._added_users

    @added_users.setter
    def added_users(self, added_users):
        """Sets the added_users of this SubscriptionInviteVM.


        :param added_users: The added_users of this SubscriptionInviteVM.  # noqa: E501
        :type added_users: list[InvitedUser]
        """

        self._added_users = added_users

    @property
    def creator_user_id(self):
        """Gets the creator_user_id of this SubscriptionInviteVM.  # noqa: E501


        :return: The creator_user_id of this SubscriptionInviteVM.  # noqa: E501
        :rtype: str
        """
        return self._creator_user_id

    @creator_user_id.setter
    def creator_user_id(self, creator_user_id):
        """Sets the creator_user_id of this SubscriptionInviteVM.


        :param creator_user_id: The creator_user_id of this SubscriptionInviteVM.  # noqa: E501
        :type creator_user_id: str
        """

        self._creator_user_id = creator_user_id

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
        if not isinstance(other, SubscriptionInviteVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubscriptionInviteVM):
            return True

        return self.to_dict() != other.to_dict()