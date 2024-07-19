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
from hoprd_sdk.api.checks_api import ChecksApi  # noqa: E501
from hoprd_sdk.rest import ApiException


class TestChecksApi(unittest.TestCase):
    """ChecksApi unit test stubs"""

    def setUp(self):
        self.api = ChecksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_healthyz(self):
        """Test case for healthyz

        Check whether the node is healthy.  # noqa: E501
        """
        pass

    def test_readyz(self):
        """Test case for readyz

        Check whether the node is ready to accept connections.  # noqa: E501
        """
        pass

    def test_startedz(self):
        """Test case for startedz

        Check whether the node is started.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
