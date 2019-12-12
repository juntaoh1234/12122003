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
        driver.find_element_by_xpath('//*[text()="人力资源"]').click()
        sleep(1)
        # 进入一级节点
        menu2 = driver.find_element_by_css_selector('span[title="人力设置"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(1)
        # 进入二级节点
        menu3 = driver.find_element_by_css_selector('li[class="bottomBar"][title="花名册设置"]')
        actions.move_to_element(menu3)
        actions.click(menu3)
        actions.perform()

        sleep(2)
        titleName = driver.find_element_by_css_selector(
            '#home_header > div > div.tab--38iB- > ul > li > p').get_attribute('title')
        assert u"花名册设置" in titleName, u"页面源码中不存在该关键字！"
        sleep(1)
        iframe = driver.find_element_by_id('HRSZ030070')
        driver.switch_to.frame(iframe)

        # 增加花名册
        driver.find_element_by_xpath('//span[text()="新增花名册"]').click()
        # driver.find_element_by_xpath('//span[@class="search-wraper"]/label').click()
        # 点击组织右侧的按钮
        driver.find_element_by_xpath('//span[text()="所属组织"]/following-sibling::div/span[1]').click()
        sleep(2)
        # 点击展开按钮
        driver.find_element_by_xpath('//span[@class="button level1 switch noline_close"]').click()

        # 再次点击展开按钮
        driver.find_element_by_xpath('//span[@class="button level2 switch noline_close"]').click()

        # 点击仓储中心北京
        driver.find_element_by_xpath(
            '//div[@id="refContainerorgid"]//a[@title="仓储中心-北京"]//span[text()="仓储中心-北京"]').click()

        # 点击使用范围右侧按钮
        driver.find_element_by_xpath('//span[text()="适用范围"]/following-sibling::div/span[1]').click()
        sleep(2)

        # 点击展开按钮
        driver.find_element_by_xpath('//span[@class="button level1 switch noline_close"]').click()

        # 再次点击展开按钮
        driver.find_element_by_xpath('//span[@class="button level2 switch noline_close"]').click()

        # 点击北京仓储中心
        driver.find_element_by_xpath(
            '//div[@id="refContainerscopeorgids"]//a[@title="仓储中心-北京"]//span[text()="仓储中心-北京"]').click()

        # 点击选项
        driver.find_element_by_xpath(
            '//div[@id="refContainerscopeorgids"]//a[@title="仓储中心-北京"]/parent::li/span[2]').click()

        # 点击确定按钮
        driver.find_element_by_xpath('//div[@class="btn-group pull-right"]/button[text()="确定"]').click()

        # 点击编码按钮
        # 输入编码
        num = random.randint(999, 10000)
        code = "BM{}".format(num)
        driver.find_element_by_xpath('//span[text()="编码"]/following-sibling::input').send_keys(code)

        # 输入名称
        num1 = random.randint(999, 10000)
        name = "NM{}".format(num1)
        driver.find_element_by_xpath('//span[text()="名称"]/following-sibling::input').send_keys(name)

        # 点击信息集右侧的按钮
        driver.find_element_by_xpath('//label[text()="信息集："]/following-sibling::div/span').click()
        sleep(2)
        # 选中一条数据
        driver.find_element_by_xpath('//td[text()="基本信息"]').click()

        # 点击全选按钮
        driver.find_element_by_xpath(
            '//*[@id="shiftLeftAndRight"]/div/div[1]/div[2]/table/thead/tr/th[1]/div/label').click()

        # 点击保存按钮
        driver.find_element_by_xpath('//div[@class="buttons text-right"]/button[2]').click()
        sleep(2)
        # 断言
        self.assertIn(name, driver.page_source)

        driver.switch_to.default_content()
        driver.find_element_by_class_name('u-button').click()
        sleep(1)
        driver.find_element_by_class_name('u-dropdown-menu-item').click()
