#读取txt文件中的数据
file = open('data.txt')
lines = file.readlines()

import time, datetime
def timeStampToDate(timeStamp):
    timeArray = time.localtime(timeStamp)
    return time.strftime("%Y-%m-%d %H", timeArray)


#按日期-小时提取数据，并存入字典
data = {}
for line in lines:
    row_data =line.split(" ") #将一行数据按空格分隔
    date_hour = timeStampToDate(int(row_data[2])) #将第三个数据（时间戳）转换成设定的日期-时间格式
    data.setdefault(date_hour,[]) #以日期-时间为键，相同日期-时间的数据存为它的值
    data[date_hour].append(row_data) #数据存入data字典

#写入数据函数
def To_txt(filename, data):#filename为写入文件的路径，data为要写入数据列表.
    file = open(filename + '.txt','a')
    for i in range(len(data)):
        for j in range(len(data[i])):
            text = data[i][j]
            if j != len(data[i])-1: #判断是否最后一个元素
                text = text+' '   #若不是最后一个元素才加空格
            file.write(text)
    file.close()

#批量写入数据
for i in data:
    print(i)
    To_txt(i, data[i])