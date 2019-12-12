# coding=utf-8
from time import time, sleep

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from script.common import utils
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
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
        driver.find_element_by_xpath('//*[text()="财务管理"]').click()
        sleep(1)
        # 进入一级节点
        menu2 = driver.find_element_by_css_selector('span[title="费用管理"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(1)
        # 进入二级节点
        menu3 = driver.find_element_by_css_selector('li[class="bottomBar"][title="记事类型配置"]')
        actions.move_to_element(menu3)
        actions.click(menu3)
        actions.perform()

        sleep(1)
        titleName = driver.find_element_by_css_selector(
            '#home_header > div > div.tab--38iB- > ul > li > p').get_attribute('title')
        assert u"记事类型配置" in titleName, u"页面源码中不存在该关键字！"
        sleep(2)
        iframe = driver.find_element_by_id('FICO_JSLXPZ')
        driver.switch_to.frame(iframe)

        # 点击新增记账类型
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//div[text()="新增记账类型 "]')))
        driver.find_element_by_xpath('//div[text()="新增记账类型 "]').click()

        # 输入编码
        num = random.randint(999, 10000)
        code = 'BM{}'.format(num)
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//input[@placeholder="请输入编码"]')))
        driver.find_element_by_xpath('//input[@placeholder="请输入编码"]').send_keys(code)

        # 输入名称
        num1 = random.randint(999, 10000)
        name = '记账类型{}'.format(num1)
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//div[text()="名称"]/parent::div//input')))
        driver.find_element_by_xpath('//div[text()="名称"]/parent::div//input').send_keys(name)

        # 点击所属上及输入框
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//div[text()="所属上级"]/parent::div//input')))
        driver.find_element_by_xpath('//div[text()="所属上级"]/parent::div//input').click()

        # 选择一个条目
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath(
                '//ul[@class="dropdown-menu bootstrap-typeahead-menu dropdown-menu-justify"]/li[1]')))
        driver.find_element_by_xpath(
            '//ul[@class="dropdown-menu bootstrap-typeahead-menu dropdown-menu-justify"]/li[1]').click()

        # 点击保存
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//button[text()="保存"]')))
        driver.find_element_by_xpath('//button[text()="保存"]').click()

        self.assertIn(name, driver.page_source)

        # 搜索
        driver.find_element_by_xpath('//input[@placeholder="搜索"]').send_keys("交通")
        driver.find_element_by_xpath('//input[@placeholder="搜索"]').send_keys(Keys.ENTER)

        driver.switch_to.default_content()
        driver.find_element_by_class_name('u-button').click()
        sleep(1)
        driver.find_element_by_class_name('u-dropdown-menu-item').click()
