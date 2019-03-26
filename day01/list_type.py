def list_demo():
    alist = [4,'ysl', 6,7,8,9,0,5]
    print(alist)
    # 通过引索访问 元素
    print(alist[0])
    print(alist[1])

    #倒序访问
    print(alist[-1])
    print(alist[-2])

    # 更新列表中的元素
def list_update(alist):
    alist[0] = 1
    print(alist[0])
    print(alist)

# 切片操作
def list_update1(alist):
    print(alist[2:5])
    print(alist[:5])
    print(alist[3:])

def int_demo():
    int = 1
    aint = 2
    print(int, aint)
    print(1+2)
# 默认末尾加值
def reverse_demo():
    alist.reverse()
    print(alist)
    # alist.append(888)
    # print(alist)
if __name__ == '__main__':
    alist = [4,'ysl',6,7,8,9,0,5]
    list_update1(alist)
    int_demo()
    alist.append(888)
    print(alist)