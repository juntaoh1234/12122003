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
        menu2 = driver.find_element_by_css_selector('span[title="流程管理"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()

        # 进入二级节点
        menu3 = driver.find_element_by_css_selector('li[class="bottomBar"][title="模型管理"]')
        actions.move_to_element(menu3)
        actions.click(menu3)
        actions.perform()

        assert u"模型管理" in driver.page_source, u"页面源码中不存在该关键字！"
        sleep(3)
        # 切换iframe
        iframe = driver.find_element_by_id('XTLCZX0006')
        driver.switch_to.frame(iframe)
        sleep(3)
        # 点击采购供应展开
        driver.find_element_by_xpath('//span[text()="采购供应"]').click()
        sleep(1)
        # 点击采购管理展开
        driver.find_element_by_xpath('//span[text()="采购管理"]').click()
        # 点击采购订单
        driver.find_element_by_xpath('//span[text()="采购订单"]').click()
        # 点击普通采购
        driver.find_element_by_xpath('//span[text()="普通采购"]').click()
        # 新增
        driver.find_element_by_xpath('//span[contains(text(),"新增")]').click()
        # 取消
        driver.find_element_by_xpath('//span[contains(text(),"取消")]').click()
        sleep(1)

        # 返回主窗体
        driver.switch_to.default_content()

        driver.find_element_by_class_name('u-button').click()
        sleep(1)
        driver.find_element_by_class_name('u-dropdown-menu-item').click()
        sleep(1)