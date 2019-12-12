# -*-CodeIng:utf-8 -*-
# @time :2019/10/31 20:02
# @author:HuangJunTao
# @email:1341890679@qq.com
# @file:审批流_薪资.py
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
        # #进入社交协同
        # driver.find_element_by_xpath('//*[text()="数字化建模"]').click()
        # sleep(2)
        # 进入一级节点
        menu2 = driver.find_element_by_css_selector('span[title="组织管理"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(1)
        # 进入二级节点
        driver.find_element_by_xpath('//li[@title="组织单元"]').click()

        sleep(1)
        # 跳转模型管理iframe
        iframe = driver.find_element_by_id('GZTORG001')
        # driver.switch_to.frame(iframe)
        SwitchTo(driver).frame(iframe)
        sleep(1)

        # 点击展开按钮
        driver.find_element_by_xpath('//div[@class="expand-icon"]').click()
        sleep(1)
        # 进入编辑
        driver.find_element_by_xpath('//a[text()="bj_cczx"]').click()
        sleep(3)
        # 点击编辑按钮
        driver.find_element_by_xpath('//span[text()="编辑"]').click()
        driver.find_element_by_xpath('//label[text()="纳税人识别号"]/parent::div/following-sibling::div//input').clear()
        driver.find_element_by_xpath('//label[text()="纳税人识别号"]/parent::div/following-sibling::div//input').send_keys(123456789)
        # 点击保存
        driver.find_element_by_xpath('//span[text()="保存"]').click()
        sleep(2)
        # 关闭当前页面
        driver.switch_to.default_content()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()
