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
from hoprd_sdk.api.settings_api import SettingsApi  # noqa: E501
from hoprd_sdk.rest import ApiException


class TestSettingsApi(unittest.TestCase):
    """SettingsApi unit test stubs"""

    def setUp(self):
        self.api = SettingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_settings_get_settings(self):
        """Test case for settings_get_settings

        """
        pass

    def test_settings_set_setting(self):
        """Test case for settings_set_setting

        """
        pass


if __name__ == '__main__':
    unittest.main()
