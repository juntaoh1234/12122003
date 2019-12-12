# coding=utf-8
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
        # 左上方公共节点
        driver.find_element_by_class_name('lebra-navbar-left-icon').click()
        sleep(2)
        # #进入社交协同
        # driver.find_element_by_xpath('//*[text()="数字化建模"]').click()
        # sleep(2)
        # 进入一级节点
        menu2 = driver.find_element_by_css_selector('span[title="流程管理"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(2)
        # 进入二级节点
        driver.find_element_by_xpath('//li[@title="模型管理"]').click()

        sleep(2)
        # 跳转模型管理iframe
        iframe = driver.find_element_by_id('XTLCZX0006')
        # driver.switch_to.frame(iframe)
        SwitchTo(driver).frame(iframe)
        sleep(2)

        # 点击左侧树按钮
        driver.find_element_by_xpath('//*[@id="app"]//span[text()="人力资源"]').click()
        sleep(6)
        # 点击左侧树按钮
        driver.find_element_by_xpath('//*[@id="app"]//span[text()="员工管理"]').click()
        sleep(3)
        wins0 = driver.window_handles
        # 选中请假
        driver.find_element_by_xpath('//*[@id="app"]//span[text()="组织内变动"]').click()

        # 点击设计按钮
        driver.find_element_by_xpath(
            '//*[@id="app"]//table[@class="el-table__body"]/tbody/tr/td[4]/div/span[2]').click()

        # 跳转新页面
        wins = driver.window_handles
        driver.switch_to_window(wins[-1])
        sleep(2)
        driver.find_element_by_xpath('//span[@class="icon-designer-banner active"]').click()

        driver.find_element_by_xpath('//span[@class="button icon-designer-minus"]').click()
        sleep(0.5)
        driver.find_element_by_xpath('//span[@class="button icon-designer-minus"]').click()
        sleep(0.5)
        driver.find_element_by_xpath('//span[@class="button icon-designer-minus"]').click()
        sleep(0.5)
        driver.find_element_by_xpath('//span[@class="button icon-designer-minus"]').click()
        sleep(0.5)
        driver.find_element_by_xpath('//span[@class="button icon-designer-minus"]').click()
        sleep(0.5)
        # 双击主管审批
        # driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div[2]/button[2]').click()
        driver.find_element_by_xpath('//span[@title="组织负责人审批"]').doubleClick()
        sleep(3)
        action = ActionChains(driver)
        ele = driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[4]/div/div/div[2]/div[2]/div[1]/div/div[4]/div')
        action.drag_and_drop_by_offset(ele, 1, 110)
        action.perform()
        sleep(1)
        # 点击审批流的发起人
        driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[4]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[2]/label[1]/span[2]').click()

        # 点击保存
        driver.find_element_by_xpath('//button[@class="yy-btn yy-btn-primary"]').click()


        # 双击BP_header
        # driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div[2]/button[2]').click()
        driver.find_element_by_xpath('//span[@title="HR BPHead审批"]').doubleClick()
        sleep(3)
        action = ActionChains(driver)
        ele = driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[4]/div/div/div[2]/div[2]/div[1]/div/div[4]/div')
        action.drag_and_drop_by_offset(ele, 1, 110)
        action.perform()
        sleep(1)
        # 点击审批流的发起人
        driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[4]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[2]/label[1]/span[2]').click()

        # 点击保存
        driver.find_element_by_xpath('//button[@class="yy-btn yy-btn-primary"]').click()

        # 点击保存并发布
        driver.find_element_by_xpath('//button[@class="right-run yy-btn yy-btn-primary"]').click()

        driver.close()
        sleep(1)
        win = driver.window_handles
        driver.switch_to.window(win[0])
        sleep(2)
        # 关闭当前页面
        driver.switch_to.default_content()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()