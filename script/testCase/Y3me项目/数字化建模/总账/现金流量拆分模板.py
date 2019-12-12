# coding=utf-8
from time import time, sleep

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from script.common import utils
from selenium import webdriver
from selenium.webdriver import ActionChains
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
        WebDriverWait(driver, 10, 0.3).until(
            ec.visibility_of(driver.find_element_by_class_name('lebra-navbar-left-icon')))
        driver.find_element_by_class_name('lebra-navbar-left-icon').click()
        # 进入财务管理
        WebDriverWait(driver, 10, 0.3).until(
            ec.visibility_of(driver.find_element_by_xpath('//*[text()="财务管理"]')))
        driver.find_element_by_xpath('//*[text()="财务管理"]').click()
        WebDriverWait(driver, 10, 0.3).until(
            ec.visibility_of(driver.find_element_by_css_selector('span[title="总账"]')))
        # 进入一级节点
        menu2 = driver.find_element_by_css_selector('span[title="总账"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        WebDriverWait(driver, 10, 0.3).until(
            ec.visibility_of(driver.find_element_by_css_selector('li[class="bottomBar"][title="现金流量拆分模板"]')))
        # 进入二级节点
        menu3 = driver.find_element_by_css_selector('li[class="bottomBar"][title="现金流量拆分模板"]')
        actions.move_to_element(menu3)
        actions.click(menu3)
        actions.perform()

        WebDriverWait(driver, 10, 0.3).until(
            ec.visibility_of(driver.find_element_by_css_selector(
                '#home_header > div > div.tab--38iB- > ul > li > p')))
        titleName = driver.find_element_by_css_selector(
            '#home_header > div > div.tab--38iB- > ul > li > p').get_attribute('title')
        assert u"现金流量拆分模板" in titleName, u"页面源码中不存在该关键字！"
        WebDriverWait(driver, 10, 0.3).until(
            ec.visibility_of(driver.find_element_by_id('cashflowsplitmould')))
        iframe = driver.find_element_by_id('cashflowsplitmould')
        driver.switch_to.frame(iframe)

        # 查询
        WebDriverWait(driver, 10, 0.3).until(
            ec.visibility_of(driver.find_element_by_xpath('//*[text()="新增"]')))
        driver.find_element_by_xpath('//*[text()="新增"]').click()

        # 输入编码
        num = random.randint(999, 10000)
        code = '编码{}'.format(num)
        WebDriverWait(driver, 10, 0.3).until(
            ec.visibility_of(driver.find_element_by_xpath('//label[text()="编码"]/following-sibling::div//input')))
        driver.find_element_by_xpath('//label[text()="编码"]/following-sibling::div//input').send_keys(code)

        # 输入名称
        num1 = random.randint(999, 10000)
        name = '现金流量类型{}'.format(num1)
        WebDriverWait(driver, 10, 0.3).until(
            ec.visibility_of(driver.find_element_by_xpath('//label[text()="名称"]/following-sibling::div//input')))
        driver.find_element_by_xpath('//label[text()="名称"]/following-sibling::div//input').send_keys(name)

        # 输入优先级
        WebDriverWait(driver, 10, 0.3).until(
            ec.visibility_of(driver.find_element_by_xpath('//label[text()="优先级"]/following-sibling::div//input')))
        num2 = random.randint(199, 299)
        driver.find_element_by_xpath('//label[text()="优先级"]/following-sibling::div//input').send_keys(num2)

        # 点击主科目右侧的按钮
        WebDriverWait(driver, 10, 0.3).until(
            ec.visibility_of(driver.find_element_by_xpath(
                '//label[text()="主科目"]/following-sibling::div//span[@class="input-group-addon cursor-style"]')))
        driver.find_element_by_xpath(
            '//label[text()="主科目"]/following-sibling::div//span[@class="input-group-addon cursor-style"]').click()

        # 选择其中一个条目
        WebDriverWait(driver, 10, 0.3).until(
            ec.visibility_of(driver.find_element_by_xpath(
                '//ul[@class="dropdown-menu bootstrap-typeahead-menu dropdown-menu-justify"]/li[1]')))
        driver.find_element_by_xpath(
            '//ul[@class="dropdown-menu bootstrap-typeahead-menu dropdown-menu-justify"]/li[1]').click()

        # 输入摘要信息
        WebDriverWait(driver, 10, 0.3).until(
            ec.visibility_of(driver.find_element_by_xpath('//label[text()="摘要"]/following-sibling::div//input')))
        driver.find_element_by_xpath('//label[text()="摘要"]/following-sibling::div//input').send_keys('摘要信息00000')

        # 点击科目右侧的按钮
        WebDriverWait(driver, 10, 0.3).until(
            ec.visibility_of(driver.find_element_by_xpath(
                '//label[text()="科目"]/following-sibling::div//span[@class="input-group-addon cursor-style"]')))
        driver.find_element_by_xpath(
            '//label[text()="科目"]/following-sibling::div//span[@class="input-group-addon cursor-style"]').click()

        # 选择其中一个条目
        WebDriverWait(driver, 10, 0.3).until(
            ec.visibility_of(driver.find_element_by_xpath(
                '//ul[@class="dropdown-menu bootstrap-typeahead-menu dropdown-menu-justify"]/li[1]')))
        driver.find_element_by_xpath(
            '//ul[@class="dropdown-menu bootstrap-typeahead-menu dropdown-menu-justify"]/li[1]').click()

        # 点击保存按钮
        WebDriverWait(driver, 10, 0.3).until(ec.visibility_of(driver.find_element_by_xpath('//button[text()="保存"]')))
        driver.find_element_by_xpath('//button[text()="保存"]').click()
        self.assertIn(name, driver.page_source)

        # 点击编辑
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//span[text()="{}"]/ancestor::tr'.format(name))))

        # 鼠标移动
        ele = driver.find_element_by_xpath('//span[text()="{}"]/ancestor::tr'.format(name))
        action = ActionChains(driver)
        action.move_to_element(ele)
        action.perform()
        driver.find_element_by_xpath('//span[text()="{}"]/ancestor::tr//span[text()="编辑"]'.format(name)).click()

        # 点击保存按钮
        WebDriverWait(driver, 10, 0.3).until(ec.visibility_of(driver.find_element_by_xpath('//button[text()="保存"]')))
        driver.find_element_by_xpath('//button[text()="保存"]').click()

        # 点击删除
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//span[text()="{}"]/ancestor::tr'.format(name))))

        # 鼠标移动
        ele = driver.find_element_by_xpath('//span[text()="{}"]/ancestor::tr'.format(name))
        action = ActionChains(driver)
        action.move_to_element(ele)
        action.perform()
        driver.find_element_by_xpath('//span[text()="{}"]/ancestor::tr//span[text()="删除"]'.format(name)).click()

        # 点击确定按钮
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//button[text()="确定"]')))
        driver.find_element_by_xpath('//button[text()="确定"]').click()

        driver.switch_to.default_content()
        driver.find_element_by_class_name('u-button').click()
        WebDriverWait(driver, 10, 0.3).until(
            ec.visibility_of(driver.find_element_by_class_name('u-dropdown-menu-item')))
        driver.find_element_by_class_name('u-dropdown-menu-item').click()
