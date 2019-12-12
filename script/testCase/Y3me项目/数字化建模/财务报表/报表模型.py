# coding=utf-8
from time import time, sleep

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from script.common import utils
from selenium import webdriver
from selenium.webdriver import ActionChains
import random
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
        menu3 = driver.find_element_by_css_selector('li[class="bottomBar"][title="报表模型"]')
        actions.move_to_element(menu3)
        actions.click(menu3)
        actions.perform()

        sleep(2)
        titleName = driver.find_element_by_css_selector(
            '#home_header > div > div.tab--38iB- > ul > li > p').get_attribute('title')

        assert u"报表模型" in titleName, u"页面源码中不存在该关键字！"
        sleep(1)
        iframe = driver.find_element_by_id("rptitemtype")
        driver.switch_to.frame(iframe)

        # 新增报表模型
        driver.find_element_by_class_name('add-tasklist-font').click()
        num = random.randint(100, 999)
        driver.find_element_by_xpath('//div[text()="编码"]/../..//input').send_keys("itemtype{}".format(num))
        driver.find_element_by_xpath('//div[text()="名称"]/../..//input').send_keys("模型{}".format(num))
        driver.find_element_by_xpath('//div[text()="创建组织"]/../..//input').click()
        driver.find_element_by_xpath('//span[text()="globalorg 企业账号级"]').click()
        driver.find_element_by_xpath('//div[text()="会计期间方案"]/../..//input').click()

        case_item = driver.find_element_by_xpath('//span[text()="0001 基准会计期间方案"]')
        driver.execute_script("arguments[0].scrollIntoView();", case_item)
        case_item.click()
        driver.find_element_by_xpath('//button[text()="确定"]').click()
        sleep(1)

        driver.switch_to.default_content()
        driver.find_element_by_class_name('u-button').click()
        sleep(1)
        driver.find_element_by_class_name('u-dropdown-menu-item').click()
