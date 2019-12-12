# -*-CodeIng:utf-8 -*-
# @time :2019/10/30 13:33
# @author:HuangJunTao
# @email:1341890679@qq.com
# @file:发薪方案.py
# @SoftWare:PyCharm

import random
from time import sleep

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from SRC.webdriver.switchTo import SwitchTo
from script.common import utils
from selenium.webdriver import ActionChains


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
        # driver.find_element_by_xpath('//*[@id="_dropdown_popcontainer"]/div/i').click()
        # driver.find_element_by_xpath('//*[@id="home_header"]//div[text()="UI测试专属"]').click()
        # driver.find_element_by_xpath(
        #     '//button[@class="u-button btn__style___37bsb u8c_primary__style___RFibc  btn__style___20DQM "]').click()
        # sleep(2)
        # 左上方公共节点
        driver.find_element_by_class_name('lebra-navbar-left-icon').click()
        sleep(2)
        # 进入社交协同
        driver.find_element_by_xpath('//*[text()="人力资源"]').click()
        sleep(2)
        # 进入一级节点
        menu2 = driver.find_element_by_css_selector('span[title="薪资核算"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(2)
        # 进入二级节点
        driver.find_element_by_xpath('//li[@title="发薪方案"]').click()
        sleep(2)
        # 跳转劳动合同签订iframe
        iframe = driver.find_element_by_id('HRXC030010')
        # # driver.switch_to.frame(iframe)
        SwitchTo(driver).frame(iframe)
        sleep(2)

        # 点击新增方案按钮
        driver.find_element_by_xpath(
            '//div[@class="fn-sort"]//button[4]').click()
        sleep(2)
        # 输入方案名称
        num = random.randint(100, 999)
        name = "方案名称{}".format(num)
        driver.find_element_by_xpath('//label[text()="方案名称"]/following-sibling::div//input').send_keys(name)

        # 点击所属组织右侧的按钮
        driver.find_element_by_xpath(
            '//label[text()="所属组织"]/following-sibling::div//span[@class="el-input__suffix"]').click()
        sleep(1.5)
        driver.find_element_by_xpath(
            '//*[@id="ref-tree-container"]/div/div/div/div[1]/div/div/div[1]/div[2]/div/div[1]/span[1]').click()
        # 点击选择条目
        driver.find_element_by_xpath(
            '//span[text()="仓储中心-北京"]/parent::span').click()

        # 点击确定按钮
        driver.find_element_by_xpath('//div[@class="op-button"]/button[2]').click()
        sleep(0.5)

        # 点击期间方案右侧的按钮
        driver.find_element_by_xpath(
            '//label[text()="期间方案"]/following-sibling::div//span[@class="el-input__suffix"]').click()
        sleep(1)
        # 点击选择条目
        driver.find_element_by_xpath(
            '//div[@class="ref-content-wrap ref-content-grid-wrap"]//tbody//tr[1]').click()

        # 点击确定按钮
        driver.find_element_by_xpath('//div[@class="op-button"]/button[2]').click()
        sleep(1)

        # 点击起始期间右侧按钮
        driver.find_element_by_xpath(
            '//label[text()="起始期间"]/following-sibling::div//span[@class="el-input__suffix"]').click()

        # 选择期间条目
        driver.find_element_by_xpath('//div[@class="el-col el-col-16"]//tbody//tr[1]').click()

        # 点击确定
        driver.find_element_by_xpath(
            '//div[@class="op-button"]/button[2]').click()
        sleep(1)

        # 输入方案说明
        driver.find_element_by_xpath('//textarea').send_keys("方案说明信息09929")
        # 点击保存按钮
        driver.find_element_by_xpath(
            '//div[@class="pp-container container-edit"]//div[@class="in-bottom"]//button[2]').click()
        sleep(0.75)
        self.assertEqual("操作成功！", driver.find_element_by_xpath('//p[text()="操作成功！"]').text)
        # 关闭当前页面
        driver.switch_to.default_content()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()
