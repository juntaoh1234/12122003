# coding=utf-8
from time import sleep

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from SRC.webdriver.switchTo import SwitchTo
from script.common import utils
from selenium.webdriver import ActionChains


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
        menu2 = driver.find_element_by_css_selector('span[title="员工管理"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(2)
        # 进入二级节点
        driver.find_element_by_xpath('//li[@title="入职报到办理"]').click()

        sleep(2)
        # 跳转转正办理iframe
        iframe = driver.find_element_by_id('HRGXFW020')
        # # driver.switch_to.frame(iframe)
        SwitchTo(driver).frame(iframe)
        sleep(2)

        # 点击入职办理

        driver.find_element_by_xpath('//div[@class="main-container"]//tbody/tr[1]//span[text()="入职办理"]').click()

        # 填写合同期限

        driver.find_element_by_xpath('//*[@id="termmonth"]').send_keys(12)

        # 点击确认入职
        driver.find_element_by_xpath('//span[text()="确认入职"]').click()

        # 点击取消
        driver.find_element_by_xpath('//button[text()="取消"]').click()

        # 再次点击确认入职
        driver.find_element_by_xpath('//span[text()="确认入职"]').click()

        # 点击确认
        driver.find_element_by_xpath('//button[text()="确认"]').click()
    # # 选择第一调数据
    # driver.find_element_by_xpath('//div[@class="main-container"]//tbody/tr[1]//label[1]').click()
    #
# # 点击确认入职
# driver.find_element_by_xpath('//button[text()="确认入职"]').click()
        # 关闭当前页面
        sleep(2)
        driver.switch_to.default_content()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()