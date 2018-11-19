# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 14:57
# @Author  : lishanshan

import os
import time
import unittest

import xlrd
from ddt import ddt, data
from common import HTMLTestRunner
def excel_data():
    file = xlrd.open_workbook('E:/脚本/Test_study/unittest/ddt_study_data/case.xlsx')
    sheet = file.sheets()[0]  # sheet[0]打开第一个sheet页面
    nrows = sheet.nrows  # 获取行数
    case_name=[]
    input_1=[]
    input_2=[]
    case_list = []
    case_dir = {}
    for i in range(1,nrows):
        # print(i)
        case_name.append(sheet.cell(i, 0).value)
        input_1.append(sheet.cell(i, 1).value)
        input_2.append(sheet.cell(i, 2).value)
    mid = map(list,zip(case_name,input_1,input_2))
    #zip对象中对应的元素打包成一个元组,然后返回一个可迭代的zip对象
    #map(function, iterable, ...)根据提供的函数对指定序列做映射
    for item in mid:
        case_dir=dict(zip(['case_name','input_1','input_2'],item))
        case_list.append(case_dir)
    return case_list

case_list=excel_data()
@ddt
class Testexcel(unittest.TestCase):
    def setUp(self):
        pass

    @data(*case_list)
    def test_jiafa(self, a):
        SJ=int(a['input_1'])+int(a['input_2'])
        YQ=10
        self.assertEqual(SJ, YQ)

if __name__=='__main__':
    unittest.main()
