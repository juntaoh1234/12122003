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
        sleep(1)
        # 进入财务管理
        driver.find_element_by_xpath('//*[text()="人力资源"]').click()
        sleep(1)
        # 进入一级节点
        menu2 = driver.find_element_by_css_selector('span[title="人力设置"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(1)
        # 进入二级节点
        menu3 = driver.find_element_by_css_selector('li[class="bottomBar"][title="变动类型"]')
        actions.move_to_element(menu3)
        actions.click(menu3)
        actions.perform()

        sleep(1)
        titleName = driver.find_element_by_css_selector(
            '#home_header > div > div.tab--38iB- > ul > li > p').get_attribute('title')
        assert u"变动类型" in titleName, u"页面源码中不存在该关键字！"
        sleep(1)
        iframe = driver.find_element_by_id('HRSZ030020')
        driver.switch_to.frame(iframe)

        # 新增
        driver.find_element_by_xpath('//p[text()="入职"]/..//*[text()="新增"]').click()

        # 点击新增
        driver.find_element_by_xpath(
            '//p[text()="入职"]/parent::div/div//span[text()="新增"]/following-sibling::i').click()

        # 输入编码
        num = random.randint(999, 10000)
        code = "BM{}".format(num)
        driver.find_element_by_xpath(
            '//p[text()="入职"]/parent::div/div//span[text()="新增"]/parent::div/following-sibling::div//label[text()="编码"]/following-sibling::div//input').send_keys(
            code)

        # 点击离职
        # 输入名称
        num1 = random.randint(999, 10000)
        name = "BM{}".format(num1)
        driver.find_element_by_xpath(
            '//p[text()="入职"]/parent::div/div//span[text()="新增"]/parent::div/following-sibling::div//label[text()="名称"]/following-sibling::div//input').send_keys(
            name)

        # 点击保存按钮
        driver.find_element_by_xpath('//p[text()="入职"]/parent::div/div//button[2]').click()
        sleep(2)
        # 断言
        self.assertIn(name, driver.page_source)

        driver.switch_to.default_content()
        driver.find_element_by_class_name('u-button').click()
        sleep(1)
        driver.find_element_by_class_name('u-dropdown-menu-item').click()
