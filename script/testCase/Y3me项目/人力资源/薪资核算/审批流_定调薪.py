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
        menu2 = driver.find_element_by_css_selector('span[title="流程管理"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(1)
        # 进入二级节点
        driver.find_element_by_xpath('//li[@title="模型管理"]').click()

        sleep(1)
        # 跳转模型管理iframe
        iframe = driver.find_element_by_id('XTLCZX0006')
        # driver.switch_to.frame(iframe)
        SwitchTo(driver).frame(iframe)
        sleep(1)

        # 点击左侧树按钮
        driver.find_element_by_xpath('//*[@id="app"]//span[text()="人力资源"]').click()
        sleep(1)
        # 点击左侧树按钮
        driver.find_element_by_xpath('//*[@id="app"]//span[text()="薪资核算"]').click()
        sleep(1)
        wins0 = driver.window_handles
        # 选中请假
        driver.find_element_by_xpath('//*[@id="app"]//span[text()="定调薪"]').click()

        # 点击新增按钮
        driver.find_element_by_xpath('//div[@class="btns-wrapper"]//button[1]').click()
        sleep(2)

        # 输入流程名称
        driver.find_element_by_xpath('//label[text()="名称"]/following-sibling::div//input').send_keys('定调薪流程')

        # 备注信息
        driver.find_element_by_xpath('//textarea').send_keys("备注信息0002")

        # 点击确定按钮
        driver.find_element_by_xpath(
            '//span[text()="新增流程模型"]/ancestor::div[@class="el-dialog__wrapper"]//button[2]').click()
        sleep(1)
        # 断言
        self.assertEqual("创建成功", driver.find_element_by_xpath('//p[text()="创建成功"]').text)

        # 点击设计按钮
        driver.find_element_by_xpath(
            '//*[@id="app"]//table[@class="el-table__body"]/tbody/tr/td[4]/div/span[2]').click()

        # 跳转新页面
        wins = driver.window_handles
        driver.switch_to_window(wins[-1])
        sleep(2)

        # 双击主管审批
        # driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div[2]/button[2]').click()
        # driver.find_element_by_xpath('//span[@title="主管审批"]').doubleClick()
        driver.find_element_by_xpath('//div[@id="designer"]//div/span[1]/span').doubleClick()
        sleep(2)

        # 输入节点名称
        driver.find_element_by_xpath('//input[@placeholder="请输入流程环节名称"]').send_keys("提交")

        # 移动滚动条
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

        # 跳转回原来的页面
        win1 = driver.window_handles
        driver.switch_to_window(win1[0])
        # 关闭当前页面
        sleep(2)
        driver.switch_to.default_content()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()