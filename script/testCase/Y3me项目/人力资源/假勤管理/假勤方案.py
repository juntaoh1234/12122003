# -*-CodeIng:utf-8 -*-
# @time :2019/10/22 19:42
# @author:HuangJunTao
# @email:1341890679@qq.com
import random
from time import sleep

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from SRC.webdriver.switchTo import SwitchTo
from script.common import utils
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from SRC.param import context
from SRC.param.context import Name


class EasyCase(TestCase, Name):
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
        # driver.find_element_by_xpath('//*[@id="_dropdown_popcontainer"]/div/i').click()
        # driver.find_element_by_xpath('//*[@id="home_header"]//div[text()="UI测试专属"]').click()
        # driver.find_element_by_xpath('//button[@class="u-button btn__style___37bsb u8c_primary__style___RFibc  btn__style___20DQM "]').click()
        # sleep(2)
        # 左上方公共节点
        driver.find_element_by_class_name('lebra-navbar-left-icon').click()
        sleep(2)
        # 进入社交协同
        driver.find_element_by_xpath('//*[text()="人力资源"]').click()
        sleep(1)
        # 进入一级节点
        menu2 = driver.find_element_by_css_selector('span[title="假勤管理"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(1)
        # 进入二级节点
        driver.find_element_by_xpath('//li[@title="假勤方案"]').click()
        sleep(2)

        # 跳转假勤方案iframe
        iframe = driver.find_element_by_id('HRJQ020090')
        # # driver.switch_to.frame(iframe)
        SwitchTo(driver).frame(iframe)
        sleep(1)
        source = driver.page_source
        str1 = 'new假勤方案'

        # 点击新建假勤方案
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/div[1]/ul/li[1]').click()
        sleep(2)

        # 点击组织按钮
        driver.find_element_by_xpath('//*[@id="c37"]/div/span/span/span/i[2]').click()

        # 点击组织展开按钮
        driver.find_element_by_xpath(
            '//span[text()="所属组织"]/ancestor::div[@role="dialog"]//div[@role="group"]/div[1]/div/span[1]').click()

        # 点击组织
        driver.find_element_by_xpath(
            '//span[text()="所属组织"]/ancestor::div[@role="dialog"]//div[@role="group"]/div[1]/div/span[2]').click()

        # 点击确定按钮
        driver.find_element_by_xpath(
            '//span[text()="所属组织"]/ancestor::div[@role="dialog"]//button[@class="el-button el-button--primary"]').click()
        sleep(1)
        # 输入姓名
        num = random.randint(1000, 9999)
        name = "new假勤方案{}".format(num)
        driver.find_element_by_xpath('//label[text()="名称:"]/parent::div//input').send_keys(name)

        # 点击组织按钮
        driver.find_element_by_xpath('//label[text()="适用范围"]/parent::div//span[text()="选组织"]').click()
        sleep(3)
        # 选择北京仓储中心
        driver.find_element_by_xpath(
            '//span[text()="仓储中心-北京"]/ancestor::div[@class="el-tree-node__content"]/label/span').click()
        sleep(1)

        # 点击确定按钮
        driver.find_element_by_xpath('//div[@role="dialog"]//button[@class="el-button el-button--primary"]').click()

        # 点击保存按钮
        driver.find_element_by_xpath('//button[@class="el-button el-button--primary"]/span[text()="保存"]').click()
        sleep(2)

        if source.find(str1) >= 0:
            driver.find_element_by_xpath('//div[5]/div/div[3]/button[2]/span').click()

        # # 点击覆盖按钮
        # driver.find_element_by_xpath('//span[text()="提示"]/ancestor::div[@class="el-message-box"]//button[@class="el-button el-button--default el-button--small el-button--primary "]').click()
        #  断言

        driver.find_element_by_xpath('//span[text()="{}"]'.format(name)).click()
        # 点击编辑
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]/button').click()
        # # 点击组织按钮
        # driver.find_element_by_xpath('//label[text()="适用范围"]/parent::div//span[text()="选组织"]').click()
        # sleep(3)
        # 选择北京仓储中心
        # sleep(1)
        # driver.find_element_by_xpath('//span[text()="仓储中心-北京"]/ancestor::div[@class="el-tree-node__content"]/label/span').click()
        # # 点击确定按钮
        # driver.find_element_by_xpath('//div[@role="dialog"]//button[@class="el-button el-button--primary"]').click()

        # 点击保存按钮
        driver.find_element_by_xpath('//button[@class="el-button el-button--primary"]/span[text()="保存"]').click()

        # # 点击覆盖按钮
        # driver.find_element_by_xpath('//span[text()="提示"]/ancestor::div[@class="el-message-box"]//button[@class="el-button el-button--default el-button--small el-button--primary "]').click()

        # 点击删除
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/div[1]/ul/li[2]').click()

        # 弹出框点击确认
        driver.find_element_by_xpath(
            '//div[@aria-label="提示"]//button[@class="el-button el-button--default el-button--small el-button--primary "]').click()
        sleep(0.5)

        text_dele = driver.find_element_by_xpath('/html/body/div[5]/p').text

        self.assertEqual("删除成功!", text_dele)

        # 点击新建假勤方案
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/div[1]/ul/li[1]').click()
        sleep(2)

        # 点击组织按钮
        driver.find_element_by_xpath('//*[@id="c37"]/div/span/span/span/i[2]').click()

        # 点击组织展开按钮
        driver.find_element_by_xpath(
            '//span[text()="所属组织"]/ancestor::div[@role="dialog"]//div[@role="group"]/div[1]/div/span[1]').click()

        # 点击组织
        driver.find_element_by_xpath(
            '//span[text()="所属组织"]/ancestor::div[@role="dialog"]//div[@role="group"]/div[1]/div/span[2]').click()

        # 点击确定按钮
        driver.find_element_by_xpath(
            '//span[text()="所属组织"]/ancestor::div[@role="dialog"]//button[@class="el-button el-button--primary"]').click()
        sleep(1)
        # 输入姓名
        num = random.randint(1000, 9999)
        name = "new假勤方案{}".format(num)
        driver.find_element_by_xpath('//label[text()="名称:"]/parent::div//input').send_keys(name)

        # 点击组织按钮
        driver.find_element_by_xpath('//label[text()="适用范围"]/parent::div//span[text()="选组织"]').click()
        sleep(3)
        # 选择北京仓储中心
        driver.find_element_by_xpath(
            '//span[text()="仓储中心-北京"]/ancestor::div[@class="el-tree-node__content"]/label/span').click()
        sleep(1)

        # 点击确定按钮
        driver.find_element_by_xpath('//div[@role="dialog"]//button[@class="el-button el-button--primary"]').click()

        # 点击保存按钮
        driver.find_element_by_xpath('//button[@class="el-button el-button--primary"]/span[text()="保存"]').click()
        sleep(2)
        # 关闭当前页面
        driver.switch_to.default_content()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()
