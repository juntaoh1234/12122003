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
        menu3 = driver.find_element_by_css_selector('li[class="bottomBar"][title="会计科目"]')
        actions.move_to_element(menu3)
        actions.click(menu3)
        actions.perform()

        sleep(2)
        titleName = driver.find_element_by_css_selector(
            '#home_header > div > div.tab--38iB- > ul > li > p').get_attribute('title')
        assert u"会计科目" in titleName, u"页面源码中不存在该关键字！"
        sleep(2)
        iframe = driver.find_element_by_id('setting_accsubject')
        driver.switch_to.frame(iframe)
        sleep(1)

        # 点击会计主体
        driver.find_element_by_xpath(
            '//span[text()="会计主体"]/parent::div/following-sibling::div[1]//span[@class="Select-arrow-zone iconfont icon-chevron-down"]').click()

        # 选择条目
        driver.find_element_by_xpath('//div[text()="企业账号级"]').click()

        # 点击科目表右侧按钮
        driver.find_element_by_xpath(
            '//span[text()="科目表"]/parent::div/following-sibling::div[1]//span[@class="Select-arrow-zone iconfont icon-chevron-down"]').click()

        # 选择条目第一条
        driver.find_element_by_xpath('//div[@role="listbox"]/div[1]').click()
        sleep(2)
        #

        # 点击科目新增
        driver.find_element_by_xpath('//button[@class="btn btn-primary mr10 iconfont noprint"]').click()
        sleep(1)

        # 输入科目编码
        num = random.randint(1000, 9999)
        driver.find_element_by_xpath('//label[text()="科目编码"]/following-sibling::div/input').send_keys(num)

        # 输入名称
        num1 = random.randint(999, 10000)
        name = '名称{}'.format(num1)
        driver.find_element_by_xpath('//label[text()="科目名称"]/following-sibling::div//input').send_keys(name)

        # 点击会计要素表右侧按钮
        driver.find_element_by_xpath(
            '//label[text()="会计要素"]/following-sibling::div//span[@class="input-group-addon cursor-style"]').click()

        # 点击条目
        driver.find_element_by_xpath('//ul[@class="dropdown-menu bootstrap-typeahead-menu dropdown-menu-justify"]/li[1]').click()

        # 点击确定按钮
        driver.find_element_by_xpath('//button[text()="确定"]').click()
        sleep(1)
        # 断言
        self.assertIn(name, driver.page_source)

        # 鼠标移动
        # 点击编辑按钮
        ele = driver.find_element_by_xpath('//span[text()="{}"]/ancestor::tr//input'.format(name))
        action = ActionChains(driver)
        action.move_to_element(ele)
        action.perform()
        driver.find_element_by_xpath('//span[text()="{}"]/ancestor::tr//input'.format(name)).click()

        # 点击编辑按钮
        driver.find_element_by_xpath('//span[text()="{}"]/ancestor::tr//span[text()="编辑"]'.format(name)).click()
        sleep(1)
        # 点击确定按钮
        driver.find_element_by_xpath('//button[text()="确定"]').click()
        # 鼠标移动
        # 点击编辑按钮
        ele = driver.find_element_by_xpath('//span[text()="{}"]/ancestor::tr//input'.format(name))
        action = ActionChains(driver)
        action.move_to_element(ele)
        action.perform()
        driver.find_element_by_xpath('//span[text()="{}"]/ancestor::tr//input'.format(name)).click()

        # 点击删除按钮
        driver.find_element_by_xpath('//span[text()="{}"]/ancestor::tr//span[text()="删除"]'.format(name)).click()
        sleep(1)
        # 点击确定
        driver.find_element_by_xpath('//button[text()="确定"]').click()

        # 新建一条数据*****************************************************************************
        # 点击科目表右侧按钮
        driver.find_element_by_xpath(
            '//span[text()="科目表"]/parent::div/following-sibling::div[1]//span[@class="Select-arrow-zone iconfont icon-chevron-down"]').click()

        # 选择条目第一条
        driver.find_element_by_xpath('//div[@role="listbox"]/div[1]').click()
        sleep(2)
        #

        # 点击科目新增
        driver.find_element_by_xpath('//button[@class="btn btn-primary mr10 iconfont noprint"]').click()
        sleep(1)

        # 输入科目编码
        num = random.randint(1000, 9999)
        driver.find_element_by_xpath('//label[text()="科目编码"]/following-sibling::div/input').send_keys(num)

        # 输入名称
        num1 = random.randint(999, 10000)
        name = '名称{}'.format(num1)
        driver.find_element_by_xpath('//label[text()="科目名称"]/following-sibling::div//input').send_keys(name)

        # 点击会计要素表右侧按钮
        driver.find_element_by_xpath(
            '//label[text()="会计要素"]/following-sibling::div//span[@class="input-group-addon cursor-style"]').click()

        # 点击条目
        driver.find_element_by_xpath(
            '//ul[@class="dropdown-menu bootstrap-typeahead-menu dropdown-menu-justify"]/li[1]').click()

        # 点击确定按钮
        driver.find_element_by_xpath('//button[text()="确定"]').click()
        sleep(1)
        # 断言
        self.assertIn(name, driver.page_source)
        sleep(1)
        # 点击打印按钮
        driver.find_element_by_xpath('//button[text()="打印"]').click()
        sleep(1)

        # 点击关闭按钮
        driver.find_element_by_xpath('//button[text()="关闭"]').click()
        driver.switch_to.default_content()

        driver.find_element_by_class_name('u-button').click()
        sleep(1)
        driver.find_element_by_class_name('u-dropdown-menu-item').click()
