# coding=utf-8
from time import sleep

from selenium.webdriver.common.keys import Keys

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
        driver.find_element_by_xpath('//li[@title="劳动合同续签"]').click()

        sleep(2)
        # 跳转劳动合同签订iframe
        iframe = driver.find_element_by_id('HRGXFW110')
        # # driver.switch_to.frame(iframe)
        SwitchTo(driver).frame(iframe)
        sleep(2)

        # 点击新增按钮
        driver.find_element_by_xpath('//*[@id="flowApprove"]//button[@class="btn btn-primary"]').click()
        sleep(2)
        # 输入员工信息
        driver.find_element_by_xpath('//*[@id="searchVal"]').send_keys(context.Name.random_name)
        # driver.find_element_by_xpath('//*[@id="20180621192702NpniVowGaI"]').send_keys("戴英")
        # driver.find_element_by_xpath('//*[@id="searchVal"]').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="searchVal"]').send_keys(Keys.ENTER)
        driver.find_element_by_xpath('//*[@id="staffAllBody"]/div[2]/table/tbody/tr/td[1]/div/div/label').click()

        # 点击确定
        sleep(1)
        driver.find_element_by_xpath('//div[@class="modal-footer"]//button[@class="btn btn-primary"]').click()

        # 输入签订日期
        driver.find_element_by_xpath('//*[@id="edit_20180621192735yOPB73tQ1J"]/div/span[1]').click()
        driver.find_element_by_xpath('//*[@id="edit_20180621192735yOPB73tQ1J"]/div/div/div[1]/div/div/div/div[1]').click()
        sleep(0.5)
        driver.find_element_by_xpath('//*[@id="edit_20180621192735yOPB73tQ1J"]/div/div/div[1]/div/div/div[2]/div[12]').click()
        sleep(0.5)
        driver.find_element_by_xpath('//*[@id="edit_20180621192735yOPB73tQ1J"]/div/div/div[1]/div/div/div[2]/div[12]').click()
        sleep(0.5)
        driver.find_element_by_xpath(
            '//*[@id="edit_20180621192735yOPB73tQ1J"]//div[@class="u-date-panel is-visible"]//div[@class="u-date-cell current"]').click()

        # 输入合同开始日期
        driver.find_element_by_xpath('//*[@id="edit_20180621192744bUtHIJSxgW"]/div/span[1]').click()
        driver.find_element_by_xpath('//*[@id="edit_20180621192744bUtHIJSxgW"]/div/div/div[1]/div/div/div[1]/div[1]').click()
        sleep(0.5)
        driver.find_element_by_xpath('//*[@id="edit_20180621192744bUtHIJSxgW"]/div/div/div[1]/div/div/div[2]/div[12]').click()
        sleep(0.5)
        driver.find_element_by_xpath('//*[@id="edit_20180621192744bUtHIJSxgW"]/div/div/div[1]/div/div/div[2]/div[12]').click()
        sleep(0.5)
        driver.find_element_by_xpath(
            '//*[@id="edit_20180621192744bUtHIJSxgW"]//div[@class="u-date-panel is-visible"]//div[@class="u-date-cell current"]').click()

        # 输入合同期限
        driver.find_element_by_xpath('//*[@id="20180621192746amEPBBYzuc"]').send_keys(24)

        # 输入合同
        driver.find_element_by_xpath('//*[@id="edit_20180621192753n2mwSiT6Fv"]/div/span[1]').click()

        # 选择条目
        driver.find_element_by_xpath(
            '//*[@id="refContainer20180621192753n2mwSiT6Fv"]/div/div/div[2]/ul[3]/div/div[1]/div[2]/div[2]/div[1]/table/tbody/tr[1]').click()
        # 输入工作地点
        driver.find_element_by_xpath('//*[@id="edit_201806211927544Ff3WSQIEr"]/div/span[1]').click()

        # 选择条目
        driver.find_element_by_xpath(
            '//*[@id="refContainer201806211927544Ff3WSQIEr"]/div/div/div[2]/ul[3]/div/div[1]/div[2]/div[2]/div[1]/table/tbody/tr[1]').click()

        # 点击输入备注信息
        desc = context.get_paragraph()
        driver.find_element_by_xpath('//*[@id="20180621192757joRkiYUBhD"]').send_keys(desc)

        # 点击保存按钮
        driver.find_element_by_xpath('//*[@id="templatePanel"]//button/span[text()="保存"]').click()
        sleep(3)
        text = driver.find_element_by_xpath('//*[@id="templatePanel"]//button/span[text()="编辑"]').text
        self.assertEqual("编辑", text)

        # 点击提交按钮
        driver.find_element_by_xpath('//*[@id="templatePanel"]//button/span[text()="提交"]').click()
        sleep(2)
        # 关闭当前页面
        driver.switch_to.default_content()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()
