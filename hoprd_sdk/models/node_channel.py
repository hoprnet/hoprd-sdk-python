# coding: utf-8

"""
    hoprd-api

    This Rest API enables developers to interact with a hoprd node programatically through HTTP.  # noqa: E501

    OpenAPI spec version: 3.2.0
    Contact: tech@hoprnet.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NodeChannel(object):
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
        'balance': 'str',
        'id': 'str',
        'peer_address': 'str',
        'status': 'str'
    }

    attribute_map = {
        'balance': 'balance',
        'id': 'id',
        'peer_address': 'peerAddress',
        'status': 'status'
    }

    def __init__(self, balance=None, id=None, peer_address=None, status=None):  # noqa: E501
        """NodeChannel - a model defined in Swagger"""  # noqa: E501
        self._balance = None
        self._id = None
        self._peer_address = None
        self._status = None
        self.discriminator = None
        self.balance = balance
        self.id = id
        self.peer_address = peer_address
        self.status = status

    @property
    def balance(self):
        """Gets the balance of this NodeChannel.  # noqa: E501


        :return: The balance of this NodeChannel.  # noqa: E501
        :rtype: str
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this NodeChannel.


        :param balance: The balance of this NodeChannel.  # noqa: E501
        :type: str
        """
        if balance is None:
            raise ValueError("Invalid value for `balance`, must not be `None`")  # noqa: E501

        self._balance = balance

    @property
    def id(self):
        """Gets the id of this NodeChannel.  # noqa: E501


        :return: The id of this NodeChannel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NodeChannel.


        :param id: The id of this NodeChannel.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def peer_address(self):
        """Gets the peer_address of this NodeChannel.  # noqa: E501


        :return: The peer_address of this NodeChannel.  # noqa: E501
        :rtype: str
        """
        return self._peer_address

    @peer_address.setter
    def peer_address(self, peer_address):
        """Sets the peer_address of this NodeChannel.


        :param peer_address: The peer_address of this NodeChannel.  # noqa: E501
        :type: str
        """
        if peer_address is None:
            raise ValueError("Invalid value for `peer_address`, must not be `None`")  # noqa: E501

        self._peer_address = peer_address

    @property
    def status(self):
        """Gets the status of this NodeChannel.  # noqa: E501


        :return: The status of this NodeChannel.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NodeChannel.


        :param status: The status of this NodeChannel.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

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
        if issubclass(NodeChannel, dict):
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
        if not isinstance(other, NodeChannel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
