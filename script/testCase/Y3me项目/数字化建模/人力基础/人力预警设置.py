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
        menu3 = driver.find_element_by_css_selector('li[class="bottomBar"][title="人力预警设置"]')
        actions.move_to_element(menu3)
        actions.click(menu3)
        actions.perform()

        sleep(2)
        titleName = driver.find_element_by_css_selector(
            '#home_header > div > div.tab--38iB- > ul > li > p').get_attribute('title')
        assert u"人力预警设置" in titleName, u"页面源码中不存在该关键字！"
        sleep(1)
        iframe = driver.find_element_by_id('HRSZ040040')
        driver.switch_to.frame(iframe)

        # 新增
        driver.find_element_by_xpath('//button/span[text()="新增"]').click()
        # driver.find_element_by_xpath('//*[@class="back"]/a').click()
        # driver.find_element_by_xpath('//button[text()="确认"]').click()
        # driver.find_element_by_xpath('//div[@class="ant-confirm-btns"]//span[text()="确 定"]').click()

        # 输入预警编码
        num = random.randint(999, 10000)
        code = "BM{}".format(num)
        driver.find_element_by_xpath('//span[text()="预警编码"]/following-sibling::div//input').send_keys(code)

        # 输入预警名称
        num1 = random.randint(999, 10000)
        code1 = "预警{}".format(num1)
        driver.find_element_by_xpath('//span[text()="预警名称"]/following-sibling::div//input').send_keys(code1)

        # 点击下一步
        driver.find_element_by_xpath('//button[text()="下一步"]').click()
        sleep(1.5)

        # 点击通知对象按钮
        driver.find_element_by_xpath('//span[text()="通知对象"]/following-sibling::div//span').click()
        sleep(1)

        # 选择条目
        driver.find_element_by_xpath('//td[text()="本人"]').click()

        # 点击确定按钮
        driver.find_element_by_xpath('//*[@id="refContainerreceiverFuncId"]//button[text()="确定"]').click()
        #
        driver.find_element_by_xpath('//*[@id="step2"]/div[2]/div/span').click()

        # 选择条目
        driver.find_element_by_xpath('//td[text()="文库管理员"]').click()
        # 点击确定按钮
        driver.find_element_by_xpath('//*[@id="refContainerreceiverRoleId"]//button[text()="确定"]').click()
        sleep(1)
        driver.find_element_by_xpath('//span[text()="邮件"]/parent::span/preceding-sibling::label').click()
        # 点击消息
        driver.find_element_by_xpath('//span[text()="消息"]/parent::span/preceding-sibling::label').click()
        # 输入app消息内容
        driver.find_element_by_xpath('//textarea').send_keys("你好1234")
        sleep(2)

        # # 跳转iframe
        # iframe = driver.find_element_by_id('ueditor_0')
        # driver.switch_to.frame(iframe)
        # # 输入邮件内容
        # sleep(2)
        # driver.find_element_by_xpath('//body[@class="view"]/p').send_keys("邮件888")
        #
        # driver.switch_to.default_content()
        # sleep(1)
        # iframe = driver.find_element_by_id('HRSZ040040')
        # driver.switch_to.frame(iframe)
        # # 点击下一步按钮
        driver.find_element_by_xpath('//button[text()="下一步"]').click()
        sleep(1.5)

        # 输入开始时间
        driver.find_element_by_xpath('//*[@id="step3"]/div[2]/div[1]/div[1]/input').send_keys(random.randint(1, 30))
        # 输入时间点
        driver.find_element_by_xpath('//*[@id="duravalue"]').click()
        # 输入时间点
        driver.find_element_by_xpath('//div[text()="12"]').click()

        # 输入分钟
        driver.find_element_by_xpath('//div[text()="55"]').click()

        # 点击完成
        driver.find_element_by_xpath('//button[text()="完成"]').click()
        sleep(1)
        self.assertIn(code1, driver.page_source)
        driver.switch_to.default_content()
        driver.find_element_by_class_name('u-button').click()
        sleep(1)
        driver.find_element_by_class_name('u-dropdown-menu-item').click()
