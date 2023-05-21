#!/usr/bin/env python3
"""Test Suite for the Client Module"""

from unittest import TestCase
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import Mock, patch, PropertyMock
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

    def test_public_repos_url(self):
        """Test case to check for accuracy of
        repos_url key:value pair"""
        with patch('client.GithubOrgClient.public_repos',
                   new_callable=PropertyMock) as mock_url_repos:
            mock_url_repos.return_value = 'https://api.github.com/orgs/google/repos'
            GithubObject = GithubOrgClient(org_name='google')
            self.assertEqual(GithubObject._public_repos_url,
                             'https://api.github.com/orgs/google/repos')
