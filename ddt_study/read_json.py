# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 14:41
# @Author  : lishanshan

import unittest
from ddt import ddt, file_data

@ddt
class Testjson(unittest.TestCase):
    def setUp(self):
        pass

    @file_data('E:/脚本/Test_study/unittest/ddt_study_data/test_data_list.json')
    def testlist(self,value):
        print(value)

    @file_data('E:/脚本/Test_study/unittest/ddt_study_data/test_data_dict.json')
    def testdict(self,value):
        print(value)

if __name__ == '__main__':
    unittest.main()