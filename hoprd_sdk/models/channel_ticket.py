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

class ChannelTicket(object):
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
        'amount': 'str',
        'channel_epoch': 'int',
        'channel_id': 'str',
        'index': 'int',
        'index_offset': 'int',
        'signature': 'str',
        'win_prob': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'channel_epoch': 'channelEpoch',
        'channel_id': 'channelId',
        'index': 'index',
        'index_offset': 'indexOffset',
        'signature': 'signature',
        'win_prob': 'winProb'
    }

    def __init__(self, amount=None, channel_epoch=None, channel_id=None, index=None, index_offset=None, signature=None, win_prob=None):  # noqa: E501
        """ChannelTicket - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._channel_epoch = None
        self._channel_id = None
        self._index = None
        self._index_offset = None
        self._signature = None
        self._win_prob = None
        self.discriminator = None
        self.amount = amount
        self.channel_epoch = channel_epoch
        self.channel_id = channel_id
        self.index = index
        self.index_offset = index_offset
        self.signature = signature
        self.win_prob = win_prob

    @property
    def amount(self):
        """Gets the amount of this ChannelTicket.  # noqa: E501


        :return: The amount of this ChannelTicket.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ChannelTicket.


        :param amount: The amount of this ChannelTicket.  # noqa: E501
        :type: str
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def channel_epoch(self):
        """Gets the channel_epoch of this ChannelTicket.  # noqa: E501


        :return: The channel_epoch of this ChannelTicket.  # noqa: E501
        :rtype: int
        """
        return self._channel_epoch

    @channel_epoch.setter
    def channel_epoch(self, channel_epoch):
        """Sets the channel_epoch of this ChannelTicket.


        :param channel_epoch: The channel_epoch of this ChannelTicket.  # noqa: E501
        :type: int
        """
        if channel_epoch is None:
            raise ValueError("Invalid value for `channel_epoch`, must not be `None`")  # noqa: E501

        self._channel_epoch = channel_epoch

    @property
    def channel_id(self):
        """Gets the channel_id of this ChannelTicket.  # noqa: E501


        :return: The channel_id of this ChannelTicket.  # noqa: E501
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """Sets the channel_id of this ChannelTicket.


        :param channel_id: The channel_id of this ChannelTicket.  # noqa: E501
        :type: str
        """
        if channel_id is None:
            raise ValueError("Invalid value for `channel_id`, must not be `None`")  # noqa: E501

        self._channel_id = channel_id

    @property
    def index(self):
        """Gets the index of this ChannelTicket.  # noqa: E501


        :return: The index of this ChannelTicket.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this ChannelTicket.


        :param index: The index of this ChannelTicket.  # noqa: E501
        :type: int
        """
        if index is None:
            raise ValueError("Invalid value for `index`, must not be `None`")  # noqa: E501

        self._index = index

    @property
    def index_offset(self):
        """Gets the index_offset of this ChannelTicket.  # noqa: E501


        :return: The index_offset of this ChannelTicket.  # noqa: E501
        :rtype: int
        """
        return self._index_offset

    @index_offset.setter
    def index_offset(self, index_offset):
        """Sets the index_offset of this ChannelTicket.


        :param index_offset: The index_offset of this ChannelTicket.  # noqa: E501
        :type: int
        """
        if index_offset is None:
            raise ValueError("Invalid value for `index_offset`, must not be `None`")  # noqa: E501

        self._index_offset = index_offset

    @property
    def signature(self):
        """Gets the signature of this ChannelTicket.  # noqa: E501


        :return: The signature of this ChannelTicket.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this ChannelTicket.


        :param signature: The signature of this ChannelTicket.  # noqa: E501
        :type: str
        """
        if signature is None:
            raise ValueError("Invalid value for `signature`, must not be `None`")  # noqa: E501

        self._signature = signature

    @property
    def win_prob(self):
        """Gets the win_prob of this ChannelTicket.  # noqa: E501


        :return: The win_prob of this ChannelTicket.  # noqa: E501
        :rtype: str
        """
        return self._win_prob

    @win_prob.setter
    def win_prob(self, win_prob):
        """Sets the win_prob of this ChannelTicket.


        :param win_prob: The win_prob of this ChannelTicket.  # noqa: E501
        :type: str
        """
        if win_prob is None:
            raise ValueError("Invalid value for `win_prob`, must not be `None`")  # noqa: E501

        self._win_prob = win_prob

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
        if issubclass(ChannelTicket, dict):
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
        if not isinstance(other, ChannelTicket):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
