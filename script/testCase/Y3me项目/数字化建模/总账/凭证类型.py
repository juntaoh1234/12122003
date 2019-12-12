# coding=utf-8
from time import time, sleep

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from script.common import utils
from selenium import webdriver
from selenium.webdriver import ActionChains
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
        menu2 = driver.find_element_by_css_selector('span[title="总账"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(1)
        # 进入二级节点
        menu3 = driver.find_element_by_css_selector('li[class="bottomBar"][title="凭证类型"]')
        actions.move_to_element(menu3)
        actions.click(menu3)
        actions.perform()

        sleep(2)
        titleName = driver.find_element_by_css_selector(
            '#home_header > div > div.tab--38iB- > ul > li > p').get_attribute('title')
        assert u"凭证类型" in titleName, u"页面源码中不存在该关键字！"
        sleep(2)
        iframe = driver.find_element_by_id('vouchertype')
        driver.switch_to.frame(iframe)

        # 新增
        driver.find_element_by_xpath('//*[text()="新增"]').click()
        sleep(2)
        # 输入编码
        num = random.randint(999, 10000)
        code = '编码{}'.format(num)
        driver.find_element_by_xpath('//div[text()="编码"]/parent::label/following-sibling::div//input').send_keys(code)

        # 输入名称
        num1 = random.randint(999, 10000)
        name = '凭据{}'.format(num1)
        driver.find_element_by_xpath('//div[text()="名称"]/parent::label/following-sibling::div//input').send_keys(name)

        # 输入凭证字
        driver.find_element_by_xpath('//div[text()="凭证字"]/parent::label/following-sibling::div//input').send_keys(code)
        sleep(0.5)
        # 输入备注信息
        driver.find_element_by_xpath('//div[text()="备注"]/parent::label/following-sibling::div//input').send_keys(
            '备注信息00000')

        # 点击确定按钮
        driver.find_element_by_xpath('//div[@class="form-group"]//button[@class="btn btn-primary"]').click()
        sleep(1.5)

        self.assertIn(name, driver.page_source)

        # 鼠标移动
        ele = driver.find_element_by_xpath('//td[text()="{}"]/parent::tr'.format(name))

        action = ActionChains(driver)
        action.move_to_element(ele)
        action.perform()

        # 点击编辑
        driver.find_element_by_xpath('//td[text()="{}"]/parent::tr//span[text()="编辑"]'.format(name)).click()
        sleep(1)

        # 点击确定按钮
        driver.find_element_by_xpath('//div[@class="form-group"]//button[@class="btn btn-primary"]').click()
        sleep(1.5)
        # 鼠标移动
        ele = driver.find_element_by_xpath('//td[text()="{}"]/parent::tr'.format(name))
        action = ActionChains(driver)
        action.move_to_element(ele)
        action.perform()
        # 点击删除
        driver.find_element_by_xpath('//td[text()="{}"]/parent::tr//span[text()="删除"]'.format(name)).click()

        # 点击确定
        driver.find_element_by_xpath('//div[@class="modal-footer"]//button[@class="btn btn-primary"]').click()
        sleep(1)
        self.assertNotIn(name, driver.page_source)
        driver.switch_to.default_content()
        driver.find_element_by_class_name('u-button').click()
        sleep(1)
        driver.find_element_by_class_name('u-dropdown-menu-item').click()
