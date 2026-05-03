"""A set of utility functions that I use often.
"""


def __get_var_name(obj: object) -> str:
    """Get the name of a variable.

    :param any obj: The variable object.
    :return str: The name of the variable.
    """
    for _name, _value in globals().items():
        if _value is obj:
            return _name
    return 'input_var'


def __is_expected_type(obj_to_check: object, expected_type: type | None) -> bool:
    """Check if an object is the correct type,
    accounting for NoneTypes before Python 3.10.

    :param object obj_to_check: The object to check.
    :param type | None expected_type: The expected type of the object.
    :return bool: If the object is of the expected type.
    """
    if expected_type is None:
        return obj_to_check is None
    return isinstance(obj_to_check, expected_type)


def __is_empty(obj_to_check: object) -> bool:
    """Check if an object is empty, whitespace, or contains only None values.

    :param object obj_to_check: The object to check.
    :return bool: If the object is empty, whitespace, or contains only None values.
    """
    if isinstance(obj_to_check, str):
        return obj_to_check.strip() == ''

    if isinstance(obj_to_check, (list, tuple, set, frozenset)):
        return not obj_to_check or all(item is None for item in obj_to_check)

    if isinstance(obj_to_check, dict):
        return not obj_to_check or all(value is None for value in obj_to_check.values())

    return False


def validate_input(obj_to_check: object,
                   expected_type: type | None,
                   allow_empty: bool = False) -> None:
    """Check if an input is the correct type and (optionally) not empty.

    :param any obj_to_check: The input to check.
    :param type expected_type: The expected type of the input.
    :param bool allow_empty: Allow empty inputs, defaults to False.
    :raises TypeError: If the input is the wrong type.
    :raises ValueError: If the input is empty and it should not be.
    """
    # Get the name of the input, if possible.
    _var_name = __get_var_name(obj_to_check)

    # Check if the input is the right type
    if not __is_expected_type(obj_to_check, expected_type):
        raise TypeError(f"'{_var_name}' is not {expected_type}.")

    # Check if the input is empty, whitespace, or contains only None values
    if not allow_empty and __is_empty(obj_to_check):
        raise ValueError(
            f"'{_var_name}' cannot be empty, whitespace, or contain only None values."
        )
