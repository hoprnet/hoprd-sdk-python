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

class InlineResponse2001Connected(object):
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
        'peer_id': 'HoprAddress',
        'multi_addr': 'MultiAddress',
        'heartbeats': 'InlineResponse2001Heartbeats',
        'last_seen': 'float',
        'quality': 'float',
        'backoff': 'float',
        'is_new': 'bool',
        'reported_version': 'str'
    }

    attribute_map = {
        'peer_id': 'peerId',
        'multi_addr': 'multiAddr',
        'heartbeats': 'heartbeats',
        'last_seen': 'lastSeen',
        'quality': 'quality',
        'backoff': 'backoff',
        'is_new': 'isNew',
        'reported_version': 'reportedVersion'
    }

    def __init__(self, peer_id=None, multi_addr=None, heartbeats=None, last_seen=None, quality=None, backoff=None, is_new=None, reported_version=None):  # noqa: E501
        """InlineResponse2001Connected - a model defined in Swagger"""  # noqa: E501
        self._peer_id = None
        self._multi_addr = None
        self._heartbeats = None
        self._last_seen = None
        self._quality = None
        self._backoff = None
        self._is_new = None
        self._reported_version = None
        self.discriminator = None
        if peer_id is not None:
            self.peer_id = peer_id
        if multi_addr is not None:
            self.multi_addr = multi_addr
        if heartbeats is not None:
            self.heartbeats = heartbeats
        if last_seen is not None:
            self.last_seen = last_seen
        if quality is not None:
            self.quality = quality
        if backoff is not None:
            self.backoff = backoff
        if is_new is not None:
            self.is_new = is_new
        if reported_version is not None:
            self.reported_version = reported_version

    @property
    def peer_id(self):
        """Gets the peer_id of this InlineResponse2001Connected.  # noqa: E501


        :return: The peer_id of this InlineResponse2001Connected.  # noqa: E501
        :rtype: HoprAddress
        """
        return self._peer_id

    @peer_id.setter
    def peer_id(self, peer_id):
        """Sets the peer_id of this InlineResponse2001Connected.


        :param peer_id: The peer_id of this InlineResponse2001Connected.  # noqa: E501
        :type: HoprAddress
        """

        self._peer_id = peer_id

    @property
    def multi_addr(self):
        """Gets the multi_addr of this InlineResponse2001Connected.  # noqa: E501


        :return: The multi_addr of this InlineResponse2001Connected.  # noqa: E501
        :rtype: MultiAddress
        """
        return self._multi_addr

    @multi_addr.setter
    def multi_addr(self, multi_addr):
        """Sets the multi_addr of this InlineResponse2001Connected.


        :param multi_addr: The multi_addr of this InlineResponse2001Connected.  # noqa: E501
        :type: MultiAddress
        """

        self._multi_addr = multi_addr

    @property
    def heartbeats(self):
        """Gets the heartbeats of this InlineResponse2001Connected.  # noqa: E501


        :return: The heartbeats of this InlineResponse2001Connected.  # noqa: E501
        :rtype: InlineResponse2001Heartbeats
        """
        return self._heartbeats

    @heartbeats.setter
    def heartbeats(self, heartbeats):
        """Sets the heartbeats of this InlineResponse2001Connected.


        :param heartbeats: The heartbeats of this InlineResponse2001Connected.  # noqa: E501
        :type: InlineResponse2001Heartbeats
        """

        self._heartbeats = heartbeats

    @property
    def last_seen(self):
        """Gets the last_seen of this InlineResponse2001Connected.  # noqa: E501

        Timestamp on when the node was last seen (in milliseconds)  # noqa: E501

        :return: The last_seen of this InlineResponse2001Connected.  # noqa: E501
        :rtype: float
        """
        return self._last_seen

    @last_seen.setter
    def last_seen(self, last_seen):
        """Sets the last_seen of this InlineResponse2001Connected.

        Timestamp on when the node was last seen (in milliseconds)  # noqa: E501

        :param last_seen: The last_seen of this InlineResponse2001Connected.  # noqa: E501
        :type: float
        """

        self._last_seen = last_seen

    @property
    def quality(self):
        """Gets the quality of this InlineResponse2001Connected.  # noqa: E501

        A float between 0 (completely unreliable) and 1 (completely reliable) estimating the quality of service of a peer's network connection  # noqa: E501

        :return: The quality of this InlineResponse2001Connected.  # noqa: E501
        :rtype: float
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        """Sets the quality of this InlineResponse2001Connected.

        A float between 0 (completely unreliable) and 1 (completely reliable) estimating the quality of service of a peer's network connection  # noqa: E501

        :param quality: The quality of this InlineResponse2001Connected.  # noqa: E501
        :type: float
        """

        self._quality = quality

    @property
    def backoff(self):
        """Gets the backoff of this InlineResponse2001Connected.  # noqa: E501


        :return: The backoff of this InlineResponse2001Connected.  # noqa: E501
        :rtype: float
        """
        return self._backoff

    @backoff.setter
    def backoff(self, backoff):
        """Sets the backoff of this InlineResponse2001Connected.


        :param backoff: The backoff of this InlineResponse2001Connected.  # noqa: E501
        :type: float
        """

        self._backoff = backoff

    @property
    def is_new(self):
        """Gets the is_new of this InlineResponse2001Connected.  # noqa: E501

        True if the node is new (no heartbeats sent yet).  # noqa: E501

        :return: The is_new of this InlineResponse2001Connected.  # noqa: E501
        :rtype: bool
        """
        return self._is_new

    @is_new.setter
    def is_new(self, is_new):
        """Sets the is_new of this InlineResponse2001Connected.

        True if the node is new (no heartbeats sent yet).  # noqa: E501

        :param is_new: The is_new of this InlineResponse2001Connected.  # noqa: E501
        :type: bool
        """

        self._is_new = is_new

    @property
    def reported_version(self):
        """Gets the reported_version of this InlineResponse2001Connected.  # noqa: E501

        HOPR protocol version as determined from the successful ping in the Major.Minor.Patch format or \"unknown\"  # noqa: E501

        :return: The reported_version of this InlineResponse2001Connected.  # noqa: E501
        :rtype: str
        """
        return self._reported_version

    @reported_version.setter
    def reported_version(self, reported_version):
        """Sets the reported_version of this InlineResponse2001Connected.

        HOPR protocol version as determined from the successful ping in the Major.Minor.Patch format or \"unknown\"  # noqa: E501

        :param reported_version: The reported_version of this InlineResponse2001Connected.  # noqa: E501
        :type: str
        """

        self._reported_version = reported_version

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
        if issubclass(InlineResponse2001Connected, dict):
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
        if not isinstance(other, InlineResponse2001Connected):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other