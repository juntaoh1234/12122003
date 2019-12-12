# coding=utf-8
from time import time, sleep

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from script.common import utils
from selenium import webdriver
from selenium.webdriver import ActionChains


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
        driver.find_element_by_xpath('//*[text()="财务管理"]').click()
        sleep(3)
        # 进入一级节点
        menu2 = driver.find_element_by_css_selector('span[title="应付管理"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(3)
        # 进入二级节点
        menu3 = driver.find_element_by_css_selector('li[class="bottomBar"][title="应付事项期初"]')
        actions.move_to_element(menu3)
        actions.click(menu3)
        actions.perform()

        sleep(6)
        titleName = driver.find_element_by_css_selector(
            '#home_header > div > div.tab--38iB- > ul > li > p').get_attribute('title')
        assert u"应付事项期初" in titleName, u"页面源码中不存在该关键字！"
        sleep(5)
        iframe = driver.find_element_by_id('marap-ap-oapinit')
        driver.switch_to.frame(iframe)

        driver.find_element_by_xpath('//span[text()="新 增"]/../..//i').click()
        driver.find_element_by_xpath('//li[text()="蓝字期初"]').click()
        driver.find_element_by_xpath('//*[text()="取消"]').click()
        driver.find_element_by_xpath('//*[text()="确 定"]').click()

        driver.switch_to.default_content()
        driver.find_element_by_class_name('u-button').click()
        sleep(3)
        driver.find_element_by_class_name('u-dropdown-menu-item').click()
        sleep(3)
