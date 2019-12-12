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
        sleep(3)
        # 进入财务管理
        driver.find_element_by_xpath('//*[text()="营销管理"]').click()
        sleep(3)
        # 进入一级节点
        menu2 = driver.find_element_by_css_selector('span[title="会员中心"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(3)
        # 进入二级节点
        menu3 = driver.find_element_by_css_selector('li[class="bottomBar"][title="群发消息"]')
        actions.move_to_element(menu3)
        actions.click(menu3)
        actions.perform()
        sleep(3)

        titleName = driver.find_element_by_css_selector(
            '#home_header > div > div.tab--38iB- > ul > li > p').get_attribute('title')
        assert u"群发消息" in titleName, u"页面源码中不存在该关键字！"
        sleep(6)
        iframe = driver.find_element_by_id('SDMB040106')
        driver.switch_to.frame(iframe)

        #微信一键授权
        driver.find_element_by_xpath('//strong[contains(text(),"满足")]/../input').click()
        sleep(3)
        binding_button = driver.find_element_by_id('binding_Button')
        driver.execute_script("arguments[0].scrollIntoView();",binding_button)
        binding_button.click()
        sleep(3)

        driver.switch_to.default_content()
        driver.find_element_by_class_name('u-button').click()
        sleep(3)
        quit_button = driver.find_element_by_xpath('//li[@title="关闭全部页签"]')
        driver.execute_script("arguments[0].click();", quit_button)
        sleep(3)
