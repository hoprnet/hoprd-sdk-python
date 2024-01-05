# coding: utf-8

"""
    hoprd-api

    API server using the hopr-lib created HOPR node and exposing it using a HTTP REST API  # noqa: E501

    OpenAPI spec version: 0.1.0
    Contact: tech@hoprnet.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import hoprd_sdk
from hoprd_sdk.api.messages_api import MessagesApi  # noqa: E501
from hoprd_sdk.rest import ApiException


class TestMessagesApi(unittest.TestCase):
    """MessagesApi unit test stubs"""

    def setUp(self):
        self.api = MessagesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_messages(self):
        """Test case for delete_messages

        Delete messages from nodes message inbox.  # noqa: E501
        """
        pass

    def test_peek(self):
        """Test case for peek

        Peek the oldest message currently present in the nodes message inbox.  # noqa: E501
        """
        pass

    def test_peek_all(self):
        """Test case for peek_all

        Peek the list of messages currently present in the nodes message inbox.  # noqa: E501
        """
        pass

    def test_pop(self):
        """Test case for pop

        Get the oldest message currently present in the nodes message inbox.  # noqa: E501
        """
        pass

    def test_pop_all(self):
        """Test case for pop_all

        Get the list of messages currently present in the nodes message inbox.  # noqa: E501
        """
        pass

    def test_send_message(self):
        """Test case for send_message

        Send a message to another peer using a given path.  # noqa: E501
        """
        pass

    def test_size(self):
        """Test case for size

        Get size of filtered message inbox for a specific tag  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
