#!/usr/bin/env python3
"""Test Suite for the Client Module"""

import json
from unittest import TestCase
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from unittest.mock import Mock, patch, PropertyMock
from typing import Dict
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(TestCase):
    """Test Suite that implements test cases relating
    to the GitHubOrgClient class"""

    @parameterized.expand([
        ("google", {'name': "Google"}),
        ("abc", {'name': "Abc"}),
    ])
    @patch("client.get_json", )
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
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_url_repos:
            mock_url_repos.return_value = 'https://api.github.com/orgs/google/repos'
            GithubObject = GithubOrgClient(org_name='google')
            self.assertEqual(GithubObject._public_repos_url,
                             'https://api.github.com/orgs/google/repos')

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test Unit to check for accuracy of """
        test_PAYLOAD = {
            "repos_url": "https://api.github.com/orgs/google/repos",
            'repos': [
                {
                    "id": 7697149,
                    "node_id": "MDEwOlJlcG9zaXRvcnk3Njk3MTQ5",
                    "name": "episodes.dart",
                    "full_name": "google/episodes.dart",
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                        "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
                        "type": "Organization",
                        "site_admin": False
                    }
                },
                {
                    "id": 7776515,
                    "node_id": "MDEwOlJlcG9zaXRvcnk3Nzc2NTE1",
                    "name": "cpp-netlib",
                    "full_name": "google/cpp-netlib",
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                        "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
                        "type": "Organization",
                        "site_admin": False
                    }
                }
            ]
        }
        mock_get_json.return_value = test_PAYLOAD.get('repos')
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock,
                   return_value=test_PAYLOAD.get('repos_url')) as mock_public_repos_url:
            self.assertEqual(GithubOrgClient('google').public_repos(),
                             ['episodes.dart', 'cpp-netlib'], )
            mock_get_json.assert_called_once()
            mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, key, expected):
        """Test Unit Case for the has_license method"""
        GithubObject = GithubOrgClient('google').has_license(repo, key)
        self.assertEqual(GithubObject, expected)


@parameterized_class(("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
                     TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(TestCase):
    """Test Suite containing Unit Tests for methods on
    public_repos and has_license"""

    @classmethod
    def setUpClass(cls):
        """Before all tests in class starts to executed"""
        configuratn = {'return_value.json.side_effect': [
            cls.org_payload, cls.repos_payload,
            cls.org_payload, cls.repos_payload
        ]}
        cls.get_patcher = patch('requests.get', **configuratn)

        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        """Test the entire accuracy of the entire
        public_repos method"""
        GithubObj = GithubOrgClient('google')

        self.assertEqual(GithubObj.org, self.org_payload)
        self.assertEqual(GithubObj.repos_payload, self.repos_payload)
        self.assertEqual(GithubObj.public_repos(), self.expected_repos)
        self.assertEqual(GithubObj.public_repos("NOLICENSE"), [])
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """After tests in entire class executed"""
        cls.get_patcher.stop()
