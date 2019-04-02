
import pytest

if __name__ == '__main__':
    # 调用测试框架 pytest  --alluredi : 指定 allure的目录地址 ; ../Report/xml/:实际地址
    pytest.main(['-s', '-q','--alluredir', '../Report/xml/' '.'])

    # pytest.main(['-s', '-q', '--alluredir', '../Report/xml/' '.'])