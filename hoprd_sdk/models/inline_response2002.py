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

class InlineResponse2002(object):
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
        'network': 'str',
        'announced_address': 'list[str]',
        'listening_address': 'list[str]',
        'chain': 'str',
        'hopr_token': 'str',
        'hopr_channels': 'str',
        'hopr_network_registry_address': 'str',
        'hopr_node_safe_registry_address': 'str',
        'node_management_module': 'str',
        'node_safe': 'str',
        'connectivity_status': 'str',
        'is_eligible': 'bool',
        'channel_closure_period': 'float'
    }

    attribute_map = {
        'network': 'network',
        'announced_address': 'announcedAddress',
        'listening_address': 'listeningAddress',
        'chain': 'chain',
        'hopr_token': 'hoprToken',
        'hopr_channels': 'hoprChannels',
        'hopr_network_registry_address': 'hoprNetworkRegistryAddress',
        'hopr_node_safe_registry_address': 'hoprNodeSafeRegistryAddress',
        'node_management_module': 'nodeManagementModule',
        'node_safe': 'nodeSafe',
        'connectivity_status': 'connectivityStatus',
        'is_eligible': 'isEligible',
        'channel_closure_period': 'channelClosurePeriod'
    }

    def __init__(self, network=None, announced_address=None, listening_address=None, chain=None, hopr_token=None, hopr_channels=None, hopr_network_registry_address=None, hopr_node_safe_registry_address=None, node_management_module=None, node_safe=None, connectivity_status=None, is_eligible=None, channel_closure_period=None):  # noqa: E501
        """InlineResponse2002 - a model defined in Swagger"""  # noqa: E501
        self._network = None
        self._announced_address = None
        self._listening_address = None
        self._chain = None
        self._hopr_token = None
        self._hopr_channels = None
        self._hopr_network_registry_address = None
        self._hopr_node_safe_registry_address = None
        self._node_management_module = None
        self._node_safe = None
        self._connectivity_status = None
        self._is_eligible = None
        self._channel_closure_period = None
        self.discriminator = None
        if network is not None:
            self.network = network
        if announced_address is not None:
            self.announced_address = announced_address
        if listening_address is not None:
            self.listening_address = listening_address
        if chain is not None:
            self.chain = chain
        if hopr_token is not None:
            self.hopr_token = hopr_token
        if hopr_channels is not None:
            self.hopr_channels = hopr_channels
        if hopr_network_registry_address is not None:
            self.hopr_network_registry_address = hopr_network_registry_address
        if hopr_node_safe_registry_address is not None:
            self.hopr_node_safe_registry_address = hopr_node_safe_registry_address
        if node_management_module is not None:
            self.node_management_module = node_management_module
        if node_safe is not None:
            self.node_safe = node_safe
        if connectivity_status is not None:
            self.connectivity_status = connectivity_status
        if is_eligible is not None:
            self.is_eligible = is_eligible
        if channel_closure_period is not None:
            self.channel_closure_period = channel_closure_period

    @property
    def network(self):
        """Gets the network of this InlineResponse2002.  # noqa: E501

        Name of the network the node is running on.  # noqa: E501

        :return: The network of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this InlineResponse2002.

        Name of the network the node is running on.  # noqa: E501

        :param network: The network of this InlineResponse2002.  # noqa: E501
        :type: str
        """

        self._network = network

    @property
    def announced_address(self):
        """Gets the announced_address of this InlineResponse2002.  # noqa: E501


        :return: The announced_address of this InlineResponse2002.  # noqa: E501
        :rtype: list[str]
        """
        return self._announced_address

    @announced_address.setter
    def announced_address(self, announced_address):
        """Sets the announced_address of this InlineResponse2002.


        :param announced_address: The announced_address of this InlineResponse2002.  # noqa: E501
        :type: list[str]
        """

        self._announced_address = announced_address

    @property
    def listening_address(self):
        """Gets the listening_address of this InlineResponse2002.  # noqa: E501


        :return: The listening_address of this InlineResponse2002.  # noqa: E501
        :rtype: list[str]
        """
        return self._listening_address

    @listening_address.setter
    def listening_address(self, listening_address):
        """Sets the listening_address of this InlineResponse2002.


        :param listening_address: The listening_address of this InlineResponse2002.  # noqa: E501
        :type: list[str]
        """

        self._listening_address = listening_address

    @property
    def chain(self):
        """Gets the chain of this InlineResponse2002.  # noqa: E501

        Name of the Hopr network this node connects to.  # noqa: E501

        :return: The chain of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._chain

    @chain.setter
    def chain(self, chain):
        """Sets the chain of this InlineResponse2002.

        Name of the Hopr network this node connects to.  # noqa: E501

        :param chain: The chain of this InlineResponse2002.  # noqa: E501
        :type: str
        """

        self._chain = chain

    @property
    def hopr_token(self):
        """Gets the hopr_token of this InlineResponse2002.  # noqa: E501

        Contract address of the Hopr token on the ethereum chain.  # noqa: E501

        :return: The hopr_token of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._hopr_token

    @hopr_token.setter
    def hopr_token(self, hopr_token):
        """Sets the hopr_token of this InlineResponse2002.

        Contract address of the Hopr token on the ethereum chain.  # noqa: E501

        :param hopr_token: The hopr_token of this InlineResponse2002.  # noqa: E501
        :type: str
        """

        self._hopr_token = hopr_token

    @property
    def hopr_channels(self):
        """Gets the hopr_channels of this InlineResponse2002.  # noqa: E501

        Contract address of the HoprChannels smart contract on ethereum chain. This smart contract is used to open payment channels between nodes on blockchain.  # noqa: E501

        :return: The hopr_channels of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._hopr_channels

    @hopr_channels.setter
    def hopr_channels(self, hopr_channels):
        """Sets the hopr_channels of this InlineResponse2002.

        Contract address of the HoprChannels smart contract on ethereum chain. This smart contract is used to open payment channels between nodes on blockchain.  # noqa: E501

        :param hopr_channels: The hopr_channels of this InlineResponse2002.  # noqa: E501
        :type: str
        """

        self._hopr_channels = hopr_channels

    @property
    def hopr_network_registry_address(self):
        """Gets the hopr_network_registry_address of this InlineResponse2002.  # noqa: E501

        Contract address of the contract that allows to control the number of nodes in the network  # noqa: E501

        :return: The hopr_network_registry_address of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._hopr_network_registry_address

    @hopr_network_registry_address.setter
    def hopr_network_registry_address(self, hopr_network_registry_address):
        """Sets the hopr_network_registry_address of this InlineResponse2002.

        Contract address of the contract that allows to control the number of nodes in the network  # noqa: E501

        :param hopr_network_registry_address: The hopr_network_registry_address of this InlineResponse2002.  # noqa: E501
        :type: str
        """

        self._hopr_network_registry_address = hopr_network_registry_address

    @property
    def hopr_node_safe_registry_address(self):
        """Gets the hopr_node_safe_registry_address of this InlineResponse2002.  # noqa: E501

        Contract address of the contract that register node and safe pairs  # noqa: E501

        :return: The hopr_node_safe_registry_address of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._hopr_node_safe_registry_address

    @hopr_node_safe_registry_address.setter
    def hopr_node_safe_registry_address(self, hopr_node_safe_registry_address):
        """Sets the hopr_node_safe_registry_address of this InlineResponse2002.

        Contract address of the contract that register node and safe pairs  # noqa: E501

        :param hopr_node_safe_registry_address: The hopr_node_safe_registry_address of this InlineResponse2002.  # noqa: E501
        :type: str
        """

        self._hopr_node_safe_registry_address = hopr_node_safe_registry_address

    @property
    def node_management_module(self):
        """Gets the node_management_module of this InlineResponse2002.  # noqa: E501

        Contract address of the Safe module for managing the current hopr node  # noqa: E501

        :return: The node_management_module of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._node_management_module

    @node_management_module.setter
    def node_management_module(self, node_management_module):
        """Sets the node_management_module of this InlineResponse2002.

        Contract address of the Safe module for managing the current hopr node  # noqa: E501

        :param node_management_module: The node_management_module of this InlineResponse2002.  # noqa: E501
        :type: str
        """

        self._node_management_module = node_management_module

    @property
    def node_safe(self):
        """Gets the node_safe of this InlineResponse2002.  # noqa: E501

        Contract address of the safe that holds asset for the current node  # noqa: E501

        :return: The node_safe of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._node_safe

    @node_safe.setter
    def node_safe(self, node_safe):
        """Sets the node_safe of this InlineResponse2002.

        Contract address of the safe that holds asset for the current node  # noqa: E501

        :param node_safe: The node_safe of this InlineResponse2002.  # noqa: E501
        :type: str
        """

        self._node_safe = node_safe

    @property
    def connectivity_status(self):
        """Gets the connectivity_status of this InlineResponse2002.  # noqa: E501

        Indicates how good is the connectivity of this node to the HOPR network: either RED, ORANGE, YELLOW or GREEN  # noqa: E501

        :return: The connectivity_status of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._connectivity_status

    @connectivity_status.setter
    def connectivity_status(self, connectivity_status):
        """Sets the connectivity_status of this InlineResponse2002.

        Indicates how good is the connectivity of this node to the HOPR network: either RED, ORANGE, YELLOW or GREEN  # noqa: E501

        :param connectivity_status: The connectivity_status of this InlineResponse2002.  # noqa: E501
        :type: str
        """

        self._connectivity_status = connectivity_status

    @property
    def is_eligible(self):
        """Gets the is_eligible of this InlineResponse2002.  # noqa: E501

        Determines whether the staking account associated with this node is eligible for accessing the HOPR network. Always true if network registry is disabled.  # noqa: E501

        :return: The is_eligible of this InlineResponse2002.  # noqa: E501
        :rtype: bool
        """
        return self._is_eligible

    @is_eligible.setter
    def is_eligible(self, is_eligible):
        """Sets the is_eligible of this InlineResponse2002.

        Determines whether the staking account associated with this node is eligible for accessing the HOPR network. Always true if network registry is disabled.  # noqa: E501

        :param is_eligible: The is_eligible of this InlineResponse2002.  # noqa: E501
        :type: bool
        """

        self._is_eligible = is_eligible

    @property
    def channel_closure_period(self):
        """Gets the channel_closure_period of this InlineResponse2002.  # noqa: E501

        Time (in minutes) that this node needs in order to clean up before closing the channel. When requesting to close the channel each node needs some time to make sure that channel can be closed securely and cleanly. After this channelClosurePeriod passes the second request for closing channel will close the channel.  # noqa: E501

        :return: The channel_closure_period of this InlineResponse2002.  # noqa: E501
        :rtype: float
        """
        return self._channel_closure_period

    @channel_closure_period.setter
    def channel_closure_period(self, channel_closure_period):
        """Sets the channel_closure_period of this InlineResponse2002.

        Time (in minutes) that this node needs in order to clean up before closing the channel. When requesting to close the channel each node needs some time to make sure that channel can be closed securely and cleanly. After this channelClosurePeriod passes the second request for closing channel will close the channel.  # noqa: E501

        :param channel_closure_period: The channel_closure_period of this InlineResponse2002.  # noqa: E501
        :type: float
        """

        self._channel_closure_period = channel_closure_period

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
        if issubclass(InlineResponse2002, dict):
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
        if not isinstance(other, InlineResponse2002):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other