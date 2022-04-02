"""
Test cases for pwdsafe package
"""
from unittest import TestCase

import pytest

from pwdsafe import is_safe


class PwdSafeTests(TestCase):
    """
    Test cases for methods in pwdsafe module __init__.py file
    """

    def test_pawned_password(self):
        """
        Test a password that is unsafe
        """
        is_pwd_safe = is_safe("password")
        self.assertFalse(is_pwd_safe)

    def test_unpawned_password(self):
        """
        Test a password that is safe
        """
        is_pwd_safe = is_safe("xsdadsajksdui11g129@")
        self.assertTrue(is_pwd_safe)

    @classmethod
    def test_invalid_data_type(cls):
        """
        Test ValueError is thrown when integer is passed
        """
        with pytest.raises(ValueError):
            is_safe(1234)

    @classmethod
    def test_none_as_password(cls):

        """
        Test ValueError is thrown when None is passed
        """
        with pytest.raises(ValueError):
            is_safe(None)
