"""A simple application that accepts input and displays a greeting.

Usage:
- python -B say_hello.py -u <username>
- python -B say_hello.py -h

Note: Use single or double quotes for names with spaces or special characters,
      such as 'Rob G', "O'Brien", etc.

Other:
Lint:        `python -m pylint .`
Check style: `python -m autopep8 --diff --recursive .`
Test:        `python -B test_say_hello.py`
"""
import argparse

from utils.my_utils import validate_input


def say_hello(username: None | str = None) -> str:
    """Print a greeting to STDOUT.

    :param Optional[str] username: The user to greet, defaults to None.
    :returns str: The greeting to display
    """
    # Validate inputs
    _result = validate_input(username, None | str, allow_empty=False)
    if _result:
        return _result[-1]

    # Account for no argument
    username = 'World' if username is None else username
    return f"Hello, {username}!"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='python -B say_hello.py',
        description='A simple application that accepts input and displays a greeting.'
    )
    parser.add_argument('-u', '--username', type=str, default=None,
                        help="The user to greet, defaults to 'World' if not provided.")
    args = parser.parse_args()

    print(say_hello(args.username))
