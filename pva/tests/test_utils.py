import os
import unittest
from lib.utils import *
from settings import *


class TestObject(object):

    def __init__(self, data1, data2):
        self.__data1 = data1
        self.__data2 = data2

    def get_data(self):
        return self.__data1+':'+self.__data2


class TestUtils(unittest.TestCase):

    def setUp(self):
        """setUp:lib/utils tests"""
        self.in_blacklist = '190.93.240.1'
        self.notin_blacklist = '190.13.240.13'
        self.data1 = 'data1'
        self.data2 = 'data2'
        self.dump_filename = 'dump.test'
        self.second_dump_filename = 'recent.tst'


    def test_address_in_blacklist(self):
        """lib/utils:address_in_blacklist tests"""
        self.assertTrue(address_in_blacklist(self.in_blacklist))
        self.assertFalse(address_in_blacklist(self.notin_blacklist))


    def test_create_directory(self):
        """lib/utils:create_directory tests"""
        self.assertTrue(create_directory(TEST_DIR))
        self.assertTrue(os.path.exists(TEST_DIR))


    def test_dump_object(self):
        """lib/utils:dump_object tests"""
        to_dump = TestObject(self.data1, self.data2)
        filepath = TEST_DIR+self.dump_filename
        filepath2 = TEST_DIR+self.second_dump_filename
        self.assertTrue(dump_object(filepath, to_dump))
        self.assertTrue(os.path.isfile(filepath))
        self.assertTrue(dump_object(filepath2, to_dump))
        self.assertTrue(os.path.isfile(filepath2))


    def test_load_dumped_object(self):
        """lib/utils:load_dumped_object tests"""
        filepath = TEST_DIR+self.dump_filename
        loaded_dump = load_dumped_object(filepath)
        self.assertIsInstance(loaded_dump, TestObject)
        self.assertEqual(loaded_dump.get_data(), self.data1+':'+self.data2)


    def test_get_recent_file(self):
        """lib/utils:get_recent_file tests"""
        fd_filepath = TEST_DIR+self.dump_filename
        sd_filepath = TEST_DIR+self.second_dump_filename
        self.assertEqual(get_recent_file(TEST_DIR), sd_filepath)
        self.assertEqual(get_recent_file(TEST_DIR, 'test'), fd_filepath)
