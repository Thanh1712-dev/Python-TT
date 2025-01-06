#!/usr/bin/env python
# coding: utf-8

# 公司的设备会跑出一些`txt`格式的日志文件（如下图所示）。其中第一列是ID，相同的ID可能会重复出现。现在要求按ID分块将数据拆分成新的`txt`文件，ID第一次出现的数据块，存为“ID_1.txt”，第二次出现的数据块，则存为“ID_2.txt”，以此类推。比如下面的89031这个ID出现了三次，则需要存为三个单独的`txt`文件。

# ![](images\require.png)

# 首先，需要读取原始数据。我们通过`readlines()`方法，整行读取，并存入列表`lines`。查看其前5个元素，如下所示。

# In[38]:


#读取txt文件中的数据
file = open('数据.txt')
lines = file.readlines()
lines[:5]


# 然后将`lines`列表中的数据按照ID所在的数据块分块存入字典，以便后续写入到新的`txt`文件。新建一个字典`data`，用于储存最终分割好的数据。它的数据结构如下图所示。它的键是ID，值是一个列表，列表中包含不同的数据块组成的子列表。
# ![](images\data.png)

# 然后建一个空的列表`line_list`，用于中转数据块中的数据。我们将单个数据块的数据持续放入这个列表，当遇到下一个数据块的时候，就将这个列表中的数据全部以ID为键放入字典`data`。然后清空列表，将新新数据块的第一行数据放入，直到遇到下一个数据块，又执行同样的操作。我们如何知道是否进入下一个数据块呢，数据分块标识`last_id`就是起这个作用的。每处理一行`lines`中的数据，就将该行的ID赋值给`last_id`。
# <br/>
# <br/>由于数据块的ID会有重复，所以在外层的`else`语句的第一层`if`语句中，增加了嵌套的`if`语句来进行判断。如果ID重复，则将中转数据列表中的数据添加到原ID键对应的值里面；如果不重复，才新建ID并存入数据。
# <br/>
# <br/>`for`循环完成后，最后一个文字块的数据还在中转列表`line_list`中，并未放入字典`data`，所以还需要增加几行程序。同样需要判断这个文字块的ID是否已存在于字典中，如果存在，则追加到对应的ID内；不存在，才新增ID并放入。到此，数据整理完成。可以随便选一个ID，查看一下`data`里面的数据。

# In[39]:


data = {} #储存分割的数据
line_list = [] #中转列表
last_id = "start" #数据分块标识
for line in lines:
    row_data =line.split(" ") #将一行数据按空格分隔
    ID = row_data[0] #获得ID
    if last_id == "start":#用于处理数据第一行
        line_list.append(line) #将第一行数据放入中转列表
    else: #不是第一行数据，则按如下执行
        if ID != last_id: #如果出现新的数据块
            if last_id in data: #新的数据块的ID已存在字典data中
                data[last_id].append(line_list) #将中转列表的数据添加到对应的ID中
            else: #新的数据块的ID不存在字典data中
                data[last_id] = [line_list] #将中转列表中的数据以ID为键放入字典的值的列表中
            line_list = [line]#将中转列表清空，并放入新数据块的第一行数据
        else: #没出现新的数据块
            line_list.append(line) #将数据继续加入中转列表
    last_id = ID #每处理一行，将分块标识last_id更新为最新的ID
    
#将最后一个文字块的数据放入字典
if last_id in data:
    data[last_id].append(line_list)
else:
    data[last_id] = [line_list]
    
data["89031"]


# In[28]:


for i in data.keys():
    for block in data[i]:
        print(block)
        print("--"*50)


# 随后就来将数据按要求写入单个的`txt`文件。写入数据是一个重复操作，所以定义函数`to_txt()`，以便重复调用。函数有两个参数，一个是文件名，另一个是包含单个文字块的数据列表（每写入一个文件，里面的数据对应单个的文字块）。此处，手动建一个文件夹，命名为“分块”，新的`txt`文件就存入这个文件夹。然后遍历列表，将数据逐个写入。

# In[40]:


#写入数据函数
def to_txt(filename, data_list):#filename为写入文件的名字，data为要写入数据列表.
    file = open("分块\\" + filename + '.txt','a')
    for i in range(len(data_list)):
        file.write(data_list[i])
    file.close() #保存数据并关闭


# 写入函数定义好后，就可以调用它批量写入了。两个`for`循环，第一个循环先遍历字典`data`中的ID，第二个循环遍历ID中的列表，即提取出里面的文字块。传入函数`to_txt`中的第一个参数是按`ID_i+1`来命名文件的，实际中就是诸如`89031_1`、`89031_2`这样的。传入的第二个参数即是文字块所在的列表。

# In[42]:


#批量写入数据
for ID in data:
    for i in range(len(data[ID])):
        to_txt(f"{ID}_{i+1}", data[ID][i])


# 上结果图。
# ![](images\result.png)
# ![](images\result1.png)
