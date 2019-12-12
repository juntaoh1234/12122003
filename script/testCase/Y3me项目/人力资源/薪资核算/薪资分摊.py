# -*-CodeIng:utf-8 -*-
# @time :2019/10/30 13:36
# @author:HuangJunTao
# @email:1341890679@qq.com
# @file:薪资分摊.py
# @SoftWare:PyCharm


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
        menu2 = driver.find_element_by_css_selector('span[title="薪资核算"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(2)
        # 进入二级节点
        driver.find_element_by_xpath('//li[@title="薪资分摊"]').click()
        sleep(2)
        # 跳转劳动合同签订iframe
        iframe = driver.find_element_by_id('HRXC030070')
        # # driver.switch_to.frame(iframe)
        SwitchTo(driver).frame(iframe)
        sleep(2)

        # 点击组织右侧的按钮
        driver.find_element_by_xpath('//*[@id="c12"]/div/span/span/span/i[2]').click()

        # 选择组织
        driver.find_element_by_xpath('//span[text()="仓储中心-北京"]').click()

        # 点击确定
        driver.find_element_by_xpath('//div[@class="op-button"]/button[2]').click()

        # 点击添加按钮
        driver.find_element_by_xpath('//*[@id="app"]/div/section/aside/div[2]/ul/li[1]/i[1]').click()
        sleep(1)

        num = random.randint(100, 999)
        name = "分摊类型{}".format(num)
        # 输入分摊类型
        driver.find_element_by_xpath('//label[text()="分摊类型"]/following-sibling::div//input').send_keys(name)

        # 点击分摊类型右侧的按牛
        driver.find_element_by_xpath(
            '//label[text()="分摊项目"]/following-sibling::div//span[@class="el-input__suffix"]').click()
        sleep(1.5)

        # 点击全部待选项目
        driver.find_element_by_xpath(
            '//span[text()="待选项目"]/ancestor::th/preceding-sibling::th//span[@class="el-checkbox__inner"]').click()

        # 点击全部选到右侧
        driver.find_element_by_xpath('//div[@class="middle-son"]/div[2]/i').click()

        # 点击确定按钮
        driver.find_element_by_xpath(
            '//span[text()="设置分摊项目"]/ancestor::div[@class="el-dialog__wrapper"]//button[2]').click()
        sleep(1)

        # 点击影响因素
        driver.find_element_by_xpath('//label[text()="影响因素"]/following-sibling::div//input').click()

        # 选择条目
        driver.find_element_by_xpath('//span[text()="人员类别"]').click()

        # 输入分摊比例
        driver.find_element_by_xpath('//label[text()="分摊比例"]/following-sibling::div//input').send_keys(30)

        # 点击确定
        driver.find_element_by_xpath(
            '//span[text()="薪资分摊"]/ancestor::div[@class="el-dialog"]/div[3]//button[2]').click()
        sleep(1)
        # 断言
        self.assertEqual("操作成功！", driver.find_element_by_xpath('//p[text()="操作成功！"]').text)

        # 点击分摊
        driver.find_element_by_xpath('//span[text()="分摊"]').click()
        sleep(1)
        # 点击确定按钮
        driver.find_element_by_xpath('//div[@class="el-message-box__btns"]//button[2]').click()

        # 点击制单
        driver.find_element_by_xpath('//span[text()="制 单"]').click()
        sleep(2)
        # 关闭当前页面
        driver.switch_to.default_content()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()