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

class InlineResponse20010(object):
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
        'native': 'NativeAddress',
        'hopr': 'HoprAddress'
    }

    attribute_map = {
        'native': 'native',
        'hopr': 'hopr'
    }

    def __init__(self, native=None, hopr=None):  # noqa: E501
        """InlineResponse20010 - a model defined in Swagger"""  # noqa: E501
        self._native = None
        self._hopr = None
        self.discriminator = None
        if native is not None:
            self.native = native
        if hopr is not None:
            self.hopr = hopr

    @property
    def native(self):
        """Gets the native of this InlineResponse20010.  # noqa: E501


        :return: The native of this InlineResponse20010.  # noqa: E501
        :rtype: NativeAddress
        """
        return self._native

    @native.setter
    def native(self, native):
        """Sets the native of this InlineResponse20010.


        :param native: The native of this InlineResponse20010.  # noqa: E501
        :type: NativeAddress
        """

        self._native = native

    @property
    def hopr(self):
        """Gets the hopr of this InlineResponse20010.  # noqa: E501


        :return: The hopr of this InlineResponse20010.  # noqa: E501
        :rtype: HoprAddress
        """
        return self._hopr

    @hopr.setter
    def hopr(self, hopr):
        """Sets the hopr of this InlineResponse20010.


        :param hopr: The hopr of this InlineResponse20010.  # noqa: E501
        :type: HoprAddress
        """

        self._hopr = hopr

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
        if issubclass(InlineResponse20010, dict):
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
        if not isinstance(other, InlineResponse20010):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
