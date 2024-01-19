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

class NodeInfoRes(object):
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
        'announced_address': 'list[str]',
        'chain': 'str',
        'channel_closure_period': 'int',
        'connectivity_status': 'str',
        'hopr_channels': 'str',
        'hopr_management_module': 'str',
        'hopr_network_registry': 'str',
        'hopr_node_safe': 'str',
        'hopr_node_sage_registry': 'str',
        'hopr_token': 'str',
        'is_eligible': 'bool',
        'listening_address': 'list[str]',
        'network': 'str'
    }

    attribute_map = {
        'announced_address': 'announcedAddress',
        'chain': 'chain',
        'channel_closure_period': 'channelClosurePeriod',
        'connectivity_status': 'connectivityStatus',
        'hopr_channels': 'hoprChannels',
        'hopr_management_module': 'hoprManagementModule',
        'hopr_network_registry': 'hoprNetworkRegistry',
        'hopr_node_safe': 'hoprNodeSafe',
        'hopr_node_sage_registry': 'hoprNodeSageRegistry',
        'hopr_token': 'hoprToken',
        'is_eligible': 'isEligible',
        'listening_address': 'listeningAddress',
        'network': 'network'
    }

    def __init__(self, announced_address=None, chain=None, channel_closure_period=None, connectivity_status=None, hopr_channels=None, hopr_management_module=None, hopr_network_registry=None, hopr_node_safe=None, hopr_node_sage_registry=None, hopr_token=None, is_eligible=None, listening_address=None, network=None):  # noqa: E501
        """NodeInfoRes - a model defined in Swagger"""  # noqa: E501
        self._announced_address = None
        self._chain = None
        self._channel_closure_period = None
        self._connectivity_status = None
        self._hopr_channels = None
        self._hopr_management_module = None
        self._hopr_network_registry = None
        self._hopr_node_safe = None
        self._hopr_node_sage_registry = None
        self._hopr_token = None
        self._is_eligible = None
        self._listening_address = None
        self._network = None
        self.discriminator = None
        self.announced_address = announced_address
        self.chain = chain
        self.channel_closure_period = channel_closure_period
        self.connectivity_status = connectivity_status
        self.hopr_channels = hopr_channels
        self.hopr_management_module = hopr_management_module
        self.hopr_network_registry = hopr_network_registry
        self.hopr_node_safe = hopr_node_safe
        self.hopr_node_sage_registry = hopr_node_sage_registry
        self.hopr_token = hopr_token
        self.is_eligible = is_eligible
        self.listening_address = listening_address
        self.network = network

    @property
    def announced_address(self):
        """Gets the announced_address of this NodeInfoRes.  # noqa: E501


        :return: The announced_address of this NodeInfoRes.  # noqa: E501
        :rtype: list[str]
        """
        return self._announced_address

    @announced_address.setter
    def announced_address(self, announced_address):
        """Sets the announced_address of this NodeInfoRes.


        :param announced_address: The announced_address of this NodeInfoRes.  # noqa: E501
        :type: list[str]
        """
        if announced_address is None:
            raise ValueError("Invalid value for `announced_address`, must not be `None`")  # noqa: E501

        self._announced_address = announced_address

    @property
    def chain(self):
        """Gets the chain of this NodeInfoRes.  # noqa: E501


        :return: The chain of this NodeInfoRes.  # noqa: E501
        :rtype: str
        """
        return self._chain

    @chain.setter
    def chain(self, chain):
        """Sets the chain of this NodeInfoRes.


        :param chain: The chain of this NodeInfoRes.  # noqa: E501
        :type: str
        """
        if chain is None:
            raise ValueError("Invalid value for `chain`, must not be `None`")  # noqa: E501

        self._chain = chain

    @property
    def channel_closure_period(self):
        """Gets the channel_closure_period of this NodeInfoRes.  # noqa: E501

        Channel closure period in seconds  # noqa: E501

        :return: The channel_closure_period of this NodeInfoRes.  # noqa: E501
        :rtype: int
        """
        return self._channel_closure_period

    @channel_closure_period.setter
    def channel_closure_period(self, channel_closure_period):
        """Sets the channel_closure_period of this NodeInfoRes.

        Channel closure period in seconds  # noqa: E501

        :param channel_closure_period: The channel_closure_period of this NodeInfoRes.  # noqa: E501
        :type: int
        """
        if channel_closure_period is None:
            raise ValueError("Invalid value for `channel_closure_period`, must not be `None`")  # noqa: E501

        self._channel_closure_period = channel_closure_period

    @property
    def connectivity_status(self):
        """Gets the connectivity_status of this NodeInfoRes.  # noqa: E501


        :return: The connectivity_status of this NodeInfoRes.  # noqa: E501
        :rtype: str
        """
        return self._connectivity_status

    @connectivity_status.setter
    def connectivity_status(self, connectivity_status):
        """Sets the connectivity_status of this NodeInfoRes.


        :param connectivity_status: The connectivity_status of this NodeInfoRes.  # noqa: E501
        :type: str
        """
        if connectivity_status is None:
            raise ValueError("Invalid value for `connectivity_status`, must not be `None`")  # noqa: E501

        self._connectivity_status = connectivity_status

    @property
    def hopr_channels(self):
        """Gets the hopr_channels of this NodeInfoRes.  # noqa: E501


        :return: The hopr_channels of this NodeInfoRes.  # noqa: E501
        :rtype: str
        """
        return self._hopr_channels

    @hopr_channels.setter
    def hopr_channels(self, hopr_channels):
        """Sets the hopr_channels of this NodeInfoRes.


        :param hopr_channels: The hopr_channels of this NodeInfoRes.  # noqa: E501
        :type: str
        """
        if hopr_channels is None:
            raise ValueError("Invalid value for `hopr_channels`, must not be `None`")  # noqa: E501

        self._hopr_channels = hopr_channels

    @property
    def hopr_management_module(self):
        """Gets the hopr_management_module of this NodeInfoRes.  # noqa: E501


        :return: The hopr_management_module of this NodeInfoRes.  # noqa: E501
        :rtype: str
        """
        return self._hopr_management_module

    @hopr_management_module.setter
    def hopr_management_module(self, hopr_management_module):
        """Sets the hopr_management_module of this NodeInfoRes.


        :param hopr_management_module: The hopr_management_module of this NodeInfoRes.  # noqa: E501
        :type: str
        """
        if hopr_management_module is None:
            raise ValueError("Invalid value for `hopr_management_module`, must not be `None`")  # noqa: E501

        self._hopr_management_module = hopr_management_module

    @property
    def hopr_network_registry(self):
        """Gets the hopr_network_registry of this NodeInfoRes.  # noqa: E501


        :return: The hopr_network_registry of this NodeInfoRes.  # noqa: E501
        :rtype: str
        """
        return self._hopr_network_registry

    @hopr_network_registry.setter
    def hopr_network_registry(self, hopr_network_registry):
        """Sets the hopr_network_registry of this NodeInfoRes.


        :param hopr_network_registry: The hopr_network_registry of this NodeInfoRes.  # noqa: E501
        :type: str
        """
        if hopr_network_registry is None:
            raise ValueError("Invalid value for `hopr_network_registry`, must not be `None`")  # noqa: E501

        self._hopr_network_registry = hopr_network_registry

    @property
    def hopr_node_safe(self):
        """Gets the hopr_node_safe of this NodeInfoRes.  # noqa: E501


        :return: The hopr_node_safe of this NodeInfoRes.  # noqa: E501
        :rtype: str
        """
        return self._hopr_node_safe

    @hopr_node_safe.setter
    def hopr_node_safe(self, hopr_node_safe):
        """Sets the hopr_node_safe of this NodeInfoRes.


        :param hopr_node_safe: The hopr_node_safe of this NodeInfoRes.  # noqa: E501
        :type: str
        """
        if hopr_node_safe is None:
            raise ValueError("Invalid value for `hopr_node_safe`, must not be `None`")  # noqa: E501

        self._hopr_node_safe = hopr_node_safe

    @property
    def hopr_node_sage_registry(self):
        """Gets the hopr_node_sage_registry of this NodeInfoRes.  # noqa: E501


        :return: The hopr_node_sage_registry of this NodeInfoRes.  # noqa: E501
        :rtype: str
        """
        return self._hopr_node_sage_registry

    @hopr_node_sage_registry.setter
    def hopr_node_sage_registry(self, hopr_node_sage_registry):
        """Sets the hopr_node_sage_registry of this NodeInfoRes.


        :param hopr_node_sage_registry: The hopr_node_sage_registry of this NodeInfoRes.  # noqa: E501
        :type: str
        """
        if hopr_node_sage_registry is None:
            raise ValueError("Invalid value for `hopr_node_sage_registry`, must not be `None`")  # noqa: E501

        self._hopr_node_sage_registry = hopr_node_sage_registry

    @property
    def hopr_token(self):
        """Gets the hopr_token of this NodeInfoRes.  # noqa: E501


        :return: The hopr_token of this NodeInfoRes.  # noqa: E501
        :rtype: str
        """
        return self._hopr_token

    @hopr_token.setter
    def hopr_token(self, hopr_token):
        """Sets the hopr_token of this NodeInfoRes.


        :param hopr_token: The hopr_token of this NodeInfoRes.  # noqa: E501
        :type: str
        """
        if hopr_token is None:
            raise ValueError("Invalid value for `hopr_token`, must not be `None`")  # noqa: E501

        self._hopr_token = hopr_token

    @property
    def is_eligible(self):
        """Gets the is_eligible of this NodeInfoRes.  # noqa: E501


        :return: The is_eligible of this NodeInfoRes.  # noqa: E501
        :rtype: bool
        """
        return self._is_eligible

    @is_eligible.setter
    def is_eligible(self, is_eligible):
        """Sets the is_eligible of this NodeInfoRes.


        :param is_eligible: The is_eligible of this NodeInfoRes.  # noqa: E501
        :type: bool
        """
        if is_eligible is None:
            raise ValueError("Invalid value for `is_eligible`, must not be `None`")  # noqa: E501

        self._is_eligible = is_eligible

    @property
    def listening_address(self):
        """Gets the listening_address of this NodeInfoRes.  # noqa: E501


        :return: The listening_address of this NodeInfoRes.  # noqa: E501
        :rtype: list[str]
        """
        return self._listening_address

    @listening_address.setter
    def listening_address(self, listening_address):
        """Sets the listening_address of this NodeInfoRes.


        :param listening_address: The listening_address of this NodeInfoRes.  # noqa: E501
        :type: list[str]
        """
        if listening_address is None:
            raise ValueError("Invalid value for `listening_address`, must not be `None`")  # noqa: E501

        self._listening_address = listening_address

    @property
    def network(self):
        """Gets the network of this NodeInfoRes.  # noqa: E501


        :return: The network of this NodeInfoRes.  # noqa: E501
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this NodeInfoRes.


        :param network: The network of this NodeInfoRes.  # noqa: E501
        :type: str
        """
        if network is None:
            raise ValueError("Invalid value for `network`, must not be `None`")  # noqa: E501

        self._network = network

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
        if issubclass(NodeInfoRes, dict):
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
        if not isinstance(other, NodeInfoRes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
