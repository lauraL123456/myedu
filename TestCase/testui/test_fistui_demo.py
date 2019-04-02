

from selenium import webdriver
import time
import os


from Common.Assert import Assertions


class TestFirstUIDemo:

    def test_testdemo1(self):
        # 打开浏览器
        # 确定chromedriver.exe的位置
        driver_path = os.path.join(os.path.dirname(__file__), "../../ChromDriver/chromedriver.exe")
        print(driver_path)
        driver = webdriver.Chrome(driver_path)
        driver.maximize_window()  # 最大化浏览器
        driver.implicitly_wait(8)  # 设置隐式时间等待
        time.sleep(2)
        # 打开网址
        driver.get("http://192.168.60.132/home#/login")
        # 输入用户名
        username = driver.find_element_by_xpath("//input[@name='username']")
        username.clear()
        username.send_keys("admin")
        # 数据密码
        password = driver.find_element_by_xpath("//input[@name = 'password']")
        password.clear()
        password.send_keys('123456')
        # 点击登录
        login = driver.find_element_by_xpath("//span[contains(text(),'登录')]")
        login.click()
        time.sleep(2)
        # 点击营销
        login = driver.find_element_by_xpath("//span[contains(text(),'营销')]")
        login.click()
        # 点击优惠券列表
        login = driver.find_element_by_xpath("//span[contains(text(),'优惠券列表')]")
        login.click()
        #输入优惠券名称
        driver.find_element_by_xpath("//input[@placeholder='优惠券名称']")
        login.click()
        login1 = driver.find_element_by_xpath("//input[@placeholder='优惠券名称']")
        login1.send_keys('通用券')
        # 点击查询搜索
        login = driver.find_element_by_xpath("//span[contains(text(),'查询搜索')]")
        login.click()
        # 断言
        assertions = Assertions()
        assertions.assert_in_text(driver.page_source, '首页')

        # 断言
        assertions1 = Assertions()
        assertions1.assert_in_text(driver.page_source, '通用券')

        # 退出浏览器
        driver.quit()

