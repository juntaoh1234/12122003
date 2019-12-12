# coding=utf-8
from time import time, sleep

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from script.common import utils
from selenium import webdriver
from selenium.webdriver import ActionChains
import random


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
        driver.find_element_by_xpath('//*[text()="营销管理"]').click()
        sleep(3)
        # 进入一级节点
        menu2 = driver.find_element_by_css_selector('span[title="B2C商城"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(3)
        # 进入二级节点
        menu3 = driver.find_element_by_css_selector('li[class="bottomBar"][title="运费模板"]')
        actions.move_to_element(menu3)
        actions.click(menu3)
        actions.perform()

        sleep(6)
        titleName = driver.find_element_by_css_selector(
            '#home_header > div > div.tab--38iB- > ul > li > p').get_attribute('title')
        assert u"运费模板" in titleName, u"页面源码中不存在该关键字！"
        sleep(5)
        iframe = driver.find_element_by_id('0503')
        driver.switch_to.frame(iframe)

        # 新增
        driver.find_element_by_xpath('//a[text()=" 新 增 "]').click()
        name = random.randint(10,99)
        driver.find_element_by_xpath('//*[text()="运费模板名称:"]/..//input').send_keys("衣物{}".format(name))
        driver.find_element_by_xpath('//*[text()="首重费用:"]/..//input[@name="firstprice"]').send_keys("10")
        driver.find_element_by_xpath('//*[text()="续重费用:"]/..//input[@name="continueprice"]').send_keys("8")
        sleep(3)
        # 保存
        driver.find_element_by_xpath('//button[text()="保存"]').click()
        driver.switch_to.default_content()
        driver.find_element_by_class_name('u-button').click()
        sleep(3)
        driver.find_element_by_class_name('u-dropdown-menu-item').click()
        sleep(3)
