# coding=utf-8
import random
from time import sleep

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from SRC.webdriver.switchTo import SwitchTo
from script.common import utils
from selenium.webdriver import ActionChains
from SRC.param import context


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
        menu2 = driver.find_element_by_css_selector('span[title="员工服务"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(2)
        # 进入二级节点
        driver.find_element_by_xpath('//li[@title="我的申请"]').click()

        sleep(2)
        # 跳转我的申请iframe
        iframe = driver.find_element_by_id('HRP010020')
        # # driver.switch_to.frame(iframe)
        print(iframe)
        SwitchTo(driver).frame(iframe)
        sleep(2)
        # 点击请假申请tab页
        driver.find_element_by_xpath('//ul[@class="el-menu--horizontal el-menu"]/li[3]').click()
        # 点击新增按钮
        driver.find_element_by_xpath('//button[@class="el-button el-button--primary"]/span[text()="新增"]').click()
        sleep(2)
        # 点击休假类型右侧按钮
        driver.find_element_by_xpath('//*[@id="edit_20180817141749XV4Fwki935"]/div/span[1]').click()
        sleep(1)

        # 点击第一条数据
        driver.find_element_by_xpath('//td[text()="事假"]').click()

        # 输入请假事由
        num = random.randint(1000, 9999)
        result = "联合国议事[{}]号文件".format(num)
        driver.find_element_by_xpath('//*[@id="20180706103429AartUFuqhI"]').send_keys(result)
        sleep(1)

        # # 点击上传附件
        # driver.find_element_by_xpath('//*[@id="chosenFile"]').click()
        # sleep(1)
        # context.upload_file(r"D:\张红-999001234.png", "员工服务-我的申请上传附件操作")

        # 点击添加请假明
        # driver.find_element_by_xpath('//*[@id="leaveapply"]/div[3]/div[1]/div/button').click()

        # 点击开始时间右侧的按钮
        driver.find_element_by_xpath('//*[@id="begintime0"]/label/i').click()

        # 选择当天
        driver.find_element_by_xpath('//*[@id="begintime0"]/div/div[2]/button[1]').click()

        # 点击结束时间的有测按钮
        driver.find_element_by_xpath('//*[@id="endtime0"]/label/i').click()
        sleep(0.5)
        # # 选择下一天
        # driver.find_element_by_xpath('//*[@id="endtime0"]/div/div[1]/div/div/div[1]/div[2]').click()
        # driver.find_element_by_xpath('//*[@id="endtime0"]/div/div[1]/div/div/div[2]/div[11]').click()
        # # driver.find_element_by_xpath('//div[@class="u-date-cell current"]/following-sibling::div[1]').click()

        # 选择当天
        driver.find_element_by_xpath(
            '//input[@id="end-date0"]/parent::div//div[@class="u-date-cell current"]/following-sibling::div[1]').click()

        # 点击确定按钮
        driver.find_element_by_xpath(
            '//input[@id="end-date0"]/parent::div//button[@class="u-button u-date-ok right primary"]').click()
        # 点击保存
        sleep(0.5)
        driver.find_element_by_xpath('//*[@id="leaveapply"]//button/span[text()="保存"]').click()
        sleep(2)
        # 点击提交按钮
        driver.find_element_by_xpath('//div[@class="control-btn"]/div/button[1]').click()
        sleep(2)

        # 点击撤销 按钮
        driver.find_element_by_xpath(
            '//div[contains(text(),"{}")]/ancestor::tr//span[text()="撤销"]'.format(result)).click()
        # 点击确定按钮
        sleep(1)
        driver.find_element_by_xpath('//div[@class="el-message-box__btns"]/button[2]').click()
        sleep(3)
        text = driver.find_element_by_xpath('//div[contains(text(),"{}")]/ancestor::tr/td[6]/div'.format(result)).text
        self.assertEqual(text, "已撤回")
        # # 点击编辑按钮
        # driver.find_element_by_xpath('//*[@id="leaveapply"]//button/span[text()="编辑"]').click()
        # sleep(2)
        # # 点击保存
        # driver.find_element_by_xpath('//*[@id="leaveapply"]//button/span[text()="保存"]').click()
        # sleep(3)
        driver.switch_to.default_content()

        ele = driver.find_element_by_xpath('//p[text()="我的申请"]')
        actions = ActionChains(driver)
        actions.move_to_element(ele)
        actions.perform()
        driver.find_element_by_xpath('//span[text()="刷新"]').click()
        sleep(1)
        # 跳转休假规则iframe
        iframe = driver.find_element_by_id('HRP010020')
        # # driver.switch_to.frame(iframe)
        SwitchTo(driver).frame(iframe)
        sleep(1)
        # # 点击请假申请tab页
        # driver.find_element_by_xpath('//ul[@class="el-menu--horizontal el-menu"]/li[3]').click()

        # # 点击编辑
        # text = driver.find_element_by_xpath(
        #     '//*[@id="leaveapprove-wrap"]/div/div[2]/div[3]/table/tbody/tr[4]/td[5]/div').text
        # print(text)
        # 点击提交
        # driver.find_element_by_xpath('//*[@id="leaveapply"]/div[3]/div[2]/div/button[1]').click()

        # *****************************************************************************************
        # 点击出差申请tab页
        driver.find_element_by_xpath('//li[contains(text(),"出差申请")]').click()

        # 点击新增按钮
        driver.find_element_by_xpath('//button[@class="el-button el-button--primary"]/span[text()="新增"]').click()
        sleep(2)
        # 点击休假类型右侧按钮
        driver.find_element_by_xpath('//*[@id="edit_20181024153808q3reXc5Dc3"]/div/span[1]').click()
        sleep(1)

        # 点击第一条数据
        driver.find_element_by_xpath('//td[text()="本地出差"]').click()

        # 出差费用
        driver.find_element_by_xpath('//*[@id="20181024153808LOdNOVKJgB"]').send_keys("5000")

        # 交接人
        driver.find_element_by_xpath('//*[@id="20181024153808LvYYxBZgNO"]').send_keys("卢大达")

        # 输入出差说明
        driver.find_element_by_xpath('//*[@id="20181024153808lZ7NAO1Vdj"]').send_keys('出差说明信息888')

        # # 点击上传附件
        # driver.find_element_by_xpath('//*[@id="chosenFile"]').click()
        #
        # # 调用上传附件
        # context.upload_file(r"D:\我的头像\5.jpg", "出差申请单附件。")

        # 选择添加一行
        driver.find_element_by_xpath('//button/span[text()="添加"]').click()
        sleep(1)

        # 点击开始时间右侧的按钮
        driver.find_element_by_xpath('//*[@id="begintime0"]/label/i').click()

        # 选择当天
        driver.find_element_by_xpath('//*[@id="begintime0"]/div/div[2]/button[1]').click()

        # 点击结束时间的有测按钮
        driver.find_element_by_xpath('//*[@id="endtime0"]/label/i').click()
        sleep(0.5)
        # 选择当天
        driver.find_element_by_xpath(
            '//input[@id="end-date0"]/parent::div//div[@class="u-date-cell current"]/following-sibling::div[1]').click()
        sleep(0.5)
        # 点击确定按钮
        driver.find_element_by_xpath(
            '//input[@id="end-date0"]/parent::div//button[@class="u-button u-date-ok right primary"]').click()

        # 输入出差地点
        driver.find_element_by_xpath('//*[@id="destination0"]').send_keys("阿尔卑斯")

        # 点击保存
        sleep(0.5)
        driver.find_element_by_xpath('//button/span[text()="保存"]').click()
        sleep(3)

        # # 点击编辑按钮
        # driver.find_element_by_xpath('//button/span[text()="编辑"]').click()
        # sleep(2)
        # # 点击保存
        # driver.find_element_by_xpath('//button/span[text()="保存"]').click()
        # sleep(3)
        driver.switch_to.default_content()

        ele = driver.find_element_by_xpath('//p[text()="我的申请"]')
        actions = ActionChains(driver)
        actions.move_to_element(ele)
        actions.perform()
        driver.find_element_by_xpath('//span[text()="刷新"]').click()
        sleep(1)
        # 跳转休假规则iframe
        iframe = driver.find_element_by_id('HRP010020')
        # # driver.switch_to.frame(iframe)
        SwitchTo(driver).frame(iframe)
        sleep(2)
        # 关闭当前页面
        driver.switch_to.default_content()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()
