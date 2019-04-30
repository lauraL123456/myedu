import time
from Common import Assert
from Common.baseui import*
from selenium.webdriver import ActionChains



class TestFouDemo:
    def test_demo(self,driver):
        base = baseUI(driver)

        # 打开网页浏览器
        base.driver.get("http://192.168.60.132/home#/login")
        # 输入用户名
        base.send_keys('输入用户名','//input[@name="username"]','admin')
        # 输入密码
        base.send_keys('输入密码',"//input[@name = 'password']",'123456')
        # 点击登录
        base.click('点击登录',"//span[contains(text(),'登录')]")
        # 点击订单
        base.click('点击订单',"//span[contains(text(),'订单')]")
        # 点击订单列表
        base.click('点击订单列表',"//span[contains(text(),'订单列表')]")
        # 点击订单状态
        base.click('点击订单状态',"//label[contains(text(),'订单状态：')]/following-sibling::div/div")
        # 点击待发货
        base.click('待发货',"//span[contains(text(),'待发货')]")
        # 点击查询搜索
        base.click('点击查询搜索',"//span[contains(text(),'查询搜索')]")
        # 记录第一条的编号//tbody/tr[1]/td[2]/div
        num = base.get_text('获取编号',"//tbody/tr[1]/td[2]/div")
        order_num = base.get_text("获取订单编号","//tbody/tr[1]/td[3]/div")
        # 取第一个元素订单发货
        base.click('点击订单发货',"//span[contains(text(),'订单发货')]")
        # 点击配送方式
        base.click('点击配送方式',"//input[@placeholder='请选择物流公司']")
        # 点击顺丰快递
        base.click('点击顺丰快递',"//span[contains(text(),'顺丰快递')]")
        # 输入物流单号
        base.send_keys('输入物流单号',"(//input)[2]",2020161202)
        # 点击确定  提交
        base.click('点击确定',"//span[contains(text(),'确定')]")
        # 点击提示中的确定
        base.click('点击提示框中的确定',"(//span[contains(text(),'确定')])[2]")
        # 获取提示文本框
        text2 = base.get_text('获取提示框文本',"//div[@role='alert']/p")
        # 断言
        ppp = Assert.Assertions()
        ppp.assert_in_text(text2,'发货成功')
        # 点击订单状态 //label[contains(text(),'订单状态:')]/following-sibling::div//input
        base.click('点击订单状态',"//label[contains(text(),'订单状态：')]/following-sibling::div/div")
        # 点击已发货
        base.click("点击已发货","//span[text()='已发货']")
        # 输入订单编号 //input[@placeholder='订单编号']
        base.send_keys('输入订单编号',"//input[@placeholder='订单编号']",order_num)
        # 点击搜索查询
        base.click('点击搜索查询',"//span[contains(text(),'查询搜索')]")
        # 定位到刚才发货的订单
        time.sleep(1)
        # 通过xpath定位到一组元素,存到一个list
        nums = driver.find_elements_by_xpath ("(//tbody)[1]/tr/td[2]")
        # 存放是否能找到编号  找到true 没找到 false
        b = False
        # 遍历上边的list
        for n in nums:
            # n.text取出元素的可视文本
            print(n.text)
            # 判断可视文本是否与发货订单的编号相同
            if n.text == num:
                # 如果相同,就将true赋值给b
                b = True
        # 断言,订单状态转换是否正确
        assert True == b
        time.sleep(3)