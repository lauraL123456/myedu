# 导入 requests 第三方包
import requests

def req_demo():
    # 封装请求参数
    data = {"username": "admin", "password": "123456"}
    # 发送请求  带上两个参数 url 和 请求正文 json
    response = requests.post(url = 'http://192.168.60.132:8080/admin/login',json=data)

    text_body = response.text
    print(type(text_body))
    print(text_body)

    json_body = response.json()
    print(type(json_body))
    print(json_body)
    # 断言响应码
    assert 200 == response.status_code
    # 断言响应内容,,,字符串用in
    assert '成功' in json_body['message']
    # 断言响应正文的  code  值
    assert 200 == json_body['code']

    data_dict = json_body['data']
    token_head = data_dict['tokenHead']
    token_ = data_dict['token']
    head = {'Authorization': token_head+token_}

    response1 = requests.get(url='http://192.168.60.132:8080/admin/info',headers = head)
    print(response1.text)

    assert 200 == response1.status_code
    # 第一种 get 请求 直接将参数放入 url
    requests_get = requests.get('http://192.168.60.132:8080/brand/list?pageNum=1&pageSize=100',headers = head)
    # 第二种 get 请求,将参数 封装成一个 字典,请求的时候制定 params = 参数,将封装的字典传给这个参数
    param = {'pageNum':1,'pageSize':3}
    get1 = requests.get('http://192.168.60.132:8080/brand/list',params=param,headers=head)
    print(get1.text)
    # 获取 字典格式 的 响应正文
    json = get1.json()
    json_data_ = json['data']
    list_ = json_data_['list']
    for i in list_:
        print(i)

if __name__ == '__main__':
    req_demo()



