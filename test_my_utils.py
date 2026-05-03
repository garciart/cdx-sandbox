"""Unit tests for utils/my_utils.py.

Usage: python -B test_my_utils.py
"""
import unittest

from utils.my_utils import validate_input


class TestValidateInput(unittest.TestCase):
    """Test suite for validate_input."""

    def test_validate_input_accepts_expected_type(self):
        """validate_input should pass for valid non-empty values."""
        validate_input('Rob', str, allow_empty=False)

    def test_validate_input_rejects_wrong_type(self):
        """validate_input should raise TypeError for wrong type."""
        with self.assertRaises(TypeError):
            validate_input(123, str, allow_empty=False)

    def test_validate_input_rejects_empty_string_when_not_allowed(self):
        """validate_input should raise ValueError for empty strings."""
        with self.assertRaises(ValueError):
            validate_input('', str, allow_empty=False)

    def test_validate_input_rejects_whitespace_when_not_allowed(self):
        """validate_input should raise ValueError for whitespace-only strings."""
        with self.assertRaises(ValueError):
            validate_input('   \n\t', str, allow_empty=False)

    def test_validate_input_allows_empty_string_when_allowed(self):
        """validate_input should allow empty strings when allow_empty=True."""
        validate_input('', str, allow_empty=True)

    def test_validate_input_rejects_none_only_list_when_not_allowed(self):
        """validate_input should raise ValueError for None-only lists."""
        with self.assertRaises(ValueError):
            validate_input([None, None], list, allow_empty=False)

    def test_validate_input_rejects_none_only_dict_when_not_allowed(self):
        """validate_input should raise ValueError for None-only dicts."""
        with self.assertRaises(ValueError):
            validate_input({'a': None, 'b': None}, dict, allow_empty=False)

    def test_validate_input_allows_none_when_expected_and_empty_allowed(self):
        """validate_input should allow None if expected and allow_empty=True."""
        validate_input(None, None, allow_empty=True)


if __name__ == '__main__':
    unittest.main()
