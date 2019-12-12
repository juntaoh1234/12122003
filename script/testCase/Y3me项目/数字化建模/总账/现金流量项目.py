# coding=utf-8
from time import time, sleep

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from script.common import utils
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
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
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_class_name('lebra-navbar-left-icon')))
        driver.find_element_by_class_name('lebra-navbar-left-icon').click()

        # 进入财务管理
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//*[text()="财务管理"]')))
        driver.find_element_by_xpath('//*[text()="财务管理"]').click()
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_css_selector('span[title="总账"]')))
        # 进入一级节点
        menu2 = driver.find_element_by_css_selector('span[title="总账"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_css_selector('li[class="bottomBar"][title="现金流量项目"]')))
        # 进入二级节点
        menu3 = driver.find_element_by_css_selector('li[class="bottomBar"][title="现金流量项目"]')
        actions.move_to_element(menu3)
        actions.click(menu3)
        actions.perform()
        # 断言
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_css_selector(
                '#home_header > div > div.tab--38iB- > ul > li > p')))
        titleName = driver.find_element_by_css_selector(
            '#home_header > div > div.tab--38iB- > ul > li > p').get_attribute('title')
        assert u"现金流量项目" in titleName, u"页面源码中不存在该关键字！"
        locate = (By.ID, 'cashflowitem', 'Undefined')
        WebDriverWait(driver, 10, 0.5).until(ec.presence_of_element_located(locate))
        iframe = driver.find_element_by_id('cashflowitem')
        driver.switch_to.frame(iframe)

        # 点击会计主体右侧按钮
        WebDriverWait(driver, 10, 0.5).until(ec.visibility_of(driver.find_element_by_xpath(
            '//span[text()="会计主体"]/parent::div/following-sibling::div[1]//span[@class="Select-arrow-zone iconfont icon-chevron-down"]')))
        driver.find_element_by_xpath(
            '//span[text()="会计主体"]/parent::div/following-sibling::div[1]//span[@class="Select-arrow-zone iconfont icon-chevron-down"]').click()

        # 选择一个条目
        WebDriverWait(driver, 10, 0.5).until(ec.visibility_of(driver.find_element_by_xpath('//div[text()="企业账号级"]')))
        driver.find_element_by_xpath('//div[text()="企业账号级"]').click()

        # 点击现金流量类型右侧按钮
        WebDriverWait(driver, 10, 0.5).until(ec.visibility_of(driver.find_element_by_xpath(
            '//span[text()="现金流量类型"]/parent::div/following-sibling::div[1]//span[@class="Select-arrow-zone iconfont icon-chevron-down"]')))
        driver.find_element_by_xpath(
            '//span[text()="现金流量类型"]/parent::div/following-sibling::div[1]//span[@class="Select-arrow-zone iconfont icon-chevron-down"]').click()
        # 选择一个条目
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//div[@role="listbox"]/div[1]')))
        driver.find_element_by_xpath('//div[@role="listbox"]/div[1]').click()
        # 新增
        WebDriverWait(driver, 10, 0.5).until(ec.visibility_of(driver.find_element_by_xpath('//*[text()="新增"]')))
        driver.find_element_by_xpath('//*[text()="新增"]').click()
        # 输入编码
        num = random.randint(999, 10000)
        code = '编码{}'.format(num)
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//label[text()="编码"]/following-sibling::div//input')))
        driver.find_element_by_xpath('//label[text()="编码"]/following-sibling::div//input').send_keys(code)

        # 输入名称
        num1 = random.randint(999, 10000)
        name = '现金流量类型{}'.format(num1)
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//label[text()="名称"]/following-sibling::div//input')))
        driver.find_element_by_xpath('//label[text()="名称"]/following-sibling::div//input').send_keys(name)

        # 点击确定按钮
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//button[text()="确定"]')))
        driver.find_element_by_xpath('//button[text()="确定"]').click()

        # 断言
        self.assertIn(name, driver.page_source)

        # 点击编辑
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//span[text()="{}"]/ancestor::tr'.format(name))))

        # 鼠标移动
        ele = driver.find_element_by_xpath('//span[text()="{}"]/ancestor::tr'.format(name))
        action = ActionChains(driver)
        action.move_to_element(ele)
        action.perform()
        driver.find_element_by_xpath('//span[text()="{}"]/ancestor::tr//span[text()="编辑"]'.format(name)).click()

        # 点击确定按钮
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//button[text()="确定"]')))
        driver.find_element_by_xpath('//button[text()="确定"]').click()

        # 点击删除
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//span[text()="{}"]/ancestor::tr'.format(name))))

        # 鼠标移动
        ele = driver.find_element_by_xpath('//span[text()="{}"]/ancestor::tr'.format(name))
        action = ActionChains(driver)
        action.move_to_element(ele)
        action.perform()
        driver.find_element_by_xpath('//span[text()="{}"]/ancestor::tr//span[text()="删除"]'.format(name)).click()

        # 点击确定按钮
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//button[text()="确定"]')))
        driver.find_element_by_xpath('//button[text()="确定"]').click()

        self.assertNotIn(name, driver.page_source)

        driver.switch_to.default_content()
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_class_name('u-button')))
        driver.find_element_by_class_name('u-button').click()
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_class_name('u-dropdown-menu-item')))
        driver.find_element_by_class_name('u-dropdown-menu-item').click()
