"""
author@liyi
date: 2019/5/5
"""

import os

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import jieba
import numpy as np
from PIL import Image


def gen_word_cloud(text, name, img_path):

    #设置停用词
    stop_words = set(STOPWORDS)
    stop_words.add("用户")
    #增加关键字
    # text = text + " " + name + "网易云"

    background_image = np.array(Image.open(img_path))
    word_cloud = WordCloud(font_path="simsun.ttf", background_color="white",
                           max_font_size=100,
                           mask=background_image, stopwords=stop_words).generate(text)

    #根据图片颜色设置文字颜色
    image_color = ImageColorGenerator(background_image)
    word_cloud.recolor(color_func=image_color)
    plt.imshow(word_cloud, interpolation='bilinear')
    #去掉坐标轴
    plt.axis("off")
    # plt.show()
    word_cloud.to_file("word-cloud-img/" + name + ".jpg")


def main():
    dir_name = os.path.dirname(__file__)
    word_cloud_imgs = os.path.join(dir_name, "word-cloud-img")
    #创建存储生成词云图片的文件夹
    if not os.path.exists(word_cloud_imgs):
        os.mkdir(word_cloud_imgs)

    files = os.listdir("comments")
    for file in files:
        with open(os.path.join(dir_name, "comments", file), mode="r", encoding="utf8") as f:
            comments = ' '.join(jieba.cut(f.read()))
            gen_word_cloud(text=comments, name=file, img_path="imgs/douyin.jpg")
            print("生成了歌曲{}的评论词云......".format(file))


if __name__ == '__main__':
    main()
