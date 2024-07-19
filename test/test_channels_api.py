# coding: utf-8

"""
    hoprd-api

    This Rest API enables developers to interact with a hoprd node programatically through HTTP.  # noqa: E501

    OpenAPI spec version: 3.2.0
    Contact: tech@hoprnet.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import hoprd_sdk
from hoprd_sdk.api.channels_api import ChannelsApi  # noqa: E501
from hoprd_sdk.rest import ApiException


class TestChannelsApi(unittest.TestCase):
    """ChannelsApi unit test stubs"""

    def setUp(self):
        self.api = ChannelsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_aggregate_tickets_in_channel(self):
        """Test case for aggregate_tickets_in_channel

        Starts aggregation of tickets in the given channel.  # noqa: E501
        """
        pass

    def test_close_channel(self):
        """Test case for close_channel

        Closes the given channel.  # noqa: E501
        """
        pass

    def test_fund_channel(self):
        """Test case for fund_channel

        Funds the given channel with the given amount of HOPR tokens.  # noqa: E501
        """
        pass

    def test_list_channels(self):
        """Test case for list_channels

        Lists channels opened to/from this node. Alternatively, it can print all  # noqa: E501
        """
        pass

    def test_open_channel(self):
        """Test case for open_channel

        Opens a channel to the given on-chain address with the given initial stake of HOPR tokens.  # noqa: E501
        """
        pass

    def test_redeem_tickets_in_channel(self):
        """Test case for redeem_tickets_in_channel

        Starts redeeming all tickets in the given channel.  # noqa: E501
        """
        pass

    def test_show_channel(self):
        """Test case for show_channel

        Returns information about the given channel.  # noqa: E501
        """
        pass

    def test_show_channel_tickets(self):
        """Test case for show_channel_tickets

        Lists all tickets for the given channel  ID.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
