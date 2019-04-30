

def int_demo(aint,bint):# 传参方法
    aint_bint = aint + bint
    print(aint)
    print(bint)
    return aint_bint



if __name__ == '__main__':
    a = 6
    b = 3
    c = a + b
    print(c)
    a = int_demo(13,7)
    print(a)
# ------------------------------------------------
    list = [1,2,3,4,5,6,7,8,9,10]
    list[0] = 1   # 更新数组
    print(list[0])
    print(list[1])
    print(list[-1])
    print(list[-2])
    print(list.pop())
    print(list)
    print(list.pop(2))
    print(list)
# ------------------------------------------------------------------
    adict = {"name": "ysl", "pwd": "123456"}
    print(adict)
    # 如何取值,变量名 加[ ] ,然后中括号内放  key的名字
    print(adict['name'])
    # 删除 adict 字典 中key 为 name 的值,key 和 value 都会被删除
    adict.pop('name')
    print(adict)
    # 打印 adict 字典中的 key 为 name 的值
# -------------------------------------------------------------------
# 声明一个for 循环  ;  i: 代表循环次数 ;  range  函数,只有一个参数;
  #  5 代表 循环   从0 开始 到 4 结束(4是根据 小于5的最大整数来的)
    for i in range(5):
        print(i)
        print("hello world")
#  for :声明一个for 循环: i : 循环次数 , range 函数,有两个参数:第一个参数代表循环从3
    # (看第一个参数的 值)开始  到小于第二个参数的最大整数结束
    for i in range(3,7):
        print(i)

#声明一个for 循环: i : 循环次数 , range 函数,有三个参数:第一个参数代表循
    # 环从3(看第一个参数的 值)开始  到小于第二个参数的最大整数结束;
# 第三个参数  代表 步长 ,不写的话  每次加1 , 写几每次就加几
    for i in range(3,10,2):
        print(i)

# 之前是  递增方式  ,本次第三个参数 是负数: 那就是递减的方式
    for i in range(10,3,-1):
        print(i)
# ----------------------------------------------------
    alist = ['我','不','喜','欢','你']  # 0.1.2.3.4
    for i in range(5):
        print(alist[i])   # 会把 alist 的索引 从0 到 4 取一遍

    for i in alist:
        print(i)
# ---------------------------------------------------
    # 断言为True 不会有报错
    assert 4>2
    # 断言 为False 会报错 AssertionError
    assert 1>2




# ---------------------------------------------------------
    a = True
    if a :
        print('一生一世')
    else:
        print('我就呵呵不说话')
# ------------------------------------------------------
#     a = 0
#     # while : while(当) 条件: -->条件为True 进入循环,直到 条件为 false
#     while a <5:
#         print('hello world')
#         a += 1
# -------------------------------------------------------
   # try 用于异常处理;如果出现异常 则执行 except 内的代码 ; 不会影响后面的代码  继续执行
   # 应用场景:  用于 包裹 可能会出错的代码块
   #  try:
   #      assert '你' in astr
   #  except:
   #      print('断言没通过')
   #  print('------')
# -----------------------------------------------------------
    for i in range(5):
        print(i)
        if i == 3:
            # break 终止所有循环
            break
        print('第%s次循环最后一行代码\n'%i)
    for i in range(5):
        print(i)
        if i == 3:
            # continue 终止本次循环
            continue
        print('第%s次循环最后一行代码\n' %i)
    # \n : 换行符
    # print('aaa\nbbb')
# -----------------------------------------------------------
    