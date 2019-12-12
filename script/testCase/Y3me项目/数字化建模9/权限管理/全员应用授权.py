# coding=utf-8
from time import time, sleep

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
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
        sleep(1)
        menu2 = driver.find_element_by_css_selector('span[title="权限管理"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()

        menu3 = driver.find_element_by_css_selector('li[class="bottomBar"][title="全员应用授权"]')
        actions.move_to_element(menu3)
        actions.click(menu3)
        actions.perform()

        assert u"全员应用授权" in driver.page_source, u"页面源码中不存在该关键字！"
        sleep(1)
        iframe = driver.find_element_by_id('GZTACT040')
        driver.switch_to.frame(iframe)
        sleep(3)

        driver.find_element_by_xpath('//div[text()="领域"]').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="tree"]/div[2]/ul/li[1]/span/span/i').click()
        sleep(0.5)
        driver.find_element_by_xpath('//span[text()="流程管理"]').click()
        sleep(0.5)
        driver.find_element_by_xpath('//thead/tr[1]//input').click()
        driver.find_element_by_xpath('//button[text()="仅管理员可见"]').click()
        sleep(3)
        text = driver.find_element_by_xpath('//tbody[@class="u-table-tbody"]/tr[1]/td[3]/div/div/div').text
        self.assertEqual(text, '仅管理员可见')

        driver.find_element_by_xpath('//button[text()="全员可见"]').click()
        sleep(3)
        text1 = driver.find_element_by_xpath('//tbody[@class="u-table-tbody"]/tr[1]/td[3]/div/div/div').text
        self.assertEqual(text1, '全员可见')

        # 返回主窗体
        driver.switch_to.default_content()

        # 关闭页签
        driver.find_element_by_css_selector('button[class="u-button"]').click()
        driver.find_element_by_css_selector('li[title="关闭全部页签"]').click()
