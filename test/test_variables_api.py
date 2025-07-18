# coding: utf-8

"""
    Mednet EDC API

    The Mednet EDC (Electronic Data Capture) REST API provides a single-point of access for reading data stored across iMednet data services. This specification documents all available endpoints in the latest version of the API. 

    The version of the OpenAPI document: 1.3.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.variables_api import VariablesApi  # noqa: E501


class TestVariablesApi(unittest.TestCase):
    """VariablesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = VariablesApi()

    def tearDown(self) -> None:
        self.api.api_client.close()

    def test_list_variables(self) -> None:
        """Test case for list_variables

        List variables (fields) in a study  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
