from typing import Union

def is_palindrome(value: Union[int, str])-> bool:
    if isinstance(value, str):
        return "".join([i for i in reversed(value)]) == value
    return "".join([i for i in reversed(str(value))]) == str(value)
    
print(is_palindrome(77))