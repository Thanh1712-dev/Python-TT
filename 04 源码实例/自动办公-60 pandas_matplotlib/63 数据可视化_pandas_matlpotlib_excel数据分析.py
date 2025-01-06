# -*- coding: utf-8 -*-
# @Time : 2020/8/23 1:51
# @File : 21_数据可视化_pandas_matlpotlib_excel数据分析.py
# @Software: PyCharm
# @Description:

import pandas as pd
import numpy as np
import matplotlib.pyplot as mplt



r_file = pd.ExcelFile('student.xls')
data = r_file.parse('Sheet1')
# 求各省的个数
pt_n = pd.pivot_table(data, index=['省份'], aggfunc=np.size)  # aggfunc=np.sum 求和，默认是平均值

mplt.rcParams['font.sans-serif'] = ['SimHei']
pt_n.plot(kind='bar')

# 修改
# index的倾斜角度
mplt.xticks(rotation=45)
mplt.title('各省数量')
mplt.xlabel('省份')
mplt.ylabel('个数')
mplt.legend()

mplt.show()
