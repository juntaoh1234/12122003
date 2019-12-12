# coding=utf-8
from time import time, sleep

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from SRC.webdriver import switchTo
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
        sleep(5)
        # 进入一级节点
        menu2 = driver.find_element_by_css_selector('span[title="报表平台"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()

        # 进入二级节点
        menu3 = driver.find_element_by_css_selector('li[class="pureBottom bottomBar"][title="数据分析"]')
        actions.move_to_element(menu3)
        actions.click(menu3)
        actions.perform()

        assert u"数据分析" in driver.page_source, u"页面源码中不存在该关键字！"
        sleep(3)
        # 切换iframe
        iframe = driver.find_element_by_id('intellivworkbenchplatform-22')
        driver.switch_to.frame(iframe)
        sleep(3)
        # 新建报表
        new_button = driver.find_element_by_xpath('//button/span[text()="新建报表"]')
        driver.execute_script("arguments[0].click();", new_button)
        # 关闭
        sd_button = driver.find_element_by_xpath('//i[@title="关闭"]')
        driver.execute_script("arguments[0].click();", sd_button)
        sleep(1)

        # 返回主窗体
        driver.switch_to.default_content()

        driver.find_element_by_class_name('u-button').click()
        sleep(1)
        driver.find_element_by_class_name('u-dropdown-menu-item').click()
        sleep(1)