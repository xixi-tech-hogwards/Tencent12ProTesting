# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

"""
改造1： pytest模式
改造2： 改造成可维护的代码形态，绝对不允许有绝对路径的存在 
改造3： 将自动生成的find_element_by_**  改造成find_element(MobileBy.)
改造4： 添加断言 
"""


class TestXueQiu:
    def setup(self):
        print("setup")
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps['noReset'] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        print("teardown")
        self.driver.quit()

    def test_search(self):
        print("search")

        el1 = self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search")
        el1.click()

        el2 = self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text")
        el2.send_keys("alibaba")

        el3 = self.driver.find_element(MobileBy.XPATH, "//*[@text='阿里巴巴']")
        el3.click()

        el4 = self.driver.find_element(MobileBy.XPATH,
                                       "//*[@text='加自选']")
        el4.click()
