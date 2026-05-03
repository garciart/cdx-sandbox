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
        say_hello()

    def test_say_hello_pass_arg(self):
        """Test valid argument."""
        say_hello(username='Rob')

    def test_say_hello_fail_type(self):
        """Test invalid argument types."""
        _invalid_args = [1, 1.1, 1j, True]

        for ia in _invalid_args:
            _result = say_hello(username=ia)
            self.assertTrue(_result.lower().startswith('error'))

if __name__ == '__main__':
    unittest.main()
