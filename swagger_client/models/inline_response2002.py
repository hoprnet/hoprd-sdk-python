# coding: utf-8

"""
    HOPRd Rest API v2

    This Rest API enables developers to interact with a hoprd node programatically.  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: tech@hoprnet.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse2002(object):
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
        'connected': 'list[InlineResponse2002Connected]',
        'announced': 'list[InlineResponse2002Connected]'
    }

    attribute_map = {
        'connected': 'connected',
        'announced': 'announced'
    }

    def __init__(self, connected=None, announced=None):  # noqa: E501
        """InlineResponse2002 - a model defined in Swagger"""  # noqa: E501
        self._connected = None
        self._announced = None
        self.discriminator = None
        if connected is not None:
            self.connected = connected
        if announced is not None:
            self.announced = announced

    @property
    def connected(self):
        """Gets the connected of this InlineResponse2002.  # noqa: E501


        :return: The connected of this InlineResponse2002.  # noqa: E501
        :rtype: list[InlineResponse2002Connected]
        """
        return self._connected

    @connected.setter
    def connected(self, connected):
        """Sets the connected of this InlineResponse2002.


        :param connected: The connected of this InlineResponse2002.  # noqa: E501
        :type: list[InlineResponse2002Connected]
        """

        self._connected = connected

    @property
    def announced(self):
        """Gets the announced of this InlineResponse2002.  # noqa: E501


        :return: The announced of this InlineResponse2002.  # noqa: E501
        :rtype: list[InlineResponse2002Connected]
        """
        return self._announced

    @announced.setter
    def announced(self, announced):
        """Sets the announced of this InlineResponse2002.


        :param announced: The announced of this InlineResponse2002.  # noqa: E501
        :type: list[InlineResponse2002Connected]
        """

        self._announced = announced

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
        if issubclass(InlineResponse2002, dict):
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
        if not isinstance(other, InlineResponse2002):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other