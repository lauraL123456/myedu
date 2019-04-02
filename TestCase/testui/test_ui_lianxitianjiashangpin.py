

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
        login = driver.find_element_by_xpath("//span[contains(text(),'登录')]").click()
        time.sleep(2)
        # 点击商品
        login = driver.find_element_by_xpath("//span[contains(text(),'商品')]").click()
        time.sleep(2)
        # 点击添加商品
        login = driver.find_element_by_xpath("//span[contains(text(),'添加商品')]").click()
        time.sleep(2)
        # 点击商品分类_下拉框
        login = driver.find_element_by_xpath("//span[@class='el-cascader__label']").click()
        time.sleep(2)
        #选择下拉框_服装
        login = driver.find_element_by_xpath("//li[contains(text(),'服装')]").click()
        time.sleep(2)
        # 选择下拉框_服装_外套
        login = driver.find_element_by_xpath("//li[contains(text(),'外套')]").click()
        time.sleep(2)
        # 输入商品名称
        login = driver.find_element_by_xpath("//label[contains(text(),'商品名称：')]/following-sibling::div//input").click()
        login = driver.find_element_by_xpath("//label[contains(text(),'商品名称：')]/following-sibling::div//input").send_keys('海澜之家')
        time.sleep(2)
        # 副标题
        login = driver.find_element_by_xpath("//label[contains(text(),'副标题：')]/following-sibling::div//input").click()
        login = driver.find_element_by_xpath("//label[contains(text(),'副标题：')]/following-sibling::div//input").send_keys('海澜')
        time.sleep(2)
        # 商品品牌
        login = driver.find_element_by_xpath("//input[@placeholder='请选择品牌']").click()
        time.sleep(2)
        # 选择品牌_海澜之家
        login = driver.find_element_by_xpath("//span[contains(text(),'海澜之家')]").click()
        time.sleep(2)
        # 点击查询搜索
        login = driver.find_element_by_xpath("//span[contains(text(),'下一步，填写商品促销')]").click()
        time.sleep(2)
        # 断言
        assertions = Assertions()
        assertions.assert_in_text(driver.page_source, '海澜之家')
        # 退出浏览器
        driver.quit()

