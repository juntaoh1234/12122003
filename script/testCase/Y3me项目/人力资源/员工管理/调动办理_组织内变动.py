# coding=utf-8
from time import sleep

from selenium.webdriver.common.keys import Keys

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from SRC.webdriver.switchTo import SwitchTo
from script.common import utils
from selenium.webdriver import ActionChains
from SRC.param.context import Name


class EasyCase(TestCase):
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
        # driver.find_element_by_xpath('//button[@class="u-button btn__style___37bsb u8c_primary__style___RFibc  btn__style___20DQM "]').click()
        # sleep(2)
        # 左上方公共节点
        driver.find_element_by_class_name('lebra-navbar-left-icon').click()
        sleep(2)
        # 进入社交协同
        driver.find_element_by_xpath('//*[text()="人力资源"]').click()
        sleep(2)
        # 进入一级节点
        menu2 = driver.find_element_by_css_selector('span[title="员工管理"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(2)
        # 进入二级节点
        driver.find_element_by_xpath('//li[@title="调动办理"]').click()

        sleep(2)
        # 跳转调动办理iframe
        iframe = driver.find_element_by_id('HRGXFW050')
        # # driver.switch_to.frame(iframe)
        SwitchTo(driver).frame(iframe)
        sleep(2)

        # 点击试用期转正
        driver.find_element_by_xpath('//*[@id="staffchange-info-content"]//button[text()="组织内变动"]').click()

        sleep(2)

        # 点击变动原因右侧按钮
        driver.find_element_by_xpath('//*[@id="edit_20180605144300O0riJTyD6s"]/div/span[1]').click()
        sleep(1)

        # 选择变动原因
        driver.find_element_by_xpath(
            '//span[text()="变动原因"]/ancestor::div[@class="innerContainer"]//td[text()="3001003"]').click()

        # 选择生效日期
        driver.find_element_by_xpath('//*[@id="edit_20180605144233owHkX1lVku"]/div/span[1]').click()

        # 选择当前天
        # driver.find_element_by_xpath('//div[@class="u-date-panel is-visible"]//div[@class="u-date-cell current"]').click()

        driver.find_element_by_xpath('//*[@id="edit_20180605144233owHkX1lVku"]/div/div/div[1]/div/button[2]').click()

        driver.find_element_by_xpath(
            '//*[@id="edit_20180605144233owHkX1lVku"]/div/div/div[1]/div/div/div[3]/div[18]').click()

        # 个人信息选择变更人
        driver.find_element_by_xpath('//*[@id="201806051443543jFBPtjxiT"]').send_keys(Name.random_name)
        # driver.find_element_by_xpath('//*[@id="20180730174750cYVuonidOU"]').send_keys("戴英")
        print(Name.random_name)
        setattr(Name, "random_name", None)
        driver.find_element_by_xpath('//*[@id="201806051443543jFBPtjxiT"]').click()
        sleep(5)
        driver.find_element_by_xpath('//*[@id="201806051443543jFBPtjxiT"]').send_keys(Keys.ENTER)

        # 点击提交按钮
        sleep(3)
        driver.find_element_by_xpath(
            '//button[@class="btn btn-primary"]/span[@data-bind="text: editFlag.button"]').click()
        sleep(2)
        # 关闭当前页面
        driver.switch_to.default_content()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()