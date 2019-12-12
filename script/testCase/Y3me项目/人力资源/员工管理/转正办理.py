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
        driver.find_element_by_xpath('//li[@title="转正办理"]').click()

        sleep(2)
        # 跳转转正办理iframe
        iframe = driver.find_element_by_id('HRGXFW040')
        # # driver.switch_to.frame(iframe)
        SwitchTo(driver).frame(iframe)
        sleep(2)

        # 点击试用期转正
        driver.find_element_by_xpath('//*[@id="common-btn"]/button[text()="试用期转正"]').click()

        sleep(2)

        # 点击转正员工输入框

        driver.find_element_by_xpath('//*[@id="20180730174750cYVuonidOU"]').send_keys(Name.random_name)
        # driver.find_element_by_xpath('//*[@id="20180730174750cYVuonidOU"]').send_keys("戴英")
        print(Name.random_name)
        setattr(Name, "random_name", None)
        driver.find_element_by_xpath('//*[@id="20180730174750cYVuonidOU"]').click()
        sleep(5)
        driver.find_element_by_xpath('//*[@id="20180730174750cYVuonidOU"]').send_keys(Keys.ENTER)

        # 点击提交按钮
        sleep(3)
        driver.find_element_by_xpath('//*[@id="save2"]/span').click()
        sleep(2)
        # 关闭当前页面
        driver.switch_to.default_content()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()