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
        driver.find_element_by_xpath('//li[@title="员工信息"]').click()

        sleep(2)
        # 跳转员工信息iframe
        iframe = driver.find_element_by_id('HRPA020')
        # # driver.switch_to.frame(iframe)
        SwitchTo(driver).frame(iframe)
        sleep(2)

        # 点击新增按钮
        driver.find_element_by_xpath('//*[@id="staff-info-all-content"]//button//span[text()="新增"]').click()

        sleep(2)

        # 输入姓名
        random_name = context.get_reg_name()
        driver.find_element_by_xpath('//span[text()="姓名："]/parent::span/following-sibling::input').send_keys(
            random_name)
        setattr(Name, "random_name", random_name)

        # 选择证件信息
        driver.find_element_by_xpath(
            '//*[@id="staff-info-all-content"]/div[2]/form/fieldset/div[2]/div[1]/span[1]').click()

        driver.find_element_by_xpath('//*[@id="refContainercert_type"]//td[text()="0000000001"]').click()

        # 输入证件信息
        idcard = context.get_cre_id()
        driver.find_element_by_xpath('//*[@id="validFix"]/input[1]').send_keys(idcard)

        # 输入手机号信息
        phone = context.get_mobile()
        driver.find_element_by_xpath('//span[text()="手机："]/parent::span/following-sibling::input').send_keys(phone)

        # 输入参加工作日期
        driver.find_element_by_xpath(
            '//*[@id="staff-info-all-content"]/div[2]/form/fieldset/div[4]/div/label/i').click()

        driver.find_element_by_xpath(
            '//*[@id="staff-info-all-content"]/div[2]/form/fieldset/div[4]/div//div[@class="u-date-cell current"]').click()

        # 输入邮箱
        emil = context.get_email()
        driver.find_element_by_xpath('//span[text()="邮箱："]/parent::span/following-sibling::input').send_keys(emil)

        # 输入所属组织
        driver.find_element_by_xpath(
            '//span[text()="所属组织："]/parent::span/following-sibling::div[@class="input-group form-ref"]//input').send_keys(
            "仓储中心-北京")
        driver.find_element_by_xpath(
            '//span[text()="所属组织："]/parent::span/following-sibling::div[@class="input-group form-ref"]//input').click()
        sleep(3)
        driver.find_element_by_xpath(
            '//span[text()="所属组织："]/parent::span/following-sibling::div[@class="input-group form-ref"]//input').send_keys(
            Keys.ENTER)

        # 输入任职开始时间
        driver.find_element_by_xpath('//span[text()="任职开始日期："]/parent::span/following-sibling::div//i').click()
        driver.find_element_by_xpath(
            '//*[@id="staff-info-all-content"]//div[@class="u-date-panel is-visible"]//div[@class="u-date-cell current"]').click()

        # 输入所属部门
        driver.find_element_by_xpath(
            '//span[text()="所属部门："]/parent::span/following-sibling::div[@class="input-group form-ref"]//input').send_keys(
            "仓储中心-北京")
        driver.find_element_by_xpath(
            '//span[text()="所属部门："]/parent::span/following-sibling::div[@class="input-group form-ref"]//input').click()
        sleep(3)
        driver.find_element_by_xpath(
            '//span[text()="所属部门："]/parent::span/following-sibling::div[@class="input-group form-ref"]//input').send_keys(
            Keys.ENTER)

        # 点击人员类别左侧按钮
        driver.find_element_by_xpath('//span[text()="人员类别："]/parent::span/following-sibling::div//span').click()

        driver.find_element_by_xpath(
            '//span[text()="人员类别参照"]/ancestor::div[@id="refContainerpsncl_id"]//div[@class="refer_results2"]/ul[3]//div[@class="scroll-wrapper fixed-table-body scrollbar-dynamic"]//tbody/tr[1]').click()

        # 点击职务右侧按钮
        driver.find_element_by_xpath('//span[text()="职务："]/parent::span/following-sibling::div//span').click()
        driver.find_element_by_xpath(
            '//span[text()="职务"]/ancestor::div[@id="refContainerjob_id"]//div[@class="refer_results2"]/ul[3]//div[@class="scroll-wrapper fixed-table-body scrollbar-dynamic"]//tbody/tr[1]').click()

        # 点击职位
        driver.find_element_by_xpath('//span[text()="职位："]/parent::span/following-sibling::div//span').click()
        driver.find_element_by_xpath(
            '//span[text()="职位"]/ancestor::div[@id="refContainerpost_id"]//div[@class="refer_results2"]/ul[3]//div[@class="scroll-wrapper fixed-table-body scrollbar-dynamic"]//tbody/tr[1]').click()

        # 点击入职类型右侧按钮
        driver.find_element_by_xpath('//span[text()="入职类型："]/parent::span/following-sibling::div//span').click()

        driver.find_element_by_xpath('//*[@id="refContainertrnstype"]//td[text()="1001"]').click()

        # 输入主管姓名
        driver.find_element_by_xpath(
            '//*[@id="staff-info-all-content"]/div[2]/form/fieldset/div[7]/div[2]/input').send_keys("黄俊涛")
        driver.find_element_by_xpath(
            '//*[@id="staff-info-all-content"]/div[2]/form/fieldset/div[7]/div[2]/input').click()
        sleep(3)
        driver.find_element_by_xpath(
            '//*[@id="staff-info-all-content"]/div[2]/form/fieldset/div[7]/div[2]/input').send_keys(Keys.ENTER)

        # 点击保存按钮
        driver.find_element_by_xpath('//*[@id="staff-info-all-content"]//button//span[text()="保存"]').click()
        sleep(3)
        driver.find_element_by_xpath('//input[@type="text" and @placeholder="搜索所属公司/部门/姓名"]').send_keys(
            context.Name.random_name)

        driver.find_element_by_xpath('//*[@id="staff-info-all-content"]/div[1]/div[1]/hr-search/span/label').click()
        text = driver.find_element_by_xpath(
            '//*[@id="staff-info-all-content"]//tbody//td[text()="{}"]'.format(context.Name.random_name)).text
        self.assertEqual(context.Name.random_name, text)
        sleep(2)
        # 关闭当前页面
        driver.switch_to.default_content()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()