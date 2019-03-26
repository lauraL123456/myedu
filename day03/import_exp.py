import os

def os_demo():
    # 获取当前目录的路径
    getcwd = os.getcwd()
    print(getcwd)
    # 获取上级目录的路径
    abspath = os.path.abspath('..')
    print(abspath)
    # 获取上上级目录的路径
    abspath1 = os.path.abspath('../..')
    print(abspath1)
if __name__ == '__main__':
    os_demo()
    pass