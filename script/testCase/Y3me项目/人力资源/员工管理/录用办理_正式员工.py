# coding=utf-8
from time import sleep

from selenium.webdriver.common.keys import Keys

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from SRC.webdriver.switchTo import SwitchTo
from script.common import utils
from selenium.webdriver import ActionChains
from SRC.param import context
from SRC.param.context import Name


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
        menu2 = driver.find_element_by_css_selector('span[title="员工管理"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(2)
        # 进入二级节点
        driver.find_element_by_xpath('//li[@title="录用办理"]').click()

        sleep(2)
        # 跳转录用办理iframe
        iframe = driver.find_element_by_id('HRGXFW010')
        # # driver.switch_to.frame(iframe)
        SwitchTo(driver).frame(iframe)
        sleep(2)

        # 点击正式员工入职
        driver.find_element_by_xpath('//div[@class="staff-info-control-btn fr"]/button[text()="正式员工入职"]').click()

        sleep(2)

        # 随机生成注册人员姓名
        random_name = context.get_reg_name()

        # 赋值到context
        setattr(Name, "random_name", random_name)

        driver.find_element_by_xpath('//*[@id="20180509105133DpcOx60LOa"]').send_keys(random_name)
        # 选择证件类型，点击右侧按钮
        driver.find_element_by_xpath('//*[@id="edit_20181009204201BSMuf1Jk2V"]/div/span[1]').click()
        # 选择身份证类型
        driver.find_element_by_xpath(
            '//table[@class="msgtype-table table-hover table table-no-bordered"]//td[text()="居民身份证"]').click()

        # 输入身份证号码

        ID_CARD = context.get_cre_id()
        driver.find_element_by_xpath('//*[@id="20180509105133gZbhMtqK9n"]').send_keys(ID_CARD)
        sleep(0.5)

        # 点击个人邮箱
        # 生成一个随机邮箱
        email_num = context.get_email()

        # 输入邮箱号码
        driver.find_element_by_xpath('//*[@id="20180509105133q64hRYzrKY"]').send_keys(email_num)

        # 生成随机号码
        phone = context.get_mobile()
        # 点击手机号码
        driver.find_element_by_xpath('//*[@id="20180509105133OWWbB8ongy"]').send_keys(phone)

        # 点击最高学历右侧的按钮
        driver.find_element_by_xpath('//*[@id="edit_20180719193255BtyQkkHEeD"]//span').click()

        # 选择学历信息
        driver.find_element_by_xpath(
            '//div[@class="scroll-wrapper fixed-table-body scrollbar-dynamic"]//td[text()="博士研究生"]').click()

        # 输入工作日期
        driver.find_element_by_xpath('//*[@id="edit_20180509105133EhPNtIJgEk"]/div/span[1]').click()
        driver.find_element_by_xpath(
            '//*[@id="edit_20180509105133EhPNtIJgEk"]//div[@class="u-date-panel is-visible"]//div[@class="u-date-cell current"]').click()

        # 预计入职日期
        driver.find_element_by_xpath('//*[@id="edit_20180509105133ILCsggy7fK"]/div/span[1]').click()
        driver.find_element_by_xpath(
            '//div[@class="u-date-panel is-visible"]//div[@class="u-date-cell current"]').click()

        # 输入截止日期
        driver.find_element_by_xpath('//*[@id="edit_20180509105133b0FnhTKv98"]/div/span[1]').click()
        driver.find_element_by_xpath(
            '//div[@class="u-date-panel is-visible"]//div[@class="u-date-cell current"]').click()

        # 点击合同主体右侧按钮
        driver.find_element_by_xpath(
            '//*[@id="edit_20180509105133YUkXXQFaS1"]//span[@class= "u-form-control-feedback fa fa-list-ul refer"]').click()

        # 选择合同信息
        driver.find_element_by_xpath(
            '//span[text()="合同主体"]/ancestor::div[@class="outerContainer"]//ul[@class="ul_list2"]//td[text()="0001"]').click()

        # 点击所属公司
        driver.find_element_by_xpath('//*[@id="20180509105133aEJwm8bmGE"]').send_keys("仓储中心")
        driver.find_element_by_xpath('//*[@id="20180509105133aEJwm8bmGE"]').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="20180509105133aEJwm8bmGE"]').send_keys(Keys.ENTER)

        # 点击所属部门
        driver.find_element_by_xpath('//*[@id="20190907181108ogVN0Y2iHt"]').send_keys("仓储中心")
        driver.find_element_by_xpath('//*[@id="edit_20190907181108ogVN0Y2iHt"]').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="20190907181108ogVN0Y2iHt"]').send_keys(Keys.ENTER)

        # 点击人员类别按钮
        driver.find_element_by_xpath('//*[@id="edit_20180509105133KUUJzi1zqv"]/div/span[1]').click()

        # 选择人员类别
        driver.find_element_by_xpath('//*[@id="refContainer20180509105133KUUJzi1zqv"]//td[text()="1123"]').click()

        # 输入主管
        driver.find_element_by_xpath('//*[@id="20180509105133EXIp9xoDFE"]').send_keys('黄俊涛')
        driver.find_element_by_xpath('//*[@id="20180509105133EXIp9xoDFE"]').click()
        sleep(3)
        driver.find_element_by_xpath('//*[@id="20180509105133EXIp9xoDFE"]').send_keys(Keys.ENTER)

        # 点击工作地点按钮
        driver.find_element_by_xpath('//*[@id="edit_20180509105133pJBKEVijlT"]/div/span[1]').click()

        # 选择地点类别
        driver.find_element_by_xpath('//*[@id="refContainer20180509105133pJBKEVijlT"]//td[text()="123"]').click()

        # 输入转正工资
        driver.find_element_by_xpath('//div[@id="eidt_20180509105133gSQtBR2Ckf"]//input').send_keys("10000")

        # 输入试用期工资
        driver.find_element_by_xpath('//div[@id="eidt_20180509105133bVeJmtyxmQ"]//input').send_keys("30000")

        # 输入薪资结构
        driver.find_element_by_xpath('//div[@id="edit_201805091051333MLOv4lfoL"]//input').send_keys("16")

        # 点击提交按钮
        driver.find_element_by_xpath(
            '//button[@class="btn btn-primary"]//span[@class="btn-primary" and text()="提交"]').click()
        sleep(2)
        # 关闭当前页面
        driver.switch_to.default_content()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()

