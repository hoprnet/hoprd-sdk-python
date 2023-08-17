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
        'announced': 'list[MultiAddress]',
        'observed': 'list[MultiAddress]'
    }

    attribute_map = {
        'announced': 'announced',
        'observed': 'observed'
    }

    def __init__(self, announced=None, observed=None):  # noqa: E501
        """InlineResponse20010 - a model defined in Swagger"""  # noqa: E501
        self._announced = None
        self._observed = None
        self.discriminator = None
        if announced is not None:
            self.announced = announced
        if observed is not None:
            self.observed = observed

    @property
    def announced(self):
        """Gets the announced of this InlineResponse20010.  # noqa: E501


        :return: The announced of this InlineResponse20010.  # noqa: E501
        :rtype: list[MultiAddress]
        """
        return self._announced

    @announced.setter
    def announced(self, announced):
        """Sets the announced of this InlineResponse20010.


        :param announced: The announced of this InlineResponse20010.  # noqa: E501
        :type: list[MultiAddress]
        """

        self._announced = announced

    @property
    def observed(self):
        """Gets the observed of this InlineResponse20010.  # noqa: E501


        :return: The observed of this InlineResponse20010.  # noqa: E501
        :rtype: list[MultiAddress]
        """
        return self._observed

    @observed.setter
    def observed(self, observed):
        """Sets the observed of this InlineResponse20010.


        :param observed: The observed of this InlineResponse20010.  # noqa: E501
        :type: list[MultiAddress]
        """

        self._observed = observed

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
