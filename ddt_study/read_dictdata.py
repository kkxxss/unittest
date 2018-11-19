# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 11:35
# @Author  : lishanshan
import unittest
from ddt import ddt ,data,unpack

# @ddt
# class Testdict(unittest.TestCase):
#     def setUp(self):
#         pass
#     @data({'key1':'value1','key2':'value2'},{'key3':'value3'})
#     def testdict(self,*args, **kwargs):
#         print('开始打印数据')
#         print(args,**kwargs)
#
# if __name__ == '__main__':
#     unittest.main()

@ddt
class Test(unittest.TestCase):
    def setUp(self):
        pass
    @data({'value1': 1, 'value2': 2}, {'value1': 3, 'value2': 4})
    @unpack
    def test_dict(self, value1, value2):
        print(value1, value2)
        self.assertEqual(value2, value1 + 1)

if __name__ == '__main__':
    unittest.main()