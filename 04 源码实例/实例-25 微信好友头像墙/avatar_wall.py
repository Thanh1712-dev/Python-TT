import os
import math

import wxpy  # 通过程序操作微信
from PIL import Image
from PIL import ImageFile


class AvatarWall(object):

    def __init__(self, dir_name="avatars", img_name="avatar_wall.jpg", img_size=2400):
        # 当前路径作为根路径
        self.path = os.getcwd()
        self.avatar_dir = os.path.join(self.path, dir_name)
        # 通过机器人对象获取微信号好友列表
        self.bot = wxpy.Bot()
        self.friends = self.bot.friends(update=True)
        self.image_name = img_name
        self.image_size = img_size

    # def get_friends(self):
    #     """获取当前微信号的好友列表"""
    #     return self.wechat.friends(update=True)

    def save_avatars(self):

        self.bot.enable_puid(os.path.join(self.path, "wxpy_puid.pkl"))
        self.bot.enable_puid()
        if not os.path.exists(self.avatar_dir):
            os.mkdir(self.avatar_dir)
        for friend in self.friends:
            try:
                name = friend.name
                friend.get_avatar(save_path=os.path.join(self.avatar_dir, name+".jpg"))
            except FileNotFoundError:
                name = friend.puid
                friend.get_avatar(save_path=os.path.join(self.avatar_dir, name + ".jpg"))
            print("已经存储好友{}的头像".format(name))
        print("您共有{}位微信好友, 头像已经全部存储到{}路径下".format(len(self.friends), self.avatar_dir))

    def generate_avatar_wall(self):
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        # x, y方向上照片的个数, 要是多出一行可以手动减一
        x_count = y_count = math.ceil(math.sqrt(len(self.friends)))
        item_size = math.floor(self.image_size/math.floor(math.sqrt(len(self.friends))))
        # 只接受int 类型的size
        avatar_image = Image.new("RGB", (x_count*item_size, y_count*item_size))
        avatars = os.listdir(self.avatar_dir)
        x = y = 0
        for avatar in avatars:
            avatar_path = os.path.join(self.avatar_dir, avatar)
            try:
                item = Image.open(avatar_path)
            except IOError:
                continue
            else:
                item = item.resize((item_size, item_size))
                avatar_image.paste(item, (x*item_size, y*item_size))
                x += 1
                # 进入下一行
                if x == x_count:
                    x = 0
                    y += 1
        avatar_image.save(os.path.join(self.path, self.image_name))
        print("好友头像墙已生成, 存储在{}目录下,快去看看吧".format(self.path))


if __name__ == '__main__':
    aw = AvatarWall()
    aw.save_avatars()
    aw.generate_avatar_wall()
    # 退出微信网页端
    aw.bot.logout()
