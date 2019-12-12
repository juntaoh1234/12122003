# coding=utf-8
from time import sleep

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

        driver.find_element_by_xpath('//div[text()="审批中心"]').click()
        sleep(2)
        # 跳转模型管理iframe
        iframe = driver.find_element_by_id('XTSPZX0001')
        SwitchTo(driver).frame(iframe)
        sleep(2)
        driver.find_element_by_xpath('//div[@class="header"]//div').click()
        sleep(0.5)
        driver.find_element_by_xpath('//a[text()="增加应用"]').click()
        sleep(1)
        driver.find_element_by_xpath('//div[text()="财务管理"]/following-sibling::span').click()
        driver.find_element_by_xpath('//div[text()="人力云服务"]/following-sibling::span').click()
        driver.find_element_by_xpath('//div[text()="协同云服务"]/following-sibling::span').click()
        driver.find_element_by_xpath('//div[text()="费用管理"]/following-sibling::span').click()
        driver.find_element_by_xpath('//div[text()="采购供应"]/following-sibling::span').click()
        driver.find_element_by_xpath('//div[text()="营销管理"]/following-sibling::span').click()
        driver.find_element_by_xpath('//div[@class="operation"]/button[2]').click()
        sleep(2)
        # 关闭当前页面
        driver.switch_to.default_content()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()