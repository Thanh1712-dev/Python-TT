# -*- coding = utf-8 -*-
# @Time : 2021/1/26 15:19
# @Author : 陈良兴
# @File : 微信表情包炸群.py
# @Software : PyCharm

# 运行程序 > 输入次数 > 回车 > 打开微信对话框 > 将鼠标放置在“发送”按钮处即可


from pynput.keyboard import Controller as KB                #控制键盘输入
from pynput.mouse import Controller,Button                  #控制鼠标点击
import time
import random


Wechat_expression = [
    "[微笑]","[撇嘴]","[色]","[发呆]","[得意]","[流泪]","[害羞]","[闭嘴]","[睡]","[大哭]","[尴尬]",
    "[发怒]","[调皮]","[呲牙]","[惊讶]","[难过]","[囧]","[抓狂]","[吐]","[偷笑]","[愉快]","[白眼]",
    "[傲慢]","[困]","[惊恐]","[憨笑]","[悠闲]","[咒骂]","[疑问]","[嘘]","[晕]","[衰]","[骷髅]","[猪头]",
    "[敲打]","[再见]","[擦汗]","[抠鼻]","[鼓掌]","[坏笑]","[右哼哼]","[鄙视]","[委屈]","[快哭了]",
    "[阴险]","[亲亲]","[可怜]","[笑脸]","[生病]","[脸红]","[破涕为笑]","[恐惧]","[失望]","[无语]",
    "[嘿哈]","[捂脸]","[奸笑]","[机智]","[皱眉]","[耶]","[吃瓜]","[加油]","[汗]","[天啊]","[Emm]",
    "[社会社会]","[旺柴]","[好的]","[打脸]","[哇]","[翻白眼]","[666]","[让我看看]","[叹气]","[苦涩]",
    "[裂开]","[嘴唇]","[爱心]","[心碎]","[拥抱]","[强]","[弱]","[握手]","[胜利]","[抱拳]","[勾引]",
    "[拳头]","[OK]","[合十]","[啤酒]","[咖啡]","[蛋糕]","[玫瑰]","[凋谢]","[菜刀]","[便便]","[月亮]",
    "[太阳]","[礼物]","[红包]","[發]","[福]","[跳跳]","[发抖]","[转圈]","[炸弹]","[庆祝]","[烟花]"
]

#键盘控制函数
def keyboardInput(string):
    keyboard = KB()
    keyboard.type(string)

#鼠标控制函数
def mouseClick():
    mouse = Controller()
    mouse.press(Button.left)
    mouse.release(Button.left)

#响应函数
def response(number):
    time.sleep(5)                          #延迟5s响应
    for i in range(number):
        sentence = random.choice(Wechat_expression)
        keyboardInput(sentence)
        mouseClick()
        time.sleep(0.4)                     #每条消息间隔0.4秒


if __name__ == "__main__":
    while True:
        print("\033[1;32m发动机已启动，随时可以出发！\033[0m")
        Num = input("\033[1;32m请输入轰炸次数：\033[0m")
        if Num.isdigit():
            response(int(Num))
            print("\033[1;33m报告长官，轰炸完毕，请求下一步作战计划！！！\033[0m")
        else:
            print("\033[1;31m输入错误，请重新输入一个整数！！！\033[0m")

        #询问是否继续
        answer = input("\033[1;34m是否执行下一次作战计划？(y 或者 n)：\033[0m")
        if answer == "y":
            print("\033[1;33m继续轰炸！！！\033[0m")
            continue
        if answer == "n":
            print("\033[1;33m停止轰炸，给他们喘口气！！！\033[0m")
            break
        else:
            print("\033[1;31m输入错误，请输入“y”或者“n”!!!\033[0m")