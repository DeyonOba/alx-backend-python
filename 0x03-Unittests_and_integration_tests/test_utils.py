#!/usr/bin/env python3
"""
Unit test and Integation tests.
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Unit test for `utils.access_nested_map`"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_acces_nested_map(self, nested_map, path, output):
        """Test the utils method `access_nested_map`."""
        self.assertEqual(access_nested_map(nested_map, path), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
