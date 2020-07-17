# coding=utf-8
from appium import webdriver
import time

class TestDemo:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['appPackage'] = 'com.intretech.readerx'
        desired_caps['appActivity'] = 'com.intretech.readerx.ui.WelcomeActivity'
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['newCommandTimeout'] = "2000"
        desired_caps["unicodeKeyboard"] = True  # 使用unicode编码方式发送字符串
        desired_caps["resetKeyboard"] = True  # 隐藏键盘

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def test_demo(self):
        self.driver.find_element_by_id("com.intretech.readerx:id/tv_dialog_agreement_confirm").click()  # 点击“同意”按钮
        self.driver.find_element_by_id(
            "com.intretech.readerx:id/tv_welcome_look").click()  # 点击“我先看看”com.intretech.readerx:id/tv_welcome_look
        self.driver.find_element_by_xpath("//*[@text='搜索']").click()
        sousuo = self.driver.find_element_by_id("com.intretech.readerx:id/edit_search")

        sousuo.send_keys("祖国")
        self.driver.press_keycode(66)  # 回车键
        # assert "祖国祖国多美丽" in self.driver.find_element_by_xpath("//*[@text='祖国多美丽']").text
        sousuo.clear()
        sousuo.send_keys("爸爸")
        self.driver.press_keycode(66)  # 回车键
        # assert "我的爸爸" in self.driver.find_element_by_xpath("//*[@text='我的爸爸']").text
        sousuo.clear()

        sousuo.send_keys('hhhhh')
        self.driver.press_keycode(66)  # 回车键
        time.sleep(2)
        sousuo.send_keys('中文清除')
        sousuo.clear()
        sousuo.send_keys('中文中国馆')
        self.driver.press_keycode(66)  # 回车键
        time.sleep(2)
        search_cancel = self.driver.find_element_by_id("com.intretech.readerx:id/tv_search_cancel").click()  # 取消
        self.driver.find_element_by_id("com.intretech.readerx:id/img_toolbar_main_avatar").click()  # 点击左上角头像返回登录页面
        time.sleep(2)

    def teardown(self):
        self.driver.quit()


#####为什么这个脚本有些send——keys执行不了，不报错。把内容重新复制一份执行，结果是pass，why，问题出现在哪里？


