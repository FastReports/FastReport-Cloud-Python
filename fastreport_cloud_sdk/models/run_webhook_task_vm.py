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


class RunWebhookTaskVM(object):
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
        'headers': 'dict[str, str]',
        'url': 'str'
    }

    attribute_map = {
        'headers': 'headers',
        'url': 'url'
    }

    def __init__(self, headers=None, url=None, local_vars_configuration=None):  # noqa: E501
        """RunWebhookTaskVM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._headers = None
        self._url = None
        self.discriminator = None

        self.headers = headers
        self.url = url

    @property
    def headers(self):
        """Gets the headers of this RunWebhookTaskVM.  # noqa: E501


        :return: The headers of this RunWebhookTaskVM.  # noqa: E501
        :rtype: dict[str, str]
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this RunWebhookTaskVM.


        :param headers: The headers of this RunWebhookTaskVM.  # noqa: E501
        :type headers: dict[str, str]
        """

        self._headers = headers

    @property
    def url(self):
        """Gets the url of this RunWebhookTaskVM.  # noqa: E501


        :return: The url of this RunWebhookTaskVM.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this RunWebhookTaskVM.


        :param url: The url of this RunWebhookTaskVM.  # noqa: E501
        :type url: str
        """
        if (self.local_vars_configuration.client_side_validation and
                url is not None and len(url) > 5000):
            raise ValueError("Invalid value for `url`, length must be less than or equal to `5000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                url is not None and len(url) < 1):
            raise ValueError("Invalid value for `url`, length must be greater than or equal to `1`")  # noqa: E501

        self._url = url

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
        if not isinstance(other, RunWebhookTaskVM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RunWebhookTaskVM):
            return True

        return self.to_dict() != other.to_dict()
