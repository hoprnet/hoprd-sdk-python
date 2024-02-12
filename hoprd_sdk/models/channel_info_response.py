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

class ChannelInfoResponse(object):
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
        'channel_epoch': 'int',
        'channel_id': 'str',
        'closure_time': 'int',
        'destination_address': 'str',
        'destination_peer_id': 'str',
        'source_address': 'str',
        'source_peer_id': 'str',
        'status': 'str',
        'ticket_index': 'int'
    }

    attribute_map = {
        'balance': 'balance',
        'channel_epoch': 'channelEpoch',
        'channel_id': 'channelId',
        'closure_time': 'closureTime',
        'destination_address': 'destinationAddress',
        'destination_peer_id': 'destinationPeerId',
        'source_address': 'sourceAddress',
        'source_peer_id': 'sourcePeerId',
        'status': 'status',
        'ticket_index': 'ticketIndex'
    }

    def __init__(self, balance=None, channel_epoch=None, channel_id=None, closure_time=None, destination_address=None, destination_peer_id=None, source_address=None, source_peer_id=None, status=None, ticket_index=None):  # noqa: E501
        """ChannelInfoResponse - a model defined in Swagger"""  # noqa: E501
        self._balance = None
        self._channel_epoch = None
        self._channel_id = None
        self._closure_time = None
        self._destination_address = None
        self._destination_peer_id = None
        self._source_address = None
        self._source_peer_id = None
        self._status = None
        self._ticket_index = None
        self.discriminator = None
        self.balance = balance
        self.channel_epoch = channel_epoch
        self.channel_id = channel_id
        self.closure_time = closure_time
        self.destination_address = destination_address
        self.destination_peer_id = destination_peer_id
        self.source_address = source_address
        self.source_peer_id = source_peer_id
        self.status = status
        self.ticket_index = ticket_index

    @property
    def balance(self):
        """Gets the balance of this ChannelInfoResponse.  # noqa: E501


        :return: The balance of this ChannelInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this ChannelInfoResponse.


        :param balance: The balance of this ChannelInfoResponse.  # noqa: E501
        :type: str
        """
        if balance is None:
            raise ValueError("Invalid value for `balance`, must not be `None`")  # noqa: E501

        self._balance = balance

    @property
    def channel_epoch(self):
        """Gets the channel_epoch of this ChannelInfoResponse.  # noqa: E501


        :return: The channel_epoch of this ChannelInfoResponse.  # noqa: E501
        :rtype: int
        """
        return self._channel_epoch

    @channel_epoch.setter
    def channel_epoch(self, channel_epoch):
        """Sets the channel_epoch of this ChannelInfoResponse.


        :param channel_epoch: The channel_epoch of this ChannelInfoResponse.  # noqa: E501
        :type: int
        """
        if channel_epoch is None:
            raise ValueError("Invalid value for `channel_epoch`, must not be `None`")  # noqa: E501

        self._channel_epoch = channel_epoch

    @property
    def channel_id(self):
        """Gets the channel_id of this ChannelInfoResponse.  # noqa: E501


        :return: The channel_id of this ChannelInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """Sets the channel_id of this ChannelInfoResponse.


        :param channel_id: The channel_id of this ChannelInfoResponse.  # noqa: E501
        :type: str
        """
        if channel_id is None:
            raise ValueError("Invalid value for `channel_id`, must not be `None`")  # noqa: E501

        self._channel_id = channel_id

    @property
    def closure_time(self):
        """Gets the closure_time of this ChannelInfoResponse.  # noqa: E501


        :return: The closure_time of this ChannelInfoResponse.  # noqa: E501
        :rtype: int
        """
        return self._closure_time

    @closure_time.setter
    def closure_time(self, closure_time):
        """Sets the closure_time of this ChannelInfoResponse.


        :param closure_time: The closure_time of this ChannelInfoResponse.  # noqa: E501
        :type: int
        """
        if closure_time is None:
            raise ValueError("Invalid value for `closure_time`, must not be `None`")  # noqa: E501

        self._closure_time = closure_time

    @property
    def destination_address(self):
        """Gets the destination_address of this ChannelInfoResponse.  # noqa: E501


        :return: The destination_address of this ChannelInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._destination_address

    @destination_address.setter
    def destination_address(self, destination_address):
        """Sets the destination_address of this ChannelInfoResponse.


        :param destination_address: The destination_address of this ChannelInfoResponse.  # noqa: E501
        :type: str
        """
        if destination_address is None:
            raise ValueError("Invalid value for `destination_address`, must not be `None`")  # noqa: E501

        self._destination_address = destination_address

    @property
    def destination_peer_id(self):
        """Gets the destination_peer_id of this ChannelInfoResponse.  # noqa: E501


        :return: The destination_peer_id of this ChannelInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._destination_peer_id

    @destination_peer_id.setter
    def destination_peer_id(self, destination_peer_id):
        """Sets the destination_peer_id of this ChannelInfoResponse.


        :param destination_peer_id: The destination_peer_id of this ChannelInfoResponse.  # noqa: E501
        :type: str
        """
        if destination_peer_id is None:
            raise ValueError("Invalid value for `destination_peer_id`, must not be `None`")  # noqa: E501

        self._destination_peer_id = destination_peer_id

    @property
    def source_address(self):
        """Gets the source_address of this ChannelInfoResponse.  # noqa: E501


        :return: The source_address of this ChannelInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._source_address

    @source_address.setter
    def source_address(self, source_address):
        """Sets the source_address of this ChannelInfoResponse.


        :param source_address: The source_address of this ChannelInfoResponse.  # noqa: E501
        :type: str
        """
        if source_address is None:
            raise ValueError("Invalid value for `source_address`, must not be `None`")  # noqa: E501

        self._source_address = source_address

    @property
    def source_peer_id(self):
        """Gets the source_peer_id of this ChannelInfoResponse.  # noqa: E501


        :return: The source_peer_id of this ChannelInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._source_peer_id

    @source_peer_id.setter
    def source_peer_id(self, source_peer_id):
        """Sets the source_peer_id of this ChannelInfoResponse.


        :param source_peer_id: The source_peer_id of this ChannelInfoResponse.  # noqa: E501
        :type: str
        """
        if source_peer_id is None:
            raise ValueError("Invalid value for `source_peer_id`, must not be `None`")  # noqa: E501

        self._source_peer_id = source_peer_id

    @property
    def status(self):
        """Gets the status of this ChannelInfoResponse.  # noqa: E501


        :return: The status of this ChannelInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ChannelInfoResponse.


        :param status: The status of this ChannelInfoResponse.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def ticket_index(self):
        """Gets the ticket_index of this ChannelInfoResponse.  # noqa: E501


        :return: The ticket_index of this ChannelInfoResponse.  # noqa: E501
        :rtype: int
        """
        return self._ticket_index

    @ticket_index.setter
    def ticket_index(self, ticket_index):
        """Sets the ticket_index of this ChannelInfoResponse.


        :param ticket_index: The ticket_index of this ChannelInfoResponse.  # noqa: E501
        :type: int
        """
        if ticket_index is None:
            raise ValueError("Invalid value for `ticket_index`, must not be `None`")  # noqa: E501

        self._ticket_index = ticket_index

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
        if issubclass(ChannelInfoResponse, dict):
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
        if not isinstance(other, ChannelInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other