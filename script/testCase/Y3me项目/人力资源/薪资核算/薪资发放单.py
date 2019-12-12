# -*-CodeIng:utf-8 -*-
# @time :2019/10/30 13:35
# @author:HuangJunTao
# @email:1341890679@qq.com
# @file:薪资发放单.py
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
        driver.find_element_by_xpath('//li[@title="薪资发放单"]').click()
        sleep(2)
        # 跳转劳动合同签订iframe
        iframe = driver.find_element_by_id('HRXC030030')
        # # driver.switch_to.frame(iframe)
        SwitchTo(driver).frame(iframe)
        sleep(2)

        # 点击新增按钮
        driver.find_element_by_xpath('//span[text()="新建发放单"]').click()
        sleep(2)

        # 点击所属组织右侧的按钮
        driver.find_element_by_xpath(
            '//label[text()="所属组织"]/following-sibling::div//span[@class="el-input__suffix"]').click()
        sleep(1.5)
        # 点击选择条目
        driver.find_element_by_xpath(
            '//span[text()="仓储中心-北京"]/parent::span').click()

        # 点击确定按钮
        driver.find_element_by_xpath('//div[@class="op-button"]/button[2]').click()
        sleep(0.5)

        # 点击薪资方案右侧的按钮
        driver.find_element_by_xpath(
            '//label[text()="薪资方案"]/following-sibling::div//span[@class="el-input__suffix"]').click()
        sleep(1.5)
        # 选择薪资方案条目
        driver.find_element_by_xpath('//div[@class="el-table__body-wrapper is-scrolling-none"]//tr[1]').click()

        # 点击确定按钮
        driver.find_element_by_xpath('//div[@class="op-button"]/button[2]').click()
        sleep(0.5)

        # 点击发薪期间按钮
        driver.find_element_by_xpath(
            '//label[text()="发薪期间"]/following-sibling::div//span[@class="el-input__suffix"]').click()

        sleep(1.5)
        # 点击条目
        driver.find_element_by_xpath(
            '//div[@class="el-col el-col-16"]//tbody//tr/td/div[contains(text(),"12-01")]').click()

        # 点击确定按钮
        driver.find_element_by_xpath('//div[@class="op-button"]/button[2]').click()
        sleep(0.5)

        num = random.randint(100, 999)
        name = "申请单{}".format(num)
        # 输入发放单名称
        driver.find_element_by_xpath(
            '//label[text()="发放单名称"]/following-sibling::div//input').send_keys(name)
        # 输入发放说明信息
        driver.find_element_by_xpath('//textarea').send_keys("发放说明信息48393498")

        # 点击下一步
        driver.find_element_by_xpath('//span[text()="下一步"]').click()
        sleep(1)
        # 点击下一步
        driver.find_element_by_xpath('//span[text()="下一步"]').click()
        sleep(3)

        # 点击全选按钮
        driver.find_element_by_xpath(
            '//h3[contains(text(),"待选发薪人员")]/parent::div//span[text()="人员编码"]/ancestor::th/preceding-sibling::th//span[@class="el-checkbox__inner"]').click()
        sleep(1)
        # 点击选到右边的按钮
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[1]/i').click()

        # 点击保存
        driver.find_element_by_xpath('//div[@class="el-row"]/div/button[2]').click()
        sleep(3)
        # 点击计算按钮
        driver.find_element_by_xpath('//div[@class="nav-bottom"]//span[text()="计算"]').click()
        sleep(1)
        # 点击确定计算
        driver.find_element_by_xpath('//span[@class="dialog-footer"]//span[text()="计算"]').click()
        sleep(3)
        # 点击审核
        driver.find_element_by_xpath('//div[@class="nav-bottom"]//span[text()="审核"]').click()
        sleep(1)
        # 点击审核
        driver.find_element_by_xpath('//span[@class="dialog-footer"]//span[text()="审核"]').click()
        sleep(3)
        # 点击提交按钮
        driver.find_element_by_xpath('//span[text()="提交"]').click()

        # 点击确定
        driver.find_element_by_xpath('//div[@class="el-message-box__btns"]/button[2]').click()
        sleep(2)
        # 关闭当前页面
        driver.switch_to.default_content()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()