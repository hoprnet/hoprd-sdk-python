# coding: utf-8

"""
    HOPRd Rest API v3

    This Rest API enables developers to interact with a hoprd node programatically.  # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: tech@hoprnet.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Settings(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'include_recipient': 'bool',
        'strategy': 'str'
    }

    attribute_map = {
        'include_recipient': 'includeRecipient',
        'strategy': 'strategy'
    }

    def __init__(self, include_recipient=None, strategy=None):  # noqa: E501
        """Settings - a model defined in Swagger"""  # noqa: E501
        self._include_recipient = None
        self._strategy = None
        self.discriminator = None
        if include_recipient is not None:
            self.include_recipient = include_recipient
        if strategy is not None:
            self.strategy = strategy

    @property
    def include_recipient(self):
        """Gets the include_recipient of this Settings.  # noqa: E501

        Prepends your address to all messages so that receiver of the message can know that you sent that message.  # noqa: E501

        :return: The include_recipient of this Settings.  # noqa: E501
        :rtype: bool
        """
        return self._include_recipient

    @include_recipient.setter
    def include_recipient(self, include_recipient):
        """Sets the include_recipient of this Settings.

        Prepends your address to all messages so that receiver of the message can know that you sent that message.  # noqa: E501

        :param include_recipient: The include_recipient of this Settings.  # noqa: E501
        :type: bool
        """

        self._include_recipient = include_recipient

    @property
    def strategy(self):
        """Gets the strategy of this Settings.  # noqa: E501

        By default, hoprd runs in **passive** mode, this means that your node will not attempt to open or close any channels automatically. When you set your strategy to **promiscuous** mode, your node will attempt to open channels to a _randomly_ selected group of nodes which you have a healthy connection to. At the same time, your node will also attempt to close channels that are running low on balance or are unhealthy.  # noqa: E501

        :return: The strategy of this Settings.  # noqa: E501
        :rtype: str
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        """Sets the strategy of this Settings.

        By default, hoprd runs in **passive** mode, this means that your node will not attempt to open or close any channels automatically. When you set your strategy to **promiscuous** mode, your node will attempt to open channels to a _randomly_ selected group of nodes which you have a healthy connection to. At the same time, your node will also attempt to close channels that are running low on balance or are unhealthy.  # noqa: E501

        :param strategy: The strategy of this Settings.  # noqa: E501
        :type: str
        """
        allowed_values = ["passive", "promiscuous"]  # noqa: E501
        if strategy not in allowed_values:
            raise ValueError(
                "Invalid value for `strategy` ({0}), must be one of {1}"  # noqa: E501
                .format(strategy, allowed_values)
            )

        self._strategy = strategy

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Settings, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Settings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
