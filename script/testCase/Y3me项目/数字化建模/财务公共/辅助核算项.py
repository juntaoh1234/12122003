# -*-CodeIng:utf-8 -*-
# @time :2019/11/23 13:26
# @author:HuangJunTao
# @email:1341890679@qq.com
# @file:辅助核算项.py
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
        menu3 = driver.find_element_by_css_selector('li[class="bottomBar"][title="辅助核算项"]')
        actions.move_to_element(menu3)
        actions.click(menu3)
        actions.perform()

        sleep(2)
        titleName = driver.find_element_by_css_selector(
            '#home_header > div > div.tab--38iB- > ul > li > p').get_attribute('title')
        assert u"辅助核算项" in titleName, u"页面源码中不存在该关键字！"
        sleep(2)
        iframe = driver.find_element_by_id('setting_multidimension')
        driver.switch_to.frame(iframe)
        sleep(1)

        # 点击新增
        driver.find_element_by_xpath('//button[text()="新增"]').click()
        sleep(1)
        # 点击输入编码
        code = random.randint(999, 10000)
        driver.find_element_by_xpath(
            '//input[@placeholder="请输入编码"]/ancestor::tr//td[3]//input').send_keys(code)

        # 输入名称\
        num = random.randint(999, 10000)
        name = '名称{}'.format(num)
        driver.find_element_by_xpath('//input[@placeholder="请输入编码"]/ancestor::tr//td[4]//input').send_keys(name)

        # 点击来源档案
        driver.find_element_by_xpath('//input[@placeholder="请输入编码"]/ancestor::tr//td[5]//div[text()="请选择来源档案"]').click()
        sleep(1)

        # 点击第一个条目
        driver.find_element_by_xpath('//ul[@role="listbox"]/li[1]').click()
        sleep(1)
        ele = driver.find_element_by_xpath('//input[@placeholder="请输入编码"]/ancestor::tr//td[5]'.format(name))
        action = ActionChains(driver)
        action.move_to_element(ele)
        action.perform()
        # 点击保存
        driver.find_element_by_xpath(
            '//input[@placeholder="请输入编码"]/ancestor::tr//td[6]//span[text()="保存"]').click()
        sleep(2)
        # 断言
        self.assertIn(name, driver.page_source)

        # 点击编辑
        driver.find_element_by_xpath('//span[text()="{}"]/ancestor::tr//label//input'.format(name)).click()
        ele = driver.find_element_by_xpath('//span[text()="{}"]/ancestor::tr//label//input'.format(name))
        action = ActionChains(driver)
        action.move_to_element(ele)
        action.perform()

        # 点击编辑
        driver.find_element_by_xpath('//span[text()="{}"]/ancestor::tr//span[text()="编辑"]'.format(name)).click()
        sleep(1)

        # 点击保存
        driver.find_element_by_xpath(
            '//input[@placeholder="请输入编码"]/ancestor::tr//td[6]//span[text()="保存"]').click()

        # 点击删除
        driver.find_element_by_xpath('//button[text()="删除"]').click()
        sleep(1)

        # 点击确定
        driver.find_element_by_xpath('//button[text()="确定"]').click()

        # 新增一条数据********************************************************************
        # 点击新增
        driver.find_element_by_xpath('//button[text()="新增"]').click()
        sleep(1)
        # 点击输入编码
        code = random.randint(999, 10000)
        driver.find_element_by_xpath(
            '//input[@placeholder="请输入编码"]/ancestor::tr//td[3]//input').send_keys(code)

        # 输入名称\
        num = random.randint(999, 10000)
        name = '名称{}'.format(num)
        driver.find_element_by_xpath('//input[@placeholder="请输入编码"]/ancestor::tr//td[4]//input').send_keys(name)

        # 点击来源档案
        driver.find_element_by_xpath('//input[@placeholder="请输入编码"]/ancestor::tr//td[5]//div[text()="请选择来源档案"]').click()
        sleep(1)

        # 点击第一个条目
        driver.find_element_by_xpath('//ul[@role="listbox"]/li[1]').click()
        sleep(1)
        ele = driver.find_element_by_xpath('//input[@placeholder="请输入编码"]/ancestor::tr//td[5]'.format(name))
        action = ActionChains(driver)
        action.move_to_element(ele)
        action.perform()
        # 点击保存
        driver.find_element_by_xpath(
            '//input[@placeholder="请输入编码"]/ancestor::tr//td[6]//span[text()="保存"]').click()
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
