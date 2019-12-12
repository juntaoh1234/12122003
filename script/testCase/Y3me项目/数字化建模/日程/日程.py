# coding=utf-8
from time import time, sleep

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from script.common import utils
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class EasyCase(TestCase):
    def __init__(self, webDriver, paramsList):
        # 请不要修改该方法124421
        super(EasyCase, self).__init__(webDriver, paramsList)

    @codeException_dec('3')
    def runTest(self):
        driver = self.getDriver()
        param = self.param
        tool = utils
        driver.refresh()
        # 左上方公共节点
        driver.find_element_by_class_name('lebra-navbar-left-icon').click()
        sleep(3)
        # 进入财务管理
        driver.find_element_by_xpath('//*[text()="社交协同"]').click()
        sleep(3)
        # 进入一级节点
        menu2 = driver.find_element_by_css_selector('span[title="日程"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()

        sleep(6)
        titleName = driver.find_element_by_css_selector(
            '#home_header > div > div.tab--38iB- > ul > li > p').get_attribute('title')
        assert u"日程" in titleName, u"页面源码中不存在该关键字！"
        sleep(5)
        iframe = driver.find_element_by_id('XTRICHENG000000000')
        driver.switch_to.frame(iframe)

        # 创建日程
        driver.find_element_by_xpath('//div[text()="创建日程"]').click()
        driver.find_element_by_xpath('//input[@placeholder="请输入主题"]').send_keys("回归测试")
        driver.find_element_by_xpath('//input[@placeholder="添加地点"]').send_keys("用友产业园中区8号楼D306")
        driver.find_element_by_xpath('//div[@class="addMem mail-recipient-box"]/div').click()
        # 选择工作人员
        driver.find_element_by_xpath('//span[text()="本部门"]/../../label/span').click()
        # 确定
        driver.find_element_by_xpath('//span[text()="确 定"]').click()
        # 确定
        driver.find_element_by_xpath('//div[text()="确定"]').click()

        sleep(3)
        driver.switch_to.default_content()
        driver.find_element_by_class_name('u-button').click()
        sleep(3)
        driver.find_element_by_class_name('u-dropdown-menu-item').click()
        sleep(3)
