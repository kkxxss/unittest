# -*- coding: utf-8 -*-
# @Time    : 2018/11/16 10:12
# @Author  : lishanshan
import xlrd
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

    # case_dir={'case_name':x,'input_1':y,'input_2':z for }

    bbb = {x: x ** 2 for x in (2, 4, 6)}
    print(bbb)
    # {2: 4, 4: 16, 6: 36}

    # case_list=[x for x in ({'case_name':sheet.cell(i, 0).value,'input_1':sheet.cell(i, 1).value  for i  in range(1,nrows) })]

    return case_list

# case_list=excel_data()
#
# print(case_list)
file = xlrd.open_workbook('E:/脚本/Test_study/unittest/ddt_study_data/case.xlsx')
sheet = file.sheets()[0]  # sheet[0]打开第一个sheet页面
nrows = sheet.nrows  # 获取行数
bbb = [ sheet.cell(i, 0).value  for i in range(1,nrows) ]
c=[{'case_name':x }for x in bbb]
case_list=[{'case_name':sheet.cell(i, 0).value,'input_1':sheet.cell(i, 1).value,'input_2':sheet.cell(i, 2).value} for i in range(1,nrows) ]
print(bbb)
print(c)
print(case_list)
    # {2: 4, 4: 16, 6: 36}