import json
adictstr = '{"name":"syl","pwd":"123456","1":"数字1"}'
def china_demo():
    loads = json.loads(adictstr)
    # print(json_dumps)
    dumps = json.dumps(loads,ensure_ascii=False)
    print(dumps)

def jisuan(a,b):
    a = 10
    b = 5
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a % b)

if __name__ == '__main__':
    china_demo()
    # a = 10
    # b = 3
    # c = 10
    # print(a > b)
    # print(a < b)
    # print(a == b)
    # print(a == c)
    # print(a >= b)
    # print(a <= b)
    # print(a != b)
    #
    # print(a + b)
    # print(a - b)
    # print(a * b)
    # print(a / b)
    # print(a % b) #  % 代表取余
    a = 10
    a+=1 # a = a+1
    print(a)
    a*=2 # a = a*2
    print(a)
    a-=5 # a = a-5
    print(a)
    a/=2 # a = a/2
    print(a)