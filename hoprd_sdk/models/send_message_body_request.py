# coding: utf-8

"""
    hoprd-api

    This Rest API enables developers to interact with a hoprd node programatically through HTTP.  # noqa: E501

    OpenAPI spec version: 3.10.0
    Contact: tech@hoprnet.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SendMessageBodyRequest(object):
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
        'destination': 'str',
        'hops': 'int',
        'path': 'list[str]',
        'peer_id': 'str',
        'tag': 'int'
    }

    attribute_map = {
        'body': 'body',
        'destination': 'destination',
        'hops': 'hops',
        'path': 'path',
        'peer_id': 'peerId',
        'tag': 'tag'
    }

    def __init__(self, body=None, destination=None, hops=None, path=None, peer_id=None, tag=None):  # noqa: E501
        """SendMessageBodyRequest - a model defined in Swagger"""  # noqa: E501
        self._body = None
        self._destination = None
        self._hops = None
        self._path = None
        self._peer_id = None
        self._tag = None
        self.discriminator = None
        self.body = body
        if destination is not None:
            self.destination = destination
        if hops is not None:
            self.hops = hops
        if path is not None:
            self.path = path
        if peer_id is not None:
            self.peer_id = peer_id
        self.tag = tag

    @property
    def body(self):
        """Gets the body of this SendMessageBodyRequest.  # noqa: E501

        Message to be transmitted over the network  # noqa: E501

        :return: The body of this SendMessageBodyRequest.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this SendMessageBodyRequest.

        Message to be transmitted over the network  # noqa: E501

        :param body: The body of this SendMessageBodyRequest.  # noqa: E501
        :type: str
        """
        if body is None:
            raise ValueError("Invalid value for `body`, must not be `None`")  # noqa: E501

        self._body = body

    @property
    def destination(self):
        """Gets the destination of this SendMessageBodyRequest.  # noqa: E501

        The recipient HOPR PeerId or address  # noqa: E501

        :return: The destination of this SendMessageBodyRequest.  # noqa: E501
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this SendMessageBodyRequest.

        The recipient HOPR PeerId or address  # noqa: E501

        :param destination: The destination of this SendMessageBodyRequest.  # noqa: E501
        :type: str
        """

        self._destination = destination

    @property
    def hops(self):
        """Gets the hops of this SendMessageBodyRequest.  # noqa: E501


        :return: The hops of this SendMessageBodyRequest.  # noqa: E501
        :rtype: int
        """
        return self._hops

    @hops.setter
    def hops(self, hops):
        """Sets the hops of this SendMessageBodyRequest.


        :param hops: The hops of this SendMessageBodyRequest.  # noqa: E501
        :type: int
        """

        self._hops = hops

    @property
    def path(self):
        """Gets the path of this SendMessageBodyRequest.  # noqa: E501


        :return: The path of this SendMessageBodyRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this SendMessageBodyRequest.


        :param path: The path of this SendMessageBodyRequest.  # noqa: E501
        :type: list[str]
        """

        self._path = path

    @property
    def peer_id(self):
        """Gets the peer_id of this SendMessageBodyRequest.  # noqa: E501

        Deprecated: PeerId of the target node  # noqa: E501

        :return: The peer_id of this SendMessageBodyRequest.  # noqa: E501
        :rtype: str
        """
        return self._peer_id

    @peer_id.setter
    def peer_id(self, peer_id):
        """Sets the peer_id of this SendMessageBodyRequest.

        Deprecated: PeerId of the target node  # noqa: E501

        :param peer_id: The peer_id of this SendMessageBodyRequest.  # noqa: E501
        :type: str
        """

        self._peer_id = peer_id

    @property
    def tag(self):
        """Gets the tag of this SendMessageBodyRequest.  # noqa: E501

        The message tag used to filter messages based on application, must be from range <1024,65535>  # noqa: E501

        :return: The tag of this SendMessageBodyRequest.  # noqa: E501
        :rtype: int
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this SendMessageBodyRequest.

        The message tag used to filter messages based on application, must be from range <1024,65535>  # noqa: E501

        :param tag: The tag of this SendMessageBodyRequest.  # noqa: E501
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
        if issubclass(SendMessageBodyRequest, dict):
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
        if not isinstance(other, SendMessageBodyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
