# -*-CodeIng:utf-8 -*-
# @time :2019/10/29 17:35
# @author:HuangJunTao
# @email:1341890679@qq.com
# @file:公共薪资项目.py
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
        # driver.refresh()
        # driver.find_element_by_xpath('//*[@id="_dropdown_popcontainer"]/div/i').click()
        # driver.find_element_by_xpath('//*[@id="home_header"]//div[text()="UI测试专属"]').click()
        # driver.find_element_by_xpath(
        #     '//button[@class="u-button btn__style___37bsb u8c_primary__style___RFibc  btn__style___20DQM "]').click()
        # sleep(2)
        # 左上方公共节点
        driver.find_element_by_class_name('lebra-navbar-left-icon').click()
        sleep(1)
        # 进入社交协同
        driver.find_element_by_xpath('//*[text()="人力资源"]').click()
        sleep(1)
        # 进入一级节点
        menu2 = driver.find_element_by_css_selector('span[title="薪资核算"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(1)
        # 进入二级节点
        driver.find_element_by_xpath('//li[@title="公共薪资项目"]').click()
        sleep(2)
        # 跳转公共薪资项目iframe
        iframe = driver.find_element_by_id('HRXC010030')
        # # driver.switch_to.frame(iframe)
        SwitchTo(driver).frame(iframe)
        sleep(2)

        # 点击新增项目分类
        driver.find_element_by_xpath('//i[@title="新增项目分类"]').click()
        sleep(0.5)
        # 输入项目名称
        num = random.randint(100, 999)
        name = "项目{}".format(num)

        driver.find_element_by_xpath('//div[@class="addInput el-input"]//input').send_keys(name)

        driver.find_element_by_xpath('//i[@title="新增项目分类"]').click()
        sleep(1)
        self.assertEqual("操作成功！", driver.find_element_by_xpath('//p[text()="操作成功！"]').text)

        # 点击编辑项目分类
        driver.find_element_by_xpath('//i[@title="编辑项目分类"]').click()

        # 再次点击编辑项目分类
        driver.find_element_by_xpath('//i[@title="编辑项目分类"]').click()

        # 点击新增按钮
        driver.find_element_by_xpath(
            '//div[@class="fn-div"]//button[@class="el-button to-r el-button--primary"]').click()
        sleep(1)

        # 输入项目名称
        num = random.randint(100, 999)
        project = "项目{}".format(num)
        driver.find_element_by_xpath('//label[text()="项目名称"]/following-sibling::div//input').send_keys(project)

        # 申报个税属性按钮
        driver.find_element_by_xpath('//span[@class="el-cascader__label"]').click()
        sleep(1)
        driver.find_element_by_xpath('//span[text()="纳税收入"]').click()

        # 输入项目说明
        driver.find_element_by_xpath('//textarea').send_keys("项目信息12345")

        # 点击保存按钮
        driver.find_element_by_xpath('//div[@class="bottom-fn"]//button[2]').click()
        sleep(1.5)
        # 断言是否保存成功
        self.assertEqual("操作成功！", driver.find_element_by_xpath('//p[text()="操作成功！"]').text)

        # 点击启用状态
        driver.find_element_by_xpath('//label[text()="启用状态"]/following-sibling::div//span').click()
        sleep(1)
        self.assertEqual("停用成功", driver.find_element_by_xpath('//p[text()="停用成功"]').text)

        # 点击启用状态
        driver.find_element_by_xpath('//label[text()="启用状态"]/following-sibling::div//span').click()
        sleep(1)
        self.assertEqual("启用成功", driver.find_element_by_xpath('//p[text()="启用成功"]').text)

        # 点击编辑按钮
        driver.find_element_by_xpath('//div[@class="fn-r"]//button[2]').click()

        # 点击保存按钮
        driver.find_element_by_xpath('//div[@class="bottom-fn"]//button[2]').click()
        sleep(1.5)
        self.assertEqual("操作成功！", driver.find_element_by_xpath('//p[text()="操作成功！"]').text)

        # 点击删除按钮
        driver.find_element_by_xpath('//div[@class="fn-r"]//button[3]').click()

        # 点击确定按钮
        driver.find_element_by_xpath('//div[@class="el-message-box"]//div[3]//button[2]').click()

        # 断言删除成功
        self.assertEqual("删除成功", driver.find_element_by_xpath('//p[text()="删除成功"]').text)

        # 点击删除项目分类
        driver.find_element_by_xpath('//i[@title="删除项目分类"]').click()

        # 点击确定按钮
        driver.find_element_by_xpath('//div[@class="el-message-box"]//div[3]//button[2]').click()

        # 断言删除成功
        self.assertEqual("操作成功！", driver.find_element_by_xpath('//p[text()="操作成功！"]').text)
        # 关闭当前页面
        driver.switch_to.default_content()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()