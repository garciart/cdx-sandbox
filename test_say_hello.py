"""Simple unit tests for the say_hello.py script


Usage: python -B test_say_hello.py
"""
import unittest
# Import the functions you want to test from the target script
from say_hello import say_hello


class TestSayHello(unittest.TestCase):
    """Test suite for say_hello.py."""

    def test_say_hello_pass_no_arg(self):
        """Test default argument."""
        result = say_hello()
        self.assertEqual(result, 'Hello, World!')

    def test_say_hello_pass_arg(self):
        """Test valid argument."""
        result = say_hello(username='Rob')
        self.assertEqual(result, 'Hello, Rob!')

    def test_say_hello_fail_type(self):
        """Test invalid argument types."""
        _invalid_args = [1, 1.1, 1j, True]

        for ia in _invalid_args:
            _result = say_hello(username=ia)
            self.assertTrue(_result.lower().startswith('error'))

    def test_say_hello_fail_empty_username(self):
        """Test empty-string username returns an error."""
        result = say_hello(username='')
        self.assertTrue(result.lower().startswith('error'))
        self.assertIn('cannot be empty', result.lower())

    def test_say_hello_fail_whitespace_username(self):
        """Test whitespace-only username returns an error."""
        result = say_hello(username='   \t')
        self.assertTrue(result.lower().startswith('error'))
        self.assertIn('cannot be empty', result.lower())


if __name__ == '__main__':
    unittest.main()
