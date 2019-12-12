# coding=utf-8
from time import sleep

from selenium.webdriver.common.keys import Keys

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from SRC.webdriver.switchTo import SwitchTo
from script.common import utils
from selenium.webdriver import ActionChains
from SRC.param.context import Name


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
        driver.find_element_by_xpath('//li[@title="离职办理"]').click()

        sleep(2)
        # 跳转离职办理iframe
        iframe = driver.find_element_by_id('HRGXFW060')
        # # driver.switch_to.frame(iframe)
        SwitchTo(driver).frame(iframe)
        sleep(2)

        # 点击员工主动离职
        driver.find_element_by_xpath('//*[@id="listPanel"]//button[text()="员工主动离职"]').click()

        sleep(2)

        # 点击转正员工输入框

        driver.find_element_by_xpath('//*[@id="20180529155007gKfOl8qbEC"]').send_keys(Name.random_name)
        # driver.find_element_by_xpath('//*[@id="20180730174750cYVuonidOU"]').send_keys("戴英")
        print(Name.random_name)
        setattr(Name, "random_name", None)
        driver.find_element_by_xpath('//*[@id="20180529155007gKfOl8qbEC"]').click()
        sleep(5)
        driver.find_element_by_xpath('//*[@id="20180529155007gKfOl8qbEC"]').send_keys(Keys.ENTER)

        # 点击计划最后的工作日
        driver.find_element_by_xpath('//*[@id="edit_20180510152621sHbkJISpBo"]/div/span[1]').click()

        # 选择当前天
        driver.find_element_by_xpath(
            '//div[@class="u-date-panel is-visible"]//div[@class="u-date-cell current"]').click()

        # 点击离职原因右侧的按钮
        driver.find_element_by_xpath('//*[@id="edit_20180517152204BCcJyrup7B"]/div/span[1]').click()

        # 选择离职的原因
        driver.find_element_by_xpath(
            '//span[text()="离职原因"]/ancestor::div[@class="outerContainer"]//td[text()="4001001"]').click()

        # 点击离职去向右侧的按钮
        driver.find_element_by_xpath('//*[@id="edit_20180605201739Txr3Uko5Sb"]/div/span[1]').click()

        # 选择离职去向
        driver.find_element_by_xpath(
            '//span[text()="离职去向"]/ancestor::div[@class="outerContainer"]//td[text()="自主创业"]').click()

        # 输入离职说明
        dsc = '世界那么大，我想去看看'
        driver.find_element_by_xpath('//*[@id="20180517152256SG6V78uzpc"]').send_keys(dsc)

        # 点击提交按钮
        sleep(1)
        driver.find_element_by_xpath('//*[@id="templatePanel"]//span[text()="提交"]').click()
        sleep(2)
        # 关闭当前页面
        driver.switch_to.default_content()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()