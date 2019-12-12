# coding=utf-8
from time import sleep

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from SRC.webdriver.switchTo import SwitchTo
from script.common import utils
from selenium.webdriver import ActionChains
from SRC.param import context
import random


class EasyCase(TestCase):
    str_regular = None

    def __init__(self, webDriver, paramsList):
        # 请不要修改该方法124421
        super(EasyCase, self).__init__(webDriver, paramsList)

    @codeException_dec('3')
    def runTest(self):
        driver = self.getDriver()
        driver.implicitly_wait(30)
        param = self.param
        tool = utils
        driver.refresh()

        # 左上方公共节点
        driver.find_element_by_class_name('lebra-navbar-left-icon').click()
        sleep(2)
        # 进入社交协同
        driver.find_element_by_xpath('//*[text()="人力资源"]').click()
        sleep(2)
        # 进入一级节点
        menu2 = driver.find_element_by_css_selector('span[title="假勤管理"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(2)
        # 进入二级节点
        driver.find_element_by_xpath('//li[@title="打卡地点"]').click()

        sleep(2)
        # 跳转劳动打卡地点iframe
        iframe = driver.find_element_by_id('HRJQ020030')
        # driver.switch_to.frame(iframe)
        SwitchTo(driver).frame(iframe)
        sleep(2)
        # 点击新增按钮
        driver.find_element_by_xpath('//*[@id="attend-place"]//button/span[text()="新增"]').click()
        sleep(3)
        # 生成一个随机的区
        district = context.get_district()
        driver.find_element_by_xpath('//input[@id="suggestId" and @placeholder="请输入地址"]').send_keys(district)
        sleep(1.5)
        driver.find_element_by_xpath('//div[@class="amap-sug-result"]/div[1]').click()
        # 点击组织右侧按钮
        driver.find_element_by_xpath('//div/span/span/span/i[2]').click()
        sleep(3)

        # 选中组织
        driver.find_element_by_xpath('//*[@id="ref-tree-container"]//span[text()="仓储中心-北京"]').click()

        # 点击确认
        driver.find_element_by_xpath(
            '//div[@class="el-dialog__wrapper custom-ref-dialog"]//button[@class="el-button el-button--primary"]').click()

        # # 输入考勤地点
        # driver.find_element_by_xpath('//div[@class="form-area"]//div[@class="el-row"]/div[3]//input').send_keys(
        #     "北京市海淀区西北旺镇用友产业园中区8D用友产业园(北京)")
        sleep(1)
        # 输入考勤地点距离
        length = random.randint(51, 4999)
        driver.find_element_by_xpath('//div[@class="form-area"]//div[@class="el-row"]/div[4]//input').send_keys(length)

        # 点击保存
        driver.find_element_by_xpath('//div[@class="form-area"]//button[@class="el-button el-button--primary"]').click()

        sleep(2)
        # 断言
        self.assertIn(str(length), driver.page_source)

        # 编辑打卡地点
        driver.find_element_by_xpath('//div[text()="{}"]/ancestor::tr//div[text()="编辑"]'.format(length)).click()
        sleep(3)

        # 点击保存
        driver.find_element_by_xpath('//div[@class="form-area"]//button[@class="el-button el-button--primary"]').click()
        sleep(3)
        # # 断言
        # text = driver.find_element_by_xpath('//div[text()="1234"]').text
        # self.assertEqual(text,"1234")

        # 点击停用按钮
        driver.find_element_by_xpath('//div[text()="{}"]/ancestor::tr//div[@class="operation"][2]'.format(length)).click()
        sleep(1)
        # 点击确认
        driver.find_element_by_xpath(
            '//div[@class="el-message-box"]//button[@class="el-button el-button--default el-button--small el-button--primary "]').click()
        sleep(1)
        # 点击启用按钮
        driver.find_element_by_xpath('//div[text()="{}"]/ancestor::tr//div[@class="operation"][2]'.format(length)).click()
        sleep(1)

        # 点击停用按钮
        driver.find_element_by_xpath('//div[text()="{}"]/ancestor::tr//div[@class="operation"][2]'.format(length)).click()
        sleep(1)

        # 点击确认
        driver.find_element_by_xpath(
            '//div[@class="el-message-box"]//button[@class="el-button el-button--default el-button--small el-button--primary "]').click()
        sleep(1)

        # 点击删除按钮
        driver.find_element_by_xpath('//div[text()="{}"]/ancestor::tr//div[text()="删除"]'.format(length)).click()

        # 点击确定
        driver.find_element_by_xpath(
            '//div[@class="el-message-box"]//button[@class="el-button el-button--default el-button--small el-button--primary "]').click()

        # 断言是否删除成功
        sleep(2)
        self.assertNotIn("{}".format(length), driver.page_source)
        # 关闭当前页面
        driver.switch_to.default_content()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()
