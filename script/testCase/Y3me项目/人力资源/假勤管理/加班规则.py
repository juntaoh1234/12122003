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
        driver.find_element_by_xpath('//li[@title="加班规则"]').click()

        sleep(2)
        # 跳转劳动合同签订iframe
        iframe = driver.find_element_by_id('HRJQ020070')
        # # driver.switch_to.frame(iframe)
        SwitchTo(driver).frame(iframe)
        sleep(1)

        # 点击新建规则
        driver.find_element_by_xpath('//button[@class="el-button el-button--primary"]').click()
        sleep(2)
        # 点击所属组织右侧按钮
        driver.find_element_by_xpath('//*[@id="c69"]/div/span/span/span/i[2]').click()
        sleep(3)  # 选择北京仓储中心
        driver.find_element_by_xpath('//div[@role="dialog"]//span[text()="仓储中心-北京"]').click()

        # 点击确定按钮
        driver.find_element_by_xpath('//div[@class="op-button"]//button[@class="el-button el-button--primary"]').click()

        # 输入规则名称
        driver.find_element_by_xpath('//input[@placeholder="规则名称"]').send_keys("规则1234")

        # 选择加班类型
        driver.find_element_by_xpath('//span[text()="工作日加班"]/preceding-sibling::span').click()

        # 点击保存
        driver.find_element_by_xpath(
            '//div[@class="header-wrap"]//button[@class="el-button el-button--primary"]/span[text()="保存"]').click()
        sleep(2)

        self.assertIn("规则1234", driver.page_source)
        # 编辑考勤规则
        driver.find_element_by_xpath(
            '//div[text()="规则1234"]/ancestor::tr/td[7]/div/div[1]').click()
        sleep(2)
        # 点击保存按钮
        driver.find_element_by_xpath(
            '//div[@class="header-wrap"]//button[@class="el-button el-button--primary"]/span[text()="保存"]').click()

        sleep(2)
        # 点击停用按钮
        driver.find_element_by_xpath(
            '//div[text()="规则1234"]/ancestor::tr/td[7]/div/div[2]').click()
        sleep(2)
        # 点击确认
        driver.find_element_by_xpath(
            '//div[@class="el-message-box"]//button[@class="el-button el-button--default el-button--small el-button--primary "]').click()
        sleep(2)
        # 点击启用按钮
        driver.find_element_by_xpath(
            '//div[text()="规则1234"]/ancestor::tr/td[7]/div/div[2]').click()
        sleep(2)

        # 点击停用按钮
        driver.find_element_by_xpath(
            '//div[text()="规则1234"]/ancestor::tr/td[7]/div/div[2]').click()
        sleep(2)

        # 点击确认
        driver.find_element_by_xpath(
            '//div[@class="el-message-box"]//button[@class="el-button el-button--default el-button--small el-button--primary "]').click()
        sleep(1)
        sleep(2)

        # 点击删除按钮
        driver.find_element_by_xpath(
            '//div[text()="规则1234"]/ancestor::tr/td[7]/div/div[3]').click()

        # 点击确定
        driver.find_element_by_xpath(
            '//div[@class="el-message-box"]//button[@class="el-button el-button--default el-button--small el-button--primary "]').click()

        # 断言是否删除成功
        sleep(2)
        self.assertNotIn("规则1234", driver.page_source)

        # 关闭当前页面
        driver.switch_to.default_content()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()