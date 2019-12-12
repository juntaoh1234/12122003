# -*-CodeIng:utf-8 -*-
# @time :2019/11/27 15:21
# @author:HuangJunTao
# @email:1341890679@qq.com
# @file:常用摘要.py
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
        menu3 = driver.find_element_by_css_selector('li[class="bottomBar"][title="常用摘要"]')
        actions.move_to_element(menu3)
        actions.click(menu3)
        actions.perform()

        sleep(2)
        titleName = driver.find_element_by_css_selector(
            '#home_header > div > div.tab--38iB- > ul > li > p').get_attribute('title')
        assert u"常用摘要" in titleName, u"页面源码中不存在该关键字！"
        sleep(3)
        iframe = driver.find_element_by_id('remark')
        driver.switch_to.frame(iframe)

        # 查询
        driver.find_element_by_xpath('//*[text()="新增"]').click()
        # driver.find_element_by_xpath('//*[@id="root"]//tbody/tr[1]/td[1]//input').click()
        # driver.find_element_by_xpath('//*[text()="取消"]').click()

        # 输入编码
        num = random.randint(999, 10000)
        code = '编码{}'.format(num)
        driver.find_element_by_xpath('//input[@placeholder="请输入编码"]').send_keys(code)

        # 输入摘要
        num = random.randint(999, 10000)
        message = '摘要信息{}'.format(num)
        driver.find_element_by_xpath('//input[@placeholder="请输入摘要"]').send_keys(message)

        # 鼠标移动
        ele = driver.find_element_by_xpath('//input[@placeholder="请输入摘要"]/ancestor::tr')
        actions = ActionChains(driver)
        actions.move_to_element(ele)
        actions.perform()

        # 点击保存按钮
        driver.find_element_by_xpath('//input[@placeholder="请输入摘要"]/ancestor::tr//span[text()="保存"]').click()
        sleep(2)

        self.assertIn(message, driver.page_source)
        # 鼠标移动
        ele = driver.find_element_by_xpath('//span[text()="{}"]/ancestor::tr'.format(message))
        actions = ActionChains(driver)
        actions.move_to_element(ele)
        actions.perform()

        # 点击编辑
        driver.find_element_by_xpath('//span[text()="{}"]/ancestor::tr//span[text()="编辑"]'.format(message)).click()
        sleep(1)
        # 点击保存按钮
        driver.find_element_by_xpath('//input[@placeholder="请输入摘要"]/ancestor::tr//span[text()="保存"]').click()
        # 鼠标移动
        ele = driver.find_element_by_xpath('//span[text()="{}"]/ancestor::tr'.format(message))
        actions = ActionChains(driver)
        actions.move_to_element(ele)
        actions.perform()

        # 点击删除
        driver.find_element_by_xpath('//span[text()="{}"]/ancestor::tr//span[text()="删除"]'.format(message)).click()
        sleep(1)

        # 点击确定按钮
        driver.find_element_by_xpath('//button[text()="确定"]').click()

        driver.switch_to.default_content()
        driver.find_element_by_class_name('u-button').click()
        sleep(1)
        driver.find_element_by_class_name('u-dropdown-menu-item').click()
