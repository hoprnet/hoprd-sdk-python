# coding: utf-8

"""
    hoprd-api

    This Rest API enables developers to interact with a hoprd node programatically through HTTP.  # noqa: E501

    OpenAPI spec version: 3.1.0
    Contact: tech@hoprnet.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import hoprd_sdk
from hoprd_sdk.api.account_api import AccountApi  # noqa: E501
from hoprd_sdk.rest import ApiException


class TestAccountApi(unittest.TestCase):
    """AccountApi unit test stubs"""

    def setUp(self):
        self.api = AccountApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_addresses(self):
        """Test case for addresses

        Get node's HOPR and native addresses.  # noqa: E501
        """
        pass

    def test_balances(self):
        """Test case for balances

        Get node's and associated Safe's HOPR and native balances as the allowance for HOPR  # noqa: E501
        """
        pass

    def test_withdraw(self):
        """Test case for withdraw

        Withdraw funds from this node to the ethereum wallet address.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
