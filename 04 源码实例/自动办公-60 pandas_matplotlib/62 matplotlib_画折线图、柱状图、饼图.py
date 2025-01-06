# -*- coding: utf-8 -*-
# @Time : 2020/8/23 1:25
# @File : 20_matplotlib_画折线图、柱状图、饼图.py
# @Software: PyCharm
# @Description:

# pip install matplotlib

import matplotlib.pyplot as mplt
# 支持中文
mplt.rcParams['font.sans-serif'] = ['SimHei']

date = ['2020/7/21','2020/7/22','2020/7/23',]
yue = [10,70,30]
min = [40,50,60]

# 折线图
# mplt.plot(date,yue,color='red',label='广东')
# mplt.plot(date,min,color='blue',label='福建')
# mplt.title('降雨量')
# mplt.xlabel('日期')
# mplt.ylabel('降雨量')
# mplt.legend()
# mplt.show()

# 柱状图
# mplt.bar(date,yue,color='red',label='广东')
# mplt.bar(date,min,color='black',label='广东')
# mplt.legend()
# mplt.show()
# 水平柱状图
# mplt.barh(date,yue,color='red',label='广东')
# mplt.legend()
# mplt.show()

# 饼图
data = [1,2]
province = ['广东','福建']
colors = ['red','blue']
mplt.pie(x=data,labels=province,colors=colors)
mplt.legend()
mplt.show()
