# coding: utf-8

"""
    HOPRd Rest API v3

    This Rest API enables developers to interact with a hoprd node programatically.  # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: tech@hoprnet.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import hoprd_sdk
from hoprd_sdk.api.peer_info_api import PeerInfoApi  # noqa: E501
from hoprd_sdk.rest import ApiException


class TestPeerInfoApi(unittest.TestCase):
    """PeerInfoApi unit test stubs"""

    def setUp(self):
        self.api = PeerInfoApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_peer_info_get_peer_info(self):
        """Test case for peer_info_get_peer_info

        """
        pass


if __name__ == '__main__':
    unittest.main()
