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


class EntityVM(object):
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
        'created_time': 'datetime',
        'creator_user_id': 'str',
        'edited_time': 'datetime',
        'editor_user_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created_time': 'createdTime',
        'creator_user_id': 'creatorUserId',
        'edited_time': 'editedTime',
        'editor_user_id': 'editorUserId'
    }

    def __init__(self, id=None, created_time=None, creator_user_id=None, edited_time=None, editor_user_id=None, local_vars_configuration=None):  # noqa: E501
        """EntityVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created_time = None
        self._creator_user_id = None
        self._edited_time = None
        self._editor_user_id = None
        self.discriminator = None

        self.id = id
        if created_time is not None:
            self.created_time = created_time
        self.creator_user_id = creator_user_id
        if edited_time is not None:
            self.edited_time = edited_time
        self.editor_user_id = editor_user_id

    @property
    def id(self):
        """Gets the id of this EntityVM.  # noqa: E501


        :return: The id of this EntityVM.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EntityVM.


        :param id: The id of this EntityVM.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this EntityVM.  # noqa: E501


        :return: The created_time of this EntityVM.  # noqa: E501
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this EntityVM.


        :param created_time: The created_time of this EntityVM.  # noqa: E501
        :type created_time: datetime
        """

        self._created_time = created_time

    @property
    def creator_user_id(self):
        """Gets the creator_user_id of this EntityVM.  # noqa: E501


        :return: The creator_user_id of this EntityVM.  # noqa: E501
        :rtype: str
        """
        return self._creator_user_id

    @creator_user_id.setter
    def creator_user_id(self, creator_user_id):
        """Sets the creator_user_id of this EntityVM.


        :param creator_user_id: The creator_user_id of this EntityVM.  # noqa: E501
        :type creator_user_id: str
        """

        self._creator_user_id = creator_user_id

    @property
    def edited_time(self):
        """Gets the edited_time of this EntityVM.  # noqa: E501


        :return: The edited_time of this EntityVM.  # noqa: E501
        :rtype: datetime
        """
        return self._edited_time

    @edited_time.setter
    def edited_time(self, edited_time):
        """Sets the edited_time of this EntityVM.


        :param edited_time: The edited_time of this EntityVM.  # noqa: E501
        :type edited_time: datetime
        """

        self._edited_time = edited_time

    @property
    def editor_user_id(self):
        """Gets the editor_user_id of this EntityVM.  # noqa: E501


        :return: The editor_user_id of this EntityVM.  # noqa: E501
        :rtype: str
        """
        return self._editor_user_id

    @editor_user_id.setter
    def editor_user_id(self, editor_user_id):
        """Sets the editor_user_id of this EntityVM.


        :param editor_user_id: The editor_user_id of this EntityVM.  # noqa: E501
        :type editor_user_id: str
        """

        self._editor_user_id = editor_user_id

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
        if not isinstance(other, EntityVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EntityVM):
            return True

        return self.to_dict() != other.to_dict()
