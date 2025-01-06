# @ Time    : 2019/3/19 16:01
# @ Author  : JuRan
import sys
import random
import pygame
from pygame.locals import *

# 屏幕大小
WIDTH = 800
HEIGHT = 600
# 下落速度范围
SPEED = [15, 30]
# 字母大小范围
SIZE = [5, 30]
# CODE长度范围
LEN = [1, 8]


# 随机生成一个颜色
def randomColor():
	return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


# 随机生成一个速度
def randomSpeed():
	return random.randint(SPEED[0], SPEED[1])


# 随机生成一个大小
def randomSize():
	return random.randint(SIZE[0], SIZE[1])


# 随机生成一个长度
def randomLen():
	return random.randint(LEN[0], LEN[1])


# 随机生成一个位置
def randomPos():
	return (random.randint(0, WIDTH), -20)


# 随机生成一个字符串
def randomCode():
	return random.choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890')



pygame.init()			# 初始函数，使用pygame的第一步
screen = pygame.display.set_mode((WIDTH, HEIGHT))	#生成主屏幕screen；第一个参数是屏幕大小
pygame.display.set_caption('Code Rain-居然')	# 窗口命名



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)
    # screen.fill((1, 1, 1))					# 填充
    screen.fill((0, 0, 0))                      # 填充背景颜色