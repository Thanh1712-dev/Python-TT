#!/usr/bin/env python
# coding: utf-8

# 因工作中的某些奇葩要求，需要将PDF文件的每页内容转存成按顺序编号的图片。用第三方软件或者在线转换也可以，但批量操作还是Python方便，所谓搞定办公自动化，Python出山，一统天下；Python出征，寸草不生~ O(∩_∩)O

# 不过这个需要用到`PyMuPDF`库，电脑运行cmd，输入“pip install PyMuPDF”安装即可。安装后通过`import fitz`导入模块。等等，为什么安装的是`PyMuPDF`，导入的是`fitz`？俺`PyMuPDF`就是这么任性，怎么的，爱用不用！哈哈，开个玩笑。其实是因为`PyMuPDF`曾用名`fitz-python`，所以只是`fitz`换了个马甲而已，呵呵。

# 这里先导入`fitz`库，用于将PDF文件的页面提取成像素信息（图片）。再导入`glob`库，用于获取后缀为".pdf"的文件的文件名。`os`库可新建文件夹。

# In[12]:


#批量将PDF文件转为图片
import fitz
import glob
import os

image_path = "图片\\" #存放图片的文件夹
PDFfiles = glob.glob("PDF文件\\*.pdf") #获取所有pdf文件的文件名
for PDFfile in PDFfiles: #遍历所有PDF文件
    PDFdoc = fitz.open(PDFfile) #读取PDF文件
    folder_name = PDFfile.split("\\")[-1].split(".")[0] #按源文件名新建文件夹
    for pg in range(PDFdoc.pageCount): #根据PDF的页数,按页提取图片        
        page = PDFdoc[pg]
        #增强图片分辨率
        zoom_x = 3 #水平方向
        zoom_y = 3 #垂直方向
        mat = fitz.Matrix(zoom_x, zoom_y) 
        pix = page.getPixmap(matrix=mat)  
        #按原PDF名称新建文件夹并按顺序保存图片
        if not os.path.exists(image_path+folder_name):#判断文件夹是否已存在
            os.makedirs(image_path+folder_name)#不存在则新建，存在就跳过这行
        pix.writeImage(image_path+folder_name + "\\{}.png".format(str(pg+1))) #按PDF中的页面顺序命名并保存图片


# 以上，我们先将所有待处理的PDF文件放入“PDF文件夹”，然后通过`glob.glob("PDF文件\\*.pdf")`搜索并抓取所有以".pdf"为后缀的文件，并存入变量`PDFfiles`中。结果如下所示：

# In[2]:


PDFfiles


# 然后，遍历`PDFfiles`中的所有PDF文件，使用`fitz.open()`读取。`fitz.open()`用于创建PDF文件中页面的像素映射(pixel maps)，即用像素来表示页面信息。然后按PDF文件名命名一个新的文件夹，以便储存图片。比如给“收货记录.pdf”文件建一个名字为“收货记录”的文件夹，专门储存关于它的页面的图片。随后用`for`循环，根据PDF的页数，按页提取图片。将每页的信息存入`page`变量，它的type 是`fitz.fitz.Page`，即一页像素文件。为了让图片看起来更清晰，需要增强图片的分辨率，设定图片水平及垂直方向的增强倍数，传入`Matrix`。`Matrix`用于提升即将保存的图片的分辨率，分辨率的提升倍数为`zoom_x`与`zoom_y`的乘积。倍数越大，图片越清晰，当然占用空间也越大。这个参数可根据实际要求调整。然后将`Matrix`存入`mat`，传入`getPixmap()`。`getPixmap()`用于控制图片分辨率、色域（比如生成灰度图像或带有减色方案的图像）、透明度、旋转、镜像、移位、剪切等。由于其它都不需要专门设定，所以只增强其分辨率。

# 一页图片处理好后，就需要保存图片了。先通过`os.path.exists`判断一下需要的文件夹是否存在，若不存在就通过`os.makedirs`创建。然后用`pix.writeImage`按页码编号写入并保存图片。
# ![](result.png)
