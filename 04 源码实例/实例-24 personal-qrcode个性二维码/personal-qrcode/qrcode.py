from MyQR import myqr
import os


def get_img_qrcode(words, save_name, picture, colorized=True):
    if save_name[-3:] in ["jpg", "png", "gif"]:
        if picture[-3:] in ["png", "jpg", "gif"]:
            myqr.run(
                words=words,
                picture=picture,
                colorized=colorized,
                save_name=save_name
            )
            print("已生成图片二维码，存储至%s" % save_name)
        else:
            raise AttributeError("不支持的图片格式\t%s" % picture[-3:])
    else:
        raise AttributeError("二维码不支持保存为%s格式" % save_name[-3:])


def get_simple_qrcode(words, save_name):
    if save_name[-3:] in ["jpg", "png"]:
        myqr.run(
            words=words,
            save_name=save_name
        )
        print("已生成简单二维码，存储至%s" % save_name)
    else:
        raise AttributeError("二维码不支持保存为%s格式" % save_name[-3:])


if __name__ == '__main__':
    url = "https://git.forchange.cn/liyi"
    if not os.path.isdir("img_qrcode"):
        os.mkdir("img_qrcode")

    for root, dirs, files in os.walk("logo"):
        for file in files:
            get_img_qrcode(
                words=url,
                save_name="img_qrcode/qrcode_"+file,
                picture=os.path.join(root, file),
                colorized=True
            )