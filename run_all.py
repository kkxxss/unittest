# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 15:53
# @Author  : lishanshan

import unittest
import time
from common import HTMLTestRunner
from common import BeautifulReport
import os

curpath = os.path.dirname(os.path.realpath(__file__))
report_path = os.path.join(curpath, "report")
if not os.path.exists(report_path): os.mkdir(report_path)
case_path = os.path.join(curpath, "case")

print(curpath)
print(report_path)
print(case_path)

def add_case(casepath=case_path, rule="test*.py"):
    '''加载所有的测试用例'''
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(casepath,
                                                  pattern=rule,)
    print(discover)
    return discover


def run_case(all_case, reportpath=report_path):
    '''执行所有的用例, 并把结果写入测试报告'''
    htmlreport = reportpath+r"\result.html"
    print("测试报告生成地址：%s"% htmlreport)
    fp = open(htmlreport, "wb")
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
    #                                            verbosity=2,
    #                                            title="测试报告",
    #                                            description="用例执行情况")
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
    #                                        verbosity=2,
    #                                        title="测试报告",
    #                                        description="用例执行情况")

    result = BeautifulReport.BeautifulReport(cases)
    result.report(filename='测试报告', description='测试deafult报告', log_path='report')

    # 调用add_case函数返回值
    # result.run(all_case)
    fp.close()

if __name__ == "__main__":
    cases = add_case()
    run_case(cases)