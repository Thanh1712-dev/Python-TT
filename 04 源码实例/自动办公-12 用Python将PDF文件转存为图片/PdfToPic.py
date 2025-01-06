print("PDF转Excel开始运行！")

#批量获取PDF扫描件的内容，并存入新建的文件夹
import fitz
import glob
import os

work_path = os.getcwd()

image_path = work_path+"\\images\\" #存放图片的文件夹
PDFfiles = glob.glob(work_path+"\\扫描文件\\*.pdf") #获取所有pdf文件的文件名
for PDFfile in PDFfiles: #遍历所有PDF文件
    PDFdoc = fitz.open(PDFfile) #打开PDF文件
    for pg in range(PDFdoc.pageCount): #按页提取图片
        folder_name = PDFfile.split("\\")[-1].split(".")[0] #按源文件名新建文件夹
        page = PDFdoc[pg]
        rotate = int(0)
        zoom_x = 3 # 设置图片相对于PDF文件在X轴上的缩放比例，跟图片清晰度有关
        zoom_y = 3
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pix = page.getPixmap(matrix=mat, alpha=False)
        if not os.path.exists(image_path+folder_name):
            os.makedirs(image_path+folder_name)
        pix.writePNG(image_path+folder_name + "\\{}.png".format(str(pg+1))) #按顺序保存图片


#获取文件夹信息
pathss=[] # 存储图片文件夹下的所有文件夹
for root, dirs, files in os.walk(work_path+"\\images"):
    path = [os.path.join(root,d) for d in dirs]
    pathss.extend(path)

#获取图片路径信息
pictures = []
for i in pathss:
    for root, dirs, files in os.walk(i):
        img_list = [os.path.join(root,name) for name in files]
        pictures.append(img_list)

#新建excel文件，并插入图片并按原PDF文件名保存
from openpyxl import Workbook
from openpyxl.drawing.image import Image
wb = Workbook()
ws = wb.active

# path = 'images\\DOC1\\1.png'
for picture in pictures: 
#     [['images\\653959 PANASONIC PO#LCD-NO\\1.png',
#   'images\\653959 PANASONIC PO#LCD-NO\\2.png'],
    row = 1
    for i in range(len(picture)):
        #0,1
        img = Image(picture[i])
#         ''C:\\Users\\dywei\\python\\python_excel\\将PDF档扫描件转存到Excel文件中\\images\\653959 PANASONIC PO#LCD-NO\\1.png''
        newsize = (892.5, 1263) #原图宽高像素减半
        img.width, img.height = newsize
        ws.add_image(img, 'A'+str(row))
        row += 71
    wb.save(work_path+"\\扫描文件\\"+picture[0].split("\\")[-2]+".xlsx")

print("完成转换！")
input()