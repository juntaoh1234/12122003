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
        menu2 = driver.find_element_by_css_selector('span[title="费用管理"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(1)
        # 进入二级节点
        menu3 = driver.find_element_by_css_selector('li[class="bottomBar"][title="报销标准"]')
        actions.move_to_element(menu3)
        actions.click(menu3)
        actions.perform()

        sleep(1)
        titleName = driver.find_element_by_css_selector(
            '#home_header > div > div.tab--38iB- > ul > li > p').get_attribute('title')
        assert u"报销标准" in titleName, u"页面源码中不存在该关键字！"
        sleep(1)
        iframe = driver.find_element_by_id('FICO_BXBZ')
        driver.switch_to.frame(iframe)

        # 新增
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//*[text()="新增"]')))
        driver.find_element_by_xpath('//*[text()="新增"]').click()

        # 点击取消
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//*[text()="取消"]')))
        driver.find_element_by_xpath('//*[text()="取消"]').click()

        # 点击确定
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//button[@class="ant-btn ant-btn-danger"]')))
        driver.find_element_by_xpath('//button[@class="ant-btn ant-btn-danger"]').click()

        # 新增
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//*[text()="新增"]')))
        driver.find_element_by_xpath('//*[text()="新增"]').click()

        # 输入标准的名称
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//input[@placeholder="请输入"]')))
        num1 = random.randint(999, 10000)
        name = '报销标准{}'.format(num1)
        driver.find_element_by_xpath('//input[@placeholder="请输入"]').send_keys(name)

        # 点击适用组织
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//input[@placeholder="请选择适用组织"]')))
        driver.find_element_by_xpath('//input[@placeholder="请选择适用组织"]').click()
        sleep(2)
        # 点击第一个条目
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath(
                '//ul[@class="dropdown-menu bootstrap-typeahead-menu dropdown-menu-justify"]/li[1]')))

        driver.find_element_by_xpath(
            '//ul[@class="dropdown-menu bootstrap-typeahead-menu dropdown-menu-justify"]/li[1]').click()

        # 点击选择控制力度
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath('//span[text()="刚性控制"]/parent::span/preceding-sibling::span')))
        driver.find_element_by_xpath('//span[text()="刚性控制"]/parent::span/preceding-sibling::span').click()

        # 选择可乘坐舱位

        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath(
                    '//div[text()="国内航班"]/ancestor::div[@class="row row-rewrite"]/div[2]//label[text()="头等舱"]')))
        driver.find_element_by_xpath(
            '//div[text()="国内航班"]/ancestor::div[@class="row row-rewrite"]/div[2]//label[text()="头等舱"]').click()

        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath(
                    '//div[text()="国际航班"]/ancestor::div[@class="row row-rewrite"]/div[2]//label[text()="头等舱"]')))
        driver.find_element_by_xpath(
            '//div[text()="国际航班"]/ancestor::div[@class="row row-rewrite"]/div[2]//label[text()="头等舱"]').click()

        # 点击关联用户
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath('//span[@class="ant-select-arrow"]')))

        # 滚动屏幕
        ele = driver.find_element_by_xpath('//span[@class="ant-select-arrow"]')
        driver.execute_script('arguments[0].scrollIntoView()', ele)

        driver.find_element_by_xpath('//span[@class="ant-select-arrow"]/i').click()

        # 选择一个条目
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath('//ul[@role="listbox"]/li[1]')))
        driver.find_element_by_xpath('//ul[@role="listbox"]/li[1]').click()

        # 点击增加
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath('//button[text()="增加"]')))
        driver.find_element_by_xpath('//button[text()="增加"]').click()

        # 选择部门
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//div[text()="部门"]/following-sibling::div/div/div/div')))
        driver.find_element_by_xpath('//div[text()="部门"]/following-sibling::div/div/div/div').click()
        sleep(2)
        # 点击第一个条目
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath(
                '//ul[@class="dropdown-menu bootstrap-typeahead-menu dropdown-menu-justify"]/li[1]')))

        driver.find_element_by_xpath(
            '//ul[@class="dropdown-menu bootstrap-typeahead-menu dropdown-menu-justify"]/li[1]').click()

        # 选择职级
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//div[text()="职级"]/following-sibling::div/div/div/div')))
        driver.find_element_by_xpath('//div[text()="职级"]/following-sibling::div/div/div/div').click()
        sleep(2)
        # 点击第一个条目
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath(
                '//ul[@class="dropdown-menu bootstrap-typeahead-menu dropdown-menu-justify"]/li[1]')))
        driver.find_element_by_xpath(
            '//ul[@class="dropdown-menu bootstrap-typeahead-menu dropdown-menu-justify"]/li[1]').click()

        # 选择职务
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//div[text()="职务"]/following-sibling::div/div/div/div')))
        driver.find_element_by_xpath('//div[text()="职务"]/following-sibling::div/div/div/div').click()
        sleep(2)
        # 点击第一个条目
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath(
                '//ul[@class="dropdown-menu bootstrap-typeahead-menu dropdown-menu-justify"]/li[1]')))
        driver.find_element_by_xpath(
            '//ul[@class="dropdown-menu bootstrap-typeahead-menu dropdown-menu-justify"]/li[1]').click()

        # 点击确定
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//button[text()="确定"]')))
        driver.find_element_by_xpath('//button[text()="确定"]').click()

        # 点击保存
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//button[text()="保存"]')))
        driver.find_element_by_xpath('//button[text()="保存"]').click()
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('// a[text() = "机票"]')))
        self.assertIn(name, driver.page_source)

        # 点击编辑
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//td[text()="{}"]/parent::tr//a[text()="编辑"]'.format(name))))
        driver.find_element_by_xpath('//td[text()="{}"]/parent::tr//a[text()="编辑"]'.format(name)).click()

        # 点击保存
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//button[text()="保存"]')))
        driver.find_element_by_xpath('//button[text()="保存"]').click()

        # 点击删除
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//td[text()="{}"]/parent::tr//a[text()="删除"]'.format(name))))
        driver.find_element_by_xpath('//td[text()="{}"]/parent::tr//a[text()="删除"]'.format(name)).click()

        # 点击确定
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//button[@class="ant-btn ant-btn-danger"]')))
        driver.find_element_by_xpath('//button[@class="ant-btn ant-btn-danger"]').click()

        driver.switch_to.default_content()
        driver.find_element_by_class_name('u-button').click()
        sleep(1)
        driver.find_element_by_class_name('u-dropdown-menu-item').click()
