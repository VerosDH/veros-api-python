# coding: utf-8

"""
    Veros API

    Routes of Veros project  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import veros_api
from veros_api.api.marketcards_public_api import MarketcardsPublicApi  # noqa: E501
from veros_api.rest import ApiException


class TestMarketcardsPublicApi(unittest.TestCase):
    """MarketcardsPublicApi unit test stubs"""

    def setUp(self):
        self.api = veros_api.api.marketcards_public_api.MarketcardsPublicApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_marketcards_public_go(self):
        """Test case for marketcards_public_go

        """
        pass

    def test_marketcards_public_list(self):
        """Test case for marketcards_public_list

        """
        pass

    def test_marketcards_public_read(self):
        """Test case for marketcards_public_read

        """
        pass


if __name__ == '__main__':
    unittest.main()