# -*-CodeIng:utf-8 -*-
# @time :2019/10/30 13:32
# @author:HuangJunTao
# @email:1341890679@qq.com
# @file:定调资申请.py
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
        driver.find_element_by_xpath('//li[@title="定调资申请"]').click()
        sleep(2)
        # 跳转劳动合同签订iframe
        iframe = driver.find_element_by_id('HRXC020010')
        # # driver.switch_to.frame(iframe)
        SwitchTo(driver).frame(iframe)
        sleep(2)

        # 点击新增按钮
        driver.find_element_by_xpath('//div[@class= "el-row"]//button').click()
        sleep(2)
        num = random.randint(100, 999)
        name = "申请单{}".format(num)
        # 输入申请单名称
        driver.find_element_by_xpath(
            '//label[text()="申请单名称"]/following-sibling::div//input').send_keys(name)

        # 点击所属组织右侧的按钮
        driver.find_element_by_xpath(
            '//label[text()="所属组织"]/following-sibling::div//span[@class="el-input__suffix"]').click()
        sleep(1)
        # 点击选择条目
        driver.find_element_by_xpath(
            '//span[text()="仓储中心-北京"]/parent::span').click()

        # 点击确定按钮
        driver.find_element_by_xpath('//div[@class="op-button"]/button[2]').click()
        sleep(0.5)

        # 点击新增人员
        driver.find_element_by_xpath(
            '//span[text()="新增人员"]').click()
        sleep(2)
        # 选择人员
        driver.find_element_by_xpath('//*[@id="ref-tree-grid-container"]//div[3]/table/tbody/tr[1]/td[1]//label').click()

        # 点击确定
        driver.find_element_by_xpath('//div[@class="op-button"]//button[2]').click()
        sleep(1)

        # 点击全选按钮
        driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/div/div[5]/div[1]/table/thead/tr[1]/th[1]/div/label/span/span').click()
        sleep(1)

        # 点击批量修改
        driver.find_element_by_xpath('//button[@class="el-button el-button--info"]//span[text()="批量修改"]').click()

        # 点击时间
        driver.find_element_by_xpath('//span[text()="按生效日期"]/preceding-sibling::span/span').click()

        # 点击生效日期右侧的按钮
        driver.find_element_by_xpath(
            '//label[text()="生效日期"]/following-sibling::div//i[@class="el-input__icon iconfont wui-Calendar_bold"]').click()

        # 选择当天
        driver.find_element_by_xpath('//td[@class="available today"]/div/span').click()

        # 点击薪资项目右侧按钮
        driver.find_element_by_xpath(
            '//label[text()="薪资项目"]/following-sibling::div//span[@class="el-input__suffix"]').click()
        sleep(1)

        # 选择项目
        driver.find_element_by_xpath('//*[@id="ref-tree-grid-container"]//div[3]/table//tr[1]').click()

        # 点击确定按钮
        driver.find_element_by_xpath('//div[@class="op-button"]//button[2]').click()

        # # 输入变动原因
        # driver.find_element_by_xpath('//textarea').send_keys("变动原因123456")

        # 输入变动金额
        driver.find_element_by_xpath('//label[text()="申请金额"]/following-sibling::div//input').send_keys(80000)

        # 点击确定
        driver.find_element_by_xpath(
            '//div[@class="dialog-footer"]//button[@class="el-button el-button--primary"]').click()

        # 点击保存
        driver.find_element_by_xpath('//div[@style="float: right;"]//button[2]').click()
        sleep(1)
        # 点击提交
        driver.find_element_by_xpath('//div[@class="salary-apply-card-top-header-right"]//button[3]').click()
        sleep(1)
        self.assertEqual("提交成功!", driver.find_element_by_xpath('//p[text()="提交成功!"]').text)
        # 关闭当前页面
        driver.switch_to.default_content()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()