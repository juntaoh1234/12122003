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
        menu2 = driver.find_element_by_css_selector('span[title="假勤管理"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(2)
        # 进入二级节点
        driver.find_element_by_xpath('//li[@title="假勤档案"]').click()

        sleep(2)
        # 跳转假勤iframe
        iframe = driver.find_element_by_id('HRJQ020110')
        # # driver.switch_to.frame(iframe)
        SwitchTo(driver).frame(iframe)
        sleep(2)
        # 新增功能有异常，暂时不做自动化处理
        # 点击新增按钮
        driver.find_element_by_xpath('//button[@class="el-button el-button--primary"]/span[text()="新增"]').click()
        sleep(2)
        # 点击员工姓名右侧的按钮
        driver.find_element_by_xpath('//div[@class="el-dialog__wrapper addDialog"]//span[text()="员工姓名"]/following-sibling::div//span/span/span/i[2]').click()

        sleep(2)
        # 选择北京仓储中心
        driver.find_element_by_xpath('//div[@role="dialog"]//span[text()="仓储中心-北京"]').click()
        sleep(2)
        # 选择第一条数据
        driver.find_element_by_xpath('//div[@role="dialog"]//tbody/tr[1]').click()

        # 点击确定按钮
        driver.find_element_by_xpath('//div[@class="op-button"]//button[@class="el-button el-button--primary"]').click()
        # 选择考勤方式
        driver.find_element_by_xpath('//div[@class="el-col el-col-11"]//input[@placeholder="请选择考勤方式"]').click()
        # 选择补考勤
        sleep(1)
        driver.find_element_by_xpath('//div[@class="el-select-dropdown el-popper" and @x-placement="bottom-start"]//span[text()="不考勤"]').click()
        # 选择日期
        driver.find_element_by_xpath(
            '//*[@id="attendance-archives"]/div[5]//form/div[4]/div[2]/div/div/div[1]/span[1]/i').click()

        # 选择当天
        driver.find_element_by_xpath('//table[1]//td[@class="available today"]').click()

        # 点击保存
        driver.find_element_by_xpath('//*[@id="attendance-archives"]/div[5]//button[2]').click()

        # 编辑第一行数据
        text = driver.find_element_by_xpath('//*[@id="attendance-archives"]//table/tbody/tr[1]/td[3]/div').text
        driver.find_element_by_xpath('//*[@id="attendance-archives"]//table/tbody/tr[1]/td[13]/div/div').click()

        # 点击编辑按钮
        driver.find_element_by_xpath(
            '//*[@id="attendance-archives"]/div[6]//form//input[@placeholder="请选择考勤方式"]').click()

        # # 选择免签卡
        # driver.find_element_by_xpath('//div[@class="el-select-dropdown el-popper" and @x-placement="bottom-start"]//span[text()="免签卡"]').click()
        #
        # # 点击日期按钮
        # driver.find_element_by_xpath(
        #     '//*[@id="attendance-archives"]/div[6]//form/div[6]/div/div/div/div/span[1]/i').click()
        #
        # # 选择当天
        # driver.find_element_by_xpath('//td[@class="available today"]').click()

        # # 点击日期按钮
        # driver.find_element_by_xpath('//*[@id="attendance-archives"]/div[6]//form/div[7]/div/div/div/div/span[1]/i').click()
        #
        # # 选择当天
        # driver.find_element_by_xpath('//td[@class="available today current"]/following-sibling::td[2]').click()

        # 点击保存按钮
        driver.find_element_by_xpath(
            '//*[@id="attendance-archives"]/div[6]//button[@class="el-button el-button--primary"]').click()
        sleep(3)
        # 断言
        driver.find_element_by_xpath('//*[@id="attendance-archives"]//input[@placeholder="姓名/编号"]').send_keys(text)

        driver.find_element_by_xpath('//*[@id="attendance-archives"]/div[1]/div[2]/div/span').click()

        asert_text = driver.find_element_by_xpath('//*[@id="attendance-archives"]//table/tbody/tr[1]/td[9]/div').text
        self.assertEqual("正常考勤", asert_text)
        date_begin = driver.find_element_by_xpath('//*[@id="attendance-archives"]//table/tbody/tr[1]/td[11]/div')
        # date_end = driver.find_element_by_xpath('//*[@id="attendance-archives"]//table/tbody/tr[1]/td[12]/div')
        self.assertIsNotNone(date_begin)
    # self.assertIsNotNone(date_end)
        sleep(2)
        # 关闭当前页面
        driver.switch_to.default_content()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()