# -*-CodeIng:utf-8 -*-
# @time :2019/11/23 13:26
# @author:HuangJunTao
# @email:1341890679@qq.com
# @file:账龄方案.py
# @SoftWare:PyCharm
# coding=utf-8
from time import time, sleep
import random

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
        sleep(1)
        # 进入财务管理
        driver.find_element_by_xpath('//*[text()="财务管理"]').click()
        sleep(1)
        # 进入一级节点
        menu2 = driver.find_element_by_css_selector('span[title="财务公共"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(1)
        # 进入二级节点
        menu3 = driver.find_element_by_css_selector('li[class="bottomBar"][title="账龄方案"]')
        actions.move_to_element(menu3)
        actions.click(menu3)
        actions.perform()

        sleep(2)
        titleName = driver.find_element_by_css_selector(
            '#home_header > div > div.tab--38iB- > ul > li > p').get_attribute('title')
        assert u"账龄方案" in titleName, u"页面源码中不存在该关键字！"
        sleep(2)
        iframe = driver.find_element_by_id('marap0011')
        driver.switch_to.frame(iframe)
        sleep(1)

        # 点击新增
        driver.find_element_by_xpath('//button[@id="arap_accountagelist|btnAdd"]').click()
        sleep(1)
        # 输入名称
        num = random.randint(999, 10000)
        name = '名称{}'.format(num)
        driver.find_element_by_xpath(
            '//label[text()="名称"]/parent::div/following-sibling::div//input').send_keys(name)

        # 输入备注信息
        driver.find_element_by_xpath('//textarea').send_keys("备注信息9999")
        sleep(1)

        # 输入详细信息
        driver.find_element_by_xpath(
            '//*[@id="arap_accountage|arap_accountage_body_page_base_edit"]/div/div/div[1]/div[2]/div/div[3]/div/div/div/div[2]/div/div[1]/div/div/div/div/div').click()

        num1 = random.randint(999, 10000)
        name1 = '名称{}'.format(num1)
        driver.find_element_by_xpath(
            '//*[@id="arap_accountage|arap_accountage_body_page_base_edit"]/div/div/div[1]/div[2]/div/div[3]/div/div/div/div[2]/div/div[1]/div/div/div/div/div//input').send_keys(
            name1)

        # 输入账期
        driver.find_element_by_xpath(
            '//*[@id="arap_accountage|arap_accountage_body_page_base_edit"]/div/div/div[1]/div[2]/div/div[3]/div/div/div/div[2]/div/div[2]/div/div/div/div/div').click()

        num2 = random.randint(99, 1000)
        driver.find_element_by_xpath(
            '//*[@id="arap_accountage|arap_accountage_body_page_base_edit"]/div/div/div[1]/div[2]/div/div[3]/div/div/div/div[2]/div/div[2]/div/div/div/div/div//input').send_keys(
            num2)

        # 输入账期
        driver.find_element_by_xpath(
            '//*[@id="arap_accountage|arap_accountage_body_page_base_edit"]/div/div/div[1]/div[2]/div/div[3]/div/div/div/div[2]/div/div[3]/div/div/div/div/div').click()

        driver.find_element_by_xpath(
            '//*[@id="arap_accountage|arap_accountage_body_page_base_edit"]/div/div/div[1]/div[2]/div/div[3]/div/div/div/div[2]/div/div[3]/div/div/div/div/div//input').send_keys(
            num2 + 1)

        # 点击保存
        driver.find_element_by_xpath(
            '//button[@id="arap_accountage|btnSave"]').click()
        sleep(2)
        # 断言
        self.assertIn(name, driver.page_source)

        # 移动鼠标编辑
        ele = driver.find_element_by_xpath('//div/a[text()="{}"]'.format(name))
        action = ActionChains(driver)
        action.move_to_element(ele)
        action.perform()

        # 点击编辑
        driver.find_element_by_xpath(
            '//div/a[text()="{}"]/ancestor::div[@class="fixedDataTableRowLayout_body"]//a[text()="编辑"]'.format(name)).click()
        sleep(2)

        # 点击保存
        driver.find_element_by_xpath(
            '//button[@id="arap_accountage|btnSave"]').click()

        # 点击删除
        ele = driver.find_element_by_xpath('//div/a[text()="{}"]'.format(name))
        action = ActionChains(driver)
        action.move_to_element(ele)
        action.perform()

        driver.find_element_by_xpath(
            '//div/a[text()="{}"]/ancestor::div[@class="fixedDataTableRowLayout_body"]//a[text()="删除"]'.format(name)).click()
        sleep(1)

        # 点击确定
        driver.find_element_by_xpath('//button[@class="ant-btn ant-btn-primary ant-btn-lg"]').click()

        # 断言
        self.assertNotIn(name, driver.page_source)

        # 新增一条数据********************************************************************
        # 点击新增
        # 点击新增
        driver.find_element_by_xpath('//button[@id="arap_accountagelist|btnAdd"]').click()
        sleep(1)
        # 输入名称
        num = random.randint(999, 10000)
        name = '名称{}'.format(num)
        driver.find_element_by_xpath(
            '//label[text()="名称"]/parent::div/following-sibling::div//input').send_keys(name)

        # 输入备注信息
        driver.find_element_by_xpath('//textarea').send_keys("备注信息9999")
        sleep(1)

        # 输入详细信息
        driver.find_element_by_xpath(
            '//*[@id="arap_accountage|arap_accountage_body_page_base_edit"]/div/div/div[1]/div[2]/div/div[3]/div/div/div/div[2]/div/div[1]/div/div/div/div/div').click()

        num1 = random.randint(999, 10000)
        name1 = '名称{}'.format(num1)
        driver.find_element_by_xpath(
            '//*[@id="arap_accountage|arap_accountage_body_page_base_edit"]/div/div/div[1]/div[2]/div/div[3]/div/div/div/div[2]/div/div[1]/div/div/div/div/div//input').send_keys(
            name1)

        # 输入账期
        driver.find_element_by_xpath(
            '//*[@id="arap_accountage|arap_accountage_body_page_base_edit"]/div/div/div[1]/div[2]/div/div[3]/div/div/div/div[2]/div/div[2]/div/div/div/div/div').click()

        num2 = random.randint(99, 1000)
        driver.find_element_by_xpath(
            '//*[@id="arap_accountage|arap_accountage_body_page_base_edit"]/div/div/div[1]/div[2]/div/div[3]/div/div/div/div[2]/div/div[2]/div/div/div/div/div//input').send_keys(
            num2)

        # 输入账期
        driver.find_element_by_xpath(
            '//*[@id="arap_accountage|arap_accountage_body_page_base_edit"]/div/div/div[1]/div[2]/div/div[3]/div/div/div/div[2]/div/div[3]/div/div/div/div/div').click()

        driver.find_element_by_xpath(
            '//*[@id="arap_accountage|arap_accountage_body_page_base_edit"]/div/div/div[1]/div[2]/div/div[3]/div/div/div/div[2]/div/div[3]/div/div/div/div/div//input').send_keys(
            num2 + 1)

        # 点击保存
        driver.find_element_by_xpath(
            '//button[@id="arap_accountage|btnSave"]').click()
        sleep(2)
        # 断言
        self.assertIn(name, driver.page_source)
        driver.switch_to.default_content()

        driver.find_element_by_class_name('u-button').click()
        sleep(1)
        driver.find_element_by_class_name('u-dropdown-menu-item').click()
