import os
import sys


class GetPath(object):
    '''
    1.获取项目路径
    2.获取配置文件路径
    '''

    def __init__(self):
        # 获取项目路径
        self.base_path = os.path.split(
            os.path.realpath(
                os.path.dirname(__file__)))[0]

    def get_conf(self):
        # 获取配置文件config的路径
        config_path = os.path.join(self.base_path, 'config', 'config.ini')
        return config_path


if __name__ == "__main__":
    getpath = GetPath()
    print(getpath.base_path)
    print(getpath.get_conf())
