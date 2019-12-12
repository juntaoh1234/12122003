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
        driver.find_element_by_class_name('lebra-navbar-left-icon').click()
        sleep(1)
        # 进入财务管理
        driver.find_element_by_xpath('//*[text()="财务管理"]').click()
        sleep(1)
        # 进入一级节点
        menu2 = driver.find_element_by_css_selector('span[title="固定资产"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(1)
        # 进入二级节点
        menu3 = driver.find_element_by_css_selector('li[class="bottomBar"][title="资产状态"]')
        actions.move_to_element(menu3)
        actions.click(menu3)
        actions.perform()

        sleep(1)
        titleName = driver.find_element_by_css_selector(
            '#home_header > div > div.tab--38iB- > ul > li > p').get_attribute('title')
        assert u"资产状态" in titleName, u"页面源码中不存在该关键字！"
        sleep(1)
        iframe = driver.find_element_by_id('fixedasset0003')
        driver.switch_to.frame(iframe)

        # 新增
        WebDriverWait(driver, 30, 0.5).until(ec.visibility_of(driver.find_element_by_id("at_usagestatelist|btnAdd")))
        driver.find_element_by_id("at_usagestatelist|btnAdd").click()

        # 点击取消
        WebDriverWait(driver, 30, 0.5).until(ec.visibility_of(driver.find_element_by_xpath('//*[text()="取消"]')))
        driver.find_element_by_xpath('//*[text()="取消"]').click()

        # 点击确定
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//div[@class="ant-confirm-btns"]//span[text()="确 定"]')))
        driver.find_element_by_xpath('//div[@class="ant-confirm-btns"]//span[text()="确 定"]').click()
        # # 保存
        # driver.find_element_by_id('at_fixed_param_set|btnSave').click()

        # 新增
        WebDriverWait(driver, 30, 0.5).until(ec.visibility_of(driver.find_element_by_id("at_usagestatelist|btnAdd")))
        driver.find_element_by_id("at_usagestatelist|btnAdd").click()

        # 输入名称
        num = random.randint(100, 999)
        name = '资产{}'.format(num)
        WebDriverWait(driver, 30, 0.5).until(ec.visibility_of(
            driver.find_element_by_xpath('//label[text()="名称"]/parent::div/following-sibling::div//input')))
        driver.find_element_by_xpath('//label[text()="名称"]/parent::div/following-sibling::div//input').send_keys(name)

        # 点击是否折旧按钮
        WebDriverWait(driver, 30, 0.5).until(ec.visibility_of(
            driver.find_element_by_xpath(
                '//label[text()="是否折旧"]/parent::div/following-sibling::div//label[1]/span[1]')))
        driver.find_element_by_xpath(
            '//label[text()="是否折旧"]/parent::div/following-sibling::div//label[1]/span[1]').click()

        # 点击保存按钮
        WebDriverWait(driver, 30, 0.5).until(ec.visibility_of(
            driver.find_element_by_xpath('//button/span[text()="保存"]')))
        driver.find_element_by_xpath('//button/span[text()="保存"]').click()
        sleep(2)

        # 移动鼠标
        ele = driver.find_element_by_xpath(
            '//div[text()="{}"]/ancestor::div[@class="fixedDataTableCellGroupLayout_cellGroupWrapper"]'.format(name))

        driver.execute_script('arguments[0].scrollIntoView();', ele)
        action = ActionChains(driver)
        action.move_to_element(ele)
        action.perform()

        # 点击编辑按钮

        WebDriverWait(driver, 30, 0.5).until(ec.visibility_of(
            driver.find_element_by_xpath(
                '//div[text()="{}"]/ancestor::div[@class="fixedDataTableCellGroupLayout_cellGroupWrapper"]/following-sibling::div[2]//a[text()="编辑"]'.format(
                    name))))
        driver.find_element_by_xpath(
            '//div[text()="{}"]/ancestor::div[@class="fixedDataTableCellGroupLayout_cellGroupWrapper"]/following-sibling::div[2]//a[text()="编辑"]'.format(
                name)).click()

        # 点击保存按钮
        WebDriverWait(driver, 30, 0.5).until(ec.visibility_of(
            driver.find_element_by_xpath('//button/span[text()="保存并新增"]')))
        driver.find_element_by_xpath('//button/span[text()="保存并新增"]').click()

        # 点击取消
        WebDriverWait(driver, 30, 0.5).until(ec.visibility_of(driver.find_element_by_xpath('//*[text()="取消"]')))
        driver.find_element_by_xpath('//*[text()="取消"]').click()

        # 点击确定
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//div[@class="ant-confirm-btns"]//span[text()="确 定"]')))
        driver.find_element_by_xpath('//div[@class="ant-confirm-btns"]//span[text()="确 定"]').click()

        # 移动鼠标
        ele = driver.find_element_by_xpath(
            '//div[text()="{}"]/ancestor::div[@class="fixedDataTableCellGroupLayout_cellGroupWrapper"]'.format(name))
        action = ActionChains(driver)
        action.move_to_element(ele)
        action.perform()

        # 点击删除按钮
        WebDriverWait(driver, 30, 0.5).until(ec.visibility_of(
            driver.find_element_by_xpath(
                '//div[text()="{}"]/ancestor::div[@class="fixedDataTableCellGroupLayout_cellGroupWrapper"]/following-sibling::div[2]//a[text()="删除"]'.format(
                    name))))
        driver.find_element_by_xpath(
            '//div[text()="{}"]/ancestor::div[@class="fixedDataTableCellGroupLayout_cellGroupWrapper"]/following-sibling::div[2]//a[text()="删除"]'.format(
                name)).click()

        # 点击确定按钮
        WebDriverWait(driver, 30, 0.5).until(ec.visibility_of(
            driver.find_element_by_xpath('//button[@class="ant-btn ant-btn-primary ant-btn-lg"]')))
        driver.find_element_by_xpath('//button[@class="ant-btn ant-btn-primary ant-btn-lg"]').click()

        # 断言
        self.assertNotIn(name, driver.page_source)

        driver.switch_to.default_content()
        driver.find_element_by_class_name('u-button').click()
        sleep(1)
        driver.find_element_by_class_name('u-dropdown-menu-item').click()

