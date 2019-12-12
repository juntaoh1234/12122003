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
        driver.find_element_by_xpath('//*[text()="财务管理"]').click()
        sleep(1)
        # 进入一级节点
        menu2 = driver.find_element_by_css_selector('span[title="会计平台"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(1)
        # 进入二级节点
        menu3 = driver.find_element_by_css_selector('li[class="bottomBar"][title="影响因素设置"]')
        actions.move_to_element(menu3)
        actions.click(menu3)
        actions.perform()

        sleep(2)
        titleName = driver.find_element_by_css_selector(
            '#home_header > div > div.tab--38iB- > ul > li > p').get_attribute('title')
        assert u"影响因素设置" in titleName, u"页面源码中不存在该关键字！"
        sleep(1)
        iframe = driver.find_element_by_id('yxyssz')
        driver.switch_to.frame(iframe)

        # 新增
        new_button = driver.find_element_by_xpath('//button[text()="新增"]')
        driver.execute_script("arguments[0].click();", new_button)

        # 输入名称
        num1 = random.randint(999, 10000)
        name = '名称{}'.format(num1)
        driver.find_element_by_xpath('//input[@placeholder="请输入影响因素名称"]').send_keys(name)

        # 点击下拉列表
        driver.find_element_by_xpath('//div[text()="请选择对应基础档案类型"]/parent::div').click()

        # 选择第一个条目
        driver.find_element_by_xpath('//ul[@role="listbox"]/li[1]').click()

        # 输入备注信息
        driver.find_element_by_xpath('//input[@placeholder="请输入备注"]').send_keys('备注信息00000')
        ele = driver.find_element_by_xpath('//input[@placeholder="请输入备注"]')
        action = ActionChains(driver)
        action.move_to_element(ele)
        action.perform()
        # 点击保存
        driver.find_element_by_xpath('//span[text()="保存"]').click()
        sleep(2)
        # 断言
        self.assertIn(name, driver.page_source)

        # 点击编辑
        ele = driver.find_element_by_xpath('//span[text()="{}"]'.format(name))
        action = ActionChains(driver)
        action.move_to_element(ele)
        action.perform()

        # 点击编辑
        driver.find_element_by_xpath('//span[text()="{}"]/ancestor::tr//span[text()="编辑"]'.format(name)).click()
        # 点击保存
        driver.find_element_by_xpath('//span[text()="保存"]').click()
        sleep(1)
        # 点击删除
        ele = driver.find_element_by_xpath('//span[text()="{}"]'.format(name))
        action = ActionChains(driver)
        action.move_to_element(ele)
        action.perform()

        # 点击删除
        driver.find_element_by_xpath('//span[text()="{}"]/ancestor::tr//span[text()="删除"]'.format(name)).click()

        sleep(0.5)
        # 点击确定
        driver.find_element_by_xpath('//button[text()="确定"]').click()
        # 断言
        self.assertNotIn(name, driver.page_source)
        # 新增
        new_button = driver.find_element_by_xpath('//button[text()="新增"]')
        driver.execute_script("arguments[0].click();", new_button)

        # 输入名称
        num1 = random.randint(999, 10000)
        name = '名称{}'.format(num1)
        driver.find_element_by_xpath('//input[@placeholder="请输入影响因素名称"]').send_keys(name)

        # 点击下拉列表
        driver.find_element_by_xpath('//div[text()="请选择对应基础档案类型"]/parent::div').click()

        # 选择第一个条目
        driver.find_element_by_xpath('//ul[@role="listbox"]/li[1]').click()

        # 输入备注信息
        driver.find_element_by_xpath('//input[@placeholder="请输入备注"]').send_keys('备注信息00000')
        ele = driver.find_element_by_xpath('//input[@placeholder="请输入备注"]')
        action = ActionChains(driver)
        action.move_to_element(ele)
        action.perform()
        # 点击保存
        driver.find_element_by_xpath('//span[text()="保存"]').click()
        sleep(2)
        # 断言
        self.assertIn(name, driver.page_source)
        driver.switch_to.default_content()
        driver.find_element_by_class_name('u-button').click()
        sleep(1)
        driver.find_element_by_class_name('u-dropdown-menu-item').click()

