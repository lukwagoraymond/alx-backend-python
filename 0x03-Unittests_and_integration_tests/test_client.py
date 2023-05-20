#!/usr/bin/env python3
"""Test Suite for the Client Module"""

from unittest import TestCase
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import Mock, patch
from typing import Dict


class TestGithubOrgClient(TestCase):
    """Test Suite that implements test cases relating
    to the GitHubOrgClient class"""

    @parameterized.expand([
        ("google", {'name': "Google"}),
        ("abc", {'name': "Abc"}),
    ])
    @patch("client.get_json",)
    def test_org(self, org: str, expected: Dict, mock_func: Mock) -> None:
        """Test Case for the org method"""
        mock_func.return_value = Mock(return_value=expected)
        GithubObject = GithubOrgClient(org)
        self.assertEqual(GithubObject.org(), expected)
        mock_func.assert_called_once_with(
            f"https://api.github.com/orgs/{org}")
