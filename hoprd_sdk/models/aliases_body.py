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

class AliasesBody(object):
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
        'peer_id': 'str',
        'alias': 'str'
    }

    attribute_map = {
        'peer_id': 'peerId',
        'alias': 'alias'
    }

    def __init__(self, peer_id=None, alias=None):  # noqa: E501
        """AliasesBody - a model defined in Swagger"""  # noqa: E501
        self._peer_id = None
        self._alias = None
        self.discriminator = None
        self.peer_id = peer_id
        self.alias = alias

    @property
    def peer_id(self):
        """Gets the peer_id of this AliasesBody.  # noqa: E501

        PeerId that we want to set alias to.  # noqa: E501

        :return: The peer_id of this AliasesBody.  # noqa: E501
        :rtype: str
        """
        return self._peer_id

    @peer_id.setter
    def peer_id(self, peer_id):
        """Sets the peer_id of this AliasesBody.

        PeerId that we want to set alias to.  # noqa: E501

        :param peer_id: The peer_id of this AliasesBody.  # noqa: E501
        :type: str
        """
        if peer_id is None:
            raise ValueError("Invalid value for `peer_id`, must not be `None`")  # noqa: E501

        self._peer_id = peer_id

    @property
    def alias(self):
        """Gets the alias of this AliasesBody.  # noqa: E501

        Alias that we want to attach to peerId.  # noqa: E501

        :return: The alias of this AliasesBody.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this AliasesBody.

        Alias that we want to attach to peerId.  # noqa: E501

        :param alias: The alias of this AliasesBody.  # noqa: E501
        :type: str
        """
        if alias is None:
            raise ValueError("Invalid value for `alias`, must not be `None`")  # noqa: E501

        self._alias = alias

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
        if issubclass(AliasesBody, dict):
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
        if not isinstance(other, AliasesBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
