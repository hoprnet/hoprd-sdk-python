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

class InlineResponse20013(object):
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
        'receipt': 'str'
    }

    attribute_map = {
        'receipt': 'receipt'
    }

    def __init__(self, receipt=None):  # noqa: E501
        """InlineResponse20013 - a model defined in Swagger"""  # noqa: E501
        self._receipt = None
        self.discriminator = None
        self.receipt = receipt

    @property
    def receipt(self):
        """Gets the receipt of this InlineResponse20013.  # noqa: E501

        Receipt of the funding transaction  # noqa: E501

        :return: The receipt of this InlineResponse20013.  # noqa: E501
        :rtype: str
        """
        return self._receipt

    @receipt.setter
    def receipt(self, receipt):
        """Sets the receipt of this InlineResponse20013.

        Receipt of the funding transaction  # noqa: E501

        :param receipt: The receipt of this InlineResponse20013.  # noqa: E501
        :type: str
        """
        if receipt is None:
            raise ValueError("Invalid value for `receipt`, must not be `None`")  # noqa: E501

        self._receipt = receipt

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
        if issubclass(InlineResponse20013, dict):
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
        if not isinstance(other, InlineResponse20013):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
