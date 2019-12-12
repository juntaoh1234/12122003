# -*-CodeIng:utf-8 -*-
# @time :2019/10/30 9:34
# @author:HuangJunTao
# @email:1341890679@qq.com
# @file:薪资标准.py
# @SoftWare:PyCharm


from time import sleep
import random
from selenium.webdriver import ActionChains
from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from SRC.webdriver.switchTo import SwitchTo
from script.common import utils
from SRC.param.context import Name


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
        driver.find_element_by_xpath('//li[@title="薪资标准"]').click()
        sleep(2)
        # 跳转劳动合同签订iframe
        iframe = driver.find_element_by_id('HRXC010050')
        # # driver.switch_to.frame(iframe)
        SwitchTo(driver).frame(iframe)
        sleep(2)

        # 点击新增薪资标准按钮
        driver.find_element_by_xpath('//i[@class="el-icon-plus fn"]').click()
        sleep(2)
        num = random.randint(100, 999)
        code = 'GBM{}'.format(num)
        # 输入标准表编码
        driver.find_element_by_xpath('//label[text()="标准表编码"]/following-sibling::div//input').send_keys(code)

        # 输入标准表名称
        num1 = random.randint(100, 999)
        name = 'GBB{}'.format(num1)
        driver.find_element_by_xpath('//label[text()="标准表名称"]/following-sibling::div//input').send_keys(name)

        # 点击对应薪资项目右侧按钮
        driver.find_element_by_xpath(
            '//label[text()="对应薪资项目"]/following-sibling::div//span[@class="el-input__suffix"]').click()

        # 选择条目信息
        driver.find_element_by_xpath('//span[text()="{}"]/parent::span'.format(Name.names)).click()

        # 点击选择项目信息
        driver.find_element_by_xpath('//div[@class="el-table__body-wrapper is-scrolling-none"]/table').click()

        # 点击确定按钮
        driver.find_element_by_xpath('//div[@class="op-button"]//button[2]').click()
        sleep(1)

        # 输入薪资级数
        driver.find_element_by_xpath('//label[text()="薪级数"]/following-sibling::div//input').send_keys("2")

        # 输入薪资档数
        driver.find_element_by_xpath('//label[text()="薪档数"]/following-sibling::div//input').send_keys("2")

        # 点击下一步按钮
        driver.find_element_by_xpath('//div[@class="bottom-fn"]//button[3]').click()
        sleep(2)

        # 输入薪资信息
        driver.find_element_by_xpath(
            '//div[@class="el-table__body-wrapper is-scrolling-none"]//tr[1]/td[2]/div').click()
        driver.find_element_by_xpath('//div[@class="el-input"]/input').send_keys(8000)

        driver.find_element_by_xpath(
            '//div[@class="el-table__body-wrapper is-scrolling-none"]//tr[1]/td[3]/div').click()
        driver.find_element_by_xpath('//div[@class="el-input"]/input').send_keys(10000)

        driver.find_element_by_xpath(
            '//div[@class="el-table__body-wrapper is-scrolling-none"]//tr[2]/td[2]/div').click()
        driver.find_element_by_xpath('//div[@class="el-input"]/input').send_keys(15000)

        driver.find_element_by_xpath(
            '//div[@class="el-table__body-wrapper is-scrolling-none"]//tr[2]/td[3]/div').click()
        driver.find_element_by_xpath('//div[@class="el-input"]/input').send_keys(20000)

        # 点击保存按钮
        driver.find_element_by_xpath('//div[@class="in-bottom"]//button[4]').click()
        sleep(2)

        # 点击启用版本
        driver.find_element_by_xpath('//div[@class="btn-wrap"]//button[5]').click()

        # 点击左侧的时间按钮
        driver.find_element_by_xpath(
            '//label[text()="生效日期"]/ancestor::div[@role="dialog"]//i[@class="el-input__icon el-icon-date"]').click()

        # 点击今天
        driver.find_element_by_xpath('//table[@class="el-date-table"]//td[@class="available today"]').click()

        # 点击确定按钮
        driver.find_element_by_xpath('//label[text()="生效日期"]/ancestor::div[@role="dialog"]//button[2]').click()
        sleep(1)
        self.assertEqual("操作成功！", driver.find_element_by_xpath('//p[text()="操作成功！"]').text)

        # 点击取消启用
        driver.find_element_by_xpath('//div[@class="main-header"]//button[3]').click()
        sleep(1)
        self.assertEqual("操作成功！", driver.find_element_by_xpath('//p[text()="操作成功！"]').text)
        sleep(2)
        # 关闭当前页面
        driver.switch_to.default_content()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()