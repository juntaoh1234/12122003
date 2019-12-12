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
        driver.find_element_by_xpath('//li[@title="考勤统计规则"]').click()

        sleep(2)
        # 跳转考勤统计规则iframe
        iframe = driver.find_element_by_id('HRJQ020050')
        # # driver.switch_to.frame(iframe)
        SwitchTo(driver).frame(iframe)
        sleep(2)

        # 点击添加按钮
        driver.find_element_by_xpath('//*[@id="item"]/div[1]/div[1]/div/div[1]/ul/li[1]').click()
        sleep(1)

        # 输入考勤规则
        num = random.randint(10000, 99999)
        str_regular = "统计规则{}".format(num)
        driver.find_element_by_xpath('//label[text()="考勤统计规则名称"]/following-sibling::div//input').send_keys(str_regular)
        # 点击组织右侧按钮
        driver.find_element_by_xpath('//*[@id="c60"]/div/span/span/span/i[2]').click()
        sleep(3)

        # 选中组织
        driver.find_element_by_xpath(
            '//div[@role="dialog"]//span[text()="仓储中心-北京"]').click()

        # 点击确认
        driver.find_element_by_xpath(
            '//div[@class="el-dialog__wrapper custom-ref-dialog"]//button[@class="el-button el-button--primary"]').click()

        # 点击保存
        driver.find_element_by_xpath('//div[@aria-label="新增考勤统计规则方案"]//button[@class="el-button el-button--primary"]').click()


        sleep(3)
        # 断言
        text = driver.find_element_by_xpath(
            '//span[text()="{}"]'.format(str_regular)).text
        self.assertEqual(text, str_regular)

        # 编辑考勤规则
        driver.find_element_by_xpath(
            '//*[@id="item"]/div[1]/div[1]/div/div[1]/ul/li[3]').click()
        sleep(3)

        # 输入考勤规则
        num = random.randint(10000, 99999)
        str_regular_edit = "统计规则{}".format(num)
        driver.find_element_by_xpath('//label[text()="考勤统计规则名称"]/following-sibling::div//input').clear()
        driver.find_element_by_xpath('//label[text()="考勤统计规则名称"]/following-sibling::div//input').send_keys(str_regular_edit)
        # 点击保存按钮
        driver.find_element_by_xpath('//div[@aria-label="编辑考勤统计规则方案"]//button[@class="el-button el-button--primary"]').click()
        sleep(2)
        # 断言
        text = driver.find_element_by_xpath(
            '//span[text()="{}"]'.format(str_regular_edit)).text
        self.assertEqual(text, str_regular_edit)

        # 点击新建项目
        driver.find_element_by_xpath('//button[@class="el-button el-button--primary"]/span[text()="新增项目"]').click()
        # 新增自定义项目
        driver.find_element_by_xpath('//button[@class="el-button select-button el-button--text"]/span[text()="新增自定义项目"]').click()

        # 输入项目名称信息
        driver.find_element_by_xpath('//label[text()="项目名称："]/following-sibling::div//input').send_keys("项目12345")

        # 输入说明信息
        driver.find_element_by_xpath('//div[@class="el-form-item__content"]//textarea').send_keys("说明信息87654")

        # 点击保存
        driver.find_element_by_xpath('//button/span[text()="保存"]').click()
        sleep(10)
        ele = driver.find_element_by_xpath('//span[text()="项目12345"]')
        self.assertIsNotNone(ele)

        # 点击编辑按钮
        driver.find_element_by_xpath('//span[text()="项目12345"]/ancestor::tr/td[6]//div[text()="编辑"]').click()
        sleep(1)

        # 点击保存
        driver.find_element_by_xpath('//button/span[text()="保存"]').click()
        sleep(10)
        # 点击删除按钮
        driver.find_element_by_xpath('//span[text()="项目12345"]/ancestor::tr/td[6]//div[text()="删除"]').click()
        sleep(1)

        # 点击取消按钮
        driver.find_element_by_xpath('//div[@class="el-message-box"]//button[1]').click()
        sleep(0.5)
        self.assertEqual("已取消删除",driver.find_element_by_xpath('//p[text()="已取消删除"]').text)

        # 点击删除按钮
        driver.find_element_by_xpath('//span[text()="项目12345"]/ancestor::tr/td[6]//div[text()="删除"]').click()
        sleep(1)

        # 点击确定按钮
        driver.find_element_by_xpath('//div[@class="el-message-box"]//button[2]').click()
        sleep(0.5)
        self.assertEqual("操作成功！",driver.find_element_by_xpath('//p[text()="操作成功！"]').text)


        # 点击删除按钮
        driver.find_element_by_xpath('//*[@id="item"]/div[1]/div[1]/div/div[1]/ul/li[2]').click()
        sleep(0.5)
        driver.find_element_by_xpath('//div[@class="el-message-box"]//button[2]').click()
        sleep(0.5)
        # 断言
        self.assertEqual("操作成功", driver.find_element_by_xpath('//p[text()="操作成功"]').text)

        # 关闭当前页面
        driver.switch_to.default_content()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()