# coding=utf-8
__author__ = 'lijia'

import requests, time, hashlib, urllib.request, re, os, sys

start_time = time.time()


def Schedule_cmd(blocknum, blocksize, totalsize):
    speed = (blocknum * blocksize) / (time.time() - start_time)
    speed_str = " Speed: %s" % format_size(speed)
    recv_size = blocknum * blocksize

    # 设置下载进度条
    f = sys.stdout
    pervent = recv_size / totalsize
    percent_str = "  %.2f%% total: %sM" % (pervent * 100, format_size(totalsize))
    n = round(pervent * 50)
    s = ('#' * n).ljust(50, '-')
    f.write(percent_str.ljust(8, ' ') + ' [' + s + ']\n' + speed_str)
    f.flush()


def format_size(bytes):
    try:
        bytes = float(bytes)
        kb = bytes / 1024
    except Exception:
        print("传入的字节格式不对")
        return "Error"
    if kb >= 1024:
        M = kb / 1024
        if M >= 1024:
            G = M / 1024
            return "%.3fG" % (G)
        else:
            return "%.3fM" % (M)
    else:
        return "%.3fK" % (kb)


def down_video(url, path, title):
    print("[正在下载 {},请稍等...]:".format(title))
    currentVideoPath = os.path.join(sys.path[0], 'download', path)  # 当前目录作为下载目录
    opener = urllib.request.build_opener()
    # 请求头
    opener.addheaders = [
        ('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:56.0) Gecko/20100101 Firefox/56.0'),
        ('Accept', '*/*'),
        ('Accept-Language', 'en-US,en;q=0.5'),
        ('Accept-Encoding', 'gzip, deflate, br'),
        ('Connection', 'keep-alive'),
    ]
    urllib.request.install_opener(opener)
    # 创建文件夹存放下载的视频
    if not os.path.exists(currentVideoPath):
        os.makedirs(currentVideoPath)
    # 开始下载
    file_type = url.split('.')[-1]
    urllib.request.urlretrieve(url=url, filename=os.path.join(currentVideoPath, r'{}.{}'.format(title, file_type)), reporthook=Schedule_cmd)
    print('\n>>>>>{}.{} 下载成功, 请往 {} 查看文件.'.format(title, file_type, currentVideoPath))


if __name__ == "__main__":
    file_url = 'https://jdvod.300hu.com/4c1f7a6atransbjngwcloud1oss/7e5feae095585815090434049/v.f30.mp4'
    down_video(file_url, 'file_path', 'file_name')
