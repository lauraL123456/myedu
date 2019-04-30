import json
# 声明一个全量 dict 变量（字典）
adict = {"name":"ysl","pwd":"123456"}
adictstr = '{"name":"syl","pwd":"123456","1":"数字1"}'

def zhuanhuanleixin():
    print(type(adictstr))
    dict_str = json.loads(adictstr)
    print(type(dict_str))
    # 打印dict_str 字典中 key 为 name 的值
    print(dict_str['name'])

def china_demo():
    loads = json.loads(adictstr)
    print(type(loads))
    json_dumps = json.dumps(loads)
    print(json_dumps)
    dumps = json.dumps(loads, ensure_ascii=False)
    print(dumps)

if __name__ == '__main__':
    # 打印adict_int 字典中 key 为 1 的值
    # print(adict_int[1])
    # 打印adict 字典
    # print(adict)
    # 删除 adict 字典中 key为name的值，key 和value都会被删除
    # adict.pop('name')
    # 打印adict 字典中 key 为 name的值
    # print(dict_str['name'])
    china_demo()
#     print(type(adict))
#     print(type(adictstr))
#
# # str --> dict
#     loads = json.loads(adictstr)
#     print(type(loads))
# # dict --> str
#     dumps = json.dump(adict)
#     print(type(dumps))