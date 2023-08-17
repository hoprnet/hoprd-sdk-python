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

class TokenCapability(object):
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
        'endpoint': 'str',
        'limits': 'list[TokenCapabilityLimit]'
    }

    attribute_map = {
        'endpoint': 'endpoint',
        'limits': 'limits'
    }

    def __init__(self, endpoint=None, limits=None):  # noqa: E501
        """TokenCapability - a model defined in Swagger"""  # noqa: E501
        self._endpoint = None
        self._limits = None
        self.discriminator = None
        self.endpoint = endpoint
        if limits is not None:
            self.limits = limits

    @property
    def endpoint(self):
        """Gets the endpoint of this TokenCapability.  # noqa: E501

        Short reference of the operation this capability is tied to.  # noqa: E501

        :return: The endpoint of this TokenCapability.  # noqa: E501
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this TokenCapability.

        Short reference of the operation this capability is tied to.  # noqa: E501

        :param endpoint: The endpoint of this TokenCapability.  # noqa: E501
        :type: str
        """
        if endpoint is None:
            raise ValueError("Invalid value for `endpoint`, must not be `None`")  # noqa: E501
        allowed_values = ["tokensCreate", "tokensGetToken", "ticketsGetStatistics", "ticketsRedeemTickets", "ticketsGetTickets", "settingsGetSettings", "nodeGetVersion", "nodeStreamWebsocket", "nodeGetPeers", "nodeGetMetrics", "nodeGetInfo", "nodeGetEntryNodes", "messagesWebsocket", "messagesSendMessage", "messagesListMessages", "channelsFundChannels", "channelsOpenChannel", "channelsGetChannels", "aliasesSetAlias", "aliasesGetAliases", "accountWithdraw", "accountGetBalances", "accountGetAddresses", "tokensDelete", "settingsSetSetting", "peersGetPeerInfo", "peersPingPeer", "channelsRedeemTickets", "channelsGetTickets", "channelsGetChannel", "channelsCloseChannel", "aliasesGetAlias", "aliasesRemoveAlias"]  # noqa: E501
        if endpoint not in allowed_values:
            raise ValueError(
                "Invalid value for `endpoint` ({0}), must be one of {1}"  # noqa: E501
                .format(endpoint, allowed_values)
            )

        self._endpoint = endpoint

    @property
    def limits(self):
        """Gets the limits of this TokenCapability.  # noqa: E501


        :return: The limits of this TokenCapability.  # noqa: E501
        :rtype: list[TokenCapabilityLimit]
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """Sets the limits of this TokenCapability.


        :param limits: The limits of this TokenCapability.  # noqa: E501
        :type: list[TokenCapabilityLimit]
        """

        self._limits = limits

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
        if issubclass(TokenCapability, dict):
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
        if not isinstance(other, TokenCapability):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
