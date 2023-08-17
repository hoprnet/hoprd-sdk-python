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

class TokensBody(object):
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
        'capabilities': 'list[TokenCapability]',
        'lifetime': 'int',
        'description': 'str'
    }

    attribute_map = {
        'capabilities': 'capabilities',
        'lifetime': 'lifetime',
        'description': 'description'
    }

    def __init__(self, capabilities=None, lifetime=None, description=None):  # noqa: E501
        """TokensBody - a model defined in Swagger"""  # noqa: E501
        self._capabilities = None
        self._lifetime = None
        self._description = None
        self.discriminator = None
        self.capabilities = capabilities
        if lifetime is not None:
            self.lifetime = lifetime
        if description is not None:
            self.description = description

    @property
    def capabilities(self):
        """Gets the capabilities of this TokensBody.  # noqa: E501

        Capabilities attached to the created token.  # noqa: E501

        :return: The capabilities of this TokensBody.  # noqa: E501
        :rtype: list[TokenCapability]
        """
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        """Sets the capabilities of this TokensBody.

        Capabilities attached to the created token.  # noqa: E501

        :param capabilities: The capabilities of this TokensBody.  # noqa: E501
        :type: list[TokenCapability]
        """
        if capabilities is None:
            raise ValueError("Invalid value for `capabilities`, must not be `None`")  # noqa: E501

        self._capabilities = capabilities

    @property
    def lifetime(self):
        """Gets the lifetime of this TokensBody.  # noqa: E501

        Lifetime of the token in seconds since creation. Defaults to unlimited lifetime.  # noqa: E501

        :return: The lifetime of this TokensBody.  # noqa: E501
        :rtype: int
        """
        return self._lifetime

    @lifetime.setter
    def lifetime(self, lifetime):
        """Sets the lifetime of this TokensBody.

        Lifetime of the token in seconds since creation. Defaults to unlimited lifetime.  # noqa: E501

        :param lifetime: The lifetime of this TokensBody.  # noqa: E501
        :type: int
        """

        self._lifetime = lifetime

    @property
    def description(self):
        """Gets the description of this TokensBody.  # noqa: E501

        Description associated with the token.  # noqa: E501

        :return: The description of this TokensBody.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TokensBody.

        Description associated with the token.  # noqa: E501

        :param description: The description of this TokensBody.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(TokensBody, dict):
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
        if not isinstance(other, TokensBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
