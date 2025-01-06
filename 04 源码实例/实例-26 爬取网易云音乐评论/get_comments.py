import requests  # 网页请求
from bs4 import BeautifulSoup as Bs  #提取数据
import re #字符串匹配


def get_song_comments(song_url, post_headers, post_data, song_name):
    res = requests.post(song_url, headers=post_headers, data=post_data)
    with open(song_name, "w", encoding="utf-8") as f:
        for index, item in enumerate(res.json()["hotComments"]):
            print("用户{}\t{}\n{}".format(index+1, item["user"]["nickname"], item["content"]))
            print()
            f.writelines("用户{}\t{}\n{}\n\n".format(index+1, item["user"]["nickname"], item["content"]))
            if item["beReplied"]:
                for sub_item in item["beReplied"]:
                    print("用户{}\t{}\n{}".format("楼中楼:", sub_item["user"]["nickname"], sub_item["content"]))
                    print()
                    f.writelines("用户{}\t{}\n{}\n\n".format("楼中楼:", sub_item["user"]["nickname"], sub_item["content"]))


def get_songs(playlist_url):
    """
    :param playlist_url: 歌单url
    :return: [(song_name, song_id),]
    """
    res = requests.get(playlist_url)
    soup = Bs(res.text, "html.parser")
    result = soup.find("ul", class_="f-hide")
    link_tags = result.find_all("a")
    songs = [(item.text, re.findall(r"\d+", item["href"])[0]) for item in link_tags]
    return songs


if __name__ == '__main__':
    # 获取歌单
    play_list_id = "2768164485"
    play_list_url = "https://music.163.com/playlist?id={}".format(play_list_id)
    play_list_songs = get_songs(play_list_url)


    host = "music.163.com"
    origin = "https://www.music.163.com"
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) " \
                 "AppleWebKit/537.36(KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"

    params = "PGHaWMKZLSr/OwkYYCqVviQrjx5khzcfxPmmJtuA+CDl0PQRXKbpArS3G" \
             "Ep+wbDWYpboVs9Nu/Vc8IxTFtKQHeTimWD2GZb6UCIynnjHhtFwAz7vmPV" \
             "LCyGOjx2d9BRvVK2RBs2HYkyL+2ZZXrxya/TpnZwMopAkHwapnlRnPJadvCIiInpdsNayVgf7Zm7x"

    encSecKey = "4a15a9438e2f4736d62f8981a00f1f95b7867ed08a1a917d0e1b" \
                "ddc6298de38ed5fff7c0fe8ac81d6f62b882592b8b61aba56f0dbdf199144" \
                "5516f3c9b9c514fa45d2c1e5ea79b6f9c77e3d3e1abd54a1b1aa7eee2e6eaadefbc70eb10357b" \
                "5cae77a541f39f8f74c9b55653b52b6a955835c8c4bf31bebd7af42c6b02ee5e6f"
    data = {
        "params": params,
        "encSecKey": encSecKey
    }
    i, j = 0, 0
    for song in play_list_songs:
        song_id = song[1]
        url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token=".format(song_id)
        referer = "https://music.163.com/song?id={}".format(song_id)
        headers = {
            "Connection": "keep-alive",
            "Host": host,
            "Origin": origin,
            "referer": referer,
            "User-Agent": user_agent
        }    
        print("{}的热门评论:".format(song[0]))
        get_song_comments(url, headers, data, song[0])
        print("*"*200)
