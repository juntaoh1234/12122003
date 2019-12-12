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
        menu3 = driver.find_element_by_css_selector('li[class="bottomBar"][title="单据可用项目设置"]')
        actions.move_to_element(menu3)
        actions.click(menu3)
        actions.perform()

        sleep(2)
        titleName = driver.find_element_by_css_selector(
            '#home_header > div > div.tab--38iB- > ul > li > p').get_attribute('title')
        assert u"单据可用项目设置" in titleName, u"页面源码中不存在该关键字！"
        sleep(2)
        iframe = driver.find_element_by_id('FICO_DJKYXMSZ')
        driver.switch_to.frame(iframe)

        # 新增
        WebDriverWait(driver, 10, 0.5).until(ec.visibility_of(driver.find_element_by_xpath('//*[text()="新增"]')))
        driver.find_element_by_xpath('//*[text()="新增"]').click()

        # 点击取消
        WebDriverWait(driver, 10, 0.5).until(ec.visibility_of(driver.find_element_by_xpath('//*[text()="取消"]')))
        driver.find_element_by_xpath('//*[text()="取消"]').click()

        # 新增
        WebDriverWait(driver, 10, 0.5).until(ec.visibility_of(driver.find_element_by_xpath('//*[text()="新增"]')))
        driver.find_element_by_xpath('//*[text()="新增"]').click()

        # 输入单据类型
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath('//span[text()="单据类型"]/parent::div/following-sibling::div//input[1]')))
        driver.find_element_by_xpath('//span[text()="单据类型"]/parent::div/following-sibling::div//input[1]').click()

        # 选择一个条目
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath(
                '//ul[@class="dropdown-menu bootstrap-typeahead-menu dropdown-menu-justify"]/li[1]')))
        driver.find_element_by_xpath(
            '//ul[@class="dropdown-menu bootstrap-typeahead-menu dropdown-menu-justify"]/li[1]').click()

        # 输入限制档案
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath('//span[text()="限制档案"]/parent::div/following-sibling::div//input[1]')))
        driver.find_element_by_xpath('//span[text()="限制档案"]/parent::div/following-sibling::div//input[1]').click()

        # 选择一个条目
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath(
                '//ul[@class="dropdown-menu bootstrap-typeahead-menu dropdown-menu-justify"]/li[1]')))
        driver.find_element_by_xpath(
            '//ul[@class="dropdown-menu bootstrap-typeahead-menu dropdown-menu-justify"]/li[1]').click()

        # 输入已选项目
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath('//span[text()="已选项目"]/parent::div/following-sibling::div//input[1]')))
        driver.find_element_by_xpath('//span[text()="已选项目"]/parent::div/following-sibling::div//input[1]').click()

        # 选择一个条目
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath(
                '//ul[@class="dropdown-menu bootstrap-typeahead-menu dropdown-menu-justify"]/li[1]')))
        driver.find_element_by_xpath(
            '//ul[@class="dropdown-menu bootstrap-typeahead-menu dropdown-menu-justify"]/li[1]').click()

        # 点击保存
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//button[text()="确定"]')))
        driver.find_element_by_xpath('//button[text()="确定"]').click()

        # 断言
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath(
                '//*[@id="root"]/div/div[2]/div/div[1]/div[2]/div/table/tbody/tr[1]')))
        ele = driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div/div[1]/div[2]/div/table/tbody/tr[1]')
        self.assertIsNotNone(ele)

        # 点击编辑按钮
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath(
                '//*[@id="root"]/div/div[2]/div/div[1]/div[2]/div/table/tbody/tr[1]//span[text()="编辑"]')))
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div/div[1]/div[2]/div/table/tbody/tr[1]//span[text()="编辑"]').click()

        # 点击保存
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//button[text()="确定"]')))
        driver.find_element_by_xpath('//button[text()="确定"]').click()

        # 点击删除按钮
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath(
                '//*[@id="root"]/div/div[2]/div/div[1]/div[2]/div/table/tbody/tr[1]//span[text()="删除"]')))
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div/div[1]/div[2]/div/table/tbody/tr[1]//span[text()="删除"]').click()

        # 点击确定按钮
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath(
                '//button[@class="ant-btn ant-btn-danger"]')))
        driver.find_element_by_xpath(
            '//button[@class="ant-btn ant-btn-danger"]').click()

        driver.switch_to.default_content()
        driver.find_element_by_class_name('u-button').click()
        sleep(1)
        driver.find_element_by_class_name('u-dropdown-menu-item').click()

