#!/usr/bin/env python3
"""Test Suite for the Utils Module"""

from utils import access_nested_map, get_json, memoize
import unittest
from parameterized import parameterized
from unittest.mock import patch, MagicMock


class TestAccessNestedMap(unittest.TestCase):
    """A Test Suite containing unit tests for various methods
    under the Utils Module"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test Method for method return accuracy"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Raises exception if nested_map is not dictionary"""
        with self.assertRaises(expected) as Es:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test Suite for the Json related Methods"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, url, expected):
        """Unit test for the get_json method function"""
        # Mock_request get function returns an instance of
        # mock response class
        mock_response = MagicMock()
        mock_response.json.return_value = expected
        with patch('requests.get', return_value=mock_response) as req_get:
            response = get_json(url)
            self.assertEqual(response, expected)
            req_get.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """Test Suite containing memoize method Test Cases"""

    def test_memoize(self):
        class TestClass:
            """Test Class"""

            def a_method(self):
                """Returns 42"""
                return 42

            @memoize
            def a_property(self):
                """Memoized Property Method"""
                return self.a_method()

        test_object = TestClass()
        with patch.object(test_object, 'a_method') as mock_object:
            mock_object.return_value = 42
            senario_1 = test_object.a_property
            senario_2 = test_object.a_property
            self.assertEqual(senario_1, 42)
            self.assertEqual(senario_2, 42)
            mock_object.assert_called_once()
