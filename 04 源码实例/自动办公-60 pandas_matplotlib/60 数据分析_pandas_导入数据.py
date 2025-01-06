# -*- coding: utf-8 -*-
# @Time : 2020/8/23 0:46
# @公众号 :Python自动化办公社区 
# @File : 18_数据分析_pandas_导入数据.py
# @Software: PyCharm
# @Description:

# pip install pandas
import pandas as pd

# 一维数据
# one_d = pd.Series(['a','b','c','d'])
# print(one_d)

# 二维数据
two_d = pd.DataFrame({
    '学号': ['A2', 'A3'],
    '姓名': ['刘二', '张三'],
    '语文': ['68', '68'],
})
print(two_d)

