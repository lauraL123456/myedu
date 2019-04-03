

from selenium import webdriver
import time
import os
import random

from Common.Assert import Assertions
# from Common.baseui111 import *
from Common.baseui import baseUI

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
        # # 点击商品
        # base.click('点击商品',"//span[contains(text(),'商品')]")
        # # 点击添加商品
        # base.click('点击添加商品',"//span[contains(text(),'添加商品')]")
        # # 点击商品分类_下拉框
        # base.click('点击商品分类',"//span[@class='el-cascader__label']")
        # #选择下拉框_服装
        # base.click('选择服装',"//li[contains(text(),'服装')]")
        # # 选择下拉框_服装_外套
        # base.click('选择外套',"//li[contains(text(),'外套')]")
        # # 输入商品名称
        # base.send_keys('输入商品名称',"//label[contains(text(),'商品名称：')]/following-sibling::div//input",'海澜之家')
        # # 副标题
        # base.send_keys('副标题',"//label[contains(text(),'副标题：')]/following-sibling::div//input",'海澜')
        # # 商品品牌
        # base.click('商品品牌',"//input[@placeholder='请选择品牌']")
        # # 选择品牌_海澜之家
        # base.click('选择品牌',"//span[contains(text(),'海澜之家')]")
        # # 点击查询搜索
        # base.click('点击查询搜索',"//span[contains(text(),'下一步，填写商品促销')]")
        #
        # # 赠送积分
        # base.send_keys('输入赠送积分',"//label[contains(text(),'赠送积分：')]/following-sibling::div//input",100)
        # # 赠送成长值
        # base.send_keys('输入赠送成长值',"//label[contains(text(),'赠送成长值：')]/following-sibling::div//input",101)
        # # 积分购买限制
        # base.send_keys('输入积分购买限制',"//label[contains(text(),'积分购买限制：')]/following-sibling::div//input",1000)
        # # 预告商品
        # base.click('选择预告商品',"//label[contains(text(),'预告商品：')]/following-sibling::div//span")
        # # 商品上架
        # base.click('商品上架',"//label[contains(text(),'商品上架：')]/following-sibling::div//span")
        # # 商品推荐
        # base.click('新品',"(//span[contains(text(),'新品')]/following-sibling::div/span)[2]")
        # # 服务保证
        # base.click('选择服务保证',"//span[contains(text(),'免费包邮')]")
        # # 详细页标题
        # base.send_keys('详细页标题',"//label[contains(text(),'详细页标题：')]/following-sibling::div//input",'标题')
        # # 详细页描述
        # base.send_keys('详细页描述',"//label[contains(text(),'详细页描述：')]/following-sibling::div//input",'海澜之家')
        # # 商品关键字
        # base.send_keys('商品关键字',"//label[contains(text(),'商品关键字：')]/following-sibling::div//input",'海')
        # # 商品备注
        # base.send_keys('商品备注',"//label[contains(text(),'商品备注：')]/following-sibling::div//textarea",'之家')
        # # 点击优惠券方式
        # base.click('点击优惠券方式',"//span[contains(text(),'无优惠')]")
        # # 下一步,填写商品属性
        # base.click('点击下一步',"//span[contains(text(),'下一步，填写商品属性')]")
        #
        # # 点击商品属性类型
        # base.click('点击商品属性类型',"//label[contains(text(),'属性类型')]/following-sibling::div//input")
        # # 点击商品属性类型___T恤
        # base.click('点击服装-T恤',"//span[contains(text(),'服装-T恤')]")
        # # 点击商品规格_输入增加颜色
        # base.send_keys('增加颜色',"//label[contains(text(),'商品规格：')]/following-sibling::div//input",'red')
        # # 点击商品规格_输入增加颜色_点击增加
        # base.click('点击增加',"//span[contains(text(),'增加')]")
        # # 点击选择尺寸"M"
        # base.click('点击尺寸',"//span[contains(text(),'M')]")
        # # 填写商品编号
        # base.send_keys('填写商品编号',"//div[contains(text(),'商品编号:')]/following-sibling::div/input",1314)
        # # 点击适用季节
        # base.click('点击适用季节',"//div[contains(text(),'适用季节:')]/following-sibling::div//input")
        # # 点击适用季节_夏季
        # base.click('点击夏季',"//span[contains(text(),'夏季')]")
        # # 点击适用人群
        # base.click('点击适用人群',"//div[contains(text(),'适用人群:')]/following-sibling::div//input")
        # # 点击适用人群_点击儿童
        # base.click('点击夏季',"//span[contains(text(),'儿童')]")
        # # 点击上市时间
        # base.click('点击上市时间',"//div[contains(text(),'上市时间:')]/following-sibling::div//input")
        # # 点击上市时间_2017年秋
        # base.click('点击2017年秋',"//span[contains(text(),'2017年秋')]")
        # # 点击袖长
        # base.click('点击袖长',"//div[contains(text(),'袖长:')]/following-sibling::div//input")
        # # 点击袖长_短袖
        # base.click('点击长袖',"//span[contains(text(),'长袖')]")
        # # 点击规格参数
        #
        # # 点击下一步,选择商品关联
        # base.click('点击下一步',"//span[contains(text(),'下一步，选择商品关联')]")

        # 营销_优惠券列表_第一个编辑
        # 点击营销
        base.click('点击营销',"//span[contains(text(),'营销')]")
        # 点击优惠券列表
        base.click('点击优惠券列表',"//span[contains(text(),'优惠券列表')]")
        # 点击第一条_编辑
        base.click('点击编辑',"//span[contains(text(),' 编辑')]")
        # 点击选择优惠券类型
        base.click('点击选择优惠券类型',"//label[contains(text(),'优惠券类型：')]/following-sibling::div//input")
        # 点击选择全场赠券
        base.click('点击选择全场赠券',"//span[contains(text(),'全场赠券')]")
        # 输入优惠券名称
        base.send_keys('点击选择优惠券名称',"//label[contains(text(),'优惠券名称：')]/following-sibling::div//input",'通用券')
        # 点击选择适用平台
        base.click('点击选择适用平台',"//label[contains(text(),'适用平台：')]/following-sibling::div//input")
        # 点击选择全平台
        base.click('点击选择全平台',"//span[contains(text(),'全平台')]")
        # 输入总发行量
        base.send_keys('输入总发行量',"//label[contains(text(),'总发行量：')]/following-sibling::div//input",250)
        # 输入面额
        base.send_keys('输入面额',"//label[contains(text(),'面额：')]/following-sibling::div//input",250)
        # 输入没人限领
        base.send_keys('输入没人限领',"//label[contains(text(),'每人限领：')]/following-sibling::div//input",1)
        # 输入使用门槛
        base.send_keys('输入使用门槛',"//label[contains(text(),'使用门槛：')]/following-sibling::div//input",200)
        # 点击有效期
        # base.click('点击有效期',"//label[contains(text(),'有效期：')]/following-sibling::div//input")
        # 点击选择2019.4.8号
        # base.click('选择8号',"//span[contains(text(),'8')][1]")
        # 点击可使用商品_全场通用
        base.click('点击全场通用',"//label[contains(text(),'可使用商品：')]/following-sibling::div//span")
        # 输入备注内容
        base.send_keys('输入备注内容',"//label[contains(text(),'备注：')]/following-sibling::div//textarea",'满200减250')
        # 点击提交按钮
        base.click('点击提交按钮',"//span[contains(text(),'提交')]")
        # 点击确定按钮
        base.click('点击确定按钮',"//span[contains(text(),'确定')]")
        print(driver.page_source)
        text = base.get_text("获取页面展示文本","//div[@role='alert']/p")

        Assertions.assert_in_text(text,"修改成功")
        time.sleep(4)











