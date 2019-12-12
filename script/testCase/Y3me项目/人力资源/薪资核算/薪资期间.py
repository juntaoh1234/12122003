# -*-CodeIng:utf-8 -*-
# @time :2019/10/29 16:06
# @author:HuangJunTao
# @email:1341890679@qq.com
# @file:薪资期间.py
# @SoftWare:PyCharm
import random
from time import sleep

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from SRC.webdriver.switchTo import SwitchTo
from script.common import utils
from selenium.webdriver import ActionChains


class EasyCase(TestCase):
    str_regular = None

    def __init__(self, webDriver, paramsList):
        # 请不要修改该方法124421
        super(EasyCase, self).__init__(webDriver, paramsList)

    @codeException_dec('3')
    def runTest(self):
        driver = self.getDriver()
        driver.implicitly_wait(30)
        param = self.param
        tool = utils
        driver.refresh()
        # driver.find_element_by_xpath('//*[@id="_dropdown_popcontainer"]/div/i').click()
        # driver.find_element_by_xpath('//*[@id="home_header"]//div[text()="UI测试专属"]').click()
        # driver.find_element_by_xpath(
        #     '//button[@class="u-button btn__style___37bsb u8c_primary__style___RFibc  btn__style___20DQM "]').click()
        # sleep(2)
        # 左上方公共节点
        driver.find_element_by_class_name('lebra-navbar-left-icon').click()
        sleep(2)
        # 进入社交协同
        driver.find_element_by_xpath('//*[text()="人力资源"]').click()
        sleep(2)
        # 进入一级节点
        menu2 = driver.find_element_by_css_selector('span[title="薪资核算"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(2)
        # 进入二级节点
        driver.find_element_by_xpath('//li[@title="薪资期间"]').click()
        sleep(2)
        # 跳转劳动合同签订iframe
        iframe = driver.find_element_by_id('HRXC010020')
        # # driver.switch_to.frame(iframe)
        SwitchTo(driver).frame(iframe)
        sleep(2)

        # 点击新增薪资区间
        driver.find_element_by_xpath('//i[@title="新增"]').click()
        sleep(2)
        # 输入期间名称
        num = random.randint(100, 999)
        name = "期间{}".format(num)
        driver.find_element_by_xpath(
            '//label[text()="期间名称"]/following-sibling::div//input').send_keys(name)

        # 点击起始2期间右侧的按钮
        driver.find_element_by_xpath(
            '//label[text()="起始期间"]/following-sibling::div//span[@class = "el-input__prefix"]').click()
        sleep(1)
        # 点击选择条目
        driver.find_element_by_xpath(
            '//a[text()="一月"]').click()

        # 输入描述信息
        driver.find_element_by_xpath('//textarea').send_keys("描述信息")

        # 点击保存
        driver.find_element_by_xpath('//div[@class = "salary-duration-card-button"]//button[2]').click()
        sleep(0.1)
        # self.assertEqual("保存成功",driver.find_element_by_xpath('//p[text()="保存成功"]').text)
        self.assertIn(name, driver.page_source)
        # print(driver.page_source)
        sleep(2)
        # 生成薪资期间明细
        driver.find_element_by_xpath('//span[text()="生成"]').click()
        sleep(0.5)
        self.assertEqual("生成成功", driver.find_element_by_xpath('//p[text()="生成成功"]').text)
        sleep(2)
        # 关闭当前页面
        driver.switch_to.default_content()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()