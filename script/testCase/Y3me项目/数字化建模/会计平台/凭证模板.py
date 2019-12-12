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
        menu2 = driver.find_element_by_css_selector('span[title="会计平台"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(1)
        # 进入二级节点
        menu3 = driver.find_element_by_css_selector('li[class="bottomBar"][title="凭证模板"]')
        actions.move_to_element(menu3)
        actions.click(menu3)
        actions.perform()

        sleep(2)
        titleName = driver.find_element_by_css_selector(
            '#home_header > div > div.tab--38iB- > ul > li > p').get_attribute('title')
        assert u"凭证模板" in titleName, u"页面源码中不存在该关键字！"
        sleep(2)
        iframe = driver.find_element_by_id('conversionu8c')
        driver.switch_to.frame(iframe)

        # 点击第一行的勾选按钮
        driver.find_element_by_xpath('//tbody/tr[1]/td[1]/span').click()

        # 鼠标移动到第一行
        ele = driver.find_element_by_xpath('//tbody/tr[1]/td[1]/span')
        action = ActionChains(driver)
        action.move_to_element(ele)
        action.perform()

        # 点击删除按钮
        driver.find_element_by_xpath('//tbody/tr[1]//span[text()="删除"]').click()

        # 点击确定按
        driver.find_element_by_xpath('//button[text()="确定"]').click()
        sleep(1)
        # 新增
        new_button = driver.find_element_by_xpath('//button[text()="新增"]')
        driver.execute_script("arguments[0].click();", new_button)

        sleep(2)

        # 输入编码

        driver.find_element_by_xpath('//label[text()="编码"]/parent::div/following-sibling::div//input').send_keys(
            'AP001')

        # 输入名称
        num = random.randint(999, 10000)
        name = '名称{}'.format(num)
        driver.find_element_by_xpath('//label[text()="名称"]/parent::div/following-sibling::div//input').send_keys(name)

        # 点击来源系统
        driver.find_element_by_xpath(
            '//label[text()="来源系统"]/parent::div/following-sibling::div//div[@class="ant-select-selection__rendered"]').click()
        sleep(1)
        # 点击应付管理
        driver.find_element_by_xpath('//li[text()="应付管理"]').click()

        # 点击来源事项类型
        driver.find_element_by_xpath(
            '//label[text()="来源事项类型"]/parent::div/following-sibling::div//div[@class="ant-select-selection__rendered"]').click()
        sleep(1)
        # 点击应付管理
        driver.find_element_by_xpath('//li[text()="采购发票"]').click()

        # 点击凭证类型
        driver.find_element_by_xpath('//label[text()="凭证类型"]/parent::div/following-sibling::div//input').click()
        sleep(1)

        # 点击固定值
        driver.find_element_by_xpath('//div[text()="固定值"]').click()
        sleep(1)

        # 点击档案值
        driver.find_element_by_xpath(
            '//label[text()="档案值"]/following-sibling::div//span[@class="rc-select-arrow"]').click()

        # 选择记账凭证
        driver.find_element_by_xpath('//li[text()="记账凭证"]').click()

        # 点击确定
        driver.find_element_by_xpath(
            '//div[@class="yy-formulas-button-warp col-xs-2 col-md-2 col-sm-2"]//button[text()="确定"]').click()

        sleep(2)

        # 点击保存按钮
        driver.find_element_by_xpath('//button[text()="保存"]').click()
        sleep(2)
        self.assertIn(name, driver.page_source)

        driver.switch_to.default_content()
        driver.find_element_by_class_name('u-button').click()
        sleep(1)
        driver.find_element_by_class_name('u-dropdown-menu-item').click()
