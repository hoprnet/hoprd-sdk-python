# coding: utf-8

"""
    hoprd-api

    API server using the hopr-lib created HOPR node and exposing it using a HTTP REST API  # noqa: E501

    OpenAPI spec version: 0.2.0
    Contact: tech@hoprnet.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class MessagePopResponse(object):
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
        'body': 'str',
        'received_at': 'int',
        'tag': 'int'
    }

    attribute_map = {
        'body': 'body',
        'received_at': 'receivedAt',
        'tag': 'tag'
    }

    def __init__(self, body=None, received_at=None, tag=None):  # noqa: E501
        """MessagePopResponse - a model defined in Swagger"""  # noqa: E501
        self._body = None
        self._received_at = None
        self._tag = None
        self.discriminator = None
        self.body = body
        self.received_at = received_at
        self.tag = tag

    @property
    def body(self):
        """Gets the body of this MessagePopResponse.  # noqa: E501


        :return: The body of this MessagePopResponse.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this MessagePopResponse.


        :param body: The body of this MessagePopResponse.  # noqa: E501
        :type: str
        """
        if body is None:
            raise ValueError("Invalid value for `body`, must not be `None`")  # noqa: E501

        self._body = body

    @property
    def received_at(self):
        """Gets the received_at of this MessagePopResponse.  # noqa: E501


        :return: The received_at of this MessagePopResponse.  # noqa: E501
        :rtype: int
        """
        return self._received_at

    @received_at.setter
    def received_at(self, received_at):
        """Sets the received_at of this MessagePopResponse.


        :param received_at: The received_at of this MessagePopResponse.  # noqa: E501
        :type: int
        """
        if received_at is None:
            raise ValueError("Invalid value for `received_at`, must not be `None`")  # noqa: E501

        self._received_at = received_at

    @property
    def tag(self):
        """Gets the tag of this MessagePopResponse.  # noqa: E501


        :return: The tag of this MessagePopResponse.  # noqa: E501
        :rtype: int
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this MessagePopResponse.


        :param tag: The tag of this MessagePopResponse.  # noqa: E501
        :type: int
        """
        if tag is None:
            raise ValueError("Invalid value for `tag`, must not be `None`")  # noqa: E501

        self._tag = tag

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
        if issubclass(MessagePopResponse, dict):
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
        if not isinstance(other, MessagePopResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
