from configparser import RawConfigParser
from common.getpath import GetPath
import os


class ReadConfig(object):
    '''获取config文件里的配置信息'''

    def __init__(self):
        self.base_path = GetPath().base_path
        self.config_path = GetPath().get_conf()
        self.conf = RawConfigParser()  # 实例化
        self.conf.read(self.config_path, 'utf-8')  # 确认读取的config文件

    def get_config(self):
        sections = self.conf.sections()
        results = {}
        for section in sections:
            results[section] = {result[0]: result[1]
                                for result in self.conf.items(section)}
        return results

    def add_option(self, section, option, value):
        '''添加options'''
        self.conf.set(section, option, value)
        self.conf.write(open(self.config_path, 'w'))

if __name__ == "__main__":
    cookie = r"juhe_cn_session=eyJpdiI6IjE2ODdKcG9QVmZHYlRmaVwvYVVuUXJRPT0iLCJ2YWx1ZSI6IkJxVWdPRTRtdmU2ZlBWNDdnUkljaFEzRk1QcVdqbEl4bjh2UnhrY0MxMFIxUFZyS2V1TldwV1VzdENJTUF6K2p0eDROSUJhVkIrbGpCbW5lMjcwU1dnPT0iLCJtYWMiOiI0ZjVlYzlkNDQ4NjZlNjZkZDdhYjE5YTJiZjBmYjNmMzgxN2JkMDg4NTU3ZjYwNGVjZjc4OGIzYzM2ODg3ZDJkIn0%3D"
    s = "AAAAAA=dhasjwdasw"
    read_config = ReadConfig()
    read_config.add_option('GetCookies', 'Cookie', cookie)
