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
from api.api.feedback_themes_api import FeedbackThemesApi  # noqa: E501
from api.rest import ApiException


class TestFeedbackThemesApi(unittest.TestCase):
    """FeedbackThemesApi unit test stubs"""

    def setUp(self):
        self.api = api.api.feedback_themes_api.FeedbackThemesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_feedback_themes_list(self):
        """Test case for feedback_themes_list

        """
        pass


if __name__ == '__main__':
    unittest.main()
