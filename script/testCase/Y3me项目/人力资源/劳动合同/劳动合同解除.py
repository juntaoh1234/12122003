# coding=utf-8
from time import sleep

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from SRC.webdriver.switchTo import SwitchTo
from script.common import utils
from selenium.webdriver import ActionChains
from SRC.param import context


class EasyCase(TestCase):
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
        sleep(2)
        # 进入一级节点
        menu2 = driver.find_element_by_css_selector('span[title="劳动合同"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(2)
        # 进入二级节点
        driver.find_element_by_xpath('//li[@title="劳动合同解除"]').click()

        sleep(2)
        # 跳转劳动合同签订iframe
        iframe = driver.find_element_by_id('HRGXFW020040')
        # # driver.switch_to.frame(iframe)
        SwitchTo(driver).frame(iframe)
        sleep(2)

        # 点击新增按钮
        driver.find_element_by_xpath('//*[@id="flowApprove"]//button[@class="btn btn-primary"]').click()
        sleep(2)

        # 点击左侧书按钮
        driver.find_element_by_xpath('//span[@class="button level0 switch noline_close"]').click()

        # 点击二级的左侧树按钮
        driver.find_element_by_xpath('//span[text()="仓储中心-北京"]/ancestor::a/preceding-sibling::span').click()

        # 选择组织信息
        driver.find_element_by_xpath('//span[text()="仓储中心-北京"]/ancestor::a/following-sibling::ul//span[text()="仓储中心-北京"]').click()
        sleep(1)
        # 搜索框输入信息

        driver.find_element_by_xpath('//*[@id="searchVal"]').send_keys(context.Name.random_name)
        # driver.find_element_by_xpath('//*[@id="searchVal"]').send_keys("戴英")

        # 点击搜索按钮
        driver.find_element_by_xpath('//*[@id="searchBtn"]/span/i[2]').click()

        # 点击选中第一个
        driver.find_element_by_xpath('//*[@id="staffAllBody"]/div[2]/table/tbody/tr/td[1]/div/div/label').click()

        # 点击确定按钮
        driver.find_element_by_xpath('//*[@id="addSignsDialog"]//button[@class="btn btn-primary"]').click()

        sleep(3)

        # 输入解除原因
        # driver.find_element_by_xpath('//*[@id="edit_201901111404244vjRbIDmR8"]/div/span').click()
        # driver.find_element_by_xpath('')

        # 输入经济补偿金
        driver.find_element_by_xpath(
            '//div[@id="eidt_20190111140430sFoT9PAE1X"]//input[@class="u-form-control ui-form-control fl text-right ui-text-left"]').send_keys(
            10000)

        # 输入补偿金
        driver.find_element_by_xpath(
            '//div[@id="eidt_20190111140431914mpEyXCu"]//input[@class="u-form-control ui-form-control fl text-right ui-text-left"]').send_keys(
            10000)

        # 点击解除日期按钮

        driver.find_element_by_xpath('//*[@id="edit_20190111140414sRBCMJuXDC"]/div/span[1]').click()
        driver.find_element_by_xpath(
            '//*[@id="edit_20190111140414sRBCMJuXDC"]//div[@class="u-date-panel is-visible"]//div[@class="u-date-cell current"]').click()

        # 点击保存按钮
        driver.find_element_by_xpath('//span[text()="保存"]/ancestor::button').click()
        sleep(3)
        text = driver.find_element_by_xpath('//*[@id="templatePanel"]//button/span[text()="编辑"]').text
        self.assertEqual("编辑", text)

        # 点击提交按钮
        driver.find_element_by_xpath('//span[text()="提交"]/ancestor::button').click()
        sleep(2)
        # 关闭当前页面
        driver.switch_to.default_content()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()