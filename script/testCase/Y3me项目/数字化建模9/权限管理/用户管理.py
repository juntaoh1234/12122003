# coding=utf-8
from time import time, sleep
import random
from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from script.common import utils
from selenium import webdriver
from selenium.webdriver import ActionChains
from SRC.param import context


class EasyCase(TestCase):
    def __init__(self, webDriver, paramsList):
        # 请不要修改该方法124421
        super(EasyCase, self).__init__(webDriver, paramsList)

    @codeException_dec('3')
    def runTest(self):
        driver = self.getDriver()
        param = self.param
        tool = utils
        # 左上方公共节点
        driver.find_element_by_class_name('lebra-navbar-left-icon').click()
        sleep(1)
        menu2 = driver.find_element_by_css_selector('span[title="权限管理"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()

        menu3 = driver.find_element_by_css_selector('li[class="bottomBar"][title="用户管理"]')
        actions.move_to_element(menu3)
        actions.click(menu3)
        actions.perform()

        assert u"用户管理" in driver.page_source, u"页面源码中不存在该关键字！"
        sleep(1)

        # 切换iframe
        iframe = driver.find_element_by_id('GZTACT015')
        driver.switch_to.frame(iframe)
        sleep(3)
        # 点击新增按钮
        driver.find_element_by_xpath('//span[text()="新增 "]').click()
        sleep(1)
        num = random.randint(999, 10000)
        name = "用户名{}".format(num)
        # 输入用户名
        driver.find_element_by_xpath(
            '//span[text()="用户名 "]/ancestor::div[@class="u-col-md-3 u-col-sm-3 text-right"]/following-sibling::div/input').send_keys(
            name)
        tele = context.get_mobile()
        # 输入手机号码
        driver.find_element_by_xpath(
            '//span[text()="手机号码 "]/ancestor::div[@class="u-col-md-3 u-col-sm-3 text-right"]/following-sibling::div//input').send_keys(
            tele)

        email = context.get_email()
        # 输入邮箱地址
        driver.find_element_by_xpath(
            '//span[text()="邮箱地址 "]/ancestor::div[@class="u-col-md-3 u-col-sm-3 text-right"]/following-sibling::div//input').send_keys(
            email)
        # 点击保存按钮
        driver.find_element_by_xpath('//span[contains(text(),"保存 ")]').click()
        sleep(2)
        driver.find_element_by_xpath('//span[text()="{}"]/parent::td/preceding-sibling::td//input'.format(name)).click()
        #
        driver.find_element_by_xpath(
            '//span[text()="启用"]/parent::button[@class="u-button dropdown-button u-button-sm"]').click()
        sleep(0.5)
        driver.find_element_by_xpath(
            '//div[4]/div/div/div/button[1]/span[text()="启用"]').click()

        driver.find_element_by_xpath('//span[text()="{}"]/parent::td/preceding-sibling::td//input'.format(name)).click()

        driver.find_element_by_xpath(
            '//span[text()="启用"]/parent::button[@class="u-button dropdown-button u-button-sm"]').click()
        sleep(0.5)
        driver.find_element_by_xpath(
            '//div[3]/div/div/div/button[2]/span[text()="停用"]').click()
        driver.find_element_by_xpath('//span[text()="{}"]/parent::td/preceding-sibling::td//input'.format(name)).click()
        sleep(0.5)
        # 移除新建的用户信息
        driver.find_element_by_xpath('//button[@class="u-button tool-button u-button-sm"]/span[text()="移除 "]').click()
        sleep(1)
        driver.find_element_by_xpath('//div[@class="u-modal-content"]//span[text()="确定 "]').click()
        sleep(1)

        # 断言是否删除成功
        self.assertNotIn(name, driver.page_source)

        # 返回主窗体
        driver.switch_to.default_content()

        # 关闭页签
        driver.find_element_by_css_selector('button[class="u-button"]').click()
        shut = driver.find_element_by_css_selector('li[title="关闭全部页签"]')
        driver.execute_script("arguments[0].click();", shut)
        sleep(3)
