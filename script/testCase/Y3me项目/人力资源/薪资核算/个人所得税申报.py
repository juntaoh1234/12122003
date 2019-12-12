# -*-CodeIng:utf-8 -*-
# @time :2019/10/30 13:36
# @author:HuangJunTao
# @email:1341890679@qq.com
# @file:个人所得税申报.py
# @SoftWare:PyCharm

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
        driver.find_element_by_xpath('//li[@title="个人所得税申报"]').click()
        sleep(2)
        # 跳转劳动合同签订iframe
        iframe = driver.find_element_by_id('HRXC040010')
        # # driver.switch_to.frame(iframe)
        SwitchTo(driver).frame(iframe)
        sleep(2)

        # 点击组织右侧的按钮
        driver.find_element_by_xpath('//*[@id="c10"]/div/span/span/span/i[2]').click()

        # 选择组织
        driver.find_element_by_xpath('//span[text()="仓储中心-北京"]').click()

        # 点击确定
        driver.find_element_by_xpath('//div[@class="op-button"]/button[2]').click()

        # 点击纳税期间按钮
        driver.find_element_by_xpath('//input[@placeholder="纳税期间"]/following-sibling::span[1]/i').click()
        sleep(1)

        # 选择纳税期间
        driver.find_element_by_xpath('//a[text()="十二月"]').click()

        # 点击生成申请表
        driver.find_element_by_xpath('//span[text()="生成申请表"]').click()
        # 关闭当前页面
        driver.switch_to.default_content()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()