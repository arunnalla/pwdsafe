"""
Check if a password is safe to use
"""
import hashlib
import requests


def is_safe(password: str) -> bool:

    """
    Takes a password and returns is the password is safe to use.
        Parameters:
            password (str): A password string that needs to be checked

        Returns:
            (bool): Boolean indicating if the password is safe
    """
    if not isinstance(password, str):
        raise ValueError("Password provided must be a string.")

    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    first_five_chars_of_sha1 = sha1[0:5]

    response = requests.get(
        f"https://api.pwnedpasswords.com/range/{first_five_chars_of_sha1}"
    )

    if response.status_code == 200:
        return f"{sha1[6:]}:" not in response.text

    raise RuntimeError(
        f"Something went wrong! Got {response.status_code} as response status code."
    )
