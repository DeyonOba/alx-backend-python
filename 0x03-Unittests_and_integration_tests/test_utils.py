#!/usr/bin/env python3
"""
Unit test and Integation tests.
"""
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """Unit test for `utils.access_nested_map`"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, output):
        """Test the utils method `access_nested_map`."""
        self.assertEqual(access_nested_map(nested_map, path), output)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that KeyError is raised with the above inputs."""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Unit test for `utils.get_json`"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test that get_json returns the expected result."""
        # Configure the mock to return a response with the test payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call function with the test_url
        result = get_json(test_url)

        # Assert that the mocked get method was called exactly once with
        # the test URL
        mock_get.assert_called_once_with(test_url)

        # Assert that the result is the expected payload
        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main(verbosity=2)
