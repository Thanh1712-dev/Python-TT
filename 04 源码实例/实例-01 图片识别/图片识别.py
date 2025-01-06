##coding=utf-8
#根据肤色数量判断
from PIL import Image
basedir=r'H:\f-jc\00-fxm-tb-zy\【python】\py-0002 python源码\00-上传\03 实战小项目\Python图片识别\imag2'
import os
for filename in os.listdir(basedir):
    full_filename=os.path.join(basedir,filename)
    img = Image.open(full_filename).convert('YCbCr')
    w, h = img.size
    data = img.getdata()
    cnt = 0
    for i, ycbcr in enumerate(data):
        y, cb, cr = ycbcr
        if 86 <= cb <= 117 and 140 <= cr <= 168:
            cnt += 1
    print('%s is a porn image?:%s.'%(filename, 'Yes' if cnt > w * h * 0.3 else 'No'))
