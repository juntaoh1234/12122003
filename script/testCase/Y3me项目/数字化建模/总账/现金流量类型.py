# -*-CodeIng:utf-8 -*-
# @time :2019/11/27 14:21
# @author:HuangJunTao
# @email:1341890679@qq.com
# @file:现金流量类型.py
# @SoftWare:PyCharm
# @company:用友集团
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
        driver.find_element_by_xpath('//*[text()="财务管理"]').click()
        sleep(1)
        # 进入一级节点
        menu2 = driver.find_element_by_css_selector('span[title="总账"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(1)
        # 进入二级节点
        menu3 = driver.find_element_by_css_selector('li[class="bottomBar"][title="现金流量类型"]')
        actions.move_to_element(menu3)
        actions.click(menu3)
        actions.perform()

        sleep(2)
        titleName = driver.find_element_by_css_selector(
            '#home_header > div > div.tab--38iB- > ul > li > p').get_attribute('title')
        assert u"现金流量类型" in titleName, u"页面源码中不存在该关键字！"
        sleep(2)
        iframe = driver.find_element_by_id('cashflowtype')
        driver.switch_to.frame(iframe)
        # 新增一条数据现金流量类型为账簿设置的前置，要保留一条数据**********************************************************
        # 点击新增
        driver.find_element_by_xpath('//*[text()="新增"]').click()
        sleep(1)
        # 点击会计主体右侧按钮
        driver.find_element_by_xpath(
            '//label[text()="会计主体"]/following-sibling::div//span[@class="input-group-addon cursor-style"]').click()
        sleep(1)
        # 点击第一条数据
        driver.find_element_by_xpath(
            '//ul[@class="dropdown-menu bootstrap-typeahead-menu dropdown-menu-justify"]/li[1]').click()

        # 输入编码
        num = random.randint(999, 10000)
        code = '编码{}'.format(num)
        driver.find_element_by_xpath('//label[text()="编码"]/following-sibling::div//input').send_keys(code)

        # 输入名称
        num1 = random.randint(999, 10000)
        name = '现金流量类型{}'.format(num1)
        driver.find_element_by_xpath('//label[text()="名称"]/following-sibling::div//input').send_keys(name)

        # 输入会计准则
        driver.find_element_by_xpath(
            '//label[text()="会计准则"]/following-sibling::div//span[@class="input-group-addon cursor-style"]').click()
        sleep(1)
        # 点击第一条数据
        driver.find_element_by_xpath(
            '//ul[@class="dropdown-menu bootstrap-typeahead-menu dropdown-menu-justify"]/li[1]').click()

        # 输入描述信息
        driver.find_element_by_xpath('//textarea').send_keys('描述信息0000000')

        # 点击确定按钮
        driver.find_element_by_xpath('//button[text()="确定"]').click()
        sleep(3)
        self.assertIn(name, driver.page_source)

        # 鼠标移动
        ele = driver.find_element_by_xpath('//span[text()="{}"]/ancestor::tr'.format(name))

        action = ActionChains(driver)
        action.move_to_element(ele)
        action.perform()

        # 点击编辑
        driver.find_element_by_xpath('//span[text()="{}"]/ancestor::tr//span[text()="编辑"]'.format(name)).click()
        sleep(1)

        # 点击确定按钮
        driver.find_element_by_xpath('//button[@class="primary mr20 btn btn-primary"]').click()
        sleep(1.5)
        # 鼠标移动
        ele = driver.find_element_by_xpath('//span[text()="{}"]/ancestor::tr'.format(name))
        action = ActionChains(driver)
        action.move_to_element(ele)
        action.perform()
        # 点击删除
        driver.find_element_by_xpath('//span[text()="{}"]/ancestor::tr//span[text()="删除"]'.format(name)).click()

        # 点击确定
        driver.find_element_by_xpath('//div[@class="modal-footer"]//button[@class="btn btn-primary"]').click()
        sleep(2)
        self.assertNotIn(name, driver.page_source)

        # 点击新增
        driver.find_element_by_xpath('//*[text()="新增"]').click()
        sleep(1)
        # 点击会计主体右侧按钮
        driver.find_element_by_xpath(
            '//label[text()="会计主体"]/following-sibling::div//span[@class="input-group-addon cursor-style"]').click()
        sleep(1)
        # 点击第一条数据
        driver.find_element_by_xpath(
            '//ul[@class="dropdown-menu bootstrap-typeahead-menu dropdown-menu-justify"]/li[1]').click()

        # 输入编码
        num = random.randint(999, 10000)
        code = '编码{}'.format(num)
        driver.find_element_by_xpath('//label[text()="编码"]/following-sibling::div//input').send_keys(code)

        # 输入名称
        num1 = random.randint(999, 10000)
        name = '现金流量类型{}'.format(num1)
        driver.find_element_by_xpath('//label[text()="名称"]/following-sibling::div//input').send_keys(name)

        # 输入会计准则
        driver.find_element_by_xpath(
            '//label[text()="会计准则"]/following-sibling::div//span[@class="input-group-addon cursor-style"]').click()
        sleep(1)
        # 点击第一条数据
        driver.find_element_by_xpath(
            '//ul[@class="dropdown-menu bootstrap-typeahead-menu dropdown-menu-justify"]/li[1]').click()

        # 输入描述信息
        driver.find_element_by_xpath('//textarea').send_keys('描述信息0000000')

        # 点击确定按钮
        driver.find_element_by_xpath('//button[text()="确定"]').click()
        sleep(3)
        self.assertIn(name, driver.page_source)
        driver.switch_to.default_content()
        driver.find_element_by_class_name('u-button').click()
        sleep(1)
        driver.find_element_by_class_name('u-dropdown-menu-item').click()
