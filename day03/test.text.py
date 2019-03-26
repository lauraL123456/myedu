# open 方法演示
def open_demo():
    text_io = open('../test.text','w+')
    text_io.write("我是小萌")

def open_demo1():
    text_io = open('../test.text', 'a+')
    text_io.write("我是小萌")

def open_demo2():
    # r 代表只读模式.不可写入
    text_io = open('../test.text', 'r')
    # 读取第一行
    readline = text_io.readline()
    print(readline)
    # 读取所有行 返回一个list 对象
    readlines = text_io.readlines()
    print(readlines)


if __name__ == '__main__':
    # 相对路径 ../test.text
    # 绝对路径 c:\Users\Administrator\venv\Scripts\python.exe
    open_demo2()
    print('hello \n world')
    pass


