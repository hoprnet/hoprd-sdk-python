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

class NodeTicketStatisticsResponse(object):
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
        'neglected_value': 'str',
        'redeemed_value': 'str',
        'rejected_value': 'str',
        'unredeemed_value': 'str',
        'winning_count': 'int'
    }

    attribute_map = {
        'neglected_value': 'neglectedValue',
        'redeemed_value': 'redeemedValue',
        'rejected_value': 'rejectedValue',
        'unredeemed_value': 'unredeemedValue',
        'winning_count': 'winningCount'
    }

    def __init__(self, neglected_value=None, redeemed_value=None, rejected_value=None, unredeemed_value=None, winning_count=None):  # noqa: E501
        """NodeTicketStatisticsResponse - a model defined in Swagger"""  # noqa: E501
        self._neglected_value = None
        self._redeemed_value = None
        self._rejected_value = None
        self._unredeemed_value = None
        self._winning_count = None
        self.discriminator = None
        self.neglected_value = neglected_value
        self.redeemed_value = redeemed_value
        self.rejected_value = rejected_value
        self.unredeemed_value = unredeemed_value
        self.winning_count = winning_count

    @property
    def neglected_value(self):
        """Gets the neglected_value of this NodeTicketStatisticsResponse.  # noqa: E501


        :return: The neglected_value of this NodeTicketStatisticsResponse.  # noqa: E501
        :rtype: str
        """
        return self._neglected_value

    @neglected_value.setter
    def neglected_value(self, neglected_value):
        """Sets the neglected_value of this NodeTicketStatisticsResponse.


        :param neglected_value: The neglected_value of this NodeTicketStatisticsResponse.  # noqa: E501
        :type: str
        """
        if neglected_value is None:
            raise ValueError("Invalid value for `neglected_value`, must not be `None`")  # noqa: E501

        self._neglected_value = neglected_value

    @property
    def redeemed_value(self):
        """Gets the redeemed_value of this NodeTicketStatisticsResponse.  # noqa: E501


        :return: The redeemed_value of this NodeTicketStatisticsResponse.  # noqa: E501
        :rtype: str
        """
        return self._redeemed_value

    @redeemed_value.setter
    def redeemed_value(self, redeemed_value):
        """Sets the redeemed_value of this NodeTicketStatisticsResponse.


        :param redeemed_value: The redeemed_value of this NodeTicketStatisticsResponse.  # noqa: E501
        :type: str
        """
        if redeemed_value is None:
            raise ValueError("Invalid value for `redeemed_value`, must not be `None`")  # noqa: E501

        self._redeemed_value = redeemed_value

    @property
    def rejected_value(self):
        """Gets the rejected_value of this NodeTicketStatisticsResponse.  # noqa: E501


        :return: The rejected_value of this NodeTicketStatisticsResponse.  # noqa: E501
        :rtype: str
        """
        return self._rejected_value

    @rejected_value.setter
    def rejected_value(self, rejected_value):
        """Sets the rejected_value of this NodeTicketStatisticsResponse.


        :param rejected_value: The rejected_value of this NodeTicketStatisticsResponse.  # noqa: E501
        :type: str
        """
        if rejected_value is None:
            raise ValueError("Invalid value for `rejected_value`, must not be `None`")  # noqa: E501

        self._rejected_value = rejected_value

    @property
    def unredeemed_value(self):
        """Gets the unredeemed_value of this NodeTicketStatisticsResponse.  # noqa: E501


        :return: The unredeemed_value of this NodeTicketStatisticsResponse.  # noqa: E501
        :rtype: str
        """
        return self._unredeemed_value

    @unredeemed_value.setter
    def unredeemed_value(self, unredeemed_value):
        """Sets the unredeemed_value of this NodeTicketStatisticsResponse.


        :param unredeemed_value: The unredeemed_value of this NodeTicketStatisticsResponse.  # noqa: E501
        :type: str
        """
        if unredeemed_value is None:
            raise ValueError("Invalid value for `unredeemed_value`, must not be `None`")  # noqa: E501

        self._unredeemed_value = unredeemed_value

    @property
    def winning_count(self):
        """Gets the winning_count of this NodeTicketStatisticsResponse.  # noqa: E501


        :return: The winning_count of this NodeTicketStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._winning_count

    @winning_count.setter
    def winning_count(self, winning_count):
        """Sets the winning_count of this NodeTicketStatisticsResponse.


        :param winning_count: The winning_count of this NodeTicketStatisticsResponse.  # noqa: E501
        :type: int
        """
        if winning_count is None:
            raise ValueError("Invalid value for `winning_count`, must not be `None`")  # noqa: E501

        self._winning_count = winning_count

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
        if issubclass(NodeTicketStatisticsResponse, dict):
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
        if not isinstance(other, NodeTicketStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
