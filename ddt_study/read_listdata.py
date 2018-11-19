# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 10:42
# @Author  : lishanshan

import unittest
from ddt import ddt, data, unpack

@ddt
class Test(unittest.TestCase):
    def setUp(self):
        pass

    # @data([3, 2], [4, 3])
    # @unpack
    # def test_tuples_extracted_into_arguments(self, first_value,second_value):
    #     print(first_value)
    #     print(second_value)
    #     self.assertTrue(first_value > second_value)

    @data([{}])
    @unpack
    def test_tuples_extracted_into_arguments(self, first_value, second_value):
        print(first_value)
        print(second_value)
        # self.assertTrue(first_value > second_value)

if __name__=='__main__':
    unittest.main()
