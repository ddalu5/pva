import unittest
from lib.utils import *


class TestUtils(unittest.TestCase):

    def test_address_in_blacklist(self):
        """utils:address_in_blacklist"""
        in_blacklist = '190.93.240.1'
        notin_blacklist = '190.13.240.13'
        self.assertTrue(address_in_blacklist(in_blacklist))
        self.assertFalse(address_in_blacklist(notin_blacklist))
