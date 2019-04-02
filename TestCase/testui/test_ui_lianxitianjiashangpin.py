

from selenium import webdriver
import time
import os
import random

from Common.Assert import Assertions
from Common.baseui import *


class TestFirstUIDemo:
    def test_testdemo2(self,driver):
        base = baseUI(driver)
        # # 打开浏览器
        # # 确定chromedriver.exe的位置
        # driver_path = os.path.join(os.path.dirname(__file__), "../../ChromDriver/chromedriver.exe")
        # print(driver_path)
        # driver = webdriver.Chrome(driver_path)
        # driver.maximize_window()  # 最大化浏览器
        # driver.implicitly_wait(8)  # 设置隐式时间等待
        # time.sleep(2)
        # 打开网址
        base.driver.get("http://192.168.60.132/home#/login")
        # 输入用户名
        base.send_keys('输入用户名','//input[@name="username"]','admin')
        # 输入密码
        base.send_keys('输入密码',"//input[@name = 'password']",'123456')
        # 点击登录
        base.click('点击登录',"//span[contains(text(),'登录')]")
        # 点击商品
        base.click('点击商品',"//span[contains(text(),'商品')]")
        # 点击添加商品
        base.click('点击添加商品',"//span[contains(text(),'添加商品')]")
        # 点击商品分类_下拉框
        base.click('点击商品分类',"//span[@class='el-cascader__label']")
        #选择下拉框_服装
        base.click('选择服装',"//li[contains(text(),'服装')]")
        # 选择下拉框_服装_外套
        base.click('选择外套',"//li[contains(text(),'外套')]")
        # 输入商品名称
        base.send_keys('输入商品名称',"//label[contains(text(),'商品名称：')]/following-sibling::div//input",'海澜之家')
        # 副标题
        base.send_keys('副标题',"//label[contains(text(),'副标题：')]/following-sibling::div//input",'海澜')
        # 商品品牌
        base.click('商品品牌',"//input[@placeholder='请选择品牌']")
        # 选择品牌_海澜之家
        base.click('选择品牌',"//span[contains(text(),'海澜之家')]")
        # 点击查询搜索
        base.click('点击查询搜索',"//span[contains(text(),'下一步，填写商品促销')]")

        # 赠送积分
        base.send_keys('输入赠送积分',"//label[contains(text(),'赠送积分：')]/following-sibling::div//input",100)
        # 赠送成长值
        base.send_keys('输入赠送成长值',"//label[contains(text(),'赠送成长值：')]/following-sibling::div//input",101)
        # 积分购买限制
        base.send_keys('输入积分购买限制',"//label[contains(text(),'积分购买限制：')]/following-sibling::div//input",1000)
        # 预告商品
        base.click('选择预告商品',"//label[contains(text(),'预告商品：')]/following-sibling::div//span")
        # 商品上架
        base.click('商品上架',"//label[contains(text(),'商品上架：')]/following-sibling::div//span")
        # 商品推荐
        base.click('新品',"(//span[contains(text(),'新品')]/following-sibling::div/span)[2]")
        # 服务保证
        base.click('选择服务保证',"//span[contains(text(),'免费包邮')]")
        # 详细页标题
        base.send_keys('详细页标题',"//label[contains(text(),'详细页标题：')]/following-sibling::div//input",'标题')
        # 详细页描述
        base.send_keys('详细页描述',"//label[contains(text(),'详细页描述：')]/following-sibling::div//input",'海澜之家')
        # 商品关键字
        base.send_keys('商品关键字',"//label[contains(text(),'商品关键字：')]/following-sibling::div//input",'海')
        # 商品备注
        base.send_keys('商品备注',"//label[contains(text(),'商品备注：')]/following-sibling::div//textarea",'之家')
        # 选择优惠券方式
        base.click('选择优惠券方式',"//span[contains(text(),'无优惠')]")
        # 下一步,填写商品属性
        base.click('点击下一步',"//span[contains(text(),'下一步，填写商品属性')]")




