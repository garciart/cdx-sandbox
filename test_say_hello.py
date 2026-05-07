"""Simple unit tests for the say_hello.py script

Usage: python -B test_say_hello.py
"""
import subprocess
import sys
import unittest
from pathlib import Path

# Import the functions you want to test from the target script
from say_hello import say_hello


SCRIPT_PATH = Path(__file__).with_name('say_hello.py')


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

    def test_cli_prompts_for_username_when_option_is_missing(self):
        """Test CLI prompt uses entered username when -u is omitted."""
        result = subprocess.run(
            [sys.executable, '-B', str(SCRIPT_PATH)],
            input='Rob\n',
            capture_output=True,
            check=True,
            text=True,
        )

        self.assertEqual(result.stdout, 'Username: Hello, Rob!\n')

    def test_cli_sends_none_when_prompt_is_empty(self):
        """Test CLI sends None when -u and prompt input are blank."""
        result = subprocess.run(
            [sys.executable, '-B', str(SCRIPT_PATH)],
            input='\n',
            capture_output=True,
            check=True,
            text=True,
        )

        self.assertEqual(result.stdout, 'Username: Hello, World!\n')

    def test_cli_does_not_prompt_when_username_option_is_provided(self):
        """Test CLI skips prompt when -u is provided."""
        result = subprocess.run(
            [sys.executable, '-B', str(SCRIPT_PATH), '-u', 'Rob'],
            capture_output=True,
            check=True,
            text=True,
        )

        self.assertEqual(result.stdout, 'Hello, Rob!\n')


if __name__ == '__main__':
    unittest.main()
