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
        menu3 = driver.find_element_by_css_selector('li[class="bottomBar"][title="交易类型"]')
        actions.move_to_element(menu3)
        actions.click(menu3)
        actions.perform()

        assert u"交易类型" in driver.page_source, u"页面源码中不存在该关键字！"
        sleep(3)
        # 切换iframe
        iframe = driver.find_element_by_id('XTLCZX0027')
        driver.switch_to.frame(iframe)
        sleep(3)
        # 点击采购供应展开
        driver.find_element_by_xpath('//span[text()="采购供应"]/../../preceding-sibling::span[1]').click()
        sleep(1)
        # 点击库存管理展开
        driver.find_element_by_xpath('//span[text()="库存管理"]/../../preceding-sibling::span[1]').click()
        # 点击调拨订单
        driver.find_element_by_xpath('//span[text()="调拨订单"]').click()
        # 点击新增
        driver.find_element_by_xpath('//span[text()="新增"]').click()
        # 点击取消
        driver.find_element_by_id('bd_transtype|btnAbandon').click()
        # 点击确定
        driver.find_element_by_xpath('//span[text()="确 定"]').click()
        sleep(1)

        # 返回主窗体
        driver.switch_to.default_content()

        driver.find_element_by_class_name('u-button').click()
        sleep(1)
        driver.find_element_by_class_name('u-dropdown-menu-item').click()
        sleep(1)