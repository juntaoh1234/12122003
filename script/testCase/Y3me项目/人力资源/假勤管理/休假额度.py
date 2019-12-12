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
        driver.find_element_by_xpath('//li[@title="休假额度"]').click()

        sleep(2)
        # 跳转休假额度iframe
        iframe = driver.find_element_by_id('HRJQ020120')
        # # driver.switch_to.frame(iframe)
        SwitchTo(driver).frame(iframe)
        sleep(2)

        # 点击计算按钮
        driver.find_element_by_xpath('//button/span[text()="计算"]').click()
        sleep(3)

        self.assertEqual("操作成功", driver.find_element_by_xpath('//p[text()="操作成功"]').text)
        sleep(2)
        # 点击编辑可休时间
        driver.find_element_by_xpath('//div[3]/table/tbody/tr[1]').click()
        sleep(1)
        # 本期额度
        limit = driver.find_element_by_xpath('//div[@class="showBox"]/div[1]/span[1]').text

        # 上期结转
        carry_over = driver.find_element_by_xpath('//div[@class="showBox"]/div[2]/span[1]').text

        # 初始已休
        have_rest = driver.find_element_by_xpath('//div[@class="showBox"]/div[3]/span[1]').text

        # 可休
        can_rest = driver.find_element_by_xpath('//span[text()="可休:"]/following-sibling::span').text
        # 转为int数字
        # print(limit,carry_over,have_rest,can_rest)
        real = int(limit) + int(carry_over) - int(have_rest)
        # 断言是否正确
        self.assertEqual(int(can_rest), real)

        # 点击编辑按钮
        driver.find_element_by_xpath('//span[text()="假期期间：2019年"]/parent::p/span[3]').click()

        # 随机输入数值
        num1 = random.randint(5, 10)
        driver.find_element_by_xpath('//span[text()="本期额度"]/parent::p/div[2]//input').clear()
        driver.find_element_by_xpath('//span[text()="本期额度"]/parent::p/div[2]//input').send_keys(num1)

        # 随机输入数值
        num2 = random.randint(1, 10)
        driver.find_element_by_xpath('//span[text()="本期额度"]/parent::p/div[3]//input').clear()
        driver.find_element_by_xpath('//span[text()="本期额度"]/parent::p/div[3]//input').send_keys(num2)

        # 点击保存按钮
        driver.find_element_by_xpath('//span[text()="假期期间：2019年"]/parent::p/span[3]').click()
        sleep(1.5)
        self.assertEqual("操作成功", driver.find_element_by_xpath('//p[text()="操作成功"]').text)

        sleep(2)
        driver.find_element_by_xpath('//div[3]/table/tbody/tr[1]').click()
        sleep(1)
        # 本期额度
        limit = driver.find_element_by_xpath('//div[@class="showBox"]/div[1]/span[1]').text

        # 上期结转
        carry_over = driver.find_element_by_xpath('//div[@class="showBox"]/div[2]/span[1]').text

        # 初始已休
        have_rest = driver.find_element_by_xpath('//div[@class="showBox"]/div[3]/span[1]').text

        # 可休
        can_rest = driver.find_element_by_xpath('//span[text()="可休:"]/following-sibling::span').text
        # print(limit,carry_over,have_rest,can_rest)
        # 转为int数字
        real = int(limit) + int(carry_over) - int(have_rest)
        # 断言是否正确
        self.assertEqual(int(can_rest), real)
        sleep(2)
        # 关闭当前页面
        driver.switch_to.default_content()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()