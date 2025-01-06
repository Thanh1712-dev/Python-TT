# -*- coding: utf-8 -*-
# @Time : 2020/8/23 1:23
# @File : 19_数据分析_pandas_数据透视表.py
# @Software: PyCharm
# @Description:

# pip install numpy
import pandas as pd
import numpy as np


r_file = pd.ExcelFile('student.xls')
data = r_file.parse('Sheet1')
# print(data)
# index代表行的名称，columns代表列的名称
# aggfunc=np.sum 求和
# margins=True 总计
# 求各省的分数和
pt_s = pd.pivot_table(data, index=['省份'], aggfunc=np.sum, margins=True)  # aggfunc=np.sum 求和，默认是平均值
# print(pt_s)
# 全部显示行和列
# pt_s.set_option('display.max_rows', None)
# pt_s.set_option('display.max_columns', None)
# 求各省的个数
pt_n = pd.pivot_table(data, index=['省份'], aggfunc=np.size, margins=True)  # aggfunc=np.sum 求和，默认是平均值
print(pt_n)
#
# print(pt_s.iat[0, 0])
# print(pt_n.iat[0, 0])