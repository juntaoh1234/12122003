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
        driver.find_element_by_xpath('//li[@title="劳动合同签订"]').click()

        sleep(2)
        # 跳转劳动合同签订iframe
        iframe = driver.find_element_by_id('HRGXFW090')
        # # driver.switch_to.frame(iframe)
        SwitchTo(driver).frame(iframe)
        sleep(2)

        # 点击新增按钮
        driver.find_element_by_xpath('//*[@id="flowApprove"]//button[@class="btn btn-primary"]').click()
        sleep(2)
        # 点击新员工tab页签
        driver.find_element_by_xpath('//*[@id="staffNewSpan"]').click()

        # 输入查询数据
        driver.find_element_by_xpath('//*[@id="searchValNew"]').send_keys(context.Name.random_name)

        # 点击查询
        driver.find_element_by_xpath('//*[@id="searchBtn1"]/span/i[2]').click()

        # 点击第一条数据
        driver.find_element_by_xpath('//*[@id="addSignsDialog"]//div[@id="staffNewBody"]//tbody//td[1]//label').click()

        # 点击确定按钮
        driver.find_element_by_xpath('//*[@id="addSignsDialog"]//span[text()="确定"]').click()
        sleep(1)

        # 点击右侧的按钮
        driver.find_element_by_xpath(
            '//div[@title="合同开始日期"]/ancestor::fieldset//span[@class="u-form-control-feedback fa fa-calendar"]').click()

        # 点击时间框
        driver.find_element_by_xpath(
            '//*[@id="edit_20180621092332a9Wovv11gh"]//div[@class="u-date-cell current"]').click()

        # 点击输入合同期限
        driver.find_element_by_xpath('//*[@id="20180621092344dfpzcwrr5o"]').send_keys("6")

        # 选择合同信息
        driver.find_element_by_xpath('//*[@id="edit_20180621092410s9ne5T2NrC"]/div/span[1]').click()

        # 选择合同
        driver.find_element_by_xpath('//*[@id="refContainer20180621092410s9ne5T2NrC"]//td[text()="0001"]').click()

        # 输入工作地点

        driver.find_element_by_xpath('//*[@id="edit_20180621092415N32bSEPxgw"]/div/span[1]').click()

        # 选择工作地点
        driver.find_element_by_xpath('//*[@id="refContainer20180621092415N32bSEPxgw"]//td[text()="123"]').click()

        # 点击试用期期限
        driver.find_element_by_xpath('//*[@id="20180621092425fw1gM2Tz5j"]').send_keys(1)

        # 输入备注内容
        # 输入随机内容
        paragraph = context.get_paragraph()
        driver.find_element_by_xpath('//*[@id="20180621092453tCQEAbvHU1"]').send_keys(paragraph)

        # 点击保存按钮
        driver.find_element_by_xpath('//*[@id="templatePanel"]/div[4]/button//span[text()="保存"]').click()
        sleep(3)

        # 点击提交按钮
        driver.find_element_by_xpath('//*[@id="templatePanel"]//button//span[text()="提交"]').click()
        sleep(2)
        # 关闭当前页面
        driver.switch_to.default_content()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()