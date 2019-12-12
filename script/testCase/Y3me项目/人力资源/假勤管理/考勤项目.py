# coding=utf-8
import random
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
        # 进入社交协同
        driver.find_element_by_xpath('//*[text()="人力资源"]').click()
        sleep(2)
        # 进入一级节点
        menu2 = driver.find_element_by_css_selector('span[title="假勤管理"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(2)
        # 进入二级节点
        driver.find_element_by_xpath('//li[@title="考勤项目"]').click()

        sleep(2)
        # 跳转考勤项目iframe
        iframe = driver.find_element_by_id('HRJQ030010')
        # # driver.switch_to.frame(iframe)
        SwitchTo(driver).frame(iframe)
        sleep(2)

        # 点击新曾
        driver.find_element_by_xpath('//button/span[text()="新增项目"]').click()
        sleep(1)
        # 输入名称
        num = random.randint(1000,9999)
        name = "休假类型{}".format(num)
        driver.find_element_by_xpath('//label[text()="项目名称："]/parent::div//input').send_keys(name)

        # 输入备注信息
        driver.find_element_by_xpath('//div[@class="el-textarea"]//textarea').send_keys("备注信息01234")

        # 点击保存
        driver.find_element_by_xpath('//button[@class="el-button el-button--primary"]').click()
        sleep(3)
        self.assertEqual("操作成功！",driver.find_element_by_xpath('//p[text()="操作成功！"]').text)
        sleep(3)
        self.assertIn(name,driver.page_source)
        # 点击编辑按钮
        driver.find_element_by_xpath('//span[text()="{}"]/ancestor::tr/td[6]/div/div[1]'.format(name)).click()

        # 点击保存
        driver.find_element_by_xpath('//button[@class="el-button el-button--primary"]').click()
        sleep(3)
        self.assertEqual("操作成功！",driver.find_element_by_xpath('//p[text()="操作成功！"]').text)


        # 点击删除按钮
        driver.find_element_by_xpath('//span[text()="{}"]/ancestor::tr/td[6]/div/div[2]'.format(name)).click()
        sleep(2)
        # 点击确定
        driver.find_element_by_xpath('//div[@class="el-message-box__btns"]/button[2]').click()

        self.assertNotIn(name,driver.page_source)
        sleep(2)
        # 关闭当前页面
        driver.switch_to.default_content()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()