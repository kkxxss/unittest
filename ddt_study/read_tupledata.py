# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 11:47
# @Author  : lishanshan

import unittest
from ddt import ddt, data, unpack
@ddt
class Test(unittest.TestCase):
    def setUp(self):
        pass

    @data((1, 2, 3), (2, 3, 5), (1, 1, 1))
    # @unpack
    def test_dict(self, *args, **kwargs):
        print("开始打印数据")
        # print(*args, **kwargs)
        print(*args)
