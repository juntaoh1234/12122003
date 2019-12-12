# -*-CodeIng:utf-8 -*-
# @time :2019/11/23 13:26
# @author:HuangJunTao
# @email:1341890679@qq.com
# @file:科目表.py
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
        menu3 = driver.find_element_by_css_selector('li[class="bottomBar"][title="科目表"]')
        actions.move_to_element(menu3)
        actions.click(menu3)
        actions.perform()

        sleep(2)
        titleName = driver.find_element_by_css_selector(
            '#home_header > div > div.tab--38iB- > ul > li > p').get_attribute('title')
        assert u"科目表" in titleName, u"页面源码中不存在该关键字！"
        sleep(2)
        iframe = driver.find_element_by_id('setting_subjectchart')
        driver.switch_to.frame(iframe)
        sleep(1)

        # 点击新增
        driver.find_element_by_xpath('//button[@class="btn btn-primary"]').click()
        sleep(1)
        # 点击会计主体按钮
        driver.find_element_by_xpath(
            '//label[text()="会计主体"]/following-sibling::div//span[@class="input-group-addon cursor-style"]').click()

        # 点击条目
        driver.find_element_by_xpath('//span[text()="企业账号级"]').click()

        # 输入编码
        num = random.randint(999, 10000)
        code = 'BM{}'.format(num)
        driver.find_element_by_xpath('//label[text()="编码"]/following-sibling::div//input').send_keys(code)

        # 输入名称
        num1 = random.randint(999, 10000)
        name = '名称{}'.format(num1)
        driver.find_element_by_xpath('//label[text()="名称"]/following-sibling::div//input').send_keys(name)

        # 点击会计要素表右侧按钮
        driver.find_element_by_xpath(
            '//label[text()="会计要素表"]/following-sibling::div//span[@class="input-group-addon cursor-style"]').click()

        # 点击条目
        driver.find_element_by_xpath('//span[text()="企业会计准则要素表"]').click()

        # 输入编码规则
        # num2 = random.randint(999, 10000)
        driver.find_element_by_xpath('//label[text()="科目编码规则"]/following-sibling::div//input').send_keys(34567)

        # 点击确定按钮
        driver.find_element_by_xpath('//button[@class="primary mr20 btn btn-primary"]').click()
        sleep(2)
        # 断言
        self.assertIn(name, driver.page_source)

        # 点击应用按钮
        driver.find_element_by_xpath('//button[text()="引用"]').click()
        sleep(1)
        # 点击会计主体按钮
        driver.find_element_by_xpath(
            '//label[text()="会计主体"]/following-sibling::div//span[@class="input-group-addon cursor-style"]').click()

        # 点击条目
        driver.find_element_by_xpath('//span[text()="企业账号级"]').click()

        # 点击引用科目预制表右侧按钮
        driver.find_element_by_xpath(
            '//label[text()="引用预置科目表"]/following-sibling::div//span[@class="input-group-addon cursor-style"]').click()

        # 选择条目
        driver.find_element_by_xpath('//span[text()="基准科目表"]').click()

        # 输入编码
        num = random.randint(999, 10000)
        code = 'BM{}'.format(num)
        driver.find_element_by_xpath('//label[text()="编码"]/following-sibling::div//input').send_keys(code)

        # 输入名称
        num1 = random.randint(999, 10000)
        name = '名称{}'.format(num1)
        driver.find_element_by_xpath('//label[text()="名称"]/following-sibling::div//input').send_keys(name)

        # 输入编码规则
        # num2 = random.randint(999, 10000)
        # driver.find_element_by_xpath('//label[text()="科目编码规则"]/following-sibling::div//input').send_keys(34567)

        # 点击确定按钮
        driver.find_element_by_xpath('//button[@class="primary mr20 btn btn-primary"]').click()
        sleep(2)
        # 断言
        self.assertIn(name, driver.page_source)

        # 点击打印按钮
        driver.find_element_by_xpath('//button[text()="打印"]').click()
        sleep(1)

        # 点击关闭按钮
        driver.find_element_by_xpath('//button[text()="关闭"]').click()

        driver.switch_to.default_content()

        driver.find_element_by_class_name('u-button').click()
        sleep(1)
        driver.find_element_by_class_name('u-dropdown-menu-item').click()
