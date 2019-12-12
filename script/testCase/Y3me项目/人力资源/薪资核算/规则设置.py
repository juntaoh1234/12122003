# -*-CodeIng:utf-8 -*-
# @time :2019/10/29 16:04
# @author:HuangJunTao
# @email:1341890679@qq.com
# @file:规则设置.py
# @SoftWare:PyCharm
from time import sleep
from selenium.webdriver import ActionChains
from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from SRC.webdriver.switchTo import SwitchTo
from script.common import utils


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
        driver.find_element_by_xpath('//li[@title="规则设置"]').click()
        sleep(2)
        # 跳转劳动合同签订iframe
        iframe = driver.find_element_by_id('HRXC010010')
        # # driver.switch_to.frame(iframe)
        SwitchTo(driver).frame(iframe)
        sleep(2)

        # # 点击公共薪资项目管控模式右侧的按钮
        # driver.find_element_by_xpath(
        #     '//span[text()="公共薪资项目管控模式:"]/ancestor::div[@class="ref-col el-col el-col-24"]//i[@class = "el-select__caret el-input__icon el-icon-arrow-up"]').click()
        # sleep(2)
        # # 选择条目
        # driver.find_element_by_xpath(
        #     '//div[@class="el-autocomplete-suggestion"]/following-sibling::div//li[1]').click()

        # 点击薪资方案管控模式右侧的按钮
        driver.find_element_by_xpath(
            '//span[text()="薪资方案管控模式:"]/ancestor::div[@class="ref-col el-col el-col-24"]//i[@class = "el-select__caret el-input__icon el-icon-arrow-up"]').click()
        sleep(1)
        # 点击选择条目
        driver.find_element_by_xpath(
            '//div[@class="el-autocomplete-suggestion"]/following-sibling::div//li[2]').click()
        #
        # # 点击放弃按钮
        # driver.find_element_by_xpath('//span[text()="放弃"]').click()
        # sleep(2)
        #
        # # 弹出框 点击放弃保存
        # driver.find_element_by_xpath(
        #     '//div[@role="dialog"]//button[@class="el-button el-button--default el-button--small el-button--primary "]').click()
        # sleep(1)
        # 点击保存按钮
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/button[2]').click()
        sleep(0.75)
        self.assertEqual("操作成功", driver.find_element_by_xpath('//p[text()="操作成功"]').text)

        # 切换全局组织参数页签
        driver.find_element_by_xpath('//div[text()="全局/组织参数"]').click()

        # # 点击选择下级按钮
        # driver.find_element_by_xpath('//div[text()="控制下级"]//span[@class="el-switch__core"]').click()
        # ele = driver.find_element_by_xpath('//div[text()="控制下级"]//input[@type="text"]')
        # self.assertIsNotNone(ele)

        # 点击放弃按钮
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/button[1]').click()
        sleep(1)

        # 弹出框 点击取消
        driver.find_element_by_xpath('//div[@role="dialog"]//div[@class="el-message-box__btns"]//button[1]').click()
        sleep(0.5)
        # 点击保存
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/button[2]').click()
        sleep(1)
        self.assertEqual("操作成功", driver.find_element_by_xpath('//p[text()="操作成功"]').text)
        sleep(2)
        # 关闭当前页面
        driver.switch_to.default_content()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()