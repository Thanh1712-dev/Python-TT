import pandas as pd

#新建一个DataFrame用于存储汇总所有工作表的结果
result = pd.DataFrame()

#读取整个Excel文件中的所有表
df = pd.read_excel('日领料单.xlsx', header=2, sheet_name = None)
#按表名遍历，处理数据
for sheet_name in df.keys():    
    #按物料编号加总领料数量
    df_sum = df[sheet_name].groupby(['物料编号','物料描述'])['批号批数量'].sum().reset_index()    

    result = pd.concat([result,df_sum])
    
final = result.groupby(['物料编号','物料描述'])['批号批数量'].sum().reset_index().sort_values('批号批数量',ascending = False)
final.to_excel("汇总.xlsx")