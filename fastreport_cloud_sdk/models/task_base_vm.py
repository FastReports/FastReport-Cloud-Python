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


class TaskBaseVM(object):
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
        'cron_expression': 'str',
        'delayed_run_time': 'datetime',
        'delayed_was_run_time': 'datetime',
        'id': 'str',
        'name': 'str',
        'recurrent_run_time': 'datetime',
        'recurrent_was_run_time': 'datetime',
        'subscription_id': 'str',
        't': 'str'
    }

    attribute_map = {
        'cron_expression': 'cronExpression',
        'delayed_run_time': 'delayedRunTime',
        'delayed_was_run_time': 'delayedWasRunTime',
        'id': 'id',
        'name': 'name',
        'recurrent_run_time': 'recurrentRunTime',
        'recurrent_was_run_time': 'recurrentWasRunTime',
        'subscription_id': 'subscriptionId',
        't': '$t'
    }

    discriminator_value_class_map = {
        'FetchTaskVM': 'FetchTaskVM',
        'ThumbnailReportTaskVM': 'ThumbnailReportTaskVM',
        'ThumbnailTemplateTaskVM': 'ThumbnailTemplateTaskVM',
        'TransformTaskBaseVM': 'TransformTaskBaseVM',
        'TransportTaskBaseVM': 'TransportTaskBaseVM'
    }

    def __init__(self, cron_expression=None, delayed_run_time=None, delayed_was_run_time=None, id=None, name=None, recurrent_run_time=None, recurrent_was_run_time=None, subscription_id=None, t=None, local_vars_configuration=None):  # noqa: E501
        """TaskBaseVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._cron_expression = None
        self._delayed_run_time = None
        self._delayed_was_run_time = None
        self._id = None
        self._name = None
        self._recurrent_run_time = None
        self._recurrent_was_run_time = None
        self._subscription_id = None
        self._t = None
        self.discriminator = 't'

        self.cron_expression = cron_expression
        self.delayed_run_time = delayed_run_time
        self.delayed_was_run_time = delayed_was_run_time
        self.id = id
        self.name = name
        self.recurrent_run_time = recurrent_run_time
        self.recurrent_was_run_time = recurrent_was_run_time
        self.subscription_id = subscription_id
        self.t = t

    @property
    def cron_expression(self):
        """Gets the cron_expression of this TaskBaseVM.  # noqa: E501


        :return: The cron_expression of this TaskBaseVM.  # noqa: E501
        :rtype: str
        """
        return self._cron_expression

    @cron_expression.setter
    def cron_expression(self, cron_expression):
        """Sets the cron_expression of this TaskBaseVM.


        :param cron_expression: The cron_expression of this TaskBaseVM.  # noqa: E501
        :type cron_expression: str
        """

        self._cron_expression = cron_expression

    @property
    def delayed_run_time(self):
        """Gets the delayed_run_time of this TaskBaseVM.  # noqa: E501


        :return: The delayed_run_time of this TaskBaseVM.  # noqa: E501
        :rtype: datetime
        """
        return self._delayed_run_time

    @delayed_run_time.setter
    def delayed_run_time(self, delayed_run_time):
        """Sets the delayed_run_time of this TaskBaseVM.


        :param delayed_run_time: The delayed_run_time of this TaskBaseVM.  # noqa: E501
        :type delayed_run_time: datetime
        """

        self._delayed_run_time = delayed_run_time

    @property
    def delayed_was_run_time(self):
        """Gets the delayed_was_run_time of this TaskBaseVM.  # noqa: E501


        :return: The delayed_was_run_time of this TaskBaseVM.  # noqa: E501
        :rtype: datetime
        """
        return self._delayed_was_run_time

    @delayed_was_run_time.setter
    def delayed_was_run_time(self, delayed_was_run_time):
        """Sets the delayed_was_run_time of this TaskBaseVM.


        :param delayed_was_run_time: The delayed_was_run_time of this TaskBaseVM.  # noqa: E501
        :type delayed_was_run_time: datetime
        """

        self._delayed_was_run_time = delayed_was_run_time

    @property
    def id(self):
        """Gets the id of this TaskBaseVM.  # noqa: E501


        :return: The id of this TaskBaseVM.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskBaseVM.


        :param id: The id of this TaskBaseVM.  # noqa: E501
        :type id: str
        """
        if (self.local_vars_configuration.client_side_validation and
                id is not None and not re.search(r'^[A-Fa-f0-9]{24}$', id)):  # noqa: E501
            raise ValueError(r"Invalid value for `id`, must be a follow pattern or equal to `/^[A-Fa-f0-9]{24}$/`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this TaskBaseVM.  # noqa: E501


        :return: The name of this TaskBaseVM.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaskBaseVM.


        :param name: The name of this TaskBaseVM.  # noqa: E501
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
    def recurrent_run_time(self):
        """Gets the recurrent_run_time of this TaskBaseVM.  # noqa: E501


        :return: The recurrent_run_time of this TaskBaseVM.  # noqa: E501
        :rtype: datetime
        """
        return self._recurrent_run_time

    @recurrent_run_time.setter
    def recurrent_run_time(self, recurrent_run_time):
        """Sets the recurrent_run_time of this TaskBaseVM.


        :param recurrent_run_time: The recurrent_run_time of this TaskBaseVM.  # noqa: E501
        :type recurrent_run_time: datetime
        """

        self._recurrent_run_time = recurrent_run_time

    @property
    def recurrent_was_run_time(self):
        """Gets the recurrent_was_run_time of this TaskBaseVM.  # noqa: E501


        :return: The recurrent_was_run_time of this TaskBaseVM.  # noqa: E501
        :rtype: datetime
        """
        return self._recurrent_was_run_time

    @recurrent_was_run_time.setter
    def recurrent_was_run_time(self, recurrent_was_run_time):
        """Sets the recurrent_was_run_time of this TaskBaseVM.


        :param recurrent_was_run_time: The recurrent_was_run_time of this TaskBaseVM.  # noqa: E501
        :type recurrent_was_run_time: datetime
        """

        self._recurrent_was_run_time = recurrent_was_run_time

    @property
    def subscription_id(self):
        """Gets the subscription_id of this TaskBaseVM.  # noqa: E501


        :return: The subscription_id of this TaskBaseVM.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this TaskBaseVM.


        :param subscription_id: The subscription_id of this TaskBaseVM.  # noqa: E501
        :type subscription_id: str
        """
        if (self.local_vars_configuration.client_side_validation and
                subscription_id is not None and not re.search(r'(^$)|(^[A-Fa-f0-9]{24}$)', subscription_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `subscription_id`, must be a follow pattern or equal to `/(^$)|(^[A-Fa-f0-9]{24}$)/`")  # noqa: E501

        self._subscription_id = subscription_id

    @property
    def t(self):
        """Gets the t of this TaskBaseVM.  # noqa: E501


        :return: The t of this TaskBaseVM.  # noqa: E501
        :rtype: str
        """
        return self._t

    @t.setter
    def t(self, t):
        """Sets the t of this TaskBaseVM.


        :param t: The t of this TaskBaseVM.  # noqa: E501
        :type t: str
        """
        if self.local_vars_configuration.client_side_validation and t is None:  # noqa: E501
            raise ValueError("Invalid value for `t`, must not be `None`")  # noqa: E501

        self._t = t

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, TaskBaseVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskBaseVM):
            return True

        return self.to_dict() != other.to_dict()
