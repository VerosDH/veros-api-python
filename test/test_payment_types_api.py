# coding: utf-8

"""
    Veros API

    Routes of Veros project  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import api
from api.api.payment_types_api import PaymentTypesApi  # noqa: E501
from api.rest import ApiException


class TestPaymentTypesApi(unittest.TestCase):
    """PaymentTypesApi unit test stubs"""

    def setUp(self):
        self.api = api.api.payment_types_api.PaymentTypesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_payment_types_list(self):
        """Test case for payment_types_list

        """
        pass

    def test_payment_types_read(self):
        """Test case for payment_types_read

        """
        pass


if __name__ == '__main__':
    unittest.main()
