import requests
import os
# 文本处理 三种方法
# CSS 选择器  Xpath  处理结构化数据  re正则表达式  处理非结构化数据
from lxml import etree
from urllib.request import urlretrieve


url = 'http://www.htqyy.com/'
# 获取页面源代码
def get_page(url):
    response = requests.get(url)
    html = response.text
    # print(html)
    return html

# 打包成一个可以用xpath语法处理的对象
def parse_text(text):
    html = etree.HTML(text)
    return html

# 针对首页写首页的解析语法
def html_index(html):
    # // 选取所有的节点
    urls = html.xpath('//ul[@class="tagList clearfix"]/li/a/@href')
    # print(urls)
    all_url = []
    for i in urls:
        # 完整的URL
        new_url = url + i
        all_url.append(new_url)
    return all_url
    # print(all_url)

# 解析列表页面
def parse_list_page(list_html):
    # 提取音乐编号
    music_num = list_html.xpath('//span[@class="title"]/a/@sid')
    # 提取音乐名字
    music_name = list_html.xpath('//span[@class="title"]/a/@title')
    # print(music_name)
    music_url = []
    for num in music_num:
        url = 'http://f2.htqyy.com/play7/%s/mp3/5'%num
        # print(url)
        music_url.append(url)
    music_dict = dict(zip(music_name,music_url))
    # print(music_dict)
    return music_dict

def down_music(name,down_url):
    try:
        urlretrieve(down_url,'./music/%s.mp3'%name)
    except:
        print("下载出错")

def main():
    text = get_page(url)
    html = parse_text(text)
    all_url = html_index(html)
    # print(html)
    for i in all_url:
        list_page = get_page(i)
        list_html = parse_text(list_page)
        music_dict = parse_list_page(list_html)
        for name in music_dict:
            # print(name)
            # print(music_dict[name])
            print("正在下载:%s"%name)
            down_url = music_dict[name]
            down_music(name,down_url)


# 如果程序在当前文件运行，就执行下面的代码
if __name__ == '__main__':
    main()














