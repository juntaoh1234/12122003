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
        # 进入社交协同
        driver.find_element_by_xpath('//*[text()="财务管理"]').click()
        sleep(1)
        # 进入一级节点
        menu2 = driver.find_element_by_css_selector('span[title="财务报表"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(1)
        # 进入二级节点
        menu3 = driver.find_element_by_css_selector('li[class="bottomBar"][title="报表数据审核"]')
        actions.move_to_element(menu3)
        actions.click(menu3)
        actions.perform()

        sleep(1)
        titleName = driver.find_element_by_css_selector(
            '#home_header > div > div.tab--38iB- > ul > li > p').get_attribute('title')

        assert u"报表数据审核" in titleName, u"页面源码中不存在该关键字！"
        sleep(1)
        iframe = driver.find_element_by_id("reportDataAudit")
        driver.switch_to.frame(iframe)

        # 点击右边的按钮
        WebDriverWait(driver, 10, 0.5).until(ec.visibility_of(driver.find_element_by_xpath(
            '//label[text()="报表模型"]/following-sibling::div//span[@class="Select-arrow-zone iconfont icon-chevron-down"]')))
        driver.find_element_by_xpath(
            '//label[text()="报表模型"]/following-sibling::div//span[@class="Select-arrow-zone iconfont icon-chevron-down"]').click()

        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//div[@role="listbox"]/div[1]')))
        # 选自第一个条目
        driver.find_element_by_xpath('//div[@role="listbox"]/div[1]').click()

        # 点击年度右侧的按钮
        WebDriverWait(driver, 10, 0.5).until(ec.visibility_of(driver.find_element_by_xpath(
            '//label[text()="年度"]/following-sibling::div[1]//span[@class="Select-arrow-zone iconfont icon-chevron-down"]')))
        driver.find_element_by_xpath(
            '//label[text()="年度"]/following-sibling::div[1]//span[@class="Select-arrow-zone iconfont icon-chevron-down"]').click()

        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//div[@role="listbox"]/div[2]')))
        # 选自第一个条目
        driver.find_element_by_xpath('//div[@role="listbox"]/div[2]').click()

        # 点击月度右侧的按钮
        WebDriverWait(driver, 10, 0.5).until(ec.visibility_of(driver.find_element_by_xpath(
            '//label[text()="年度"]/following-sibling::div[2]//span[@class="Select-arrow-zone iconfont icon-chevron-down"]')))
        driver.find_element_by_xpath(
            '//label[text()="年度"]/following-sibling::div[2]//span[@class="Select-arrow-zone iconfont icon-chevron-down"]').click()

        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//div[@role="listbox"]/div[1]')))
        # 选自第一个条目
        driver.find_element_by_xpath('//div[@role="listbox"]/div[1]').click()

        # 搜索
        WebDriverWait(driver, 10, 0.5).until(ec.visibility_of(driver.find_element_by_xpath('//button[text()="搜索"]')))
        driver.find_element_by_xpath('//button[text()="搜索"]').click()
        # driver.find_element_by_id("react-select-2--option-0").click()
        # driver.find_element_by_xpath('//button[text()="搜索"]').click()

        driver.switch_to.default_content()
        driver.find_element_by_class_name('u-button').click()
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_class_name('u-dropdown-menu-item')))
        driver.find_element_by_class_name('u-dropdown-menu-item').click()
