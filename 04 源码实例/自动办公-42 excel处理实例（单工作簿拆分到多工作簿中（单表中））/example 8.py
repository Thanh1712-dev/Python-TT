import openpyxl
wb=openpyxl.load_workbook('工作表1.xlsx',
                          data_only=True)
ws=wb.worksheets[0]
rngs=list(ws.values)
d={}
for row in rngs[1:]:
    if row[2] in d.keys():
        d[row[2]]+=[row]
    else:
        d.update({row[2]:[row]})
for k,v in d.items():
    nwb=openpyxl.Workbook()
    nws=nwb.active;nws.title=k
    nws.append(rngs[0])
    for r in v:
        nws.append(r)
    wb.save('统计汇总表/'+k+'.xlsx')

