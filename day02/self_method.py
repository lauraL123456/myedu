# 步长
# def list_bianli():
#     alist = ['啊','哦','你好']
#     for i in alist:
#         print("--遍历")
#     print(i)
#     print(i + '__hello')

# def nei_xunhuan():
#     for i in range(5):
#         print('hello world')
#         for j in range(2):
#             print('内循环')

# def chenfabiao():     ##九九乘法表
#     for i in range(1,10):
#         for j in range(1,i+1):
#             print('%s × %s = %s' %(i,j,i*j),end = ' ')
#         print(' ')
# 基础 id else 语法演示
def if_demo():
    a = True
    if a:
        print('a 是 对的')
    else:
        print('a 是 错的')
# 判断 a 和 b 的大小
def if_demo1():
    a = 10
    b = 20
    if a>b:
        print('a 大于 b')
    else:
        print('a 小于 b')
# 输出 比较大的值
def if_demo2():
    a = 10
    b = 20
    if a > b:
        print(a)
    else:
        print(b)

def if_lianxi():
    a = 10  # 自己练习
    b = 5
    c = 2
    d = a / b
    e = a / c
    if d > e:
        print(d)
    else:
        print(e)
    # 将 1到50 的奇数 加起来
def jishuxiangjia():
    nub = 0
    for i in range(1, 51):
        if i % 2 != 0:
            nub = nub + i
    print(nub)
# 周末作业
# 写一个方法，传入两个int参数，将两个参数之间的偶数加起来
def sum_demo(aint,bint):
    sum = 0
    if aint > bint:
        for i in range(bint,aint+1):
            if i%2 == 0:
                sum = sum + i
        print(sum)
    elif aint < bint:
        for i in range(aint,bint+1):
            if i%2 == 0:
                sum = sum + i
        print(sum)

if __name__ == '__main__':
    # chenfabiao()
    sum_demo(2,10)
    # list_bianli()
    # nei_xunhuan()
    # jishuxiangjia()
    # sum_demo(aint,bint)
