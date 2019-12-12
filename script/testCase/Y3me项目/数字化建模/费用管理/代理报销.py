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
        menu3 = driver.find_element_by_css_selector('li[class="bottomBar"][title="代理报销"]')
        actions.move_to_element(menu3)
        actions.click(menu3)
        actions.perform()

        sleep(2)
        titleName = driver.find_element_by_css_selector(
            '#home_header > div > div.tab--38iB- > ul > li > p').get_attribute('title')
        assert u"代理报销" in titleName, u"页面源码中不存在该关键字！"
        sleep(1)
        iframe = driver.find_element_by_id('FICO_DLBX')
        driver.switch_to.frame(iframe)

        # 新增
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//*[text()="新增"]')))
        driver.find_element_by_xpath('//*[text()="新增"]').click()

        # 点击新增代理人
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//button[text()="新代理人"]')))
        driver.find_element_by_xpath('//button[text()="新代理人"]').click()

        # 点击左侧的按钮
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//ul[@class="rc-tree"]/li[1]/span[2]')))
        driver.find_element_by_xpath('//ul[@class="rc-tree"]/li[1]/span[2]').click()

        # 点击选择第一个人
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath('//div[@class="modal-lg modal-dialog"]//tbody//tr[1]//input')))
        driver.find_element_by_xpath('//div[@class="modal-lg modal-dialog"]//tbody//tr[1]//input').click()

        # 点击确定
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//button[text()="确定"]')))
        driver.find_element_by_xpath('//button[text()="确定"]').click()

        # 点击新增委托人
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//button[text()="新增委托人"]')))
        driver.find_element_by_xpath('//button[text()="新增委托人"]').click()

        # 点击左侧的按钮
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//ul[@class="rc-tree"]/li[1]/span[2]')))
        driver.find_element_by_xpath('//ul[@class="rc-tree"]/li[1]/span[2]').click()

        # 点击选择第一个人
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath('//div[@class="modal-lg modal-dialog"]//tbody//tr[1]//input')))
        driver.find_element_by_xpath('//div[@class="modal-lg modal-dialog"]//tbody//tr[1]//input').click()

        # 点击确定
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//button[text()="确定"]')))
        driver.find_element_by_xpath('//button[text()="确定"]').click()

        # 点击保存
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//button[text()="保存"]')))
        driver.find_element_by_xpath('//button[text()="保存"]').click()

        # 点击删除按钮
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath(
                '//*[@id="root"]/div/div[2]/div[1]/div[2]/div/table/tbody/tr//td/a[text()="删除"]')))
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div[1]/div[2]/div/table/tbody/tr//td/a[text()="删除"]').click()

        # 点击确定按钮
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//span[text()="确 认"]/parent::button')))
        driver.find_element_by_xpath('//span[text()="确 认"]/parent::button').click()

        driver.switch_to.default_content()
        driver.find_element_by_class_name('u-button').click()
        sleep(1)
        driver.find_element_by_class_name('u-dropdown-menu-item').click()
