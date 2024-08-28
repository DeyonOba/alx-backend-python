#!/usr/bin/env python3
"""
Client side tests.
"""
import unittest
from unittest.mock import patch, Mock, MagicMock
from parameterized import parameterized
from utils import memoize
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests the `client.GithubOrgClient.test_org` method"""
    @parameterized.expand([
        ("google", {'login': 'google'}),
        ("abc", {'login': 'abc'}),
    ])
    @patch("client.get_json")
    def test_orgithub(self, org_name, expected, mocked_method):
        """Test org method from client.GithubOrgClient"""
        expected_url = "https://api.github.com/orgs/{org}".format(org=org_name)
        mocked_method.return_value = MagicMock(return_value=expected)
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org(), expected)
        mocked_method.assert_called_with(expected_url)


if __name__ == "__main__":
    unittest.main()
