# -*-CodeIng:utf-8 -*-
# @time :2019/10/30 13:35
# @author:HuangJunTao
# @email:1341890679@qq.com
# @file:发薪人员.py
# @SoftWare:PyCharm

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
        driver.find_element_by_xpath('//li[@title="发薪人员"]').click()
        sleep(2)
        # 跳转劳动合同签订iframe
        iframe = driver.find_element_by_id('HRXC030020')
        # # driver.switch_to.frame(iframe)
        SwitchTo(driver).frame(iframe)
        sleep(2)

        # 点击第一行的人员
        driver.find_element_by_xpath(
            '//tbody/tr[1]/td[3]/div/span').click()
        sleep(2)
        # 点击新增
        driver.find_element_by_xpath('//div[@class="salary-staff-card"]/div[2]//button').click()
        sleep(1)
        # 点击选择条目
        driver.find_element_by_xpath('//div[@style="height: 330px;"]//div[3]/table//tr[1]').click()

        # 点击确定按钮
        driver.find_element_by_xpath('//div[@class="op-button"]/button[2]').click()
        sleep(2)
        # 选择日期
        driver.find_element_by_xpath(
            '//label[text()="开始时间"]/following-sibling::div//i[@class="el-input__icon iconfont wui-Calendar_bold"]').click()

        # 选择当天
        driver.find_element_by_xpath('//table[@class="el-date-table"]//td[@class="available today"]').click()

        driver.find_element_by_xpath('//span[text()="保存"]').click()
        sleep(2)
        # 点击新增
        driver.find_element_by_xpath('//div[@class="salary-staff-card"]/div[3]//button').click()
        sleep(1)

        # 点击选择条目
        driver.find_element_by_xpath(
            '//*[@id="ref-tree-grid-container"]//div[3]/table//tr[1]').click()

        # 点击确定按钮
        driver.find_element_by_xpath('//div[@class="op-button"]/button[2]').click()
        sleep(2)
        # 选择日期
        driver.find_element_by_xpath(
            '//label[text()="开始时间"]/following-sibling::div//i[@class="el-input__icon iconfont wui-Calendar_bold"]').click()

        # 选择当天
        driver.find_element_by_xpath('//table[@class="el-date-table"]//td[@class="available today"]').click()
        sleep(2)
        driver.find_element_by_xpath('//label[text()="金额"]/following-sibling::div//input').send_keys(10000)
        driver.find_element_by_xpath('//span[text()="保存"]').click()
        # 关闭当前页面
        driver.switch_to.default_content()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()