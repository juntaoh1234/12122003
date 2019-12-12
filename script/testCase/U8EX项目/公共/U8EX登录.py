# coding=utf-8
from time import time, sleep
from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from script.common import utils
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


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

        # 登录
        driver.get('https://yonsuite.diwork.com/#/')
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('// *[ @ id = "root"] / div / div[1] / div / div[3] / a')))
        driver.find_element_by_xpath('// *[ @ id = "root"] / div / div[1] / div / div[3] / a').click()
        # sleep(1)
        # 切换iframe
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_id('yhtloginIframe')))
        iframe = driver.find_element_by_id('yhtloginIframe')
        driver.switch_to.frame(iframe)
        sleep(1)
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_id('username')))
        driver.find_element_by_id('username').clear()
        driver.find_element_by_id('username').send_keys('19992888888')
        driver.find_element_by_id('password').clear()
        driver.find_element_by_id('password').send_keys('ystest*123')
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_id('submit_btn_login')))
        driver.find_element_by_id('submit_btn_login').click()
        # sleep(1)
        title = driver.title
        if title == '数字化工作台':
            print('进入页面成功')
        WebDriverWait(driver, 10, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//*[@id="_dropdown_popcontainer"]/div/i')))
        driver.find_element_by_xpath('//*[@id="_dropdown_popcontainer"]/div/i').click()
        driver.find_element_by_xpath('//*[@id="home_header"]//div[text()="1114UI测试专属"]').click()
        driver.find_element_by_xpath(
            '//button[@class="u-button btn__style___37bsb u8c_primary__style___RFibc  btn__style___20DQM "]').click()
