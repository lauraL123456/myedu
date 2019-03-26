a = "123456"
# try 用于异常处理；如果出现异常 则执行 except 内的代码
try:
    # 判断 a 是否包含5
    assert '7' in a
    #  except 报错后执行
except:
    print('a里面没有7')
print('------')

def zuihou():
    a = "123456"
    try:
        assert '7'not in a
    except:
        print('a里面没有7')
    finally:
        print('最后----')

if __name__ == '__main__':
   zuihou()