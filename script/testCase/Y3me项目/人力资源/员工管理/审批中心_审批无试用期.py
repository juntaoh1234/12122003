# coding=utf-8
from time import sleep

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from SRC.webdriver.switchTo import SwitchTo


class EasyCase(TestCase):
    def __init__(self, webDriver, paramsList):
        # 请不要修改该方法124421
        super(EasyCase, self).__init__(webDriver, paramsList)

    @codeException_dec('3')
    def runTest(self):
        driver = self.getDriver()
        driver.implicitly_wait(30)
        driver.refresh()
        # driver.find_element_by_xpath('//*[@id="_dropdown_popcontainer"]/div/i').click()
        # driver.find_element_by_xpath('//*[@id="home_header"]//div[text()="UI测试专属"]').click()
        # driver.find_element_by_xpath('//button[@class="u-button btn__style___37bsb u8c_primary__style___RFibc  btn__style___20DQM "]').click()
        # sleep(2)

        # 第一次审批********************************
        driver.find_element_by_xpath('//div[text()="审批中心"]').click()

        # 跳转iframe
        iframe = driver.find_element_by_id('XTSPZX0001')
        SwitchTo(driver).frame(iframe)
        sleep(2)

        # 点击同意按钮
        driver.find_element_by_xpath('//div[@class="listContainer"]/div[1]//div[text()="同意"]').click()

        # # 点击审批中心关闭按钮
        # driver.find_element_by_xpath('//div[@class="close--MQT19"]//i').click()

        # 第二次审批**********************************
        driver.refresh()
        driver.find_element_by_xpath('//div[text()="审批中心"]').click()

        # 跳转iframe
        iframe = driver.find_element_by_id('XTSPZX0001')
        SwitchTo(driver).frame(iframe)
        sleep(2)

        # 点击同意按钮
        driver.find_element_by_xpath('//div[@class="listContainer"]/div[1]//div[text()="同意"]').click()

        # 第三次审批**********************************
        driver.refresh()
        driver.find_element_by_xpath('//div[text()="审批中心"]').click()

        # 跳转iframe
        iframe = driver.find_element_by_id('XTSPZX0001')
        SwitchTo(driver).frame(iframe)
        sleep(2)

        # 点击进入单据详情
        driver.find_element_by_xpath(
            '//div[@class="listContainer"]/div[1]//div[@class="remarkMsg mb-flex remarkRetract"]').click()
        sleep(5)
        # 点击接受offer
        driver.find_element_by_xpath('//*[@id="acceptOffer"]').click()
        sleep(5)
        # 点击提交按钮
        driver.find_element_by_xpath('//*[@id="commitOffer"]').click()

        sleep(5)
        # 点击进入单据详情
        driver.find_element_by_xpath(
            '//div[@class="listContainer"]/div[1]//div[@class="remarkMsg mb-flex remarkRetract"]').click()
        sleep(3)
        # 输入合同期限
        driver.find_element_by_xpath('//*[@id="termmonth"]').send_keys("12")

        # # 输入试用期期限***********************************************
        # driver.find_element_by_xpath('//*[@id="promonth"]').send_keys(1)

        # 点击确认入职
        driver.find_element_by_xpath('//*[@id="rz_handler"]').click()

        # 点击确定按钮
        driver.find_element_by_xpath('//button[@class="btn btn-primary" and text()="确认"]').click()
        sleep(3)
        # 关闭当前页面
        driver.switch_to.default_content()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()
