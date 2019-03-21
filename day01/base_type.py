# 注释：model  模块
# main 主要的
# print 打印
# def 声明方法
# int 整数
# demo 例子
# return 返回
# 代码的层级关系  通过 缩进来表示
# class 类，类型
# str string 字符
# 合法标识符（变量名方法名）：必须以字母或者_开头，
# 剩下的可以是字母数字，下划线，大小写敏感，不可用关键字做标识符
def int_demo():
    aint = 1
    print(aint)
    print(type(aint))

    def int_demo():
        aint = '1'
        print(aint)
        print(type(aint))

# 声明一个add 方法 参数有两个 aint，bint
def add(aint, bint):
    # 打印aint参数
    print(aint)
    # 打印bint参数
    print(bint)
    # 返回aint+bint
    return aint + bint

def sub(aint, bint):
    return aint / bint

def float_demo():
    float = 2.90
    print(float)
    print(type(float))

def str_demo():
    a=  'hello'
    b=  ' world'
    return a+b

def str_demo1():
    a= 'hello '
    b= 250
    s = str(b)
    print(s)
    print(type(s))
    print(a+s)

if __name__ == '__main__':
    # 提取变量 ctrl + alt + v
    # 调用add方法 传入1,2参数，得到返回值，赋值给result变量
    # result = add（1,2）
    # print(result)
    str_demo1()
    print(str_demo())
    # float_demo()
    # result = add(1, 2)
    # print(result)
    # b = sub(6, 2)
    # print(b)
    pass
