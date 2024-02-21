# coding: utf-8

"""
    hoprd-api

    API server using the hopr-lib created HOPR node and exposing it using a HTTP REST API  # noqa: E501

    OpenAPI spec version: 0.2.1
    Contact: tech@hoprnet.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PingResponse(object):
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
        'latency': 'int',
        'reported_version': 'str'
    }

    attribute_map = {
        'latency': 'latency',
        'reported_version': 'reportedVersion'
    }

    def __init__(self, latency=None, reported_version=None):  # noqa: E501
        """PingResponse - a model defined in Swagger"""  # noqa: E501
        self._latency = None
        self._reported_version = None
        self.discriminator = None
        self.latency = latency
        self.reported_version = reported_version

    @property
    def latency(self):
        """Gets the latency of this PingResponse.  # noqa: E501


        :return: The latency of this PingResponse.  # noqa: E501
        :rtype: int
        """
        return self._latency

    @latency.setter
    def latency(self, latency):
        """Sets the latency of this PingResponse.


        :param latency: The latency of this PingResponse.  # noqa: E501
        :type: int
        """
        if latency is None:
            raise ValueError("Invalid value for `latency`, must not be `None`")  # noqa: E501

        self._latency = latency

    @property
    def reported_version(self):
        """Gets the reported_version of this PingResponse.  # noqa: E501


        :return: The reported_version of this PingResponse.  # noqa: E501
        :rtype: str
        """
        return self._reported_version

    @reported_version.setter
    def reported_version(self, reported_version):
        """Sets the reported_version of this PingResponse.


        :param reported_version: The reported_version of this PingResponse.  # noqa: E501
        :type: str
        """
        if reported_version is None:
            raise ValueError("Invalid value for `reported_version`, must not be `None`")  # noqa: E501

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
        if issubclass(PingResponse, dict):
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
        if not isinstance(other, PingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
