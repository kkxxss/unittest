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

    # for i in range(1,nrows):
    #     # print(i)
    #     case_name.append(sheet.cell(i, 0).value)
    #     input_1.append(sheet.cell(i, 1).value)
    #     input_2.append(sheet.cell(i, 2).value)
    # mid = map(list,zip(case_name,input_1,input_2))
    # #zip对象中对应的元素打包成一个元组,然后返回一个可迭代的zip对象
    # #map(function, iterable, ...)根据提供的函数对指定序列做映射
    # for item in mid:
    #     case_dir=dict(zip(['case_name','input_1','input_2'],item))
    #     case_list.append(case_dir)

    case_list = [
        {'case_name': sheet.cell(i, 0).value, 'input_1': sheet.cell(i, 1).value, 'input_2': sheet.cell(i, 2).value} for
        i in range(1, nrows)]
    return case_list

case_list=excel_data()

print(case_list)
# @ddt
# class Testexcel(unittest.TestCase):
#     def setUp(self):
#         pass
#
#     @data(*case_list)
#     def test_jiafa(self, a):
#         SJ=int(a['input_1'])+int(a['input_2'])
#         YQ=10
#         self.assertEqual(SJ, YQ)
#
# curpath = os.path.dirname(os.path.realpath(__file__))
# report_path = os.path.join(curpath, "report")
# if not os.path.exists(report_path): os.mkdir(report_path)
# case_path = os.path.join(curpath, "case")
#
# print(curpath)
#
# def add_case(casepath=case_path, rule="test*.py"):
#     '''加载所有的测试用例'''
#     # 定义discover方法的参数
#     discover = unittest.defaultTestLoader.discover(casepath,
#                                                   pattern=rule,)
#     print(discover)
#     return discover
#
# if __name__=='__main__':
#     # unittest.main()
#     now = time.strftime("%Y-%m-%d %H_%M_%S")
#     test_suite = unittest.TestSuite()  # 创建一个测试集合
#     # test_suite.addTest(Testexcel('test_jiafa'))  # 测试套件中添加测试用例
#     test_suite.addTest(unittest.makeSuite(Test))#使用makeSuite方法添加所有的测试方法
#     testreport = 'E:/脚本/Test_study/unittest/report/'
#     filename = testreport + now + 'result.html'
#     print(filename)
#     fp = open(filename, 'wb')
#     # fp = open('res.html', 'wb')  # 打开一个保存结果的html文件
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='api测试报告', description='测试情况')
#     print(runner)
#     # 生成执行用例的对象
#     runner.run(test_suite)
#     fp.close()
#     # 执行测试套件